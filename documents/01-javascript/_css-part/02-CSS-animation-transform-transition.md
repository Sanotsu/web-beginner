## 使用 CSS animations(动画)

CSS animations 使得可以将 **从一个 CSS 样式配置转换到另一个 CSS 样式配置**。
动画包括两个部分：*描述动画的样式规则*和*用于指定动画开始、结束以及中间点样式的关键帧*。
**创建动画序列**: 需要使用 `animation` 属性或其子属性，该属性允许配置动画时间、时长以及其他动画细节。
**动画的实际表现**: 动画的实际表现是由` @keyframes` 规则实现。

### 配置属性

`animation` 属性为以下 8 个子属性的缩写(由逗号分隔的多个值指代**可设置多个动画的相关属性**，animation 本身也支持配置多个动画):

- `animation-delay: 2s, 4ms`。设置延时，即从**元素加载完成之后到动画序列开始执行**的这段时间。
  - 延迟开始和结束时间，单位 s 或者 ms，**默认为 0s**，设置负数则立即执行动画。
- `animation-direction: normal`。指示**动画是否反向播放**，设置动画在每次运行完后是反向运行还是重新回到开始位置重复运行。
  - `normal`: 每个*动画循环结束*，动画重置到起点重新开始，这是**默认属性**。
  - `alternate`: _动画交替反向运行_，反向运行时，动画按步后退，同时，带时间功能的函数也反向。
  - `reverse`: _反向运行动画_，每周期结束动画由尾到头运行。
  - `alternate-reverse`: _反向交替_，反向开始交替。动画第一次运行时是反向的，然后下一次是正向，后面依次循环。
- `animation-duration: 10s, 30s, 230ms`。设置动画**一个周期的时长**。
- `animation-iteration-count: 2.4,0,infinite`。设置动画**重复次数**，使用`数值`(**默认为 1**)或指定`infinite`无限次重复动画。
- `animation-name: test1, animation4`。指定**由`@keyframes`描述的关键帧名称**。
- `animation-play-state: paused, running`。允许**暂停和恢复**动画。`running`: 当前动画正在运行。`paused`:当前动画已被停止。
- `animation-timing-function: ease, steps(4,end)`。设置**动画速度**，即通过建立加速度曲线，设置动画在关键帧之间是如何变化。
  - 该属性的值 7 个 关键字 `ease|ease-in|ease-out|ease-in-out|linear|step-start|step-end`，2 个 函数表达式。
  - **cubic-bezier()** 缓动函数符号定义了*三次贝塞尔曲线*。由于这些曲线是连续的，它们通常用于平滑动画的开始和结束。
    - 语法: `cubic-bezier(x1, y1, x2, y2)`，具有固定四个点值的三次贝塞尔曲线。x1 和 x2 的范围`[0,1]`，否则无效。
    - 后面列式的属性，都是缓动函数的别名而已。
    - `cubic-bezier(0.0,  0.0, 1.0,  1.0)` = **`linear`**: 动画以**恒速**运行。
    - `cubic-bezier(0.25, 0.1, 0.25, 1.0)` = **`ease`**: 动画**缓慢开始**，比 ease-in-out 快，**然后加速，最后减速直至结束**。
    - `cubic-bezier(0.42, 0.0, 1.0,  1.0)` = **`ease-in`**: 动画**缓慢开始，然后逐渐加速直到结束，在结束点时突然停止**。
    - `cubic-bezier(0.42, 0.0, 0.58, 1.0)` = **`ease-in-out`**: 动画**缓慢开始，然后加速，最后减速直至结束**。
    - `cubic-bezier(0.0,  0.0, 0.58, 1.0)` = **`ease-out`**: 动画**突然开始，然后逐渐减速直至结束**。
  - **steps()** 函数符号定义了一个阶梯函数，将输出值的域划分为等距阶梯。阶梯函数的这个子类有时也称为阶梯函数。
    - 语法: `steps(num_of_steps, direction)`。参数`num_of_steps`是一个正整数，表示步进；`direction`是一个关键字:
      - `jump-start` 表示左连续函数，因此第一步或跳跃发生在动画开始时；`start` 相当于 jump-start。
      - `jump-end` 表示右连续函数，因此最后一步或跳跃发生在动画结束时；`end` 相当于 jump-end，**默认值**。
      - `jump-both` 表示左右连续函数，包括在 0% 和 100% 标记处的暂停，有效地在动画迭代期间添加一个步骤；
      - `jump-none` 两端都没有跳跃。相反，保持在 0% 标记和 100% 标记，每个标记持续时间的 1/n。也有两个别名:
    - **`step-start`**: 动画**立即跳转到它的最终状态，并一直停留到结束**。= `steps(1, jump-start)`或`steps(1, start)`。
    - **`step-end`**: 动画**一直保持初始状态直到结束，此时它直接跳转到最终状态**。= `steps(1, jump-end)`或`steps(1, end)`。
  - 补充说明:
    - 可以在`@keyframe`规则中对各个**关键帧**指定`animation-timing-function`，如果没有指定，则应用该**动画元素**中对应的值。
    - 在一个关键帧内，`animation-timing-function`是一个 at-rule 特定的描述符，而不是同名的属性。
    - 在 100%或到关键帧上指定的`animation-timing-function`将永远不会被使用。
