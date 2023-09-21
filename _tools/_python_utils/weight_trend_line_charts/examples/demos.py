import numpy as np
import json
from datetime import datetime, timedelta

from utils.weight_intake_exercise import plot_weight_intake
from utils.weight_trend import draw_one_line_with_range_slider
from utils.weight_intake import draw_intake_and_weight


def demo_weight_intake_exercise():
    """
    weight intake 的示例
    """

    # 条形图的默认宽度
    bar_width = 0.2

    start_date = datetime(2023, 9, 1)  # 开始日期
    end_date = datetime(2023, 9, 18)  # 结束日期
    days = (end_date - start_date).days + 1  # 总天数

    # x轴为日期序列，并格式化
    original_dates = [start_date + timedelta(days=i) for i in range(days)]

    date_format = "%Y年%m月%d日"

    # x轴的日期数据（各个y轴数据都共用同一个x轴）
    formatted_dates = [date.strftime(date_format) for date in original_dates]

    # 指定JSON文件的路径(注意，这是调用处的相对路径)
    weight_file_path = "./_input_data/sept/weight_records.json"
    breakfast_file_path = "./_input_data/sept/breakfast_records.json"
    lunch_file_path = "./_input_data/sept/lunch_records.json"
    dinner_file_path = "./_input_data/sept/dinner_records.json"
    exercise_file_path = "./_input_data/sept/exercise_records.json"

    # 打开文件并读取JSON数据（y轴的各项数据）
    with open(weight_file_path, "r", encoding="utf-8", errors="ignore") as file:
        weight_data = json.load(file)

    with open(breakfast_file_path, "r", encoding="utf-8", errors="ignore") as file:
        breakfast_data = json.load(file)

    with open(lunch_file_path, "r", encoding="utf-8", errors="ignore") as file:
        lunch_data = json.load(file)

    with open(dinner_file_path, "r", encoding="utf-8", errors="ignore") as file:
        dinner_data = json.load(file)

    with open(exercise_file_path, "r", encoding="utf-8", errors="ignore") as file:
        exercise_data = json.load(file)

    plot_weight_intake(bar_width, formatted_dates, weight_data,
                       breakfast_data, lunch_data, dinner_data, exercise_data,)


def demo_weight_trend():
    """
    weight trend的示例
    """

    # 7月的数据是7.14~7.31（18天）
    weight202307 = [77.6, 77.98, 77.8, 78.17, 77.47, 77.9, 77.8, 78.5, 78.61, 78.15,
                    77.69, 76.86, 77.17, 76.9, 76.19, np.nan, 75.91, 77.31]
    # 8月的数据是8.1~8.31（31天）
    weight202308 = [77.42, 77.98, 78.39, 78.90, np.nan, np.nan, 77.97, 77.45, 77.29, 76.98, 77.44, 76.64, 76.47, 76.74,
                    76.98, 77, 76.58, 77.12, 77.13, 76.76, 76.98, 76.92, 77.63, 77.20, 76.83, 76.22, 76.26, 75.67, 75.17, 75.45, 75.39]
    # 9月的数据是9.1~9.15 （15天）
    weight202309 = [74.97, 74.49, 74.41, 74.28, 74.21,
                    74.72, 74.49, 73.73, 74.48, 73.38,
                    73.26, 73.06, 72.82, 72.77, 72.38,
                    73.20, 71.92, 71.58, 71.60, 71.40]

    start_date = datetime(2023, 7, 14)  # 开始日期
    end_date = datetime(2023, 9, 20)  # 结束日期
    date_format = "%Y年%m月%d日"

    # 生成格式化后的日期数据作为x轴
    formatted_dates = [
        (start_date + timedelta(days=i)).strftime(date_format)
        for i in range((end_date - start_date).days + 1)
    ]

    # 体重值作为y轴
    weight_data = weight202307+weight202308+weight202309

    # draw_lines_by_month(weight202307, weight202308, weight202309)
    # 可以直接使用格式化的x轴日期
    # draw_one_line(formatted_dates, weight_data)
    # 或者传入时间起止，在内部有格式化过程
    draw_one_line_with_range_slider(start_date, end_date, weight_data)


