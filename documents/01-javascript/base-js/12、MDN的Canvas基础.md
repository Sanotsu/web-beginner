<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [Canvas API 基础](#canvas-api-%E5%9F%BA%E7%A1%80)
  - [基础概念](#%E5%9F%BA%E7%A1%80%E6%A6%82%E5%BF%B5)
  - [绘制图形](#%E7%BB%98%E5%88%B6%E5%9B%BE%E5%BD%A2)
  - [使用样式和颜色](#%E4%BD%BF%E7%94%A8%E6%A0%B7%E5%BC%8F%E5%92%8C%E9%A2%9C%E8%89%B2)
  - [绘制文本](#%E7%BB%98%E5%88%B6%E6%96%87%E6%9C%AC)
  - [使用图像](#%E4%BD%BF%E7%94%A8%E5%9B%BE%E5%83%8F)
  - [画布变形](#%E7%94%BB%E5%B8%83%E5%8F%98%E5%BD%A2)
  - [合成和剪裁](#%E5%90%88%E6%88%90%E5%92%8C%E5%89%AA%E8%A3%81)
  - [基础的动画](#%E5%9F%BA%E7%A1%80%E7%9A%84%E5%8A%A8%E7%94%BB)
  - [像素操作](#%E5%83%8F%E7%B4%A0%E6%93%8D%E4%BD%9C)
  - [canvas 的优化](#canvas-%E7%9A%84%E4%BC%98%E5%8C%96)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Canvas API 基础

### 基础概念

Canvas API 提供了一个通过 JavaScript 和 HTML 的`<canvas>`元素来绘制图形的方式。  
它可以用于动画、游戏画面、数据可视化、图片编辑以及实时视频处理等方面。

Canvas API 主要聚焦于 2D 图形。而同样使用`<canvas>`元素的 [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) 则用于绘制硬件加速的 2D 和 3D 图形。

`<canvas>` 标签只有两个属性: width 和 height。**默认为`300px * 150px`**。可以使用 HTML 的高度和宽度属性来自定义 Canvas 的尺寸。  
为了在 Canvas 上绘制图形，需要使用一个 JavaScript 上下文对象，它能动态创建图像。  
所有的新版本主流浏览器都支持，但仍应该为其准备替代内容，例如提供对 canvas 内容的文字描述或者是提供动态生成内容相对应的静态图片。

**`<canvas>` 元素需要结束标签`</canvas>`**。如果结束标签不存在，则文档的其余部分会被认为是替代内容，将不会显示出来。

`<canvas>`元素创造了一个固定大小的画布，它公开了一个或多个**渲染上下文(The rendering context)**用来绘制和处理要展示的内容。

- `<canvas>` 元素有一个叫做 **`getContext()`** 的方法，这个方法是用来获得渲染上下文和它的绘画功能。
  - 获取 2D 渲染上下文类似: `let ctx = canvas.getContext('2d');`。WebGL 使用了基于 [OpenGL ES](https://www.khronos.org/opengles/) 的 3D 上下文。
- 替换内容是用于在不支持`<canvas>`标签的浏览器中展示的。通过简单的测试`getContext()`方法的存在，脚本可以**检查编程支持性**。
- 画布栅格（canvas grid）以及坐标空间:
  - canvas 元素默认被网格所覆盖。通常来说*网格中的一个单元相当于 canvas 元素中的一像素*。
  - **栅格的起点为左上角，坐标为（0,0）**。所有元素的位置都相对于原点定位。水平为 x 轴,向左为正；垂直为 y 轴，向下为正。

### 绘制图形

不同于 SVG，**`<canvas>` 只支持两种形式的图形绘制：矩形和路径（由一系列点连成的线段）**。  
所有其他类型的图形都是通过一条或者多条路径组合而成的。不过拥有众多路径生成的方法让复杂图形的绘制成为了可能。

这一节只用到默认的线条和填充样式，下一节探讨 canvas 的样式和颜色。

**1. 绘制矩形**的 3 个函数(三个函数绘制之后会马上显现在 canvas 上，**即时生效**):

- `ctx.fillRect(x, y, width, height)`: 绘制一个填充的矩形。(x,y)为矩形的开始点，width、height 为矩形的宽高。
- `ctx.strokeRect(x, y, width, height)`: 绘制一个矩形的边框。
- `ctx.clearRect(x, y, width, height)`: 清除指定矩形区域，让清除部分完全透明。

**2. 绘制路径**

**图形的基本元素是路径**。路径是通过不同颜色和宽度的线段或曲线相连形成的不同形状的点的集合。

- 一个路径，甚至一个子路径，都是闭合的。使用路径绘制图形需要一些额外的步骤：
  - 首先创建**路径起始点**。然后使用[画图命令](https://developer.mozilla.org/zh-CN/docs/Web/API/CanvasRenderingContext2D#paths)去**画出路径**。之后**把路径封闭**。一旦路径生成，就能通过描边或填充路径区域来**渲染图形**。
- 以上步骤需要使用的函数:
  - `beginPath()`: 新建一条路径，生成之后，图形绘制命令被指向到路径上生成路径。
    - _本质上，路径是由很多子路径构成_，这些子路径都是在一个列表中，所有的子路径（线、弧形、等等）构成图形。
      - 而每次这个方法调用之后，当前路径为空，列表清空重置，然后就可以重新绘制新的图形。
    - 调用 beginPath() 之后，或者 canvas 刚建的时候，第一条路径构造命令通常被视为是`moveTo()`，无论实际上是什么。
    - 出于这个原因，_几乎总是要在设置路径之后专门指定起始位置_。
  - `closePath()`: 闭合路径之后图形绘制命令又重新指向到上下文中。
  - `stroke()`: 通过线条来绘制图形轮廓。
  - `fill()`: 通过填充路径的内容区域生成实心的图形。
    - 调用 fill() 函数时，所有没有闭合的形状都会自动闭合，所以不需要调用 closePath() 函数。但是调用 stroke() 时不会自动闭合。
- 移动笔触(Moving the pen)
  - 当 canvas 初始化或 beginPath()调用后，通常会**使用`moveTo()`函数设置起点**。也能够使用 moveTo()绘制一些不连续的路径。
  - `moveTo(x, y)`: 将笔触移动到指定的坐标 x 以及 y 上。这个函数实际上并不能画出任何东西。
    - 就像在纸上画图，一支钢笔或者铅笔的笔尖从一个点到另一个点的移动过程(不连续的地方都要抬起笔移动绘制点)。

其他的画图命令简介:

**绘制直线**

- `lineTo(x, y)`: 绘制一条从当前位置到指定 x 以及 y 位置的直线。
  - (x,y)代表坐标系中**直线结束的点**。开始点和之前的绘制路径有关，也可以通过 moveTo()函数改变。

**绘制圆弧或者圆**

- `arc(x, y, radius, startAngle, endAngle, anticlockwise)`: 画一个以（x,y）为圆心的以 radius 为半径的圆弧（圆），从 startAngle 开始到 endAngle 结束，按照 anticlockwise 给定的方向（默认为顺时针）来生成。
  - **arc() 函数中表示角的单位是弧度**，不是角度。角度与弧度的 js 表达式：`弧度=(Math.PI/180)*角度`
- `arcTo(x1,y1,x2,y2,radius)`: 根据给定的控制点和半径画一段圆弧，再以直线连接两个控制点(实现不可靠，不建议使用)

**二次贝塞尔曲线及三次贝塞尔曲线**。一般用来绘制复杂有规律的图形。

- `quadraticCurveTo(cp1x, cp1y, x, y)`: 绘制二次贝塞尔曲线，cp1x,cp1y 为一个控制点，x,y 为结束点。
- `bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)`: 绘制三次贝塞尔曲线，cp1x,cp1y 为控制点一，cp2x,cp2y 为控制点二，x,y 为结束点。

**路径绘制绘制矩形**

- `rect(x, y, width, height)`: 绘制一个左上角坐标为（x,y），宽高为 width 以及 height 的矩形。
  - 当该方法执行的时候，moveTo() 方法自动设置坐标参数（0,0）。也就是说，当前笔触自动重置回默认坐标。

**3. Path2D 对象**

为了简化代码和提高性能，Path2D 对象已可以在*较新版本的浏览器中使用*，用来**缓存或记录绘画命令**，这样将能快速地回顾路径。

- `let path2DObj = new Path2D()`: Path2D()会**返回一个新初始化的 Path2D 对象**。
  - 可能将某一个路径作为变量创建一个它的副本，或者将一个包含 SVG path 数据的字符串作为变量。
    - 空的 Path 对象: `new Path2D()`; 克隆 Path 对象: `new Path2D(path)`; 从 SVG 建立 Path 对象: `new Path2D(d)`;
  - 所有的路径方法比如 moveTo, rect, arc 或 quadraticCurveTo 等，都可以在 Path2D 中使用。
- `path2DObj.addPath(path [, transform])`: **添加了一条路径到当前路径**（可能添加了一个变换矩阵）。

新的 Path2D API 还可以使用 SVG path data 来初始化 canvas 上的路径。这将允许获取路径时可以以 SVG 或 canvas 的方式来重用它们。  
类似`let p = new Path2D("M10 10 h 80 v 80 h -80 Z");`

- 先移动到点 (M10 10)，然后再水平移动 80 个单位(h 80)，然后下移 80 个单位 (v 80)，接着左移 80 个单位 (h -80)，再回到起点处 (z)。

### 使用样式和颜色

**1. 色彩 Colors**

给图形上色，有两个重要的属性可以做到(color 可以是表示 [CSS 颜色值](https://www.w3.org/TR/css-color-3/)的字符串，渐变对象或者图案对象):

- `ctx.fillStyle = color`: 设置图形的**填充**颜色。例如`ctx.fillStyle = "#FFA500";// 橙色`
- `ctx.strokeStyle = color`: 设置图形**轮廓**的颜色。

**2. 透明度 Transparency**

通过设置 globalAlpha 属性或者使用一个半透明颜色作为轮廓或填充的样式。

- `ctx.globalAlpha=透明度值`: 影响到 canvas 里所有图形的透明度，有效的值范围是 0.0(完全透明)到 1.0(完全不透明)，默认是 1.0。
  - globalAlpha 属性在需要**绘制大量拥有相同透明度的图形**时候相当高效。
- 因为 strokeStyle 和 fillStyle 属性接受符合 CSS 3 规范的颜色值，所以可以用来**设置具有透明度的颜色**。
  - `ctx.strokeStyle="rgba(255,0,0,0.5)";ctx.fillStyle="rgba(255,0,0,0.5)";`指定透明颜色用于描边和填充样式。

**3. 线型 Line styles**属性

- `ctx.lineWidth = value`: 设置线条**宽度**。默认值 1.0。
- `ctx.lineCap = type`: 设置线条**末端样式**。默认值 butt。
  - `butt`:以方形结束。`round`:以圆形结束。`square`:以方形结束，但是增加了一个宽度和线段相同，高度是线段厚度一半的矩形区域。
- `ctx.lineJoin = type`: 设定线条与线条间**接合处的样式**。。默认值 miter。
  - `round`: 通过填充一个额外的，圆心在相连部分末端的扇形，绘制拐角的形状。圆角的半径是线段的宽度。**圆弧**
  - `bevel`: 在相连部分的末端填充一个额外的以三角形为底的区域，每个部分都有各自独立的矩形拐角。**磨平**
  - `miter`: 通过延伸相连部分的外边缘，使其相交于一点，形成一个额外的菱形区域。这个设置可以通过 miterLimit 属性看到效果。**尖锐**
    - 线段的外侧边缘会被延伸交汇于一点上。线段之间夹角比较大时，交点不会太远，但**随着夹角变小，交点距离会呈指数级增大**。
- `ctx.miterLimit=value`: 限制当两条线相交时**交接处最大长度**；交接处长度是指线条交接处内角顶点到外角顶点的长度。默认值 10.0。
- `ctx.setLineDash(segments)`: **设置当前虚线样式**。segments **一组**描述交替绘制线段和间距长度的数字。**奇数个会被复制并重复**。
- `ctx.getLineDash()`: **返回一个包含当前虚线样式，长度为非负偶数的数组**，描述交替绘制线段和间距（坐标空间单位）长度的数字。
- `ctx.lineDashOffset = value`: 设置**虚线样式的起始偏移量**。参数为 float 类型，默认值 0.0。

**4. 渐变 Gradients**

新建一个 canvasGradient 对象:

- `ctx.createLinearGradient(x1, y1, x2, y2)`: 接受 4 个参数，表示渐变的起点 (x1,y1) 与终点 (x2,y2)。
- `ctx.createRadialGradient(x1, y1, r1, x2, y2, r2)`: 接受 6 个参数:
  - 前三个定义一个以 (x1,y1) 为原点，半径为 r1 的圆，后三个参数则定义另一个以 (x2,y2) 为原点，半径为 r2 的圆。

有了 canvasGradient 对象，就可以用 addColorStop 方法给它上色:

- `gradient.addColorStop(position, color)`: 接受 2 个参数:
  - position 参数必须是一个 0.0 与 1.0 之间的数值，表示渐变中颜色所在的相对位置。例如，0.5 表示颜色会出现在正中间。
  - color 参数必须是一个有效的 CSS 颜色值（如 `#FFF`，`rgba(0,0,0,1)`，等等）。

**5. 图案样式 Patterns**

- `ctx.createPattern(image,type)`:**使用指定的图像创建模式的方法**。此方法返回一个 CanvasPattern 对象。该方法接受两个参数:
  - image 可以是一个 Image 对象的引用，或者另一个 canvas 对象。
  - type 必须是下面的字符串值之一：`repeat`，`repeat-x`，`repeat-y` 和 `no-repeat`。

**6. 阴影 Shadows** 属性

- `ctx.shadowOffsetX = float` 和 `ctx.shadowOffsetY = float`，默认都为 0。
  - 用来设定**阴影在 X 和 Y 轴的延伸距离**，它们是不受变换矩阵所影响的。负值表示阴影会往上或左延伸，正值则表示会往下或右延伸。
- `ctx.shadowBlur = float`: 用于设定**阴影的模糊程度**，其数值并不跟像素数量挂钩，也不受变换矩阵的影响，默认为 0。
- `ctx.shadowColor = color`: color 是标准的 CSS 颜色值，用于**设定阴影颜色效果**，默认是*全透明的黑色*。

**7. Canvas 填充规则**

当用到 fill(或者 clip 和 isPointinPath)可以选择一个填充规则，该填充规则**根据某处在路径的外面或者里面来决定该处是否被填充**。两个可选值:

- `nonzero`: [non-zero winding rule](https://en.wikipedia.org/wiki/Nonzero-rule)，默认值。`evenodd`: [even-odd winding rule](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule)。
- `非零环绕数规则`: 平面内的任何一点 P，引出一条射线，注意不要经过多边形的顶点。然后**将多边形的边矢量化**，规定多边形的边如果**从射线的左边穿过则加 1，如果从射线的右边穿过则减 1，最终结果累加**，如果**为 0**，则点 P 在多边的**外面**；如果**非 0** 则点 P 在多边形的**内部**。
- `奇偶规则`: 平面内的任何一点 P，引出一条射线，注意不要经过多边形的顶点，如果**射线与多边形的交点的个数为奇数，则点 P 在多边形的内部**，如果交点的个数为**偶数**，则点 P 在多边形的**外部**。

### 绘制文本

canvas 提供了两种方法来渲染文本：

- `ctx.fillText(text, x, y [, maxWidth])`: 在指定的 (x,y) 位置**填充指定的文本**，绘制的最大宽度是可选的。
- `ctx.strokeText(text, x, y [, maxWidth])`: 在指定的 (x,y) 位置**绘制文本边框**，绘制的最大宽度是可选的。

有样式的文本,有更多的属性可以让你改变 canvas 显示文本的方式:

- `ctx.font = value`: 当前用来**绘制文本的样式**。这个字符串使用和 CSS font 属性相同的语法。默认的字体是 `10px sans-serif`。
- `ctx.textAlign = value`: **文本对齐**选项。可选的值包括：start(默认), end, left, right, center。
- `textBaseline = value`: **基线对齐**选项。可选的值包括：top, hanging, middle, alphabetic(默认), ideographic, bottom。

  ![canvas-text-baselines](../../../pandoc/format-doc/pictures/pictures-js/canvas-text-baselines.png)

- `ctx.direction = value`: **文本方向**。可能的值包括：ltr, rtl, inherit(默认)。

预测量文本宽度:

- `ctx.measureText()`: 将返回一个 [TextMetrics](https://developer.mozilla.org/zh-CN/docs/Web/API/TextMetrics) 对象的宽度、所在像素，这些体现文本特性的属性。

### 使用图像

canvas 有一项**图像操作**能力的特性。可以用于**动态的图像合成或者作为图形的背景，以及游戏界面**（Sprites）等等。  
浏览器支持的**任意格式的外部图片**都可以使用，比如 PNG、GIF 或者 JPEG。甚至可以将**同一个页面中其他 canvas 元素生成的图片**作为图片源。

引入图像到 canvas 里需要以下两步基本操作：

- 获得一个指向 [HTMLImageElement](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLImageElement) 的对象或者另一个 canvas 元素的引用作为源，也可以通过提供一个 URL 的方式来使用图片。
- 使用 `drawImage()` 函数将图片绘制到画布上。

**1. 可以作为源的图片类型**:

- [HTMLImageElement](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLImageElement): 这些图片是由 `Image()` 函数构造出来的，或者任何的 `<img>` 元素
- [HTMLVideoElement](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLVideoElement): 用一个 HTML 的 `<video>`元素作为图片源，可以从视频中抓取当前帧作为一个图像
- [HTMLCanvasElement](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCanvasElement): 可以使用另一个 `<canvas>` 元素作为你的图片源。
- [ImageBitmap](https://developer.mozilla.org/zh-CN/docs/Web/API/ImageBitmap): 这是一个高性能的位图，可以低延迟地绘制，它可以从上述的所有源以及其它几种源中生成。

这些源统一由 CanvasImageSource 类型来引用。

**2. 获得需要绘制的图片**

- 使用*相同页面*内的图片:
  - `document.images`集合；`document.getElementsByTagName()`方法；`document.getElementById()`获得这个图片。
- 使用*其它域名下*的图片:
  - 在 HTMLImageElement 上使用 crossOrigin 属性，可以请求加载其它域名上的图片。
  - 如果图片的服务器允许跨域访问这个图片，那么可以使用这个图片而不污染 canvas，否则，使用这个图片将会污染 canvas。
- 使用*其它 canvas* 元素:
  - 用 document.getElementsByTagName 或 document.getElementById 方法来获取其它已经准备好的 canvas 元素。
  - 一个常用的应用就是将第二个 canvas 作为另一个大的 canvas 的缩略图。
- 由零开始*创建图像*: 使用 `Image()` 构造函数。`let img = new Image(); img.src = 'myImage.png';`。
- 通过 `data:url` 方式嵌入 Base64 编码的字符串定义的图像:`img.src = 'data:image/gif;base64,R0lGODlhCw……'`。
- 使用*视频帧*: `document.getElementById('myvideotag')`得到 HTMLVideoElement 作为图像源。

**3. 绘制图片**

- `ctx.drawImage(image, x, y)`: 其中 image 是 image 或者 canvas 对象，x 和 y 是其在目标 canvas 里的起始坐标。
  - SVG 图像必须在 `<svg>` 根指定元素的宽度和高度。

**4. 缩放图片**

- `ctx.drawImage(image, x, y, width, height)`: 额外参数 width 和 height 用来控制当向 canvas 画入时应该**缩放的大小**。

**过度缩放图像可能会导致图像模糊或像素化**(反锯齿)。  
可以使用绘图环境的 imageSmoothingEnabled 属性来控制是否在缩放图像时使用平滑算法。默认值为 true，即启用平滑缩放。也可如下禁用:

```cs
ctx.mozImageSmoothingEnabled = false; ctx.webkitImageSmoothingEnabled = false;
ctx.msImageSmoothingEnabled = false; ctx.imageSmoothingEnabled = false;
```

**5. 图片切片**

- `ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)`，9 个参数的变种:
  - 第一个参数也是一个图像或 canvas 的引用；前 4 个是定义图像**源的切片**位置和大小；后 4 个则是定义切片的**目标显示**位置和大小。
  - 图片中切片截取的大小，在画布中的目标位置大小并不一定百分比重合的。源图片截取过大画布显示会显示不全，过小则复制重复。

### 画布变形

之前只有根据需要使用默认的网格，改变整个画布的大小。变形是一种更强大的方法，可以**将原点移动到另一点、对网格进行旋转和缩放**。

**1. 状态的保存和恢复**

绘制复杂图形时必不可少的方法:

- `save()` 和 `restore()`: save 和 restore 方法是用来保存和恢复存画布 (canvas)所有状态状态的，都没有参数。
  - Canvas 的状态就是当前画面应用的所有样式和变形的一个快照。

**Canvas 状态**存储在**栈**中，_每当 save()方法被调用后，当前的状态就被推送到栈中保存_。

一个**绘画状态**包括:

- 当前应用的*变形*(移动，旋转和缩放)
- 这些*属性*：strokeStyle, fillStyle, globalAlpha, lineWidth, lineCap, lineJoin, miterLimit, lineDashOffset, shadowOffsetX, shadowOffsetY, shadowBlur, shadowColor, globalCompositeOperation, font, textAlign, textBaseline, direction, imageSmoothingEnabled
- 当前的*裁切路径*（clipping path）

设置配置，save 一次，存入栈顶；修改配置，save 一次，再存入栈顶……restore 一次，取出栈顶配置，用于 canvas 绘制……

在做变形之前先保存状态是一个良好的习惯。大多数情况下，**调用 restore 方法比手动恢复原先的状态要简单**得多。  
另外，如果**在一个循环中做位移但没有保存和恢复** canvas 的状态，很可能到最后因为**超出 canvas 范围以外**导致有些东西看不见了。

**2. 移动 Translating**

`translate(x, y)`: **移动 canvas 和它的原点**到一个不同的位置。接受两个参数，x 是左右偏移量，y 是上下偏移量。

**3. 旋转 Rotating**

`rotate(angle)`:以**原点为中心旋转 canvas**。接受一个参数：旋转的角度 (angle)，它是顺时针方向的，以*弧度为单位*的值。

- 旋转的中心点始终是 canvas 的原点，如果要改变原点，需要先用 translate 方法。

**4. 缩放 Scaling**

`scale(x, y)`: **缩放画布的水平和垂直的单位**。两个参数都是实数，可以为负数:

- 参数为负实数，相当于以 x 或 y 轴作为对称轴镜像反转。即 x、y 都是正数则在第一象限，有负数则在其他象限。
- x 为水平缩放因子，y 为垂直缩放因子，如果比 1 小，会缩小图形，如果比 1 大会放大图形。默认值为 1，为实际大小。
- _默认情况下，canvas 的 1 个单位为 1 个像素_。设置缩放因子是 0.5，1 个单位就变成对应 0.5 个像素，其他数值同理。

**5. 变形 Transforms**

- `transform(a, b, c, d, e, f)`: **允许对变形矩阵直接修改**。将当前的变形矩阵乘上一个基于自身参数的矩阵。
  - 参数说明: a (m11) 水平**缩放**。b (m12) 垂直**倾斜**。c (m21) 水平倾斜。d (m22) 垂直缩放。 e (dx) 水平**移动**。f (dy) 垂直移动。
- `setTransform(a, b, c, d, e, f)`: 会将**当前的变形矩阵重置为单位矩阵，然后用相同的参数调用 transform 方法**。
- `resetTransform()`: **重置当前变形为单位矩阵**，和调用语句是一样的:`ctx.setTransform(1, 0, 0, 1, 0, 0)`。

### 合成和剪裁

之前是将一个图形画在另一个之上，对于其他更多的情况，仅仅这样是远远不够的。比如，对合成的图形来说，绘制顺序会有限制。
可以利用 globalCompositeOperation 属性来改变这种状况。此外，clip 属性允许隐藏不想看到的部分图形。

**1. [globalCompositeOperation 属性](https://developer.mozilla.org/zh-CN/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation)**

`ctx.globalCompositeOperation = type`: 属性设定了**在画新图形时采用的遮盖策略**，其值是一个标识遮盖方式的字符串:

- `source-over`: 这是默认设置，**在现有画布上下文之上**绘制新图形。
- `source-in`: 新图形只在新图形和目标画布**重叠的**地方绘制。**其他的都是透明**的。
- `source-out`: 在**不与**现有画布内容**重叠**的地方绘制新图形。
- `source-atop`: 新图形**只在**与现有画布内容**重叠的**地方绘制。
- `destination-over`: 在现有的画布内容**后面**绘制新的图形。
- `destination-in`: 现有的画布内容**保持在**新图形和现有画布内容**重叠的位置**。**其他的都是透明的**。
- `destination-out`: 现有内容**保持在**新图形**不重叠**的地方。
- `destination-atop`: 现有的画布**只保留**与新图形**重叠的**部分，新的图形是在画布内容**后面**绘制的。
- `lighter`: 两个重叠图形的颜色是通过**颜色值相加**来确定的。
- `copy`: **只显示新图形**。
- `xor`: 图像中，那些**重叠和正常绘制之外**的其他地方是**透明**的。
- `multiply`: 将顶层像素与底层相应**像素相乘**，结果是一幅*更黑暗*的图片。`screen`: **像素被倒转，相乘，再倒转**，结果是一幅*更明亮*的图片。
- `overlay`: multiply 和 screen 的结合，_原本暗的地方更暗，原本亮的地方更亮_。
- `darken`: **保留**两个图层中**最暗**的像素。`lighten`: **保留**两个图层中**最亮**的像素。
- `color-dodge`: **将底层除以顶层的反置**。
- `color-burn`: **将反置的底层除以顶层，然后将结果反过来**。
- `hard-light`:屏幕相乘（A combination of multiply and screen）类似于叠加，但上下图层互换了。
- `soft-light`: 用顶层减去底层或者相反来得到一个正值。
- `difference`: 一个柔和版本的强光（hard-light）。纯黑或纯白不会导致纯黑或纯白。
- `exclusion`: 和 difference 相似，但对比度较低。
- `hue`: 保留了底层的亮度（luma）和色度（chroma），同时采用了顶层的色调（hue）。
- `saturation`: 保留底层的亮度（luma）和色调（hue），同时采用顶层的色度（chroma）。
- `color`: 保留了底层的亮度（luma），同时采用了顶层的色调 (hue) 和色度 (chroma)。
- `luminosity`: 保持底层的色调（hue）和色度（chroma），同时采用顶层的亮度（luma）。

**2. 裁切路径**

裁切路径和普通的 canvas 图形差不多，不同的是**它的作用是遮罩，用来隐藏不需要的部分**。  
可以实现与 globalCompositeOperation 的 `source-in` 和 `source-atop` 差不多的效果。  
最重要的区别是**裁切路径不会在 canvas 上绘制东西，而且它永远不受新图形的影响**。这些特性使得它在*特定区域里绘制图形时相当好用*。

- `ctx.clip(path, fillRule)`: **将当前正在构建的路径转换为当前的裁剪路径**。
  - `fillRule`:这个算法判断一个点是在路径内还是在路径外。允许的值：`nonzero`非零环绕(默认)；`evenodd`奇偶环绕。
  - `path`:需要剪切的 [Path2D](https://developer.mozilla.org/zh-CN/docs/Web/API/Path2D) 路径。

### 基础的动画

**1. 动画的基本步骤**

- **清空 canvas**。除非接下来要画的内容会完全充满 canvas(例如背景图)，否则需要清空所有。最简单的做法就是用 `clearRect` 方法。
- **保存 canvas 状态**。如果要改变一些会改变 canvas 状态的设置(样式、变形之类的)，又要在每画一帧之时都是原始状态，需要先保存一下。
- **绘制动画图形**(animated shapes)。这一步才是重绘动画帧。
- **恢复 canvas 状态**。如果已经保存了 canvas 的状态，可以先恢复它，然后重绘下一帧。

**2. 操控动画**

在 canvas 上绘制内容是用 canvas 提供的或者自定义的方法，而通常，**仅仅在脚本执行结束后才能看见结果**。  
为了实现动画，需要一些可以定时执行重绘的方法。可以通过 setInterval 和 setTimeout 方法来控制在设定的时间点上执行重绘。

- `setInterval(function, delay)`: 当设定好*间隔时间后*，function 会*定期执行*。
- `setTimeout(function, delay)`: 在设定好的*时间之后执行函数*。
- `requestAnimationFrame(callback)`: **告诉浏览器希望执行一个动画，并在重绘之前，请求浏览器执行一个特定的函数来更新动画**。
  - 提供了*更加平缓并更加有效率的方式来执行动画*，当系统准备好了重绘条件的时候，才调用绘制动画帧。
  - 一般每秒钟回调函数执行 60 次，也有可能会被降低。

更多高级动画示例，可查看 MDN 的教程 canvas[高级动画](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Advanced_animations)进行学习。

### 像素操作

可以直接通过 ImageData 对象**操纵像素数据**，直接读取或将数据数组写入该对象中。
或者更进一步，控制图像使其平滑（**反锯齿**）以及如何**从 Canvas 画布中保存图像**。

**1. ImageData 对象**

ImageData 对象中存储着 canvas 对象*真实的像素数据*，它包含以下几个**只读属性**：

- `width`: 图片宽度，单位是像素；`height`: 图片高度，单位是像素
- `data`: Uint8ClampedArray 类型的一维数组，包含着 RGBA 格式的整型数据，范围在 0 至 255 之间（包括 255）。
  - data 属性返回一个 Uint8ClampedArray，它可以被使用作为*查看初始像素数据*。
  - **每个像素用 4 个 1 bytes 值**(按照红，绿，蓝和透明值的顺序; 这就是"RGBA"格式) 来代表。
  - **每个颜色值部份用 0 至 255 来代表**。
  - 每个部份被分配到*一个在数组内连续的索引*，_左上角像素的红色部份在数组的索引 0 位置_。
  - 像素*从左到右被处理，然后往下*，遍历整个数组。

例如，要读取图片中位于第 50 行，第 200 列的像素的蓝色部份:

```js
blueComponent = imageData.data[50 * (imageData.width * 4) + 200 * 4 + 2];
```

**创建一个 ImageData 对象**: 使用 createImageData 创建一个新的、空白的、指定大小的 ImageData 对象。所有的像素在新对象中都是透明的:

- `let imageData = ctx.createImageData(width, height)`: 指定 ImageData 新对象的宽度和高度。
- `let imageData = ctx.createImageData(imagedata)`: 从现有对象复制一个和其宽度和高度相同的对象。图像自身不允许被复制。

**得到场景(context)像素数据**: 使用 getImageData() 方法(例如事项颜色选择器功能)。

`ctx.getImageData(sx, sy, sw, sh)`: 返回一个 ImageData 对象，包含 canvas 给定的矩形图像数据。参数为:

- `sx,sy`: 将要被提取的图像数据矩形区域的左上角 x,y 坐标。`sw,sh`: 将要被提取的图像数据矩形区域的宽度、高度。
- 如果高度或者宽度变量为 0，则抛出 IndexSizeError 错误。

**在场景(context)中写入像素数据**: 使用 putImageData() 方法(例如灰度和反转颜色，修改图片色彩风格)。

`ctx.putImageData(myImageData, dx, dy)`:

- `myImageData`: 包含像素值的数组对象。`dx,dy`: 源图像数据在**目标画布中的位置偏移量**（x 轴、y 轴方向的偏移量）。

`ctx.putImageData(imagedata, dx, dy, dirtyX, dirtyY, dirtyWidth, dirtyHeight)`: 再后面还可跟 4 个可选参数:

- `dirtyX,dirtyY`:在源图像数据中，**矩形区域左上角的位置**。默认是整个图像数据的左上角。
- `dirtyWidth,dirtyHeight` 在源图像数据中，**矩形区域的宽度、高度**。默认是图像数据的宽度、高度。

**2. 缩放和反锯齿**

在 drawImage() 方法、第二个画布和 imageSmoothingEnabled 属性(布尔值表示图片是否平滑)的帮助下，可以**放大显示图片及看到详情内容**。

- 例如裁剪出鼠标的位置`5*5`px 的图片，在`100*100`px 的画布上显示。**反锯齿默认是启用的**，可以关闭它以看到清楚的像素。

**3. 保存图片**

HTMLCanvasElement 提供一个 toDataURL() 方法，它返回一个**包含被类型参数规定的图像表现格式的数据链接**。返回的图片分辨率是 96dpi:

- `canvas.toDataURL('image/png')`: 默认设定。创建一个 PNG 图片。
- `canvas.toDataURL('image/jpeg', quality)`: 创建一个 JPG 图片。从 0 到 1 的品质量，0 基本不被辨析但有比较小的文件大小。

画布中生成了一个数据链接，可以将它**用于任何`<image>`元素**，或者将它放在一个有**download 属性的超链接**里用于保存到本地。

或者**从画布中创建一个 Blob 对象**:

`canvas.toBlob(callback, type, encoderOptions)`: 这个创建了一个在画布中的代表图片的 Blob 对象。

### canvas 的优化

- 在**离屏 canvas 上预渲染**相似的图形或重复的对象。
- **避免浮点数的坐标点**，用整数取而代之。
- **不要在用 drawImage 时缩放图像**，在离屏 canvas 中缓存图片的不同尺寸。
- 使用**多层画布去画一个复杂的场景**。
- **用 CSS 设置大的背景图**。可以避免在每一帧在画布上绘制大图。
- **用 CSS transforms 特性缩放画布**。CSS transforms 使用 GPU，因此速度更快。最好的情况是不直接缩放画布
- 在不需要时**关闭透明度**。` canvas.getContext('2d', { alpha: false })`这个选项可以帮助*浏览器进行内部优化*。
- 其他:
  - 将画布的函数调用集合到一起（例如，画一条折线，而不要画多条分开的直线）
  - 避免不必要的画布状态改变
  - 渲染画布中的不同点，而非整个新状态
  - 尽可能避免 shadowBlur 特性
  - 尽可能避免 text rendering
  - 尝试不同的方法来清除画布 (`clearRect()` vs. `fillRect()` vs. 调整 canvas 大小)
  - 有动画，请使用 `window.requestAnimationFrame()` 而非 `window.setInterval()`
  - 请谨慎使用大型物理库

更多 canvas 性能优化参看 web.dev [Improving HTML5 Canvas performance](https://web.dev/canvas-performance/)

---

补充.鼠标事件获取的属性中几个关于坐标的区别:

- `clientX,clientY`: 与 x，y 一样的，以**浏览器显示区域**的左上角开始，指鼠标的坐标。`x,y`是新浏览器支持
- `offsetX,offsetY`: 针对**目标元素**的左上角坐标，从 padding 开始。
- `layerX,layerY`: 往上找有定位属性的**父元素**的左上角(自身有定位属性的话就是相对于自身)，都没有的话，就是相对于 body 的左上角
- `pageX,pageY`: **相对页面**左上角的距离
- `screenX,screenY`: **相对屏幕**左上角的位置

---

ref: MDN 足够清楚了，也有示例，其他的简单参看就行了。

- MDN [Canvas](https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API)
- 掘金 [案例+图解带你一文读懂 Canvas（2W+字）](https://juejin.cn/post/7119495608938790942)
- 掘金 [为了让她 10 分钟入门 canvas，我熬夜写了 3 个小项目和这篇文章](https://juejin.cn/post/6986785259966857247)
- 掘金 [Canvas 保姆级教程（上）：绘制篇](https://juejin.cn/post/7008064185972031524)
- 掘金 [Canvas 保姆级教程（下）：动画篇](https://juejin.cn/post/7008811592733655077)
- 掘金 [Canvas 从入门到劝朋友放弃（图解版）](https://juejin.cn/post/7116784455561248775)
