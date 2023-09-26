from datetime import datetime, timedelta
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
# 这个是之前 weight_intake_exercise 中的处理类似，只不过两者的源数据结构不一样（应该想办法弄成一样的）
def plot_detail_bars(ax, positions, data, bar_width, color_dict, font_size):
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
        # 这里的 data[i] 结构是 [{'k': "abs", 'v': 19}, {'k': "dumbbell", 'v': 19}],
        # 这里的 exercise 结构是 {'k': "abs", 'v': 19}
        for exercise in data[i]:
            # exercise['k'] 取得每项运动的key，如果这个key是新的，则使用新的颜色；已存在，就使用旧的颜色
            name = exercise['k']
            if name not in color_dict:
                color_dict[name] = generate_light_color()  # 生成随机RGB颜色值
            color = color_dict[name]

            # exercise['v'] 取得每项运动的value。
            value = exercise['v']
            # 绘制柱状图，有多少个key就要绘制多少个柱子，但后一个柱子高度会y轴偏移前一个柱子的高度
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
                # 没有锻炼的，y轴偏移5再显示文字
                bottom[i] + value / 2 if bottom[i] + value / 2 > 0 else 5,
                text_label,
                ha="center",
                va="center",
                rotation=90,
                color="black",
                fontsize=font_size,
            )
            # 每绘制一个柱子，下一个柱子底部就偏移前一个柱子的高度
            bottom[i] += value

        bars.append(bottom[i])

    return bars


# === 绘制锻炼条形图(子项可以由不同颜色区分，但图例的平均值没法改变)
def draw_exercise_bar(bar_width, ax, dates, exercise, font_size):
    """
    在给定的坐标系上绘制锻炼柱状图。
    参数：
    - bar_width：柱状图的宽度（浮点数）
    - ax：用于绘图的坐标系对象
    - dates：日期列表（一维数组）
    - exercise：每个日期对应的锻炼量（二维数组，内部为对象数组）
    """

    # 柱状图的横坐标值（一维数组）
    positions = np.arange(len(dates))

    # 记录食物键对应的颜色
    color_dict = {}

    # 绘制锻炼柱状图（因为前面有个摄入的柱子，所以宽度要加一个柱子宽度）
    exercise_bars = plot_detail_bars(
        ax, positions + bar_width, exercise, bar_width, color_dict, font_size
    )

    # 设置柱状图的显示范围
    ax.set_ylim(0, max(exercise_bars) * 1.2)

    # 在柱子的顶部显示总摄入量
    for i in range(len(dates)):
        value = sum([exercise['v'] for exercise in exercise[i]])
        ax.text(
            positions[i] + bar_width,  # 和三餐的柱状图空1个预设柱宽度(数据太多就不留)
            # exercise_bars[i]+1,  # 文字与柱子顶部有点空隙（+1 是根据刻度的高度）
            exercise_bars[i],
            f" 锻炼:{value}",
            ha="center",
            va="bottom",
            color="grey",  # 与y轴刻度颜色一致
            rotation=90,
            fontsize=font_size,
        )

    # 不加这个，主函数有旋转也不生效
    plt.xticks(positions, dates, rotation=90)


# 绘制摄入条形图(锻炼子项不会用其他颜色区分，但图例处可以显示使用平均值)
def draw_exercise_merged_bar(bar_width, ax, dates, data, font_size):

    exercise_arr = [sum([exercise['v'] for exercise in month_data])
                    for month_data in data]

    exercise_label_arr = [
        ",".join([f"{exercise['k']}:{exercise['v']}" for exercise in month_data]) for month_data in data
    ]

    # 坐标系1绘制柱状图
    exercise_bar = ax.bar(
        np.arange(len(dates))+bar_width,
        exercise_arr,
        width=bar_width,
        color="grey",
    )

    # 柱状图的横坐标值（一维数组）
    positions = np.arange(len(dates))

    # 在柱子的顶部显示总摄入量
    for i in range(len(dates)):
        value = sum([exercise['v'] for exercise in data[i]])
        ax.text(
            positions[i]+bar_width,
            # exercise_arr[i],
            exercise_arr[i] if exercise_arr[i] > 10 else 10,
            f" 锻炼:{value}",
            ha="center",
            va="bottom",
            color="grey",  # 与y轴刻度颜色一致
            rotation=90,
            fontsize=font_size,
        )

        # 柱子内部文字
        ax.text(
            positions[i]+bar_width,
            1,  # 标签从最底部往上(贴着底不好看就偏一点，实际高度根据刻度值来)
            exercise_label_arr[i],
            rotation=90,
            ha='center',
            va='bottom',  # 从底部往上显示标签值
            color='black',
            fontsize=font_size,
        )

        # 设置第一个 y 轴的范围和刻度并限定y轴范围（不设定就从0开始）
    ax.set_ylim([0, None])
    # 设置y轴的刻度间隔（这里500往上才显示刻度，以下不显示。因为step就是500,所以没差）
    # rang的上限+1500是为了让weight折现在柱子上面，不遮挡。
    ax.set_yticks(np.arange(0, max(exercise_arr)+80, 20))

    return exercise_bar