def demo_weight_intake_simple():
    intake202308 = [{'k': "称菜、瓜子300g", 'v': 3216},
                    {'k': "蛋炒饭、花生100g", 'v': 2074},
                    {'k': "清淡饮食", 'v': 1103},
                    {'k': "炸鸡块、西瓜2斤", 'v': 2207},
                    {'k': "清淡饮食", 'v': 1109},
                    {'k': "蛋炒饭、西瓜5斤", 'v': 2326},
                    {'k': "清淡饮食", 'v': 1227},
                    {'k': "清淡饮食", 'v': 1423},
                    {'k': "称菜", 'v': 1403},
                    {'k': "称菜", 'v': 1564},
                    {'k': "炸鸡块、炸鸡翅根", 'v': 1738},
                    {'k': "方便面、火鸡面", 'v': 1366},
                    {'k': "清淡饮食", 'v': 1171},
                    {'k': "清淡饮食", 'v': 1252},
                    {'k': "汉堡2、鸡肉卷2、鸡排、小酥肉、可乐1", 'v': 2911},
                    {'k': "清淡饮食、可乐1", 'v': 1309},
                    {'k': "清淡饮食", 'v': 1009},
                    {'k': "清淡饮食", 'v': 1418},
                    {'k': "清淡饮食", 'v': 1196},
                    {'k': "肉片滑蛋、麻辣肉片", 'v': 2180},
                    {'k': "清淡饮食", 'v': 875},
                    {'k': "炸鸡块、炸鸡柳", 'v': 2129},
                    {'k': "清淡饮食", 'v': 1016},
                    {'k': "炒面", 'v': 1466}]
    intake202309 = [{'k': "清淡饮食", 'v': 1115},
                    {'k': "清淡饮食", 'v': 1111},
                    {'k': "炒菜", 'v': 1526},
                    {'k': "清淡饮食", 'v': 1227},
                    {'k': "清淡饮食", 'v': 1182},
                    {'k': "扒鸡、汉堡2、鸡肉卷2", 'v': 2448},
                    {'k': "清淡饮食", 'v': 374},
                    {'k': "清淡饮食", 'v': 1008},
                    {'k': "炸鸡块、炸鸡腿2", 'v': 1944},
                    {'k': "清淡饮食", 'v': 755},
                    {'k': "清淡饮食", 'v': 1203},
                    {'k': "清淡饮食", 'v': 1120},
                    {'k': "清淡饮食", 'v': 886},
                    {'k': "清淡饮食", 'v': 1016},
                    {'k': "清淡饮食", 'v': 987},
                    {'k': "炸鸡块、炸鸡柳", 'v': 2315},
                    {'k': "清淡饮食", 'v': 1054},
                    {'k': "清淡饮食", 'v': 1306},
                    {'k': "清淡饮食", 'v': 843},
                    {'k': "清淡饮食", 'v': 987}]
    weight202308 = [77.45, 77.29, 76.98, 77.44, 76.64,
                    76.47, 76.74, 76.98, 77, 76.58,
                    77.12, 77.13, 76.76, 76.98, 76.92,
                    77.63, 77.20, 76.83, 76.22, 76.26,
                    75.67, 75.17, 75.45, 75.39]
    weight202309 = [74.97, 74.49, 74.41, 74.28, 74.21,
                    74.72, 74.49, 73.73, 74.48, 73.38,
                    73.26, 73.06, 72.82, 72.77, 72.38,
                    73.20, 71.92, 71.58, 71.60, 71.40]

    # 示例用法
    start_date = datetime(2023, 8, 8)
    end_date = datetime(2023, 9, 20)
    intake_data = {
        "202308": intake202308,
        "202309": intake202309,
    }
    weight_data = {
        "202308": weight202308,
        "202309": weight202309,
    }

    draw_intake_and_weight(start_date, end_date, intake_data, weight_data)
