- [从浏览器多进程到 JS 单线程，JS 运行机制最全面的一次梳理](https://segmentfault.com/a/1190000012925872)-2018-01
- [WASEC: understanding the browser](https://odino.org/wasec-understanding-the-browser/)-29 July 2018
- [How Web Browsers Work ?](https://medium.com/@pdster/how-web-browsers-work-6385b9374375)- 2018-12(有参考 2011 年 web.dev 那篇)
- [Chrome 浏览器架构](https://xie.infoq.cn/article/5d36d123bfd1c56688e125ad3)-2020-10-06-参看上一篇比较多
- [what-is-browser](https://www.browserstack.com/guide/what-is-browser)-2023(他的产品的推广相关吧)
- [The Chromium Projects- Design Documents](https://www.chromium.org/developers/design-documents/)-Chromium 设计文档
- [Chromium Design Documents 的中文翻译](https://github.com/ahangchen/Chromium_doc_zh)-最近到 2019 年左右，大部分都没翻译

---推荐

- \*[极客时间的浏览器工作原理与实践](https://github.com/poetries/browser-working-principle)-2020 左右
- \*web.dev-[How browsers work](https://web.dev/howbrowserswork/)-2011 年博客
- [翻译:浏览器内部的工作原理](https://www.cnblogs.com/cnwebdeveloper/articles/2234423.html)-上一篇博客的中文翻译-博客园
- \*web.dev-[Inside look at modern web browser](https://developer.chrome.com/blog/inside-browser-part1/)-2018-web.dev,有 4 篇

- [[译] 现代浏览器内部揭秘（第一部分）](https://juejin.cn/post/6844903679389073415)-上面 4 篇文章的掘金翻译计划
- [[译] 现代浏览器内部揭秘（第二部分）](https://juejin.cn/post/6844903692890537992)
- [[译] 现代浏览器内部揭秘（第三部分）](https://juejin.cn/post/6844903692894732295)
- [[译] 现代浏览器内部揭秘（第四部分）](https://juejin.cn/post/6844903695600058375)
- [图解浏览器的基本工作原理](https://zhuanlan.zhihu.com/p/47407398)-也是上面 4 篇为基础的扩展学习

---

- web 浏览器的核心功能：网页浏览：浏览器能够加载和显示网页的内容，包括文字、图像、视频和音频等。

- web 网页的发展史，对应到浏览器的发展史

- 网页的组成，对应浏览器的组成

- 网页解析渲染的过程，浏览器各个核心组成部件的功能

- 配套的网络部分 HTTP 等内容、资源访问 URI、GIS 硬件加速等

- 其他浏览功能上的补充：web 浏览器软件形态上的组成：导航、搜索、书签、下载、隐私安全、扩展等

---

## 浏览器的功能：

- 解析 uri 的 web 资源并进行显示
- 关联关键字：uri、HTML 和 CSS 规范、部分浏览器并不完全兼容规范、有的还有自己的扩展……

## 浏览器的用户界面：

- 地址栏、前进后退按钮、刷新和停止按钮、主页按钮、书签、web 显示的主窗口、用来显示你所请求页面的主窗口之外的其他部分……

## 浏览器的主要组件：

- 用户界面－ 包括地址栏、后退/前进按钮、书签目录等，也就是你所看到的除了用来显示你所请求页面的主窗口之外的其他部分
- 浏览器引擎－ 用来查询及操作渲染引擎的接口
- 渲染引擎－ 用来显示请求的内容，例如，如果请求内容为 html，它负责解析 html 及 css，并将解析后的结果显示出来
- 网络－ 用来完成网络调用，例如 http 请求，它具有平台无关的接口，可以在不同平台上工作
- UI 后端－ 用来绘制类似组合选择框及对话框等基本组件，具有不特定于某个平台的通用接口，底层使用操作系统的用户接口
- JS 解释器－ 用来解释执行 JS 代码
- 数据存储－ 属于持久层，浏览器需要在硬盘中保存类似 cookie 的各种数据，HTML5 定义了 web database 技术，这是一种轻量级完整的客户端存储技术

### 渲染引擎

- 功能
  - 默认情况下，渲染引擎可以显示 HTML 和 XML 文档和图像。可以通过插件或扩展显示其他类型的数据；
- 分类（不同浏览器不同渲染引擎或者都用的引擎）
- 工作主要流程
  - 渲染引擎在取得内容之后的基本流程：解析 html 以构建 dom 树->构建 render 树->布局 render 树->绘制 render 树
  - **页面的解析、渲染过程，重点**，还有 CRP(关键渲染路径)等内容
