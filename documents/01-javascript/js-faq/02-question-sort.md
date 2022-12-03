时间紧，就看这两篇

- x 390243 9.1k[🔥 连八股文都不懂还指望在前端混下去么](https://juejin.cn/post/7016593221815910408)
- x 291517 6.3k[做了一份前端面试复习计划，保熟～](https://juejin.cn/post/7061588533214969892)
- x 470618 6.4k[2021 年前端面试必读文章【超三百篇文章/赠复习导图】](https://juejin.cn/post/6844904116339261447)
- x 275299 5.6k[2021 年我的前端面试准备](https://juejin.cn/post/6989422484722286600)
- **x** 83122 1.8k[【🐯 初/中级前端面经】中小型公司面试时都会问些什么?](https://juejin.cn/post/7064740689178787871)

## 网络相关（http、web 安全）

osi7 层模型，tcp5 层模型  
http 协议等、状态码、跨域

tcp 握手等、udp、粘包问题

dns 解析等

网络安全、HTTP 协议  
TCP UDP 区别  
Http 和 Https 区别（高频）  
GET 和 POST 区别（高频）  
理解 xss，csrf，ddos 攻击原理以及避免方式  
http 特性以及状态码  
http 三次握手  
http 四次挥手  
http1.0、http1.1、http2.0 的区别  
http 如何实现缓存  
输入 url 后 http 请求的完整过程

HTTP1, HTTP2, HTTPS、常见的 http 状态码；  
浏览从输入网址到回车发生了什么；  
前端安全（CSRF、XSS）

TCP 连接(三次握手, 四次挥手)

post 和 get 的区别  
http 的基本知识  
跨域

Websocket  
前端的网络请求方式  
谈谈 HTTP 协议中的短轮询、长轮询、长连接和短连接

TCP 的拥塞控制

xss 和 csrf

http 状态码  
状态码分类  
常见状态码  
关于协议和规范  
http 缓存  
关于缓存  
强制缓存  
协商缓存（对比缓存）  
综述  
三种刷新操作对 http 缓存的影响  
正常操作：地址栏输入 url，跳转链接，前进后退等。  
手动刷新：f5，点击刷新按钮，右键菜单刷新。  
强制刷新：ctrl + f5，shift+command+r。

HTTP/2 有哪些改进？  
HTTPS 的一些原理

## 浏览器相关

localstorage 等

从输入 URL 到页面加载的全过程  
浏览器重绘与重排的区别？  
如何触发重排和重绘？  
如何避免重绘或者重排？  
介绍下 304 过程  
浏览器的缓存机制 强制缓存 && 协商缓存  
说下进程、线程和协程

浏览器渲染机制、重绘、重排

从一个 url 到最终页面渲染完成，发生了什么？

缓存  
前端跨域、浏览器缓存、cookie, session, token, localstorage, sessionstorage；  
Cookies 与 Session，SessionStore，LocalStore 的区别及使用

cookie  
localStorage 和 sessionStorage

## 性能问题

前端性能优化

前端性能优化的几种方式

什么是同源策略

前后端如何通信

跨域通信的几种方式

能不能说一说浏览器的本地存储？各自优劣如何？

图片优化的方式

500 张图片，如何实现预加载优化

懒加载具体实现

减少 http 请求的方式

webpack 如何配置大型项目

防抖和节流（resize，scroll，input）。

减少回流（重排）和重绘。

事件委托。

css 放 ，js 脚本放 最底部。

减少 DOM 操作。

按需加载，比如 React 中使用 React.lazy 和 React.Suspense ，通常需要与 webpack 中的 splitChunks 配合。

构建方面：

压缩代码文件，在 webpack 中使用 terser-webpack-plugin 压缩 Javascript 代码；使用  
css-minimizer-webpack-plugin 压缩 CSS 代码；使用 html-webpack-plugin 压缩 html 代码。

开启 gzip 压缩，webpack 中使用 compression-webpack-plugin ，node 作为服务器也要开启，使用 compression。

常用的第三方库使用 CDN 服务，在 webpack 中我们要配置 externals，将比如 React， Vue 这种包不打倒最终生成的文
件中。而是采用 CDN 服务。

其它：

使用 http2。因为解析速度快，头部压缩，多路复用，服务器推送静态资源。

使用服务端渲染。

图片压缩。

使用 http 缓存，比如服务端的响应中添加 Cache-Control / Expires 。

怎么解决白屏问题

## html+css

HTML5 新特性、语义化  
CSS 选择器及优先级  
position 属性的值有哪些及其区别  
box-sizing 属性  
CSS 盒子模型  
BFC（块级格式上下文）  
让一个元素水平垂直居中  
隐藏页面中某个元素的方法  
用 CSS 实现三角符号  
页面布局  
1.Flex 布局  
2.Rem 布局 3.百分比布局 4.浮动布局  
如何使用 rem 或 viewport 进行移动端适配  
清除浮动的方式

常见的 DOM 操作有哪些

html5 新特性、语义化

css 盒子模型  
css 样式优先级  
什么是 BFC？BFC 的布局规则是什么？如何创建 BFC？BFC 应用？  
DOM、BOM 对象

浏览器内核  
盒模型、flex 布局、两/三栏布局、水平/垂直居中；  
BFC、清除浮动；  
css3 动画、H5 新特性。

CSS 基础面试题（附答案）  
如何居中 div？  
CSS3 新特性  
清除浮动  
media 媒体查询  
讲一讲 Flex 布局，以及常用的属性？  
BFC  
px rem em vh vw 之间的区别到底是啥？  
0.5px 的线  
12px 以下的字体

如何理解 HTML 语义化？  
script 标签中 defer 和 async 的区别？  
从浏览器地址栏输入 url 到请求返回发生了什么  
盒模型介绍  
css 选择器和优先级  
重排（reflow）和重绘（repaint）的理解  
对 BFC 的理解  
实现两栏布局（左侧固定 + 右侧自适应布局）  
实现圣杯布局和双飞翼布局（经典三分栏布局）  
水平垂直居中多种实现方式  
flex 布局  
line-height 如何继承？

## js 一些技巧

函数柯里化的实现  
介绍节流防抖原理、区别以及应用

防抖、节流

去重

## 前端编译

webpack  
esbuild  
babel  
swc

前端工程化  
webpack 配置，webpack4.0 有哪些优化点  
webpack 如何实现代码分离  
常见的 Webpack Loader? 如何实现一个 Webpack Loader(NO)  
常见的 Webpack Plugin? 如何实现一个 Webpack Plugin(NO)  
loader 和 plugin 对比？  
前端模块化，CMD、AMD、CommonJS  
CommonJS  
commonJs 规范：  
优势：  
缺点：  
AMD  
AMD 规范  
优点  
CMD  
CMD 规范  
优点

## 数据库相关

介绍关系型数据库 RD、nosql 型、newsql 型各自简单对比和代表作

各自一些特征 features

## 架构设计相关

分布式架构、微服务架构的好处等

常听说的大算法的作用  
比如拜占庭算法用来干啥、raft 算法、布隆过滤器等等

## 工作实践经验

工作项目的架构说明  
踩坑与解决
