

import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np


# 绘制简单的折线图
def plot_simple_line(dates, data, postion, label, color, step=2):

    # 第一个子图 - 折线图
    ax = plt.subplot(postion)
    # 绘制图表
    ax.plot(dates, data, color=color, marker='o', linewidth=0.7)
    # 添加x轴标签，并旋转90度
    ax.set_xticklabels(dates, rotation=90)
    # 添加y轴标签
    ax.set_ylabel(label, color=color)
    # 设置y轴刻度的颜色
    ax.tick_params("y", colors=color)

    # 设置y轴的刻度间隔（这里y轴从weights的最小值开始，最大值+step结束，step默认为2）
    ax.set_yticks(np.arange(int(min(data)), int(max(data))+step, step))

    # 给折线图描点绘制数值
    for i in range(len(data)):
        ax.text(
            i,
            data[i]+0.2,  # 文字稍微上一点别被线遮住
            f'{data[i]:.2f}',
            ha='center',
            va='bottom',
            fontsize=8,
        )

    pass


# 绘制简单的条状图
def plot_simple_bar(dates, data, postion, label, color):
    # 按位置创建坐标系
    ax = plt.subplot(postion)
    # 绘制条状图
    ax.bar(dates, data, color=color)
    # 绘制y轴标签和颜色
    ax.set_ylabel(label, color=color)
    # 设置y轴刻度的颜色
    ax.tick_params("y", colors=color)
    # 设置x轴标签，旋转90度
    ax.set_xticklabels(dates, rotation=90)
    # 条状图上添加文字
    for i in range(len(data)):
        ax.text(
            i,
            data[i],  # 文字稍微上一点别被线遮住
            f'{data[i]:.0f}',
            ha='center',
            va='bottom',
            color=color,
            fontsize=8,
        )
    pass


# 共用x轴的折线图
def plot_line_sharex(ax, dates, data, label, color, fontsize):
    # 绘制第一个图 - 折线图（体重）
    ax.plot(dates, data, color=color, marker='o')
    # 绘制y轴标签和颜色
    ax.set_ylabel(label, color=color)
    # 设置y轴刻度的颜色
    ax.tick_params("y", colors=color)
    # ax.tick_params(
    #     axis='x',  # 表示对 x 轴进行设置
    #     top=True,  # 表示将刻度线放在底部。
    #     labeltop=True,  # 表示不显示刻度标签(True则显示底部标签)。
    # )

    # 给折线图描点绘制数值
    for i in range(len(data)):
        ax.text(
            i,
            data[i]+0.2,  # 文字稍微上一点别被线遮住
            f'{data[i]:.2f}',
            ha='center',
            va='bottom',
            fontsize=fontsize,
        )

    # 只设置x轴方向的网格线
    ax.grid(axis='x')


