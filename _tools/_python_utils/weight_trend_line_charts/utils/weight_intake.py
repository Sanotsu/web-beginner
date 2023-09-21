from matplotlib.widgets import RangeSlider
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta


def draw_intake_and_weight(start_date, end_date, intake_data, weight_data):
    # 生成日期列表
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    # 划分数据到月份中(传入数据可能时间跨度多个月，这里拼接每个月的数据)
    start_month = start_date.strftime('%Y%m')
    end_month = end_date.strftime('%Y%m')
    months = []
    current_month = start_month
    while current_month <= end_month:
        months.append(current_month)
        year = int(current_month[0:4])
        month = int(current_month[4:6])
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        current_month = f"{year:04d}{month:02d}"

    # 创建坐标系和实例
    fig, ax1 = plt.subplots(figsize=(16, 8))

    # 创建第二个坐标系，但和第一个共用x轴
    ax2 = ax1.twinx()
    # 设置x轴的刻度和标签
    ax1.set_xticks(range(len(dates)))
    ax1.set_xticklabels(dates, rotation=90)
    # 设置共用的x轴和不同的y轴的名称
    ax1.set_xlabel("Date (day)")
    ax1.set_ylabel("Intake (kcal)", color='green')
    ax2.set_ylabel("Weight (ky)", color='blue')

    # 提取每天的摄入量和体重数据
    intake_arr = [x["v"] for month_data in intake_data.values()
                  for x in month_data]
    weight_arr = [x for month_data in weight_data.values() for x in month_data]

    # 计算摄入平均值
    intake_mean = np.mean(intake_arr)

    # 坐标系1绘制柱状图
    intake_bar = ax1.bar(np.arange(len(dates)), intake_arr, color="#d9d4c5")
    # 坐标系2绘制折线图(虚线，描点为圆点)
    ax2.plot(weight_arr, linestyle="--",
             linewidth=0.7, marker="o", color="blue")

    # 给摄入柱状图绘制文字(柱子中标签，顶部数值)
    idx = 0
    for month_key, month_data in intake_data.items():
        month_len = len(month_data)
        for i in range(month_len):
            label = month_data[i]["k"]
            value = month_data[i]["v"]
            ax1.text(
                idx,  # 标签的 x 坐标位置。这里是柱子的中心位置，即柱子的x轴偏移量加上半个柱子的宽度。
                # 标签的 x 坐标位置。这里摄入的数值显示在柱子顶部
                # 如果柱子小于500,在顶部显示数值可能会和标签重叠，所以稍微区别一下
                intake_arr[idx] if value > 500 else 500,
                value,  # 要显示的文本内容。这里是摄入的数值
                ha='center',  # 水平对齐方式。可选值包括 'center'(默认)、'right'、'left'。
                # 垂直对齐方式。可选值包括 'center'、'top'、'bottom'、'baseline'(默认)。
                va='bottom',
                color='grey' if label == "清淡饮食" else "red"
            )

            ax1.text(
                idx,
                20,  # 标签从最底部往上(贴着底不好看就偏一点)
                label,
                rotation=90,
                ha='center',
                va='bottom',  # 从底部往上显示标签值
                color='grey' if label == "清淡饮食" else "red"  # 如果不是清淡饮食就显示红色
            )
            idx += 1

    # 给折线图描点绘制数值
    for i in range(len(weight_arr)):
        ax2.text(
            i,
            weight_arr[i]+0.2,  # 文字稍微上一点别被线遮住
            f'{weight_arr[i]:.2f}',
            ha='center',
            va='bottom',
            fontsize=8,
        )

    # == 注意，吧这个y轴刻度范围限制提到上面，范围设置似乎就失效了
    # 设置第一个 y 轴的范围和刻度并限定y轴范围（不设定就从0开始）
    ax1.set_ylim([0, None])
    # 设置y轴的刻度间隔（这里500往上才显示刻度，以下不显示。因为step就是500,所以没差）
    # rang的上限+1500是为了让weight折现在柱子上面，不遮挡。
    ax1.set_yticks(np.arange(500, max(intake_arr)+2000, 500))

    # 并限定y轴范围（y轴下方与最小值间隔多一点，避免与下方的柱子重叠，但可能折线上数据会重叠，因为高度不够）
    ax2.set_ylim([int(min(weight_arr))-8, None])
    # 设置y轴的刻度间隔（这里y轴从60开始，但是70往上，step为1才显示刻度）
    ax2.set_yticks(np.arange(int(min(weight_arr)), max(weight_arr)+2, 1))

    # 添加每天摄入量的平均值参考线和标注文本
    intake_mean_line = ax1.axhline(intake_mean, color='gray', linestyle='--')
    intake_mean_label = ax1.text(
        len(dates)-1,
        intake_mean,
        f"平均值: {intake_mean:.2f}",
        ha='right',
        va='bottom',
        color='black',
    )

    # 添加图例，调整位置
    ax2.legend(["Weight"], loc="upper right", bbox_to_anchor=(0.98, 0.995))
    # ax1.legend(["Intake"], loc="upper right", bbox_to_anchor=(0.92, 0.995))
    # 摄入的图例有两个：柱子和平均线
    ax1.legend(
        [intake_bar, intake_mean_line],
        ['Intake', f'Intake 平均值: {intake_mean:.2f}'],
        loc="upper right",
        bbox_to_anchor=(0.92, 1.01)
    )

    plt.title("Daily Intake and Weight")
    plt.tight_layout()
    plt.grid(True)

    # 添加范围滑块
    slider_ax = plt.axes([0.7, 0.95, 0.2, 0.04])  # 滑块位置，右上角
    slider = RangeSlider(
        slider_ax,
        'data range',
        valmin=0,
        valmax=len(dates)-1,
        valstep=1,
        valinit=(0, len(dates)-1),
    )

    # 滑块变动时，只显示指定x轴范围的数据，其他位置的文本也隐藏
    def update(val):
        # 获取滑块的值
        start_index, end_index = val
        start_index = int(start_index)
        end_index = int(end_index)

        # 有0.5在滑动时左右边缘就不会显示半个
        ax1.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围
        ax2.set_xlim(start_index-0.5, end_index+0.5)  # 设置x轴范围

        # 选择了滑块范围之后，重新绘制各项图，避免缩小范围后y轴外面还显示文字
        axes = [ax1, ax2]
        for ax in axes:
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

        # 在update函数中，intake_mean_line的作用域不是全局范围内，所以不能直接在函数内部引用它。
        # 为了解决这个问题，可以使用 nonlocal 声明将其声明为嵌套作用域内的变量。
        nonlocal intake_mean_line, intake_mean_label

        # 移除旧的参考线和数值文本，并添加新的
        intake_mean_line.remove()
        intake_mean_line = ax1.axhline(
            new_intake_mean, color='gray', linestyle='--')

        intake_mean_label.remove()
        intake_mean_label = ax1.text(
            end_index-1,
            new_intake_mean,
            f"平均值: {new_intake_mean:.2f}",
            ha='right',
            va='bottom',
            color='black',
        )

        # 图例更新即可
        ax1.legend(
            [intake_bar, intake_mean_line],
            ['Intake', f'Intake 平均值: {new_intake_mean:.2f}'],
            loc="upper right",
            bbox_to_anchor=(0.92, 1.01)
        )

        fig.canvas.draw_idle()  # 重新绘制图形
        # 重新绘制图表
        # plt.draw()

    # 滑块范围变化是触发文本更新
    slider.on_changed(update)

    # dpi表示每英寸点数，bbox_inches='tight'会裁剪边界框，以适应图表内容
    fig.savefig('daily_intake_weight_chart.png', dpi=300,  bbox_inches='tight')
    plt.show()
