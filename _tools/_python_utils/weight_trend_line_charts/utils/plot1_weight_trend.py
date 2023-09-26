import matplotlib.pyplot as plt
from datetime import timedelta
import matplotlib.dates as mdates
# 从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
from matplotlib.pyplot import MultipleLocator
# x轴范围滑动条
from matplotlib.widgets import RangeSlider
import numpy as np


# 按月数据绘制多个折线图
def draw_lines_by_month(jul_data, aug_data, sept_data):

    x = list(range(1, 32))

    # 利用切片使用列表切片操作可以非常方便地获取列表的子集，
    # 语法，list[start:end:step]，包含start，不包含end，都可省略，start默认0,end默认列表尾，step默认1。

    fig, ax = plt.subplots(figsize=(18, 9))

    # 7月份的数据是14号到31号，所以显示的内容是x轴31天的切片 [31-7月数据长度，31]
    plt.plot(x[(len(x) - len(jul_data)):],
             jul_data, label='Jul')
    plt.plot(x[:len(aug_data)], aug_data, label='Aug')
    # 9月份的数据是1号到15号，所以显示的内容是x轴31天的切片 [0,9月数据长度]
    plt.plot(x[:len(sept_data)], sept_data, label='Sept')

    # 添加数据文本
    # 7月在月末，文本显示从知道日期开始
    for i in range(len(jul_data)):
        plt.text(
            x[i+(len(x) - len(jul_data))],
            jul_data[i],
            "" if np.isnan(jul_data[i]) else str(jul_data[i]),
            ha='center',
            va='bottom',
        )
    # 8月数据完整，一一对应即可
    for i in range(len(x)):
        plt.text(
            x[i],
            aug_data[i],
            "" if np.isnan(aug_data[i]) else str(aug_data[i]),
            ha='center',
            va='bottom',
        )
    # 9月在月头，从头开始即可
    for i in range(len(sept_data)):
        plt.text(
            x[i],
            sept_data[i],
            "" if np.isnan(sept_data[i]) else str(sept_data[i]),
            ha='center',
            va='bottom',
        )

    # 添加图例
    plt.legend()

    # 设置标题和轴标签
    plt.title('Weight Trends - Monthly Statistics')
    plt.xlabel('Time (day)')
    plt.ylabel('Weight (kg)')

    # 设置x轴步进
    x_ticks = list(range(1, 32, 1))
    plt.xticks(x_ticks)

    plt.tight_layout()

    fig.savefig('./_output/weight_trend_monthly.png',
                dpi=300,  bbox_inches='tight')

    # 展示图形
    plt.show()


# 所有数据绘制一条折线图
def draw_one_line(formatted_dates, weight_data):

    # x轴为日期序列
    x = formatted_dates
    # y轴为对应数据
    y = weight_data

    # 修改图表尺寸为指定（单位英寸）
    fig, ax = plt.subplots(figsize=(18, 9))
    # 自动格式化日期
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # 把x轴的主刻度设置为1的倍数
    # ax.xaxis.set_major_locator(MultipleLocator(2))
    # 自动绘制刻度的话显示的可能比较分散，不好看
    # ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    # 在折线图上显示数值
    for i in range(len(x)):

        # 每个点都展示数据
        # 因为y轴weight数组中有nan值，所以绘制折线图的时候会出现：posx and posy should be finite values
        # 所以先选择判断是否为nan，是则显示空字串
        plt.text(
            x[i],
            y[i],
            "" if np.isnan(y[i]) else str(y[i]),
            ha='left',
            va='bottom'
        )

        # 控制间隔一个点展示数据
        # if i % 2 == 0:
        #     plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')

    # 绘制折线图
    plt.plot(x, y, marker='o', label='2023')  # 使用圆形标记

    # x轴y轴以及标题的名称
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.title('Weight Trends - Oneline')

    # 绘制图例
    plt.legend()
    # 设置x轴刻度的旋转角度
    plt.xticks(rotation=270)
    # 显示网格线
    plt.grid(True)

    plt.rcParams['figure.figsize'] = [18, 6]  # 宽度为 18 英寸，高度为 6 英寸

    plt.tight_layout()

    # 调整图表尺寸并保存为图片文件
    fig.savefig('./_output/weight_trend_oneline.png',
                dpi=300,  bbox_inches='tight')

    plt.show()


