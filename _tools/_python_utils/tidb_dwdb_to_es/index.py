import time
from datetime import datetime
from typing import List
from peewee import *

from playhouse.shortcuts import model_to_dict

from tools.utils import my_logger

from table_classes.es_device_event_record_index import (
    bulk_docs_to_index,
    init_es_index,
    insert_doc_to_index,
    scroll_all_docs_from_index,
)
from table_classes.dwd_device_event_record import (
    MyDwdDeviceEventRecord,
    DwdbDwdDeviceEventRecord,
    init_db_and_table,
)


# 把数据存到备份表中
def dwdb_der_to_backup_table(records: list, batch_size=114):

    # perf_counter()会包含sleep()休眠时间，单位小数秒，适用测量短持续时间
    # process_time()不包括sleep()休眠时间期间经过的时间。
    # time()是系统时间，返回自纪元以来的秒数作为浮点数，会把sleep()的时间也算进去。
    #   gmtime(0)查看自己平台上的纪元。
    start = time.perf_counter()

    my_logger(f"开始向tidb设备事件记录备份表插入数据 {len(records)} 条，每次插入 {batch_size} 条……")

    # 将宽表的数据插入的测试表中，单个插入语句处理114条数据
    MyDwdDeviceEventRecord.bulk_create(records, batch_size)

    end = time.perf_counter()
    elapsed = end - start
    my_logger(f"向tidb设备事件记录备份表插入数据 {len(records)} 条，耗时 {elapsed} 秒。")


# 查询tidb宽表中的设备时间记录，插入到es中
def dwdb_der_insert_to_es(records: list, index_name, bulk_type="bulk"):

    # 批量插入es
    my_logger(f"开始格式化tidb查询结果数据 {len(records)} 条……")

    # 把查询的结果转为字典列表，并手动处理部分属性的值
    formatted_list = []
    for v in records:
        dic = model_to_dict(v)

        # 有两个栏位的值需要手动处理一下
        dic.update(
            {
                "data_info": str(dic["data_info"]),
                "device_related_user": []
                if dic["device_related_user"] == None
                else eval(dic["device_related_user"]),
            }
        )

        # 本来想删除值为空的属性，但这样插入es的action构建时也需要处理(没有属性取不到值不动态处理要报错)
        # for key, value in dic.copy().items():
        #     if value is None:
        #         del dic[key]

        formatted_list.append(dic)

    # 逐行逐条插入es中
    if bulk_type == "single":
        my_logger(f"开始向es【逐条】插入数据 {len(formatted_list)} 条……")
        start = time.time()
        for v in formatted_list:
            insert_doc_to_index(v["msg_id"], v, index=index_name)
        end = time.time()
        my_logger(f"向ES【逐条】插入数据 {len(formatted_list)} 条数据，耗时 {end - start} 秒!")

    # 或者批量插入
    else:
        my_logger("开始向es【批量】插入数据……")
        bulk_docs_to_index(
            formatted_list,
            index=index_name,
            bulk_type=bulk_type,
        )


# 测试写入tidb和各种bulk写入es的速度
def bulk_docs_test():

    # 测试不同插入es的方式，对应测试index名称不同，但结构一致
    # 修改这个名字就好: parallel_bulk | streaming_bulk | bulk | single (从快到慢)
    # 但最好不用single，逐条插入10万条要好几个小时，其他方法不到1分组
    es_bulk_type = "parallel_bulk"

    index_name = f"david_der_{es_bulk_type}"

    # 先备份es中指定索引中已有的数据，避免同步后出现问题可以有恢复的东西
    my_logger("开始备份es原有数据……")
    scroll_all_docs_from_index(
        index=index_name,
        file_name=f"./_self_files/{index_name}_bak/{(datetime.now()).strftime('%Y-%m-%d %H:%M:%S.%f') }.json",
    )

    my_logger("开始初始化tidb宽表和es索引……")
    # 初始化数据库连接和宽表
    init_db_and_table()
    # 初始化es连接和索引
    init_es_index(index_name)

    my_logger("开始查询tidb宽表数据……")
    # 查询全部设备事件记录
    query = DwdbDwdDeviceEventRecord.select()
    # .where(DwdbDwdDeviceEventRecord.msg_id == 67758868368728064)
    all_records = list(query)

    # 1 插入tidb中
    # 将宽表的数据插入的测试表中，单个插入语句处理114条数据
    dwdb_der_to_backup_table(all_records, 500)

    # 2 插入es中
    dwdb_der_insert_to_es(all_records, index_name, bulk_type=es_bulk_type)


if __name__ == '__main__':
    bulk_docs_test()
