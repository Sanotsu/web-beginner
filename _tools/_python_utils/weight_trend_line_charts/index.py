import numpy as np
import json
from datetime import datetime, timedelta

from utils.weight_intake import plot_weight_intake
from utils.weight_trend import draw_one_line_with_range_slider


if __name__ == "__main__":

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

    # 指定JSON文件的路径
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
    weight202309 = [74.97, 74.49, 74.41, 74.28, 74.21, 74.72,
                    74.49, 73.73, 74.48, 73.38, 73.26, 73.06, 72.82, 72.77, 72.38, 73.2, 71.92, 71.58]

    start_date = datetime(2023, 7, 14)  # 开始日期
    end_date = datetime(2023, 9, 18)  # 结束日期
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


"""
7月30日早上空腹75.91
7月31日晚上睡前77.31
8月01日晚上睡前77.42 
8月02日晚上睡前77.98 
8月03日晚上睡前78.39 
8月04日晚上睡前78.90 

6天长6斤，共摄入

7.30    肠粉	       3斤糯米饭	   1斤糯米饭,1个短保蛋糕            300g瓜子
7.31    1.5斤糯米饭     1个短保面包	    2个鸡蛋2根火腿肠的蛋炒饭          200g瓜子
8.01    1个短保面包	    2个短保面包	    16.6称菜                       200g瓜子
8.02    1个短保面包	    3个短保面包     1个鸡蛋2个番茄2根火腿肠1包泡面     200g瓜子
8.03    2个短保面包	    2个短保面包     14称菜                         200g瓜子
8.04    2个短保面包	    2个短保面包     2包火鸡面,2个短保面包            100g瓜子
"""
