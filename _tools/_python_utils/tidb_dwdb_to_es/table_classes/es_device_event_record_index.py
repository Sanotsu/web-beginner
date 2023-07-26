import time
from elasticsearch import Elasticsearch, helpers
import json

from tools.utils import create_directory, my_logger


es_client = Elasticsearch(
    "http://<domain>:<port>/",  # Elasticsearch endpoint
    # API key ID and secret
    basic_auth=('<name>', '<password>'),
)

# 默认的设备事件记录索引名称
default_index = "david_test_index"

# 默认设备事件记录索引的 mapping （针对设备事件记录mer，索引名称可能不一样，但映射一定一样）
device_event_record_mappings = {
    "mappings": {
        "properties": {
            "msg_id": {"type": "long"},
            "device_id": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "device_related_user": {"type": "long"},
            "function_tag": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "number_value": {"type": "float"},
            "json_value": {"type": "text"},
            "str_value": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "msg_level": {"type": "short"},
            "origin_time": {"type": "date"},
            "parent_device_id": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "product_id": {"type": "long"},
            "product_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "product_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "prod_cn_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "product_category": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "node_type": {"type": "short", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "data_format": {"type": "text"},
            "net_type": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "function_id": {"type": "long"},
            "function_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "function_category": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "function_type": {"type": "short"},
            "data_type": {"type": "text"},
            "data_info": {"type": "text"},
            "sw_version": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "hw_version": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "division_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "division_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "project_id": {"type": "long"},
            "project_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "project_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "building_id": {"type": "long"},
            "building_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "building_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "building_type": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "floor_id": {"type": "long"},
            "floor_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "floor_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "unit_code": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "detailed_address": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "longitude": {"type": "float"},
            "latitude": {"type": "float"},
            "is_processed": {"type": "short"},
            "remark": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "remark_tag": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
            "upd_usr_id": {"type": "long"},
            "gmt_create": {"type": "date"},
            "gmt_modified": {"type": "date"}
        }
    }
}


# 初始化index
def init_es_index(index=default_index):

    # 索引存在，先删除索引
    if es_client.indices.exists(index=index):
        my_logger(f'索引 {index} 已存在，先删除')
        es_client.indices.delete(index=index)
    else:
        my_logger(f'索引 {index} 不存在，可以创建')
    # 创建索引(不存在本来就可以创建，已存在删除之后再创建)
    es_client.indices.create(
        index=index,
        body=device_event_record_mappings,
    )

    # 查看索引的信息
    my_logger(f'成功创建索引，es client信息: {es_client}')  # {es_client.info()


# 批量插入数据
"""
bulk有三个相关函数：
    parallel_bulk()：并发批量执行；
    streaming_bulk()：流式批量执行；
    bulk()：在源码里可以看到，本质上是对streaming_bulk()的封装，返回了统计结果，方便处理。
"""


# 批量插入前构建数据是一样的
def generate_actions(index, records):
    actions = [
        {
            "_index": index,
            # '_type': '_doc', # es 7.x 之后不再指定类型
            "_id": record["msg_id"],
            "_source": {
                "msg_id": record["msg_id"],
                "device_id": record["device_id"],
                "device_related_user": record["device_related_user"],
                "function_tag": record["function_tag"],
                "number_value": record["number_value"],
                "json_value": record["json_value"],
                "str_value": record["str_value"],
                "msg_level": record["msg_level"],
                "origin_time": record["origin_time"],
                "parent_device_id": record["parent_device_id"],
                "product_id": record["product_id"],
                "product_code": record["product_code"],
                "product_name": record["product_name"],
                "prod_cn_name": record["prod_cn_name"],
                "product_category": record["product_category"],
                "node_type": record["node_type"],
                "data_format": record["data_format"],
                "net_type": record["net_type"],
                "function_id": record["function_id"],
                "function_name": record["function_name"],
                "function_category": record["function_category"],
                "function_type": record["function_type"],
                "data_type": record["data_type"],
                "data_info": record["data_info"],
                "sw_version": record["sw_version"],
                "hw_version": record["hw_version"],
                "division_code": record["division_code"],
                "division_name": record["division_name"],
                "project_id": record["project_id"],
                "project_code": record["project_code"],
                "project_name": record["project_name"],
                "building_id": record["building_id"],
                "building_code": record["building_code"],
                "building_name": record["building_name"],
                "building_type": record["building_type"],
                "floor_id": record["floor_id"],
                "floor_code": record["floor_code"],
                "floor_name": record["floor_name"],
                "unit_code": record["unit_code"],
                "detailed_address": record["detailed_address"],
                "longitude": record["longitude"],
                "latitude": record["latitude"],
                "is_processed": record["is_processed"],
                "remark": record["remark"],
                "remark_tag": record["remark_tag"],
                "upd_usr_id": record["upd_usr_id"],
                "gmt_create": record["gmt_create"],
                "gmt_modified": record["gmt_modified"]
            },
        } for record in records
    ]

    return actions


