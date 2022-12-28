## WebGL API 基础

### 基础概念

WebGL（Web 图形库）是一个 JavaScript API，可**在任何兼容的 Web 浏览器中渲染高性能的交互式 3D 和 2D 图形**，而无需使用插件。

- 引入一个与 OpenGL ES 2.0 **非常一致的 API** 在`<canvas>`元素中使用。这种一致性使 API 可以利用用户设备提供的硬件图形加速。
- 现代浏览器都支持 WebGL ，但一些特性也需要用户的硬件设备支持。
- WebGL 2 API 引入了对大部分的 OpenGL ES 3.0 功能集的支持; 它是通过 WebGL2RenderingContext 接口提供的。
- **WebGL 程序由** JS 的**控制代码**(control code)，和在计算机的图形处理单元(GPU)中执行的**渲染代码**(shader code)**组成**。
- WebGL 元素可以和其他 HTML 元素混合，并且会和页面的其他部分或页面背景相合成。

注意:和 canvas 的教程相比，WebGL 的本身就难理清很多，最好还是要明白概念，示例看最后的说明好了。

**准备 3D 渲染**

1. 为了使用 WebGL 进行 3D 渲染，你首先需要一个 canvas 元素。`const canvas = document.querySelector("#glcanvas");`
2. 准备 WebGL 上下文: `const gl = canvas.getContext("webgl");`。如果浏览器不支持 webgl，getContext 将会返回 null。

### 使用 WebGL 的简单示例