# 所有数据绘制一条折线图，并带有滑块
def draw_one_line_with_range_slider(start_date, end_date, weight_data):

    # 总天数
    days = (end_date - start_date).days + 1

    # 生成日期序列
    x = [start_date + timedelta(days=i) for i in range(days)]
    # y轴为体重数据
    y = weight_data

    # 创建子图
    fig, ax = plt.subplots(figsize=(18, 9))

    # 调整子图位置
    plt.subplots_adjust(bottom=0.25)

    # 绘制折线图并保存返回值
    line, = ax.plot(x, y, '.-', label='2023')

    # 绘制x、y轴、标题文字和图例
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.title('Weight Trends - Oneline RangeSlider')
    plt.legend()
    # x轴标签文字旋转角度
    plt.xticks(rotation=270)
    # 显示网格
    plt.grid(True)

    # 自动格式化日期和定位刻度
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # 把x轴的主刻度设置为1的倍数
    ax.xaxis.set_major_locator(MultipleLocator(1))
    # 自动绘制刻度的话显示的可能比较分散，不好看
    # ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    # 定义滑动条的位置和尺寸的坐标轴对象。它是一个列表 [left, bottom, width, height]，
    # 其中 (left, bottom) 是滑动条的左下角坐标，width 和 height 是滑动条的宽度和高度比例。
    ax_slider = plt.axes([0.7, 0.95, 0.2, 0.04])

    slider = RangeSlider(
        ax_slider,
        'Range',  # 滑动条的描述文本，显示在滑动条旁边。
        0,  # 滑动条的最小值。
        len(x)-1,  # 滑动条的最大值。
        valinit=[0, len(x)-1],  # 定义滑动条的初始值。
        valstep=1,  # 滑动条的步长。
    )

    # 更新图表函数，根据滑动条的值更新显示范围
    # val 为当前滑块的范围，值类似(10,39)，就是下面的slider.val用于取值
    def update_chart(val):
        # 获取范围滑动条的起始值，并将其转换为整数类型。这将用于切片 x 和 y 的值。
        start_index = int(val[0])
        # 获取范围滑动条的结束值，并将其转换为整数类型。同样，这将用于切片 x 和 y 的值。
        end_index = int(val[1])
        # 根据新的索引范围更新绘图对象 line 的数据。这将重新绘制图形，显示范围滑动条所选择的数据范围。
        line.set_data(x[start_index:end_index+1], y[start_index:end_index+1])
        # 重新计算坐标轴的数据限制。这将确保绘图的数据范围正确显示在坐标轴上。
        ax.relim()
        # 自动调整坐标轴的视图范围，以适应更新后的数据范围。
        ax.autoscale_view()

        # 清除已添加的标签
        for annotation in ax.texts:
            annotation.remove()

        # 添加文本标签
        for i in range(start_index, end_index+1):
            ax.annotate(
                str(y[i]),  # 要显示的文本内容。可以是字符串或任何可转换为字符串的对象。
                (x[i], y[i]),  # 要注释的点的坐标，即文本注释的目标位置。它是一个二元组 (x, y)，表示水平和垂直坐标。
                # 文本注释的偏移量。它是一个二元组 (x, y)，表示相对于注释点的水平和垂直方向上的偏移距离。
                xytext=(0, 3),
                # 文本注释的坐标系统。默认值为 'offset points'，表示偏移量是以点为单位。其他可选值包括 'data'（使用数据坐标系）和 'axes fraction'（使用轴坐标系）等。
                textcoords='offset points',
                fontsize=8
            )

        # 启动绘图的命令。该命令将在交互式模式下使用，并且它告诉 matplotlib 在必要时重新绘制已更改的对象。
        fig.canvas.draw_idle()

    # 在一开始就调用一次，以便初始化是就展示描点上方文本
    update_chart((0, len(x)-1))
    # 在滑块变动时及时更新显示的文字
    slider.on_changed(update_chart)

    plt.tight_layout()

    # 调整图表尺寸并保存为图片文件
    fig.savefig('./_output/weight_trend_oneline_range.png',
                dpi=300,  bbox_inches='tight')

    plt.show()