# 批量插入
def bulk_docs_to_index(records, index=default_index, bulk_type="bulk"):
    start = time.time()

    my_logger(f"开始构建用于 {bulk_type} 的 actions {len(records)} 条……")
    action = generate_actions(index, records)

    my_logger(f"开始执行 {bulk_type} ……")

    if bulk_type == "bulk":
        try:
            # 执行批量索引操作，并设置 raise_on_error=False
            success, failed = helpers.bulk(
                es_client, action, raise_on_error=False)
            if failed:
                for item in failed:
                    print(item)
        except Exception as e:
            print(str(e))

    elif bulk_type == "parallel_bulk":
        # parallel_bulk是个惰性的生成器，不消费则不会实际运行
        # 参看：https://discuss.elastic.co/t/helpers-parallel-bulk-in-python-not-working/39498

        # 修改一些默认配置
        parallel_bulk_custom_config = {
            "thread_count": 4,
            "refresh": False,
            "raise_on_error": False,
            "request_timeout": 30,
            "chunk_size": 1000,
        }
        for success, info in helpers.parallel_bulk(es_client, action, **parallel_bulk_custom_config):
            if not success:
                my_logger(f'        {bulk_type} 发生错误:', info)

    elif bulk_type == "streaming_bulk":

        # 修改一些默认配置
        streaming_bulk_custom_config = {
            "chunk_size": 1000,
            "refresh": False,
            "timeout": "10s",
            "raise_on_error": False
        }

        for success, info in helpers.streaming_bulk(es_client, action, **streaming_bulk_custom_config):
            if not success:
                my_logger(f"        {bulk_type} 错误信息：{info}")
    else:
        my_logger(f'UNKNOWN : 无效的批量插入类型：{bulk_type} 。')

    end = time.time()
    my_logger(f"向ES使用 {bulk_type} 插入 {len(records)} 条数据，耗时 {end - start} 秒!")


# 查询指定索引的所有数据，并存入指定json文件
def scroll_all_docs_from_index(index, file_name):
    start = time.time()

    my_logger("开始以scroll=5s,size=5000，查询ES中指定index的全部doc的数据……")

    # 指定搜索条件和索引
    body = {
        "query": {
            "match_all": {}
        }
    }

    # 初始的 scroll 请求
    response = es_client.search(
        index=index,
        scroll="5s",  # 设置scroll时间窗口 1m为1分钟查一次
        size=5000,   # 每次返回的文档数量
        body=body
    )

    scroll_id = response['_scroll_id']
    total_documents = response['hits']['total']['value']

    my_logger(f"开始把查询的 {total_documents} 条文档写入json文件……")

    create_directory(file_name)

    # 将查询结果写入文件
    with open(file_name, "w") as file:
        for doc in response['hits']['hits']:
            file.write(json.dumps(doc) + '\n')

    # 滚动浏览剩余的数据
    while True:
        response = es_client.scroll(scroll_id=scroll_id, scroll="5s")

        if len(response['hits']['hits']) == 0:
            break

        # 将查询结果继续追加到文件中
        with open(file_name, "a") as file:
            for doc in response['hits']['hits']:
                file.write(json.dumps(doc) + '\n')

    end = time.time()
    my_logger(f"向 {file_name} 写入 {total_documents} 条数据，耗时 {end - start} 秒!")


# ------------------------


# 指定id，单条插入数据
def insert_doc_to_index(id, doc, index=default_index):
    try:
        response = es_client.index(index=index, id=id, document=doc)
    # 处理成功响应
    except Exception as e:
        print("发生错误：", str(e))


# 条件查询数据
def search_docs_from_index(index, query):
    # search 查询数据
    # 查询所有商品数据 match_all
    body = {
        'query': {
            'match_all': {}
        },
        'from': 1 * 2,       # 从第几条数据开始
        'size': 2   # 获取多少条数据
    }
    requ_data = es_client.search(index=index, body=query)
    print("----------------------")
    print(len(requ_data))

    # # 将响应对象转换为JSON字符串
    # json_str = json.dumps(requ_data)

    # 将JSON字符串写入文件
    with open("dwd_device_event_record.json", "a") as file:
        file.write(str(requ_data))


# 通过指定id获取单条数据
def get_doc_by_id(index, id):
    temp_doc = es_client.get(index=index, id=id)
    print("=====================")
    print(temp_doc)