- `animation-fill-mode: none, backwards`。指定**动画执行前后如何为目标元素应用样式**。
  - `none`: 当动画未执行时，动画将不会将任何样式应用于目标，而是已经赋予给该元素的 CSS 规则来显示该元素。这是**默认值**。
  - `forwards`: **目标**将保留由执行期间遇到的**最后一个关键帧计算值**。(关键帧的值为 `0% / from`和 `100% / to`)
    - 最后一个关键帧取决于 animation-direction 和 animation-iteration-count 的值。
    - `normal` 加 `偶数或者奇数`，则为`100% / to`；`reverse`加`偶数或奇数`则为`0 / from`；
    - `alternate`加`偶数`则为`0% / from`；`alternate`加`奇数`则为`100% / to`；
    - `alternate-reverse`加`even`则为`100% / to`；`alternate-reverse`加`奇数`则为`0% / from`。
  - `backwards`: 动画将在应用于目标时立即应用**第一个关键帧中定义的值**，并在 animation-delay 期间保留此值。
    - 第一个关键帧取决于 animation-direction 的值。
    - `normal` or `alternate`则为 `0% / from`，`reverse` or `alternate-reverse`则为 `100% / to`。
  - `both`: 动画将遵循 forwards 和 backwards 的规则，从而在两个方向上扩展动画属性。

### 使用 keyframes 定义动画序列

**定义动画的表现**: 通过使用`@keyframes`建立两个或两个以上关键帧来实现。每一个关键帧都描述了动画元素在给定的时间点上应该如何渲染。

- 因为动画的时间设置是通过 CSS 样式定义的，关键帧使用百分比来指定动画发生的时间点。
  - **0% 表示动画的第一时刻，100% 表示动画的最终时刻**。因为这两个时间点十分重要，所以还有特殊的别名：from 和 to。
  - 这两个都是可选的，若 from/0% 或 to/100% 未指定，则浏览器使用计算值开始或结束动画。
- Webkit 内核浏览器或者早期版本浏览器可能需要*在 CSS 动画属性上使用前缀*，例如`-webkit-`前缀。

示例:`<p>`元素由浏览器窗口右边滑至左边

```cs
p { animation-duration: 3s; animation-direction: revert; animation-name: slidein;}
/*@keyframes duration |timing-function |delay |iteration-count |direction |fill-mode |play-state|name*/
// 缩写为: animation: 3s revert slidein; /**默认值依次为 0s ease 0s 1 normal none running none*/
@keyframes slidein { from { margin-left: 100%; width: 300%;}  to { margin-left: 0%; width: 100%;} }
```

```css
animation = <single-animation> 子属性顺序:
<single-animation> =
  <time>                            ||<time>的第一个值被分配给animation-duration，第二个分配给animation-delay
  <easing-function>                 ||
  <time>                            ||
  <single-animation-iteration-count>||
  <single-animation-direction>      ||
  <single-animation-fill-mode>      ||
  <single-animation-play-state>     ||
  [ none | <keyframes-name> ]
例如: animation: 4s linear 0s infinite alternate sun-rise; (sun-rise是关键帧名称)
默认值依次:       0s ease   0s 1        normal <none running> name (尖括号是上面省略的mode和paly)
```

## 使用 CSS transforms(变换)

通过改变坐标空间，CSS transforms 可以在 **不影响正常文档流的情况下改变作用内容的位置**。
CSS transforms 通过一系列 CSS 属性实现，通过使用这些属性，可以对 HTML 元素进行线性仿射变形。可以进行的变形包括**旋转，倾斜，缩放以及位移**，这些变形同时适用于平面与三维空间。

