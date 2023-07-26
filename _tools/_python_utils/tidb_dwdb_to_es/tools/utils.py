
from datetime import datetime
import os


# 简单的日志打印
def my_logger(msg: str):
    print(f"{ (datetime.now()).strftime('%Y-%m-%d %H:%M:%S.%f') } ::: {msg}")


# 创建指定文件路径的文件夹
def create_directory(file_path):
    # 获取文件夹路径
    directory = os.path.dirname(file_path)

    # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
