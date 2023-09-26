from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# 绘制摄入条形图(锻炼子项不会用其他颜色区分，但图例处可以显示使用平均值)
def draw_exercise_merged_bar(bar_width, main_ax, dates, data, font_size):

    # 创建一个与主坐标系共享 x 轴的另一个坐标系 exercise_ax
    exercise_ax = main_ax.twinx()
    # y轴的刻度和颜色
    exercise_ax.set_ylabel("Exercise (min)", color="grey")
    exercise_ax.tick_params("y", colors="grey")
    # 将y轴右侧边框线从默认位置移动到1.05倍axes的宽度处
    exercise_ax.spines["right"].set_position(("axes", 1.05))

    exercise_arr = [sum([exercise['v'] for exercise in month_data])
                    for month_data in data]

    exercise_label_arr = [
        ",".join([f"{exercise['k']}:{exercise['v']}" for exercise in month_data]) for month_data in data
    ]

    # 坐标系1绘制柱状图
    exercise_bar = exercise_ax.bar(
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
        exercise_ax.text(
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
        exercise_ax.text(
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
    exercise_ax.set_ylim([0, None])
    # 设置y轴的刻度间隔（这里500往上才显示刻度，以下不显示。因为step就是500,所以没差）
    # rang的上限+1500是为了让weight折现在柱子上面，不遮挡。
    exercise_ax.set_yticks(np.arange(0, max(exercise_arr)+80, 20))

    return exercise_bar, exercise_ax


# 绘制摄入条形图
def draw_intake_bar(bar_width, main_ax, dates, intake_data, font_size):

    # 创建一个与主坐标系共享 x 轴的另一个坐标系 intake_ax
    intake_ax = main_ax.twinx()
    intake_ax.set_ylabel("Intake (kcal)", color='green')
    intake_ax.tick_params("y", colors="green")

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

    return intake_bar, intake_ax


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


# 滑块数值更新事件
def slider_update(
    slider, weight_ax,
    is_show_intake,
    is_show_exercise,
    options,
):

    # 坐标系默认只有体重的，摄入和锻炼根据是否显示而加入
    axes = [weight_ax]

    # 这个取变量放在update()里的话，nonlocal就会报错了
    if is_show_intake:
        intake_ax = options["intake_ax"]
        intake_arr = options["intake_arr"]
        intake_bar = options["intake_bar"]
        intake_mean_line = options["intake_mean_line"]
        intake_mean_label = options["intake_mean_label"]

        axes.append(intake_ax)

    if is_show_exercise:
        exercise_ax = options["exercise_ax"]
        exercise_arr = options["exercise_arr"]
        exercise_bar = options["exercise_bar"]
        exercise_mean_line = options["exercise_mean_line"]
        exercise_mean_label = options["exercise_mean_label"]

        axes.append(exercise_ax)

    # 滑块变动时，只显示指定x轴范围的数据，其他位置的文本也隐藏

    def update(val):
        # 获取滑块的值
        start_index, end_index = val
        start_index = int(start_index)
        end_index = int(end_index)

        # 如果显示了摄入柱状图，滑块更新后要做的事情
        if is_show_intake:

            # 在update函数中，intake_mean_line的作用域不是全局范围内，所以不能直接在函数内部引用它。
            # 为了解决这个问题，可以使用 nonlocal 声明将其声明为嵌套作用域内的变量。
            nonlocal intake_mean_line, intake_mean_label

            new_intake_mean = np.mean(intake_arr[start_index:end_index])

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

            # 图例更新即可
            intake_ax.legend(
                [intake_bar, intake_mean_line],
                ['Intake', f'Intake 平均值: {new_intake_mean:.2f}'],
                loc="upper right",
                bbox_to_anchor=(0.93, 1.01)
            )

        # 如果显示了锻炼柱状图，滑块更新后要做的事情
        if is_show_exercise:
            # 在update函数中，intake_mean_line的作用域不是全局范围内，所以不能直接在函数内部引用它。
            # 为了解决这个问题，可以使用 nonlocal 声明将其声明为嵌套作用域内的变量。
            nonlocal exercise_mean_line, exercise_mean_label

            # 选择滑动块指定范围后，平均值和参考线要重新计算和绘制
            new_exercise_mean = np.mean(exercise_arr[start_index:end_index])

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

            exercise_ax.legend(
                [exercise_bar, exercise_mean_line],
                ['Exercise', f'Exercise 平均值: {new_exercise_mean:.2f}'],
                loc="upper right",
                bbox_to_anchor=(0.78, 1.01)
                if is_show_intake else (0.93, 1.01),
            )

        # 选择了滑块范围之后，重新绘制各项图，避免缩小范围后y轴外面还显示文字
        for ax in axes:

            # 设置x轴范围，有0.5在滑动时左右边缘就不会显示半个
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

        # fig.canvas.draw_idle()  # 重新绘制图形
        # 重新绘制图表
        plt.draw()

    slider.on_changed(update)


# 创建主坐标系
def create_plot(dates):
    """创建坐标系，默认只有体重的，摄入和锻炼的改为了可选显示，所以在绘制图表时才创建坐标系

    Args:
        dates (list): x轴显示的日期范围

    Returns:
        _type_: 图和主坐标轴
    """

    # 创建坐标系和实例
    fig, weight_ax = plt.subplots(figsize=(16, 8))

    # 调整子图布局
    fig.subplots_adjust(top=0.96, bottom=0.129, left=0.032,
                        right=0.921, hspace=0.2, wspace=0.2)

    # 设置x轴的刻度和标签
    weight_ax.set_xticks(range(len(dates)))
    weight_ax.set_xticklabels(dates, rotation=90)
    # 设置共用的x轴和不同的y轴的名称和颜色
    weight_ax.set_xlabel("Date (day)")
    weight_ax.set_ylabel("Weight (kg)", color='blue')
    weight_ax.tick_params("y", colors="blue")

    # 图表的标题
    plt.title("Daily Intake、Exercise and Weight")
    # fig.tight_layout()

    plt.grid(True)

    return fig, weight_ax

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
def draw_weight_intake_exercise_simple_optional(
        bar_width, start_date, end_date,
        intake_data, weight_data, exercise_data,
        is_show_intake=True, is_show_exercise=True
):
    """体重折线是一定会显示的，但摄入和锻炼的柱状图，改为可指定是否显示

    Args:
        bar_width (number): 柱状图宽度
        start_date (datetime): 开始日期
        end_date (datetime): 结束日期
        intake_data (list): 摄入数据
        weight_data (list): 体重数据
        exercise_data (list): 锻炼数据
        is_show_intake (bool, optional): 是否显示摄入柱状图. Defaults to True.
        is_show_exercise (bool, optional): 是否显示锻炼柱状图. Defaults to True.
    """

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
    [fig, weight_ax] = create_plot(dates)
    # 绘制体重折线图
    draw_weight_line(weight_ax, weight_arr)
    # 添加折线图图例，调整位置(没有其他特殊设定)
    weight_ax.legend(["Weight"], loc="upper right",
                     bbox_to_anchor=(1.0, 1.01))

    # 根据显示的内容记录更新时需要传入的配置
    intake_options = {}
    exercise_options = {}

    # 绘制锻炼状图
    if is_show_exercise:
        [exercise_bar, exercise_ax] = draw_exercise_merged_bar(
            bar_width, weight_ax, dates, exercise_data, font_size)

        # 绘制锻炼平均参考线
        [exercise_mean_line, exercise_mean_label] = add_reference_line(
            exercise_ax, exercise_arr, "#6cf08f")

        # 添加锻炼图例(可根据滑块选中内容在图例显示平均值)
        add_refrence_legend(
            exercise_ax, exercise_bar,
            exercise_mean_line, exercise_arr,
            "exercise",
            (0.78, 1.01) if is_show_intake else (0.93, 1.01),
        )

        exercise_options = {
            "exercise_ax": exercise_ax, "exercise_arr": exercise_arr, "exercise_bar": exercise_bar,
            "exercise_mean_line": exercise_mean_line, "exercise_mean_label": exercise_mean_label
        }

    # 绘制摄入柱状图
    if is_show_intake:
        [intake_bar, intake_ax] = draw_intake_bar(
            bar_width, weight_ax, dates, intake_data, font_size)

        # 绘制摄入平均参考线
        [intake_mean_line, intake_mean_label] = add_reference_line(
            intake_ax, intake_arr, "grey")

        # 添加摄入图例(可根据滑块选中内容在图例显示平均值)
        add_refrence_legend(
            intake_ax, intake_bar,
            intake_mean_line, intake_arr,
            "intake", (0.93, 1.01),
        )

        intake_options = {
            "intake_ax": intake_ax, "intake_arr": intake_arr, "intake_bar": intake_bar,
            "intake_mean_line": intake_mean_line, "intake_mean_label": intake_mean_label
        }

    # 添加滑块和滑块更新写到一起，滑块事件会失效，原因还没去分析
    # 滑块更新事件也根据展示的内容而有所不同
    slider = add_range_slider(dates)
    # 要更新的内容根据选择显示的内容而定
    options = {**intake_options, **exercise_options}
    # 滑块更新事件。滑块范围变化是触发文本更新
    slider_update(
        slider, weight_ax,
        is_show_intake,
        is_show_exercise,
        options
    )

    # dpi表示每英寸点数，bbox_inches='tight'会裁剪边界框，以适应图表内容
    fig.savefig('./_output/weight_intake_exercise_simple_optional.png',
                dpi=300,  bbox_inches='tight')

    fig.tight_layout()

    plt.show()
