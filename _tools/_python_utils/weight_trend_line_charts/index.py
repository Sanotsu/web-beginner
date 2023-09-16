import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
# 从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
from matplotlib.pyplot import MultipleLocator
# x轴范围滑动条
from matplotlib.widgets import RangeSlider

# 7月的数据是7.17~7.31（15天）
weight202307 = [78.17, 77.47, 77.9, 77.8, 78.5, 78.61, 78.15,
                77.69, 76.86, 77.17, 76.9, 76.19, 76.19, 75.91, 77.31]
# 8月的数据是8.1~8.31（31天）
weight202308 = [77.42, 77.98, 78.39, 78.90, 78.90, 78.90, 77.97, 77.45, 77.29, 76.98, 77.44, 76.64, 76.47, 76.74,
                76.98, 77, 76.58, 77.12, 77.13, 76.76, 76.98, 76.92, 77.63, 77.20, 76.83, 76.22, 76.26, 75.67, 75.17, 75.45, 75.39]
# 9月的数据是9.1~9.15 （15天）
weight202309 = [74.97, 74.49, 74.41, 74.28, 74.21, 74.72,
                74.49, 73.73, 74.48, 73.38, 73.26, 73.06, 72.82, 72.77, 72.38]


# 按月数据绘制多个折线图
def draw_lines_by_month():

    x = list(range(1, 32))

    # 利用切片使用列表切片操作可以非常方便地获取列表的子集，
    # 语法，list[start:end:step]，包含start，不包含end，都可省略，start默认0,end默认列表尾，step默认1。

    # 7月份的数据是14号到31号，所以显示的内容是x轴31天的切片 [31-7月数据长度，31]
    plt.plot(x[(len(x) - len(weight202307)):],
             weight202307, label='weight202307')
    plt.plot(x[:len(weight202308)], weight202308, label='weight202308')
    # 9月份的数据是1号到15号，所以显示的内容是x轴31天的切片 [0,9月数据长度]
    plt.plot(x[:len(weight202309)], weight202309, label='weight202309')

    # 添加数据文本
    # 7月在月末，文本显示从知道日期开始
    for i in range(len(weight202307)):
        plt.text(x[i+(len(x) - len(weight202307))], weight202307[i], str(
            weight202307[i]), ha='center', va='bottom')
    # 8月数据完整，一一对应即可
    for i in range(len(x)):
        plt.text(x[i], weight202308[i], str(
            weight202308[i]), ha='center', va='bottom')
    # 9月在月头，从头开始即可
    for i in range(len(weight202309)):
        plt.text(x[i], weight202309[i], str(
            weight202309[i]), ha='center', va='bottom')

    # 添加图例
    plt.legend()

    # 设置标题和轴标签
    plt.title('Weight Trends')
    plt.xlabel('Time (day)')
    plt.ylabel('Weight (kg)')

    # 设置x轴步进
    x_ticks = list(range(1, 32, 1))
    plt.xticks(x_ticks)

    # 展示图形
    plt.show()


# 所有数据绘制一条折线图
def draw_one_line():

    # 日期数据
    start_date = datetime(2023, 7, 17)  # 开始日期
    end_date = datetime(2023, 9, 15)  # 结束日期
    days = (end_date - start_date).days + 1  # 总天数

    # x轴为日期序列
    x = [start_date + timedelta(days=i) for i in range(days)]
    # y轴为对应数据
    y = weight202307 + weight202308 + weight202309

    """
    把x轴显示的内容缩小到step为1
    """
    # ax为两条坐标轴的实例
    # ax = plt.gca()

    # 修改图表尺寸为指定（单位英寸）
    fig, ax = plt.subplots(figsize=(18, 9))
    # 自动格式化日期
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # 把x轴的主刻度设置为1的倍数
    ax.xaxis.set_major_locator(MultipleLocator(1))
    # 自动绘制刻度的话显示的可能比较分散，不好看
    # ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    # 在折线图上显示数值
    for i in range(len(x)):
        # 每个点都展示数据
        plt.text(
            x[i],
            y[i],
            str(y[i]),
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
    plt.title('Weight Trends')

    # 绘制图例
    plt.legend()
    # 设置x轴刻度的旋转角度
    plt.xticks(rotation=270)
    # 显示网格线
    plt.grid(True)

    plt.rcParams['figure.figsize'] = [18, 6]  # 宽度为 8 英寸，高度为 6 英寸

    # 保存为图片文件
    plt.savefig('weight_trend_20230717-202230915.png', dpi=300)

    plt.show()


# 所有数据绘制一条折线图，并带有滑块
def draw_one_line_with_range_slider():
    # 日期数据
    start_date = datetime(2023, 7, 17)  # 开始日期
    end_date = datetime(2023, 9, 15)  # 结束日期
    days = (end_date - start_date).days + 1  # 总天数

    # 生成日期序列
    x = [start_date + timedelta(days=i) for i in range(days)]
    # 对应的数值
    y = weight202307 + weight202308 + weight202309

    # 创建子图
    fig, ax = plt.subplots()

    # 调整子图位置
    plt.subplots_adjust(bottom=0.25)

    # 绘制折线图并保存返回值
    line, = ax.plot(x, y, '.-', label='2023')

    # 绘制x、y轴、标题文字和图例
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.title('Weight Trends')
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
    ax_slider = plt.axes([0.1, 0.05, 0.8, 0.04])

    slider = RangeSlider(
        ax_slider,
        'Range',  # 滑动条的描述文本，显示在滑动条旁边。
        0,  # 滑动条的最小值。
        len(x)-1,  # 滑动条的最大值。
        valinit=[10, len(x)-1],  # 定义滑动条的初始值。
        valstep=1,  # 滑动条的步长。
    )

    # 更新图表函数，根据滑动条的值更新显示范围
    # val 为当前滑块的范围，值类似(10,39)，就是下面的slider.val用于取值
    def update_chart(val):
        # 获取范围滑动条的起始值，并将其转换为整数类型。这将用于切片 x 和 y 的值。
        start_index = int(slider.val[0])
        # 获取范围滑动条的结束值，并将其转换为整数类型。同样，这将用于切片 x 和 y 的值。
        end_index = int(slider.val[1])
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
                xytext=(0, 10),
                textcoords='offset points')  # 文本注释的坐标系统。默认值为 'offset points'，表示偏移量是以点为单位。其他可选值包括 'data'（使用数据坐标系）和 'axes fraction'（使用轴坐标系）等。

        # 启动绘图的命令。该命令将在交互式模式下使用，并且它告诉 matplotlib 在必要时重新绘制已更改的对象。
        fig.canvas.draw_idle()

    # 在一开始就调用一次，以便初始化是就展示描点上方文本
    update_chart((0, len(x)-1))
    # 在滑块变动时及时更新显示的文字
    slider.on_changed(update_chart)

    plt.show()


"""
绘制两个月的体重变化折线图
"""
if __name__ == '__main__':
    # draw_lines_by_month()
    draw_one_line()
    # draw_one_line_with_range_slider()
