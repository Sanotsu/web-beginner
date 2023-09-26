import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import numpy as np
import random

# 生成随机浅色


def generate_light_color():
    r = random.randint(128, 255)  # 生成范围在 128-255 之间的随机红色值
    g = random.randint(128, 255)  # 生成范围在 128-255 之间的随机绿色值
    b = random.randint(128, 255)  # 生成范围在 128-255 之间的随机蓝色值
    return f"#{r:02X}{g:02X}{b:02X}"  # 格式化为十六进制颜色代码


# 绘制组合式条形图的柱子
def plot_detail_bars(ax, positions, data, bar_width, color_dict):
    """
    在给定的坐标系上绘制组合式条形图的柱子。
    参数：
    - ax：用于绘图的坐标系对象
    - positions：柱状图的横坐标值（一维数组）
    - data：要绘制柱子的数据（二维数组，内部为对象数组）
    - bar_width：柱状图的宽度（浮点数）
    - color_dict：颜色字体，data中同一个key使用同一种颜色

    """

    bars = []
    bottom = [0] * len(positions)  # 将bottom改为列表以储存柱形图的高度

    for i in range(len(data)):
        for food in data[i]:
            for name, value in food.items():
                if name not in color_dict:
                    color_dict[name] = generate_light_color()  # 生成随机RGB颜色值
                color = color_dict[name]
                ax.bar(
                    positions[i],
                    value,
                    width=bar_width,
                    align="center",
                    bottom=bottom[i],
                    label=name,
                    color=color,
                    zorder=1,
                )
                # 添加食物键和值的文本标签，并旋转文本
                text_label = f"{name}:{value}"
                ax.text(
                    positions[i],
                    bottom[i] + value / 2,
                    text_label,
                    ha="center",
                    va="center",
                    rotation=90,
                    color="black",
                    fontsize="8",
                )
                bottom[i] += value
        bars.append(bottom[i])

    return bars


# 绘制三餐条形图（三餐和锻炼的柱状图数据结构是一样的，但是y轴刻度单位不一样，所以分为两个图不放在一起）
def draw_three_meals_bar(
    bar_width, ax, positions, dates, breakfast_data, lunch_data, dinner_data
):
    """
    在给定的坐标系上绘制三餐柱状图。
    参数：
    - bar_width：柱状图的宽度（浮点数）
    - ax：用于绘图的坐标系对象
    - positions：柱状图的横坐标值（一维数组）
    - dates：日期列表（一维数组）
    - breakfast_data：每个日期对应的早餐数据（二维数组，内部为对象数组）
    - lunch_data：每个日期对应的早餐数据（二维数组，内部为对象数组）
    - dinner_data：每个日期对应的早餐数据（二维数组，内部为对象数组）
    """

    # 记录食物键对应的颜色
    color_dict = {}

    # 绘制早餐柱状图
    breakfast_bars = plot_detail_bars(
        ax, positions - bar_width, breakfast_data, bar_width, color_dict
    )

    # 绘制午餐柱状图
    lunch_bars = plot_detail_bars(
        ax, positions, lunch_data, bar_width, color_dict)

    # 绘制晚餐柱状图
    dinner_bars = plot_detail_bars(
        ax, positions + bar_width, dinner_data, bar_width, color_dict
    )

    # 设置柱状图的显示范围
    ax.set_ylim(0, max(max(breakfast_bars), max(
        lunch_bars), max(dinner_bars)) * 1.2)

    ax.set_ylabel("摄入量 (g)", color="red")
    ax.tick_params("y", colors="red")

    # 在柱子的顶部显示总摄入量
    for i in range(len(dates)):
        ax.text(
            positions[i] - bar_width,
            breakfast_bars[i] + 10,  # 文字与柱子顶部有点空隙
            f" 早餐:{sum([list(food.values())[0] for food in breakfast_data[i]])}克",
            ha="center",
            va="bottom",
            color="red",  # 与y轴刻度颜色一致
            rotation=90,
        )
        ax.text(
            positions[i],
            lunch_bars[i] + 10,
            f"午餐:{sum([list(food.values())[0] for food in lunch_data[i]])}克",
            ha="center",
            va="bottom",
            color="red",  # 与y轴刻度颜色一致
            rotation=90,
        )
        ax.text(
            positions[i] + bar_width,
            dinner_bars[i] + 10,
            f"晚餐:{sum([list(food.values())[0] for food in dinner_data[i]])}克",
            ha="center",
            va="bottom",
            color="red",  # 与y轴刻度颜色一致
            rotation=90,
        )

    # 不加这个，主函数有旋转也不生效
    plt.xticks(positions, dates, rotation=90)

    return [breakfast_bars, lunch_bars, dinner_bars]