> 只有**被盒子模型定位的元素才能被转换**。如果一个元素有 `display: block`，它就被盒子模型定位了。

### CSS transforms 属性

有两个主要的属性被用来定义 CSS transforms：`transform` 和 `transform-origin`:

- `transform-origin: left 5px -3px;`: 指定原点的位置。**默认值为元素的中心，可以被移动**。
  - 很多变形需要用到这个属性，比如旋转，缩放和倾斜，他们都需要一个指定的点作为参数。
  - 该属性可以使用一个，两个或三个值来指定，其中每个值都表示一个偏移量。面向屏幕`x-offset(左右)|y-offset(上下)|z-offset(远近)`
    - 一个值：必须是`<length>`，`<percentage>`，或 `left`, `right`, `center`, `top`, `bottom`关键字中的一个。
    - 两个值：其中一个必须是`<length>`，`<percentage>`，或`left`, `center`, `right`关键字中的一个。
      - 另一个必须是`<length>`，`<percentage>`，或`top`, `center`, `bottom`关键字中的一个。
    - 三个值：前两个值和只有两个值时的用法相同。第三个值必须是`<length>`。它始终代表 Z 轴偏移量。
- `transform: scaleY(0.5);` 属性允许旋转，缩放，倾斜或平移给定元素。这是通过修改 CSS 视觉格式化模型的坐标空间来实现的。
  - **取值为空格分隔的一系列变形的列表**，即可以指定多种变换，他们会像被组合操作请求一样被分别执行。
  - 可以指定为关键字值`none`(不做任何变换) 或一个或多个`<transform-function>`值。
  - `<transform-function>` CSS 数据类型用于对元素的显示做变换。通常，这种变换可以由矩阵表示，并且可以使用每个点上的矩阵乘法来确定所得到的图像。
    - `matrix()`: 用六个指定的值来**指定一个均匀的二维（2D）变换矩阵**。
    - `matrix3d()`: 用一个 `4 × 4` 的齐次矩阵来**描述一个三维（3D）变换**。
    - `perspective(l)`: 设置用户与 z=0 平面之间的距离(远近)。参数是数值
    - `rotate(a)`: 围绕二维平面上的一个固定点**旋转**一个元素(rotation)。参数表示代表旋转的角度；正值，顺时针；负值，逆时针。
    - **`rotate3d(x, y, z, a)`**: 围绕三维空间的固定轴线旋转一个元素。参数为 x、y、z 轴坐标和角度。
    - `rotateX(a)`: 围绕横轴旋转一个元素。参数为旋转角度。是`rotate3D(1, 0, 0, a)`的简写形式。
    - `rotateY(a)`: 围绕纵轴旋转一个元素。参数为旋转角度。是`rotate3D(0, 1, 0, a)`的简写形式。
    - `rotateZ(a)`: 围绕 Z 轴旋转一个元素。参数为旋转角度。是`rotate3D(0, 0, 1, a)`的简写形式。
    - `scale(sx,[sy])`: 在二维平面上**放大或缩小**一个元素(resizing)。参数为缩放矢量的横坐标和纵坐标。
    - **`scale3d(sx, sy, sz)`**: 在三维空间中放大或缩小一个元素。参数为代表缩放矢量的横坐标、纵坐标和 Z 轴值。
    - `scaleX(s)`: 水平地放大或缩小一个元素。参数为缩放因子，一个数字。`scale(sx,1)`和`scale3d(sx,1,1)`的简写形式。
    - `scaleY(s)`: 垂直地放大或缩小一个元素。参数为缩放因子，一个数字。`scale(1,sy)`和`scale3d(1,sy,1)`的简写形式。
    - `scaleZ(s)`: Z 轴放大或缩小一个元素。参数为缩放因子，一个数字。`scale3d(1, 1, sz)` 的简写形式。
    - **`skew(ax, [ay])`**: 在二维平面上**扭曲**一个元素(distortion)。参数为用于沿着横坐标、纵坐标扭曲元素的角度。
    - `skewX(a)`: 沿水平方向歪斜元素。(skew:歪斜,倾斜,扭曲)
    - `skewY(a)`: 沿垂直方向歪斜元素。
    - `translate(tx, [ty])`: 在二维平面上**平移**一个元素(moving)。参数为要移动矢量的横坐标、纵坐标。
    - **`translate3d(tx, ty, tz)`**: 在三维空间中平移一个元素。参数为代表移动矢量的横坐标、纵坐标和 Z 轴值。
    - `translateX(tx)`: 水平地平移一个元素。`translate(tx, 0)` 的简写形式。
    - `translateY(ty)`: 垂直地平移一个元素。`translate(0, ty)` 的简写形式。
    - `translateZ(tz)`: 沿 Z 轴平移一个元素。`translate3d(0, 0, tz)` 的简写形式。