# 绘制摄入条形图
def draw_intake_bar(bar_width, intake_ax, dates, intake_data, font_size):

    intake_arr = [x["v"] for month_data in intake_data.values()
                  for x in month_data]

    # 坐标系1绘制柱状图
    intake_bar = intake_ax.bar(
        np.arange(len(dates)),
        intake_arr,
        width=bar_width,
        color="#00FF00",
    )

    # 给摄入柱状图绘制文字(柱子中标签，顶部数值)
    idx = 0
    for month_key, month_data in intake_data.items():
        month_len = len(month_data)
        for i in range(month_len):
            label = month_data[i]["k"]
            value = month_data[i]["v"]

            # 柱子顶部文字
            intake_ax.text(
                idx,  # 标签的 x 坐标位置。这里是柱子的中心位置，即柱子的x轴偏移量加上半个柱子的宽度。
                # 标签的 x 坐标位置。这里摄入的数值显示在柱子顶部
                # 如果柱子小于500,在顶部显示数值可能会和标签重叠，所以稍微区别一下
                intake_arr[idx]+20 if value > 500 else 500,
                f"摄入:{value}",  # 要显示的文本内容。这里是摄入的数值
                ha='center',  # 水平对齐方式。可选值包括 'center'(默认)、'right'、'left'。
                # 垂直对齐方式。可选值包括 'center'、'top'、'bottom'、'baseline'(默认)。
                va='bottom',
                color='black' if label == "清淡饮食" else "red",
                rotation=90,
                fontsize=font_size,
            )

            # 柱子内部文字
            intake_ax.text(
                idx,
                20,  # 标签从最底部往上(贴着底不好看就偏一点)
                label,
                rotation=90,
                ha='center',
                va='bottom',  # 从底部往上显示标签值
                color='black' if label == "清淡饮食" else "red",  # 如果不是清淡饮食就显示红色
                fontsize=font_size,
            )
            idx += 1

    # == 注意，吧这个y轴刻度范围限制提到上面，范围设置似乎就失效了
    # 设置第一个 y 轴的范围和刻度并限定y轴范围（不设定就从0开始）
    intake_ax.set_ylim([0, None])
    # 设置y轴的刻度间隔（这里500往上才显示刻度，以下不显示。因为step就是500,所以没差）
    # rang的上限+2000是为了让weight折现在柱子上面，不遮挡。
    intake_ax.set_yticks(np.arange(500, max(intake_arr)+2000, 500))

    return intake_bar


# 绘制体重折线图
def draw_weight_line(weight_ax, weight_arr):
    # 坐标系2绘制折线图(虚线，描点为圆点)
    weight_line = weight_ax.plot(weight_arr, linestyle="--",
                                 linewidth=0.7, marker="o", color="blue")

    # 给折线图描点绘制数值
    for i in range(len(weight_arr)):
        weight_ax.text(
            i,
            weight_arr[i]+0.2,  # 文字稍微上一点别被线遮住
            f'{weight_arr[i]:.2f}',
            ha='center',
            va='bottom',
            fontsize=8,
        )

     # 并限定y轴范围（y轴下方与最小值间隔多一点，避免与下方的柱子重叠，但可能折线上数据会重叠，因为高度不够）
    weight_ax.set_ylim([int(min(weight_arr))-18, None])
    # 设置y轴的刻度间隔（这里y轴从60开始，但是70往上，step为1才显示刻度）
    weight_ax.set_yticks(np.arange(int(min(weight_arr)), max(weight_arr)+2, 1))

    return weight_line


# 添加平均值参考线(指定范围、坐标系、数组)
def add_reference_line(ref_ax, ref_arr, color):

    # 计算摄入平均值
    ref_mean = np.mean(ref_arr)

    # 添加每天摄入量的平均值参考线和标注文本
    ref_mean_line = ref_ax.axhline(
        ref_mean, color=color, linestyle='--')

    # 平均线文字不好看，就看图例上即可
    ref_mean_label = ref_ax.text(
        0,
        ref_mean,
        f"平均值: {ref_mean:.2f}",
        ha='left',
        va='bottom',
        # color=color,
        color="black",
    )

    return ref_mean_line, ref_mean_label