# 绘制体重折线图
def draw_weight_line(ax, dates, weights):
    ax.plot(dates, weights, marker="o", linestyle="-", color="b", zorder=2)
    ax.set_xlabel("日期")
    ax.set_ylabel("体重 (kg)", color="blue")
    ax.tick_params("y", colors="blue")

    # 显示折线图上的数值
    for i in range(len(dates)):
        ax.text(
            dates[i],
            weights[i],
            str(weights[i]),
            ha="center",
            va="bottom",
            color="blue",
        )


# 绘制锻炼条形图
def draw_exercise_bar(bar_width, ax, positions, dates, exercise):
    """
    在给定的坐标系上绘制锻炼柱状图。
    参数：
    - bar_width：柱状图的宽度（浮点数）
    - ax：用于绘图的坐标系对象
    - positions：柱状图的横坐标值（一维数组）
    - dates：日期列表（一维数组）
    - exercise：每个日期对应的锻炼量（二维数组，内部为对象数组）
    """

    # 记录食物键对应的颜色
    color_dict = {}

    # 绘制锻炼柱状图（和三餐的柱状图空1个预设柱宽度。实际数据太多时，不留空，就 + 3 * bar_width）
    exercise_bars = plot_detail_bars(
        ax, positions + 2 * bar_width, exercise, bar_width, color_dict
    )

    # 设置柱状图的显示范围
    ax.set_ylim(0, max(exercise_bars) * 1.2)

    # 将y轴右侧边框线从默认位置移动到1.05倍axes的宽度处
    ax.spines["right"].set_position(("axes", 1.05))

    # y轴的刻度
    ax.set_ylabel("锻炼量 (分钟/次)", color="grey")
    ax.tick_params("y", colors="grey")

    # 在柱子的顶部显示总摄入量
    for i in range(len(dates)):
        ax.text(
            positions[i] + 2 * bar_width,  # 和三餐的柱状图空1个预设柱宽度(数据太多就不留)
            exercise_bars[i],  # 文字与柱子顶部有点空隙
            f" 锻炼:{sum([list(food.values())[0] for food in exercise[i]])}",
            ha="center",
            va="bottom",
            color="grey",  # 与y轴刻度颜色一致
            rotation=90,
        )

    # 不加这个，主函数有旋转也不生效
    plt.xticks(positions, dates, rotation=90)


