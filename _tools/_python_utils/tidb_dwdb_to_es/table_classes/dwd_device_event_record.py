from peewee import *
from playhouse.mysql_ext import *
from playhouse.db_url import connect

from tools.utils import my_logger


# 連接到tidb
database: MySQLDatabase = connect(
    'mysql://root:<passwprd>@<ip>/<dbname1>')


database_dwdb: MySQLDatabase = connect(
    'mysql://root:<passwprd>@<ip>/<dbname2>')


# 栏位说明参看:https://docs.peewee-orm.com/en/latest/peewee/models.html?highlight=CharField#table-constraints


# 目标表的基础栏位(两个数据库中栏位一样，名称和数据库地址不一样，所以这个抽出来)
class BaseDwdDeviceEventRecord(Model):
    msg_id = BigIntegerField(primary_key=True)  # 主键
    device_id = CharField(255, null=False)  # 不可为null
    device_related_user = CharField(4000, null=True)  # 可以为null
    function_tag = CharField(100, null=True)
    number_value = FloatField(null=True)
    json_value = JSONField(null=True)
    str_value = CharField(45, null=True)
    msg_level = SmallIntegerField(1)
    origin_time = DateTimeField(6, null=True)
    parent_device_id = CharField(100, null=True)
    product_id = BigIntegerField()
    product_code = CharField(10)
    product_name = CharField(45)
    prod_cn_name = CharField(45, null=True)
    product_category = CharField(120)
    node_type = SmallIntegerField(1)
    data_format = CharField(45)
    net_type = CharField(45)
    function_id = BigIntegerField()
    function_name = CharField(120)
    function_category = CharField(100)
    function_type = SmallIntegerField(1)
    data_type = CharField(45, null=True)
    data_info = JSONField(null=True)
    sw_version = CharField(45, null=True)
    hw_version = CharField(45, null=True)
    division_code = CharField(12, null=True)
    division_name = CharField(300, null=True)
    project_id = BigIntegerField(null=True)
    project_code = CharField(100, null=True)
    project_name = CharField(45, null=True)
    building_id = BigIntegerField(null=True)
    building_code = CharField(45, null=True)
    building_name = CharField(120, null=True)
    building_type = CharField(45, null=True)
    floor_id = BigIntegerField(null=True)
    floor_code = CharField(45, null=True)
    floor_name = CharField(45, null=True)
    unit_code = CharField(10, null=True)
    detailed_address = CharField(120, null=True)
    longitude = FloatField(null=True)
    latitude = FloatField(null=True)
    is_processed = SmallIntegerField(null=True)
    remark = TextField(null=True)
    remark_tag = CharField(120, null=True)
    upd_usr_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(6, null=True)
    gmt_modified = DateTimeField(null=True)


class MyDwdDeviceEventRecord(BaseDwdDeviceEventRecord):
    class Meta:
        database = database
        table_name = "my_dwd_device_event_record"


class DwdbDwdDeviceEventRecord(BaseDwdDeviceEventRecord):
    class Meta:
        database = database_dwdb
        table_name = "dwd_device_event_record"


# 创建宽表(如果有，则先删除)
def create_dwd_device_event_record():
    with database:
        database.drop_tables([MyDwdDeviceEventRecord])
        database.create_tables([MyDwdDeviceEventRecord])


# 初始化连接db和创建表
def init_db_and_table():

    if database.is_closed():
        database.connect()
        create_dwd_device_event_record()
        my_logger("tidb database 为关闭状态，现已连接并创建宽表")
    else:
        my_logger("tidb database 为已经处于连接状态")

    if database_dwdb.is_closed():
        database_dwdb.connect()
        my_logger("tidb database_dwdb 为关闭状态，现已连接")
    else:
        my_logger("tidb database_dwdb 为已经处于连接状态")