# 绘制参考图例(带平均值)
def add_refrence_legend(ax, bar, mean_line, data_arr, legend_name, loc):

    mean_value = np.mean(data_arr)

    # 摄入的图例有两个：柱子和平均线
    ax.legend(
        [bar, mean_line],
        [legend_name, f'{legend_name} 平均值: {mean_value:.2f}'],
        loc="upper right",
        bbox_to_anchor=loc
    )
    pass


# 添加范围滑块
def add_range_slider(dates) -> RangeSlider:
    slider_ax = plt.axes([0.7, 0.95, 0.2, 0.04])  # 滑块位置，右上角
    slider = RangeSlider(
        slider_ax,
        'data range',
        valmin=0,
        valmax=len(dates)-1,
        valstep=1,
        valinit=(0, len(dates)-1),
    )

    return slider


# === 参考线更新单独函数也会报错。
def update_refrence_line(ax, data_arr, start_index, end_index, mean_line, mean_label):

    new_mean = np.mean(data_arr[start_index:end_index])

    # 移除旧的参考线和数值文本，并添加新的
    mean_line.remove()
    mean_line = ax.axhline(
        new_mean, color='gray', linestyle='--')

    mean_label.remove()
    mean_label = ax.text(
        end_index-1,
        new_mean,
        f"平均值: {new_mean:.2f}",
        ha='right',
        va='bottom',
        color='black',
    )


# 滑块数值更新事件
def slider_update(slider, intake_ax, weight_ax, exercise_ax, intake_arr, exercise_arr,
                  intake_bar, exercise_bar, intake_mean_line, intake_mean_label,
                  exercise_mean_line, exercise_mean_label):

    # 滑块变动时，只显示指定x轴范围的数据，其他位置的文本也隐藏

    def update(val):

        # 获取滑块的值
        start_index, end_index = val
        start_index = int(start_index)
        end_index = int(end_index)

        # 有0.5在滑动时左右边缘就不会显示半个
        # intake_ax.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围
        # weight_ax.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围

        # 选择了滑块范围之后，重新绘制各项图，避免缩小范围后y轴外面还显示文字
        axes = [intake_ax, weight_ax, exercise_ax]
        for ax in axes:

            # 有0.5在滑动时左右边缘就不会显示半个
            ax.set_xlim(start_index-0.5, end_index+0.5)

            for annotation in ax.texts:
                # 取得标签文字的x轴坐标
                x = annotation.get_position()[0]
                # 滑块之外的x轴上标签文字设置不可见，滑块内的设置为可见
                if x < start_index-0.5 or x > end_index+0.5:
                    # annotation.remove()
                    annotation.set_visible(False)
                else:
                    annotation.set_visible(True)

        # 选择滑动块指定范围后，平均值和参考线要重新计算和绘制
        new_intake_mean = np.mean(intake_arr[start_index:end_index])
        new_exercise_mean = np.mean(exercise_arr[start_index:end_index])

        # 在update函数中，intake_mean_line的作用域不是全局范围内，所以不能直接在函数内部引用它。
        # 为了解决这个问题，可以使用 nonlocal 声明将其声明为嵌套作用域内的变量。
        nonlocal intake_mean_line, intake_mean_label, exercise_mean_line, exercise_mean_label

        # update_refrence_line(
        #     intake_ax, intake_arr,
        #     start_index, end_index,
        #     intake_mean_line, intake_mean_label,
        # )

        # 移除旧的参考线和数值文本，并添加新的
        intake_mean_line.remove()
        intake_mean_line = intake_ax.axhline(
            new_intake_mean, color='gray', linestyle='--')

        intake_mean_label.remove()
        intake_mean_label = intake_ax.text(
            start_index,  # 平均线标签文字显示在左边
            new_intake_mean,
            f"平均值: {new_intake_mean:.2f}",
            ha='left',
            va='bottom',
            color='black',
        )
        # 滑块变更返回不显示文字，去看图例(依旧添加文本是因为上面有移除，没有文本移除会报错)
        intake_mean_label.set_visible(False)

        exercise_mean_line.remove()
        exercise_mean_line = exercise_ax.axhline(
            new_exercise_mean, color='#dfebe2', linestyle='--')

        exercise_mean_label.remove()
        exercise_mean_label = exercise_ax.text(
            start_index,
            new_exercise_mean,
            f"平均值: {new_exercise_mean:.2f}",
            ha='left',
            va='bottom',
            color='black',
        )
        # 滑块变更返回不显示文字，去看图例(依旧添加文本是因为上面有移除，没有文本移除会报错)
        exercise_mean_label.set_visible(False)

        # 图例更新即可
        intake_ax.legend(
            [intake_bar, intake_mean_line],
            ['Intake', f'Intake 平均值: {new_intake_mean:.2f}'],
            loc="upper right",
            bbox_to_anchor=(0.93, 1.01)
        )

        exercise_ax.legend(
            [exercise_bar, exercise_mean_line],
            ['Exercise', f'Exercise 平均值: {new_exercise_mean:.2f}'],
            loc="upper right",
            bbox_to_anchor=(0.78, 1.01)
        )

        # fig.canvas.draw_idle()  # 重新绘制图形
        # 重新绘制图表
        plt.draw()

    slider.on_changed(update)