```cs
<div class="trans-elem">Transformed element</div>
// 先水平向左平移30px，垂直向下平移20px，然后围绕div左上角(不指定-origin则为其中心点)顺时针旋转20度。
.trans-elem {
    border: solid red;width: 140px;height: 60px;
    transform-origin: left top;  transform: translate(30px, 20px) rotate(20deg);
}
```

### 使用 CSS transitions(过渡)

CSS transitions 提供了一种在更改 CSS 属性时 **控制动画速度**的方法。其可以让属性变化成为一个持续一段时间的过程，而不是立即生效的。

通常将两个状态之间的过渡称为**隐式过渡**（implicit transitions），因为开始与结束之间的状态由浏览器决定。

CSS transitions 可以决定*哪些属性发生动画效果* (明确地列出这些属性)，_何时开始_ (设置 delay），_持续多久_ (设置 duration) 以及*如何动画* (定义 timing function，比如匀速地或先快后慢)。

### 定义过渡的属性

CSS 过渡由简写属性 `transition` 定义是最好的方式，可以避免属性值列表长度不一，节省调试时间。包含以下属性:

- `transition-property`: **指定哪个或哪些 CSS 属性用于过渡**。只有指定的属性才会在过渡中发生动画，其它属性仍如通常那样瞬间变化。
- `none`: `没有过渡动画。all`: 所有可被动画的属性都表现出过渡动画。`<IDENT>`:属性名称
- `transition-duration`: **指定过渡的时长**。或者为*所有属性指定一个值*，或者*指定多个值，为每个属性指定不同的时长*。
- `transition-timing-function`: **指定一个函数，定义属性值怎么变化**。缓动函数 Timing functions 定义属性如何计算。
  - 多数 [timing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function) 由四点定义一个 bezier 曲线。也可以从 [Easing Functions Cheat Sheet](https://easings.net/) 选择缓动效果。
  - 和动画的`animation-timing-function`属性是一样的用法。
- `transition-delay`: **指定延迟**，在过渡效果开始作用之前需要等待的时间。单位为 s 或者 ms。

简写形式: `transition: <property> <duration> <timing-function> <delay>;`

**当属性值列表长度不一致时**

_以 `transition-property` 的值列表长度为标准_，如果某个属性值列表长度**短于它的则重复其值以长度一致；长于它的则被截断**:

```cs
div { transition-property: opacity, left, top, height; transition-duration: 3s, 5s;}
// 处理成
div { transition-property: opacity, left, top, height; transition-duration: 3s, 5s, 3s, 5s;}
```

### 检测过渡是否完成

**当过渡完成时触发一个事件**，在符合标准的浏览器下，这个事件是 **`transitionend`**, 在 WebKit 下是 webkitTransitionEnd。

transitionend 事件提供两个属性:

- `propertyName`: 字符串，指示已完成过渡的属性。
- `elapsedTime`: 浮点数，指示当触发这个事件时过渡已运行的时间（秒）。这个值不受 transition-delay 影响。

例如: `el.addEventListener("transitionend", updateTransition, true);`

> 如果在过渡完成之前，因为元素被做成 `display: none` 或者动画属性的值被改变而中止过渡，过渡结束事件不会触发。

---

ref

- MDN [使用 CSS 动画(Using_CSS_animations)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations)
- MDN [使用 CSS 变换(Using_CSS_transforms)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transforms/Using_CSS_transforms)
- MDN [使用 CSS 过渡(Using_CSS_transitions)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)
- [《现代 JavaScript 教程》之动画](https://zh.javascript.info/animation) - 这个教程咋看起来还不错，但没有仔细看
- [深入浅出 CSS 动画](https://www.cnblogs.com/coco1s/p/15796478.html) - 咋一看好像有几个 CSS 动画的实例。
  - 推荐其博文 github 仓库[chokcoco/iCSS](https://github.com/chokcoco/iCSS)。