跟着 MDN 的 [WebGL tutorial](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial)学习，可以有一个基本了解，不要看中文版，比较拉。实在不行跟着它在[github 的代码](https://github.com/mdn/dom-examples/tree/main/webgl-examples)调试，也是好的。

这里只是列示该教程的大概内容，和用到 WebGLRenderingContext 实例方法。

**1. 渲染场景**

**着色器**是使用 OpenGL ES 着色语言 [GLSL](https://registry.khronos.org/OpenGL/specs/es/3.2/GLSL_ES_Specification_3.20.pdf) 编写的程序，它**携带着绘制形状的顶点信息以及构造绘制在屏幕上像素的所需数据**，

- 换句话说，它*负责记录着像素点的位置和颜色*。
- 绘制 WebGL 时候有两种不同的着色器函数，**顶点着色器**和**片段着色器**。(顶点着色器和片段着色器的集合常称之为**着色器程序**)
  - 需要通过用 GLSL 编写这些着色器，并将代码文本传递给 WebGL，使之在 GPU 执行时编译。

**顶点着色器**: 每次渲染一个形状时，顶点着色器会在形状中的每个顶点运行。它的工作是**将输入顶点从原始坐标系转换到 WebGL 使用的缩放空间(clipspace)坐标系**，其中每个轴的坐标范围从 -1.0 到 1.0，并且**不考虑纵横比，实际尺寸或任何其他因素**。顶点着色器需要*对顶点坐标*进行必要的*转换*，在每个顶点基础上进行其他*调整或计算*，然后通过将其*保存在*由 GLSL 提供的*特殊变量*(称为`gl_Position`)中来*返回变换后的顶点*。

**片段着色器**在顶点着色器处理完图形的顶点后，_会被要绘制的每个图形的每个像素点调用一次_。它的职责是**确定像素的颜色**，通过指定应用到像素的*纹理元素*（也就是图形纹理中的像素），获取*纹理元素的颜色*，然后*将适当的光照应用于颜色*。之后颜色*存储在特殊变量* `gl_FragColor` 中，_返回到 WebGL 层_。**该颜色将最终绘制到屏幕上图形对应像素的对应位置**。

(着色器这个比较难写示例，主要还是了解在渲染场景时，着色器的作用)

在初始化着色器这块，可能用到的函数:

- `gl.createShader(type)`: **创建**一个 [WebGLShader](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLShader) **着色器对象**。参数为`gl.VERTEX_SHADER`或`gl.FRAGMENT_SHADER`其一。
- `gl.shaderSource(shader, source)`: 设置 WebGLShader `着色器`（顶点着色器及片元着色器）的 `GLSL 程序代码字符串`。
- `gl.compileShader(shader)`: **编译一个 GLSL 着色器**，使其成为为二进制数据，然后就可以被 [WebGLProgram](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLProgram) 对象所使用。
- `gl.getShaderParameter(shader, pname)`: 返回给定的**着色器信息**。参数为`指定着色器对象`和`需要查询的属性`。
- `gl.getShaderInfoLog(shader)`: 返回指定 WebGLShader 对象的**信息日志**。它包含警告、调试和编译信息。

**2. 创建对象**

在画正方形对象前，我们需要创建一个**缓冲器**来*存储它的顶点*。可能用到的函数:

- `gl.createBuffer()`: 创建并初始化一个用于储存顶点数据或着色数据的 WebGLBuffer 对象
- `gl.bindBuffer(target, buffer)`: 将给定的 WebGLBuffer 绑定到目标。
- `gl.bufferData(target, size, usage)`: 创建并初始化了 Buffer 对象的数据存储区。有其他可省略值和用法。
  - target: 指定 Buffer 绑定点。size: Buffer 对象的数据存储区大小。usage: 指定数据存储区的使用方法。
    - target 和 usage 的可选值为 gl 的几个全局变量。

当着色器和物体都创建好后，可以开始**渲染这个场景**。例如用背景色擦除画布，接着建立摄像机透视矩阵。加载特定位置。绑定并配置好正方形的顶点缓冲到上下文。调用指定方法来画出对象。例如可以把这样步骤集中到类似`drawScene()`的方法中。可能用到的 gl 函数:

- `gl.clear(mask)`: 使用预设值来清空缓冲。
  - 可选值: `gl.COLOR_BUFFER_BIT`颜色缓冲区；`gl.DEPTH_BUFFER_BIT`深度缓冲区；`gl.STENCIL_BUFFER_BIT`模板缓冲区。
- `gl.vertexAttribPointer(index, size, type, normalized, stride, offset)`:
  - 绑定当前缓冲区范围到 gl.ARRAY_BUFFER，成为当前顶点缓冲区对象的通用顶点属性，并指定它的布局 (缓冲区对象中的偏移量)。
  - 指定要修改的顶点属性的索引。指定每个顶点属性的组成数量，必须是 1，2，3 或 4。指定数组中每个元素的数据类型,值为 gl 指定全局变量。当转换为浮点数时是否应该将整数数值归一化到特定的范围。以字节为单位指定连续顶点属性开始之间的偏移量。
- `gl.enableVertexAttribArray(index)`: 打开属性数组列表中指定索引处的通用顶点属性数组。
- `gl.getAttribLocation(program, name)`: 返回了给定 WebGLProgram 对象中某属性的下标指向位置。参数为程序名和属性名。
- `gl.useProgram(program)`: 将定义好的 WebGLProgram 对象添加到当前的渲染状态中。
- `gl.uniformMatrix[234]fv(location, transpose, value)`: 为 uniform 变量指定了矩阵值，输入值可以为 2、3、4 阶。
  - 参数为: 要修改的 uniform 属性的位置。是否转置矩阵，必须为 false。输入的矩阵值，以列主要顺序提供。
- `gl.drawArrays(mode, first, count)`: 从向量数组中绘制图元。参数类型参看[WebGL types](<(https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Types)>)
  - 参数为: GLenum 类型，指定绘制图元的方式；GLint 类型，指定从哪个点开始绘制；GLsizei 类型，指定绘制需要使用到多少个点。
- 还有一些其他 [gl-matrix](https://github.com/toji/gl-matrix) 库的 [mat4](https://glmatrix.net/docs/module-mat4.html) 的方法: `mat4.perspective()`；`mat4.create()`；`mat4.translate()`等等。

**3. 给顶点和片段着色，并绘制**

_在 GL 中，物体是由一系列顶点组成的，**每一个顶点都有位置和颜色信息**_。  
在**默认情况下**，所有像素的颜色（以及它所有的属性，包括位置）都由**线性插值计算**得来，自动形成平滑的渐变。  
如果顶点着色器*没有给顶点添加任何特定的颜色*——在顶点着色器与片段着色器之间给每个像素着白色，于是*整个正方形被渲染成纯白*。

例如给一个 2D 正方形四个角上色可能用到的步骤:

- 使用一个包含四组（需要用多个就多少组）四值向量的数组，每一组向量代表一个顶点的颜色。
- 创建一个 WebGL 缓冲区用来存储这些颜色。将数组中的值转换成 WebGL 所规定的浮点型后，存储在该缓冲区中。
- 修改顶点着色器，使得着色器可以从颜色缓冲区中正确取出颜色(例如每个顶点都与一个颜色数组中的数值相连接)。
- 修改片段着色器，例如每个片段只是根据其相对于顶点的位置得到一个插值过的颜色，而不是一个指定的颜色值。
- 在绘制场景的逻辑中，初始化颜色属性，并调用着色器程序使用绘制。

**4. 让目标动起来**

例如旋转正方形平面，可能用到的步骤:

- 创建一个变量，用于跟踪正方形的当前旋转。
- 更新绘制场景的 drawScene()函数以在绘制正方形时将当前旋转应用于正方形。
- 添加 squareRotation 随时间更改值的代码。例如创建一个新变量来跟踪上次动画播放的时间。
- 使用 requestAnimationFrame 要求浏览器在每一帧上旋转变化，形成 动画。

**5. 绘制 3D 图像**

例如之前是个 2D 的正方形，可以多绘制 5 个面，使其成为一个正方体，并继续动画旋转。
最简单的方式就是通过调用方法 gl.drawElements() 使用**顶点数组列表**来**替换**之前的通过方法 gl.drawArrays() 直接使用**顶点数组**。
而顶点数组列表里保存着将会被引用到一个个独立的顶点。

修改步骤大概有:

- 定义立方体顶点的位置: 绘制正方形改为正方体，定义立方体顶点的位置，操作类似，但有 24 个顶点（每边 4 个）
  - 顶点添加了 z 分量，因此我们需要将属性的 更新 vertexPosition 的变量 numComponents 为 3。
- 定义顶点的颜色: 首先为每个面定义一种颜色，然后使用循环为每个顶点组装一个包含所有颜色的数组。
- 定义元素数组: 将每个面定义为一对三角形，将每个三角形的顶点指定为立方体顶点数组的索引。因此立方体被描述为 12 个三角形的集合数组。
  - 这元素数组也是放在缓存区的，需要使用时取得。
- 绘制立方体: 添加新的 gl.bindBuffer()和 gl.drawElements()调用。
  - 立方体的每个面都由两个三角形组成，因此每边有 6 个顶点，即立方体中总共有 36 个顶点，尽管其中许多是重复的。
  - 然而，因为索引数组的每个元素都是简单的整数类型，所以每一帧动画需要传递给渲染程序的数据也不是很多。
- 最后，用 cubeRotation 替换变量 squareRotation，并增加一个围绕 x 轴的第二次旋转。

可能用到的新函数:

- `gl.drawElements(mode, count, type, offset)`: 在 WebGL API 从数组数据渲染图元。参数如下:
  - 指定要渲染的图元枚举类型；指定要渲染的元素数量；指定元素数组缓冲区中的值的枚举类型；指定元素数组缓冲区中的偏移量。

**6. 给 3D 图像添加纹理**

之前是每个面定义了一种颜色，现在使用贴图来代替每个面的单一的颜色。

修改步骤大概有:

- 加载纹理: 使用一张单一的纹理贴到立方体的 6 个面上，但是同样的方法可以用来加载任意数量的纹理贴图。
- 映射纹理到面: 加载纹理之后，还要创建好纹理坐标到立方体各个面的顶点的映射关系。
- 更新着色器: 着色器程序和着色器程序的初始化代码都需要进行修改，之前是使用颜色，现在使用纹理。
  - 顶点着色器 现在不再需要获取顶点颜色数据，而是获取纹理坐标数据。
  - 片段着色器 不会再使用一个简单的颜色值填充片段颜色，片段的颜色是通过采样器使用最好的映射方式从纹理中的每一个像素计算出来的。
- 绘制具体纹理贴图的立方体: 绘制时使用纹理代替颜色进行映射的绘制。
- 注意: _WebGL 纹理的加载受跨域访问控制的约束_。为了让您的内容从另一个域加载纹理，需要获得 CORS 批准。

可能用到的新函数:

- `gl.createTexture()`: 创建并初始化了一个 [WebGLTexture](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLTexture) 目标。
- `gl.bindTexture(target, texture)`: 将给定的 WebGLTexture 绑定到目标（绑定点）。
- `gl.texImage2D(args)`: 指定了二维纹理图像。参数很多，[查看](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/texImage2D)
- `gl.generateMipmap(target)`: 为 WebGLTexture 对象生成一组 mipmaps。
  - Mipmaps 是用来与物体建立距离的。高分辨率的 mipmap 用于较近的物体，而低分辨率的 mipmap 则用于较远的物体。
  - 它从纹理图像的分辨率开始，将分辨率减半，直到创建一个 1x1 维的纹理图像。
- `gl.texParameterf(target, pname, param)`: 用于给指定绑定点，设置指定的纹理参数。
  - 参数为目标绑定点，要设置的纹理参数，和该参数的值
- `gl.pixelStorei(pname, param)`: 用于图像预处理的函数。参数为处理的方式，和方式的参数。
- `gl.activeTexture(texture)`: 激活指定的纹理单元。
- `gl.uniform[1234][fi][v]()`: 指定了 uniform 变量的值。有 `f`,`fv`,`i`,`iv`与 `1,2,3,4` 交叉[共 16 种组合](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLRenderingContext/uniform)。

**7. 光照**

WebGL 并没有继承 OpenGL 中灯光的支持。所以你只能由自己完全得控制灯光。

光源类型可以概括成如下三种：

- **环境光** 是一种可以渗透到场景的每一个角落的光。它是非方向光并且会均匀地照射物体的每一个面，无论这个面是朝向哪个方向的。
- **方向光** 是一束从一个固定的方向照射过来的光。这种光的特点可以理解为好像是从一个很遥远的地方照射过来的，然后光线中的每一个光子与其它光子都是平行运动的。举个例子来说，阳光就可以认为是方向光。
- **点光源光** 是指光线是从一个点发射出来的，是向着四面八方发射的。这种光在我们的现实生活中是最常被用到的。举个例子来说，电灯泡就是向各个方向发射光线的。

如果简化光照模型，_只考虑简单的方向光和环境光，不会考虑任何镜面反射和点光源_。这样只需要在使用的环境光上加上照射到旋转立方体的方向光就可以了。
但是关于方向光还是有两点需要注意一下:

- 需要在每个顶点信息中加入面的**朝向法线**。这个法线是一个垂直于这个顶点所在平面的向量。
- 需要明确方向光的传播方向，可以使用一个**方向向量**来定义。

给之前的正方体加上简化光照模型，大概要修改:

<!-- - 更新顶点着色器，考虑到环境光，再考虑到方向光（方向光的作用会因为光线方向与面的夹角关系而不同），计算每一个顶点的颜色。 -->

- 建立顶点法线: 建立一个数组来存放立方体所有顶点的法线。如果是对复杂物体，则法线的计算方法需要更深入的研究。
- 更新着色器: 顶点着色器，让它给每一个基于环境光和方向光的顶点一个着色器值。片段着色器现在需要根据顶点着色器计算出的光照值来更新。

**8. 动画纹理**

之前正方体的纹理为一个静态图片，可以将静态纹理替换为正在播放的 mp4 视频文件的帧，达到一个动画纹理的效果。

似乎只需要替换纹理部分，大概修改步骤如下:

- 获取视频: 创建 `<video>` 将用于检索视频帧的元素
- 用视频帧作为纹理: 创建一个空的纹理对象，在其中放置一个像素。之前使用 texImage2D()传递 Image 对象，现在传递`<video>` 元素。
  - WebGL 知道如何从 `<video>` 元素中取出当前帧并将其用作纹理。

跟着官方示例一步步做下来，大概有几个体验:

- 着色器很重要，但使用比较麻烦，创建、绑定 GLSL 源代码、编译等一系列操作。在使用时，还需要注意其`attrib`、`uniform`的位置，统一存储传递。
- buffer 很重要，也是要创建再绑定数据，注意 buffer 数据数组类型的不同。
- 注意场景的渲染和设置。背景色、角度、坐标系等等。
- 对于物体对象的渲染，纯色，或者静态图、视频帧的纹理都可以，但是用视频帧挺炫酷的。
- 对于很多矩阵运算，数学基础不够也比较难以理解。就像 js-matrix 库能提供一些方法，都不知道要用啥。
- 因为使用到了 GPU，在虚拟机中的 vue 的 demo，浏览器的 GPU 渲染的 CPU 占用很高，非常卡。
- 几个重点: 着色器程序、物体对象、场景、数学矩阵。反正直接使用 WebGL 的 API 是比较麻烦的，不建议。

还是推荐看下 MDN [WebGL 模型视图投影](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_model_view_projection)这一章节的内容。
掘金的博文 [零基础玩转 WebGL - 快速上手](https://juejin.cn/post/7146385806347730952)有兴趣也可以看看。
但更建议使用 WebGL 之上的封装库，例如 three.js 之类的。

---

ref: 使用原生接口的可能不太现实，都用封装的库比较多，例如 three.js，Cesium.js，Babylon.js 等。建议还是了解各基本原理即可。就算 MDN 的说明看起来都挺复杂的。

- MDN [WebGL 教程](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial)
- MDN [WebGL 模型视图投影](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_model_view_projection)
- [WebGL2 理论基础](https://webgl2fundamentals.org/webgl/lessons/zh_cn/)
- [WebGLRenderingContext](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGLRenderingContext) 基于 OpenGL ES 2.0 的绘图上下文
- [WebGL2RenderingContext](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL2RenderingContext) 在底层使用了 OpenGL ES 3.0 的绘图上下文
- 掘金 [WebGL 概念和基础入门](https://juejin.cn/post/6994940475459731463)
- 掘金 [零基础玩转 WebGL - 快速上手](https://juejin.cn/post/7146385806347730952)
