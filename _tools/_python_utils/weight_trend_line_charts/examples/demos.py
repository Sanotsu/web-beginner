import numpy as np
import json
from datetime import datetime, timedelta
from utils.plot1_weight_trend import draw_lines_by_month, draw_one_line, draw_one_line_with_range_slider
from utils.plot2_weight_intake_exercise_detail import draw_weight_intake_exercise_detail
from utils.plot3_weight_intake_simple import draw_weight_intake_simple
from utils.plot4_weight_intake_exercise_simple import draw_weight_intake_exercise_simple
from utils.plot5_weight_intake_exercise_simple_optional import draw_weight_intake_exercise_simple_optional
from utils.plot6_weight_intake_exercise_separated import draw_weight_intake_exercise_separated


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
                    73.20, 71.92, 71.58, 71.60, 71.40,
                    70.86, 70.89, 71.23, 70.48, 70.78]

    start_date = datetime(2023, 7, 14)  # 开始日期
    end_date = datetime(2023, 9, 25)  # 结束日期
    date_format = "%Y年%m月%d日"

    # 生成格式化后的日期数据作为x轴
    formatted_dates = [
        (start_date + timedelta(days=i)).strftime(date_format)
        for i in range((end_date - start_date).days + 1)
    ]

    # 体重值作为y轴
    weight_data = weight202307+weight202308+weight202309

    draw_lines_by_month(weight202307, weight202308, weight202309)
    # 可以直接使用格式化的x轴日期
    draw_one_line(formatted_dates, weight_data)
    # 或者传入时间起止，在内部有格式化过程
    draw_one_line_with_range_slider(start_date, end_date, weight_data)


def demo_weight_intake_exercise_detail():
    """
    weight intake 的示例
    """

    # 条形图的默认宽度
    bar_width = 0.2

    start_date = datetime(2023, 9, 1)  # 开始日期
    end_date = datetime(2023, 9, 24)  # 结束日期
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

    draw_weight_intake_exercise_detail(bar_width, formatted_dates, weight_data,
                                       breakfast_data, lunch_data, dinner_data, exercise_data,)


"""
后面的几个测试数据可以是一样的，就放在外面
"""


def gen_test_data():

    # 在index执行就是index的相对路径
    # test_data_file_path = "test_data.json"
    test_data_file_path = "./examples/test_data.json"

    # 打开文件并读取JSON数据（y轴的各项数据）
    with open(test_data_file_path, "r", encoding="utf-8", errors="ignore") as file:
        test_data = json.load(file)

        weight202308 = test_data["weight"][0]["weight202308"]
        weight202309 = test_data["weight"][1]["weight202309"]
        intake202308 = test_data["intake"][0]["intake202308"]
        intake202309 = test_data["intake"][1]["intake202309"]
        exercise202308 = test_data["exercise"][0]["exercise202308"]
        exercise202309 = test_data["exercise"][1]["exercise202309"]

    # 示例用法
    start_date = datetime(2023, 8, 8)
    end_date = datetime(2023, 9, 25)

    intake_data = {
        "202308": intake202308,
        "202309": intake202309,
    }
    weight_data = {
        "202308": weight202308,
        "202309": weight202309,
    }

    exercise_data = exercise202308 + exercise202309

    # return start_date, end_date, weight202308, weight202309, intake202308, intake202309, exercise202308, exercise202309
    return start_date, end_date, intake_data, weight_data, exercise_data


def demo_weight_intake_simple():
    [start_date, end_date, intake_data, weight_data, exercise_data] = gen_test_data()
    draw_weight_intake_simple(start_date, end_date, intake_data, weight_data)


def demo_weight_intake_exercise_simple():
    # 柱状图柱子的预设宽度
    bar_width = 0.4
    [start_date, end_date, intake_data, weight_data, exercise_data] = gen_test_data()

    draw_weight_intake_exercise_simple(
        bar_width,
        start_date, end_date,
        intake_data, weight_data, exercise_data,
    )


def demo_weight_intake_exercise_simple_optional(is_show_intake, is_show_exercise):

    # 柱状图柱子的预设宽度
    bar_width = 0.4
    [start_date, end_date, intake_data, weight_data, exercise_data] = gen_test_data()

    draw_weight_intake_exercise_simple_optional(
        bar_width,
        start_date, end_date,
        intake_data, weight_data, exercise_data,
        is_show_intake, is_show_exercise
    )


def demo_weight_intake_exercise_separated():

    [start_date, end_date, intake_data, weight_data, exercise_data] = gen_test_data()

    draw_weight_intake_exercise_separated(
        start_date, end_date,
        intake_data, weight_data, exercise_data,
    )