# 创建坐标系
def create_plot(dates):
    # 创建坐标系和实例
    fig, intake_ax = plt.subplots(figsize=(16, 8))
    # 设置x轴的刻度和标签
    intake_ax.set_xticks(range(len(dates)))
    intake_ax.set_xticklabels(dates, rotation=90)
    # 设置共用的x轴和不同的y轴的名称和颜色
    intake_ax.set_xlabel("Date (day)")
    intake_ax.set_ylabel("Intake (kcal)", color='green')
    intake_ax.tick_params("y", colors="green")

    # 创建一个与 intake_ax 坐标系共享 x 轴的另一个坐标系 weight_ax
    weight_ax = intake_ax.twinx()
    weight_ax.set_ylabel("Weight (kg)", color='blue')
    weight_ax.tick_params("y", colors="blue")

    # 创建一个与 intake_ax 坐标系共享 x 轴的另一个坐标系 exercise_ax
    exercise_ax = intake_ax.twinx()
    # y轴的刻度和颜色
    exercise_ax.set_ylabel("Exercise (min)", color="grey")
    exercise_ax.tick_params("y", colors="grey")
    # 将y轴右侧边框线从默认位置移动到1.05倍axes的宽度处
    exercise_ax.spines["right"].set_position(("axes", 1.05))

    # 图表的标题
    plt.title("Daily Intake、Exercise and Weight")
    plt.tight_layout()
    plt.grid(True)

    return fig, weight_ax, intake_ax, exercise_ax


# 处理日期数据
def generate_dates(start_date, end_date):
    # 生成日期列表
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates


# 主函数
def draw_weight_intake_exercise_simple(bar_width, start_date, end_date, intake_data, weight_data, exercise_data):

    # 统一的文本显示大小
    font_size = 8

    # 提取每天的摄入量、体重数据、运动总量
    intake_arr = [x["v"] for month_data in intake_data.values()
                  for x in month_data]
    weight_arr = [x for month_data in weight_data.values() for x in month_data]
    exercise_arr = [sum([exercise['v'] for exercise in month_data])
                    for month_data in exercise_data]

    # 生成日期列表
    dates = generate_dates(start_date, end_date)

    # 创建坐标系
    [fig, weight_ax, intake_ax, exercise_ax] = create_plot(dates)

    # 绘制运动柱状图
    # draw_exercise_bar(
    #     bar_width, exercise_ax, dates, exercise_data, font_size)

    exercise_bar = draw_exercise_merged_bar(
        bar_width, exercise_ax, dates, exercise_data, font_size)

    # 绘制摄入柱状图
    intake_bar = draw_intake_bar(
        bar_width, intake_ax, dates, intake_data, font_size)
    # 绘制体重折线图
    weight_line = draw_weight_line(weight_ax, weight_arr)

    # 绘制摄入参考线
    [intake_mean_line, intake_mean_label] = add_reference_line(
        intake_ax, intake_arr, "grey")

    [exercise_mean_line, exercise_mean_label] = add_reference_line(
        exercise_ax, exercise_arr, "#6cf08f")

    # 添加折线图图例，调整位置(没有其他特殊设定)
    weight_ax.legend(["Weight"], loc="upper right",
                     bbox_to_anchor=(1.0, 1.01))
    # 添加图例(可根据滑块选中内容在图例显示平均值)
    add_refrence_legend(intake_ax, intake_bar,
                        intake_mean_line, intake_arr,
                        "intake", (0.93, 1.01))
    add_refrence_legend(exercise_ax, exercise_bar,
                        exercise_mean_line, exercise_arr,
                        "exercise",  (0.78, 1.01))

    # 添加滑块和滑块更新写到一起，滑块事件会失效，原因还没去分析
    # 添加滑块
    slider = add_range_slider(dates)
    # 滑块更新事件。滑块范围变化是触发文本更新
    slider_update(
        slider, intake_ax, weight_ax, exercise_ax,
        intake_arr, exercise_arr, intake_bar, exercise_bar,
        intake_mean_line, intake_mean_label, exercise_mean_line, exercise_mean_label,
    )

    # dpi表示每英寸点数，bbox_inches='tight'会裁剪边界框，以适应图表内容
    fig.savefig('./_output/weight_intake_exercise_simple.png',
                dpi=300,  bbox_inches='tight')
    plt.show()