# 绘制图表的主入口
def draw_weight_intake_exercise_detail(
    bar_width, dates, weights, breakfast_data, lunch_data, dinner_data, exercise_data
):
    """
    参数分别为：
    bar_width：柱状图的宽度
    date：x轴坐标日期列表
    weights：体重列表
    breakfast_data：早餐列表
    lunch_data：午餐列表
    dinner_data：晚餐列表
    exercise_data：锻炼列表(后4个列表结构一样)
    """

    # 生成日期的索引(横坐标的索引列表)

    # 注意，因为每个刻度的最左边的柱状图是positions - bar_width，而整体的柱状图占位是5（4个柱子+空隙）
    # 所以位置索引要稍微偏一点，才能使得x轴刻度标签居中
    # positions = np.arange(len(dates)) - 1 * bar_width

    positions = np.arange(len(dates)) - 0.5 * bar_width

    # 于创建一个新的图形窗口和坐标系，并将其分配给变量 fig 和 ax
    # fig 是代表整个图形窗口的对象，可以用于设置图形窗口的属性和保存图形。
    # meal_ax 是代表子图（坐标系）的对象，可以用于对子图进行各种操作，包括绘制图形、设置坐标轴、添加标签等。
    # figsize=(10, 6) 是一个可选参数，用于指定图形窗口的尺寸，单位是英寸。这里设置的尺寸是宽度为 10 英寸，高度为 6 英寸。
    fig, meal_ax = plt.subplots(figsize=(16, 8))
    draw_three_meals_bar(
        bar_width, meal_ax, positions, dates, breakfast_data, lunch_data, dinner_data
    )

    # 创建一个与 meal_ax 坐标系共享 x 轴的另一个坐标系 exercise_ax，可以在同一个图形窗口中同时显示两个不同的坐标系。
    exercise_ax = meal_ax.twinx()
    # 绘制运动柱状图
    draw_exercise_bar(bar_width, exercise_ax, positions, dates, exercise_data)

    # 创建一个与 meal_ax 坐标系共享 x 轴的另一个坐标系
    weight_ax = meal_ax.twinx()
    # 绘制体重趋势折线图
    draw_weight_line(weight_ax, dates, weights)

    plt.title("体重趋势与摄入量、运动量")
    plt.xticks(positions, dates, rotation=90, fontsize=8)

    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["figure.autolayout"] = True

    # 设置图片显示(有tight layout就没效果了)
    plt.subplots_adjust(bottom=0.12, top=0.95, left=0.04, right=0.92)

    # 添加范围滑块
    slider_ax = plt.axes([0.7, 0.95, 0.2, 0.04])  # 滑块位置，右上角
    slider = RangeSlider(
        slider_ax,
        '日期范围',
        valmin=0,
        valmax=len(dates)-1,
        valstep=1,
        valinit=(0, len(dates)-1),
    )

    # 滑块变动时，只显示指定x轴范围的数据，其他位置的文本也隐藏
    def update(val):
        start_index, end_index = val  # 获取滑块的值
        start_index = int(start_index)
        end_index = int(end_index)
        weight_ax.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围
        exercise_ax.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围
        meal_ax.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围

        # 选择了滑块范围之后，重新绘制各项图，避免缩小范围后y轴外面还显示文字
        axes = [weight_ax, meal_ax, exercise_ax]

        for ax in axes:
            for annotation in ax.texts:
                x = annotation.get_position()[0]

                # 柱状图取位置是索引，但这个折线图是日期字符串，所以取得对应日期字符串所在的索引再比较
                if ax == weight_ax:  # 仅在 weight_ax 中进行索引转换
                    x = dates.index(str(x))

                # 滑块之外的设置不可见，滑块内的设置为可见
                if x < start_index-0.5 or x > end_index+0.5:
                    # annotation.remove()
                    annotation.set_visible(False)
                else:
                    annotation.set_visible(True)

        fig.canvas.draw_idle()  # 重新绘制图形

    slider.on_changed(update)

    # dpi表示每英寸点数，bbox_inches='tight'会裁剪边界框，以适应图表内容
    fig.savefig('./_output/weight_intake_exercise_detail.png',
                dpi=300,  bbox_inches='tight')

    plt.show()


# if __name__ == "__main__":

#     # 条形图的默认宽度
#     bar_width = 0.2

#     start_date = datetime(2023, 9, 1)  # 开始日期
#     end_date = datetime(2023, 9, 18)  # 结束日期
#     days = (end_date - start_date).days + 1  # 总天数

#     # x轴为日期序列，并格式化
#     original_dates = [start_date + timedelta(days=i) for i in range(days)]

#     date_format = "%Y年%m月%d日"

#     # x轴的日期数据（各个y轴数据都共用同一个x轴）
#     formatted_dates = [date.strftime(date_format) for date in original_dates]

#     # 指定JSON文件的路径
#     weight_file_path = "./_input_data/sept/weight_records.json"
#     breakfast_file_path = "./_input_data/sept/breakfast_records.json"
#     lunch_file_path = "./_input_data/sept/lunch_records.json"
#     dinner_file_path = "./_input_data/sept/dinner_records.json"
#     exercise_file_path = "./_input_data/sept/exercise_records.json"

#     # 打开文件并读取JSON数据（y轴的各项数据）
#     with open(weight_file_path, "r", encoding="utf-8", errors="ignore") as file:
#         weight_data = json.load(file)

#     with open(breakfast_file_path, "r", encoding="utf-8", errors="ignore") as file:
#         breakfast_data = json.load(file)

#     with open(lunch_file_path, "r", encoding="utf-8", errors="ignore") as file:
#         lunch_data = json.load(file)

#     with open(dinner_file_path, "r", encoding="utf-8", errors="ignore") as file:
#         dinner_data = json.load(file)

#     with open(exercise_file_path, "r", encoding="utf-8", errors="ignore") as file:
#         exercise_data = json.load(file)

#     plot_weight_intake(bar_width, formatted_dates, weight_data,
#                        breakfast_data, lunch_data, dinner_data, exercise_data,)