# 共用x轴的条状图
def plot_bar_sharex(ax, dates, data, original_data, label, color, fontsize):
    # 绘制第二个图 - 条状图（摄入热量）
    ax.bar(dates, data, color=color)
    # 绘制y轴标签和颜色
    ax.set_ylabel(label, color=color)
    # 设置y轴刻度的颜色
    ax.tick_params("y", colors=color)
    # ax.tick_params(
    #     axis='x', bottom=True,
    #     labelbottom=False,  # 表示不显示刻度标签(True则显示底部标签)。
    # )

    # 条状图顶部添加文字
    for i in range(len(data)):
        ax.text(
            i,
            data[i],  # 文字稍微上一点别被线遮住
            f'{data[i]:.0f}',
            ha='center',
            va='bottom',
            color=color,
            fontsize=fontsize,
        )

    """
    # 给柱子内部绘制文字
    # 注意，因为摄入的原始数据和锻炼的原始数据结构不一样，所以处理的方法也不一样。
    # 具体可以看test_data.json的数据格式
    idx = 0

    # 这个不出意外是摄入
    if type(original_data) == list:
        # 柱状图的横坐标值（一维数组）
        positions = np.arange(len(dates))
        exercise_label_arr = [
            ",".join([f"{exercise['k']}:{exercise['v']}" for exercise in month_data]) for month_data in original_data
        ]

        # 在柱子的顶部显示总摄入量
        for i in range(len(dates)):

            # 柱子内部文字
            ax.text(
                positions[i],
                1,  # 标签从最底部往上(贴着底不好看就偏一点，实际高度根据刻度值来)
                exercise_label_arr[i],
                rotation=90,
                ha='center',
                va='bottom',  # 从底部往上显示标签值
                color='black',
                fontsize=fontsize-4,
            )

    # 这个不出意外是锻炼
    else:
        for month_key, month_data in original_data.items():
            month_len = len(month_data)
            for i in range(month_len):
                label = month_data[i]["k"]

                # 柱子内部文字
                ax.text(
                    idx,
                    20,  # 标签从最底部往上(贴着底不好看就偏一点)
                    label,
                    rotation=90,
                    ha='center',
                    va='bottom',  # 从底部往上显示标签值
                    color='black' if label == "清淡饮食" else "red",  # 如果不是清淡饮食就显示红色
                    fontsize=fontsize-4,
                )
                idx += 1
    """

    # ax.grid(True)
    ax.grid(axis='x')


# 格式化日期格式的日期列表为指定字符串形式列表
def generate_dates(start_date, end_date):
    # 生成日期列表
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates


def draw_weight_intake_exercise_separated(start_date, end_date,
                                          intake_data, weight_data, exercise_data,):

    dates = generate_dates(start_date, end_date)

    # 提取每天的摄入量、体重数据、运动总量
    intake_arr = [x["v"] for month_data in intake_data.values()
                  for x in month_data]
    weight_arr = [x for month_data in weight_data.values() for x in month_data]
    exercise_arr = [sum([exercise['v'] for exercise in month_data])
                    for month_data in exercise_data]

    """
    这是绘制x轴不共用版本
    """
    # 创建图形和子图
    # fig = plt.figure(figsize=(16, 9))
    # plot_simple_line(dates, weight_arr, 311, "Weight (kg)", "blue")
    # plot_simple_bar(dates, intake_arr, 312, "Intake (kcal)", "green")
    # plot_simple_bar(dates, exercise_arr, 313, "Exercise (min)", "grey")

    """
    这是x轴共用版本
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(16, 9))

    plot_line_sharex(ax1, dates, weight_arr, "Weight (kg)",  "blue", 8)
    plot_bar_sharex(ax2, dates, intake_arr, intake_data,
                    "Intake (kcal)",  "green", 12)
    plot_bar_sharex(ax3, dates, exercise_arr, exercise_data,
                    "Exercise (min)",  "grey", 12)

    # 设置y轴的刻度间隔（这里y轴从数据中的最小值开始，也可以指定的整数，最大值+2*step结束）
    # 也可以放到绘制的共用函数中，但最大值最小值刻度不好自定义
    ax1.set_yticks(np.arange(int(min(weight_arr)), int(max(weight_arr))+4, 2))
    ax2.set_yticks(np.arange(500, int(max(intake_arr))+1000, 500))
    ax3.set_yticks(np.arange(20, int(max(exercise_arr))+40, 20))

    # 旋转x轴的标签文本(示例中a2、ax不需要显示标签，都共用最下面这个即可)
    ax3.set_xticklabels(dates, rotation=90)
    ax3.tick_params(
        axis='x', bottom=True,  # 标识标签放在底部(key改为top或者值改成False都可以配置)
        labelbottom=True,  # 表示不显示刻度标签(True则显示底部标签)。
    )

    # 设置整个图表的标题
    fig.suptitle("Daily Intake、Exercise and Weight Separated")

    plt.tight_layout()

    # dpi表示每英寸点数，bbox_inches='tight'会裁剪边界框，以适应图表内容
    fig.savefig('./_output/weight_intake_exercise_separated.png',
                dpi=300,  bbox_inches='tight')

    # 显示图形
    plt.show()
