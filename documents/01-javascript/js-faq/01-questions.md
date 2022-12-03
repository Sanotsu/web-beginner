阅读量和 star 数，都是 2022-08-3 查看时记录，github 项目也是当时最近一个月内有更新的，没有更新的更多 star 的也没统计

很多都是 web 前端一起的，此处仅关注 js 部分

post

- x 328556 2.3k[「2021」高频前端面试题汇总之 JavaScript 篇（上）](https://juejin.cn/post/6940945178899251230)
- x 390243 9.1k[🔥 连八股文都不懂还指望在前端混下去么](https://juejin.cn/post/7016593221815910408)
- x 275299 5.6k[2021 年我的前端面试准备](https://juejin.cn/post/6989422484722286600)
- x 261668 4.8k[由浅入深，66 条 JavaScript 面试知识点](https://juejin.cn/post/6844904200917221389)
- x 124389 4.8k[2021 前端面试经常被问到的题(附答案)](https://blog.csdn.net/xieanna123/article/details/105545758)
- x 291517 6.3k[做了一份前端面试复习计划，保熟～](https://juejin.cn/post/7061588533214969892)
- x 84669 1.1k[2021 年我的前端面试小结(70 题)](https://juejin.cn/post/7026947170683076621)
- x 127059 3.3k[前端面试知识点（一）](https://juejin.cn/post/6987549240436195364)
- x 470618 6.4k[2021 年前端面试必读文章【超三百篇文章/赠复习导图】](https://juejin.cn/post/6844904116339261447)

贴近面试

- **x** 83122 1.8k[【🐯 初/中级前端面经】中小型公司面试时都会问些什么?](https://juejin.cn/post/7064740689178787871)
- **x** 61000 115[Web 中高级前端面试题集合（200+）](https://segmentfault.com/a/1190000021966814)
- **x** 207139 3.4k[最近两周出去面试遇到的面试题（前端初级、长更）](https://juejin.cn/post/7073869980411887652)

- 有点关键字 [2022 前端面试小册【腾讯 9、美团 7、百度 t5、快手 3b】的 offer](https://juejin.cn/post/7071922989238845453)
- 100969 [「2021」高频前端面试题汇总之 JavaScript 篇（下）](https://juejin.cn/post/6941194115392634888)
- 48680 [2022 年我的前端面试准备](https://juejin.cn/post/7072158430294704135)
- [「offer 来了」JavaScript 篇，保姆级巩固你的 js 知识体系](https://juejin.cn/post/7026502510172962829)
- [javascript 高频面试题整理](https://juejin.cn/post/6948600448388038670)
- [【刘建】2022 年前端面试题汇总](https://segmentfault.com/a/1190000041629712)

github

- 54.8k [h5bp/Front-end-Developer-Interview-Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions)
- 34.7k [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook)
- 5.6k [CavsZhouyou/Front-End-Interview-Notebook](https://github.com/CavsZhouyou/Front-End-Interview-Notebook)
- 4.6k [febobo/web-interview](https://github.com/febobo/web-interview)
- 2.1k [yisainan/web-interview](https://github.com/yisainan/web-interview)

---

# [「2021」高频前端面试题汇总之 JavaScript 篇（上）](https://juejin.cn/post/6940945178899251230)

JavaScript 有哪些数据类型，它们的区别？

数据类型检测的方式有哪些

判断数组的方式有哪些

null 和 undefined 区别

typeof null 的结果是什么，为什么？

intanceof 操作符的实现原理及实现

为什么 0.1+0.2 ! == 0.3，如何让其相等

如何获取安全的 undefined 值？

typeof NaN 的结果是什么？

isNaN 和 Number.isNaN 函数的区别？

== 操作符的强制类型转换规则？

其他值到字符串的转换规则？

其他值到数字值的转换规则？

其他值到布尔类型的值的转换规则？

|| 和 && 操作符的返回值？

Object.is() 与比较操作符 “===”、“==” 的区别？

什么是 JavaScript 中的包装类型？

JavaScript 中如何进行隐式类型转换？

操作符什么时候用于字符串的拼接？

为什么会有 BigInt 的提案？

object.assign 和扩展运算法是深拷贝还是浅拷贝，两者区别

let、const、var 的区别

const 对象的属性可以修改吗

如果 new 一个箭头函数的会怎么样

箭头函数与普通函数的区别

箭头函数的 this 指向哪⾥？

扩展运算符的作用及使用场景

Proxy 可以实现什么功能？

对对象与数组的解构的理解

如何提取高度嵌套的对象里的指定属性？

对 rest 参数的理解

ES6 中模板语法与字符串处理

new 操作符的实现原理

map 和 Object 的区别

map 和 weakMap 的区别

JavaScript 有哪些内置对象

常用的正则表达式有哪些？

对 JSON 的理解

JavaScript 脚本延迟加载的方式有哪些？

JavaScript 类数组对象的定义？

数组有哪些原生方法？

Unicode、UTF-8、UTF-16、UTF-32 的区别？

常见的位运算符有哪些？其计算规则是什么？

按位与运算符（&）

按位或运算符（|）

异或运算符（^）

取反运算符 (~)

左移运算符（<<）

右移运算符（>>）

原码、补码、反码

为什么函数的 arguments 参数是类数组而不是数组？如何遍历类数组?

什么是 DOM 和 BOM？

对类数组对象的理解，如何转化为数组

escape、encodeURI、encodeURIComponent 的区别

对 AJAX 的理解，实现一个 AJAX 请求

JavaScript 为什么要进行变量提升，它导致了什么问题？

什么是尾调用，使用尾调用有什么好处？

ES6 模块与 CommonJS 模块有什么异同？

常见的 DOM 操作有哪些

use strict 是什么意思 ? 使用它区别是什么？

如何判断一个对象是否属于某个类？

强类型语言和弱类型语言的区别

解释性语言和编译型语言的区别

for...in 和 for...of 的区别

如何使用 for...of 遍历对象

ajax、axios、fetch 的区别

数组的遍历方法有哪些

forEach 和 map 方法有什么区别

对原型、原型链的理解

原型修改、重写

原型链指向

原型链的终点是什么？如何打印出原型链的终点？

如何获得对象非原型链上的属性？

对闭包的理解

对作用域、作用域链的理解

对执行上下文的理解

执行上下文类型

执行上下文栈

创建执行上下文

# [🔥 连八股文都不懂还指望在前端混下去么](https://juejin.cn/post/7016593221815910408)

JS 中的 8 种数据类型及区别

JS 中的数据类型检测方案

1.typeof

2.instanceof

3.Object.prototype.toString.call()

var && let && const

JS 垃圾回收机制

作用域和作用域链

闭包的两大作用：保存/保护

JS 中 this 的五种情况

原型 && 原型链

new 运算符的实现机制

EventLoop 事件循环

浏览器中的事件环（Event Loop)

Node 环境中的事件环（Event Loop)

setTimeout、Promise、Async/Await 的区别

Async/Await 如何通过同步的方式实现异步

介绍节流防抖原理、区别以及应用

# [2021 年我的前端面试准备](https://juejin.cn/post/6989422484722286600)

js 数据类型、typeof、instanceof、类型转换

闭包(高频)

原型、原型链(高频)

this 指向、new 关键字

作用域、作用域链、变量提升

继承(含 es6)、多种继承方式

EventLoop

原生 ajax

事件冒泡、捕获(委托)

ES6

# [由浅入深，66 条 JavaScript 面试知识点](https://juejin.cn/post/6844904200917221389)

介绍一下 js 的数据类型有哪些，值是如何存储的

&& 、 ||和!! 运算符分别能做什么

js 的数据类型的转换

JS 中数据类型的判断（ typeof，instanceof，constructor，Object.prototype.toString.call()

介绍 js 有哪些内置对象？

undefined 与 undeclared 的区别？

null 和 undefined 的区别？

{}和[]的 valueOf 和 toString 的结果是什么？

Javascript 的作用域和作用域链

javascript 创建对象的几种方式？

JavaScript 继承的几种实现方式？

寄生式组合继承的实现？

谈谈你对 this、call、apply 和 bind 的理解

JavaScript 原型，原型链？ 有什么特点？

js 获取原型的方法？

什么是闭包，为什么要用它？

什么是 DOM 和 BOM？

三种事件模型是什么？

事件委托是什么？

什么是事件传播?

什么是事件捕获？

什么是事件冒泡？

DOM 操作——怎样添加、移除、移动、复制、创建和查找节点？

js 数组和字符串有哪些原生方法,列举一下

常用的正则表达式（仅做收集，涉及不深）

Ajax 是什么? 如何创建一个 Ajax？

创建步骤：

面试手写（原生）：

jQuery 写法

promise 封装实现：

js 延迟加载的方式有哪些？

谈谈你对模块化开发的理解？

js 的几种模块规范？

AMD 和 CMD 规范的区别？

ES6 模块与 CommonJS 模块、AMD、CMD 的差异。

requireJS 的核心原理是什么？

谈谈 JS 的运行机制

js 单线程

js 事件循环

arguments 的对象是什么？

为什么在调用这个函数时，代码中的 b 会变成一个全局变量?

简单介绍一下 V8 引擎的垃圾回收机制

哪些操作会造成内存泄漏？

ECMAScript 是什么？

ECMAScript 2015（ES6）有哪些新特性？

var,let 和 const 的区别是什么？

什么是箭头函数？

什么是类？

什么是模板字符串？

什么是对象解构？

什么是 Set 对象，它是如何工作的？

什么是 Proxy？

写一个通用的事件侦听器函数

什么是函数式编程? JavaScript 的哪些特性使其成为函数式语言的候选语言？

什么是高阶函数？

为什么函数被称为一等公民？

手动实现 Array.prototype.map 方法

手动实现 Array.prototype.filter 方法

手动实现 Array.prototype.reduce 方法

js 的深浅拷贝

手写 call、apply 及 bind 函数

函数柯里化的实现

js 模拟 new 操作符的实现

什么是回调函数？回调函数有什么缺点

Promise 是什么，可以手写实现一下吗？

Iterator 是什么，有什么作用？

Generator 函数是什么，有什么作用？

什么是 async/await 及其如何工作,有什么优缺点？

instanceof 的原理是什么，如何实现

js 的节流与防抖

什么是设计模式？

概念

设计原则

设计模式的类型

# [2021 前端面试经常被问到的题(附答案)](https://blog.csdn.net/xieanna123/article/details/105545758)

Symbol

dom 常用的操作

Promise

this

new

手写各种原生方法

单线程异步

获取元素节点

判断一个对象是 Array 类型

事件循环

Set 和 Map

proxy

Promise/async/Generator

继承

一个合格的中级前端工程师需要掌握的 28 个 JavaScript 技巧

闭包

函数柯里化

for...in 和 for...of 区别

数组去重

# [做了一份前端面试复习计划，保熟～](https://juejin.cn/post/7061588533214969892)

数据类型

基本的数据类型介绍，及值类型和引用类型的理解

数据类型的判断

手写深拷贝

根据 0.1+0.2 ! == 0.3，讲讲 IEEE 754 ，如何让其相等？

原型和原型链

作用域与作用域链

执行上下文

闭包

call、apply、bind 实现

new 实现

异步

event loop、宏任务和微任务

Promise

async/await 和 Promise 的关系

浏览器的垃圾回收机制

实现一个 EventMitter 类

# [2021 年我的前端面试小结(70 题)](https://juejin.cn/post/7026947170683076621)

基本数据类型、引用类型、基本类型的区别...

promise 和 async await 相关知识 es6

宏任务和微任务(event loop) promise 属于哪个

es6 原理

高阶函数和偏函数、柯里化

async Generator promise 区别 都是异步解决方案

怎么判断浏览器是否支持 es6

form 和 json 等等 post 传参的区别

# [【🐯 初/中级前端面经】中小型公司面试时都会问些什么?](https://juejin.cn/post/7064740689178787871)

js 原型和原型链

Person.prototype.constructor 是什么

函数有没有 `__proto__` 属性

谈一谈 js 数据类型

如何判断数据类型的多种方式，有什么区别，适用场景

Promise 如何一次进行多个异步请求

Promise.all 的返回机制是什么

如果想要其中一个请求出错了但是不返回结果怎么办

let,const,var 有什么区别

遍历数组的 n 种方法

ajax 是什么?有什么优缺点

同步和异步的区别

如何解决跨域问题

不使用 promise.all , async/await 怎么实现?

promise.all 和 async/await 有什么区别?

promise.all 是为了解决什么问题?

call，apply，bind 有什么区别和应用场景

数组深拷贝

es6 有哪些新特性

promise 都有哪些方法

遍历数组的 n 种方法

ts 和 js 的优缺点

说一下闭包和函数柯里化

解释一下事件循环，微任务和宏任务都有哪些？

解释一下原型链

所有的对象都有原型吗？

promise 你都用过哪些方法

ts 跟 js 有什么区别，优点和缺点

# [Web 中高级前端面试题集合（200+）](https://segmentfault.com/a/1190000021966814)

Vue 的响应式原理中 Object.defineProperty 有什么缺陷？为什么在 Vue3.0 采用了 Proxy，抛弃了 Object.
defineProperty？

[['1', '2', '3'].map(parseInt) what & why ?]

（挖财）什么是防抖和节流？有什么区别？如何实现？

介绍下 Set、Map、WeakSet 和 WeakMap 的区别？

ES5/ES6 的继承除了写法以外还有什么区别？

setTimeout、Promise、Async/Await 的区别

（头条、微医）Async/Await 如何通过同步的方式（形式）实现异步

简述一下 Generator 函数

（滴滴、挖财、微医、海康）JS 异步解决方案的发展历程以及优缺点。

简述浏览器缓存读取规则

实现一个 sleep 函数

call 和 apply 的区别是什么，哪个性能更好一些

（百度）实现 (5).add(3).minus(2) 功能

操作题（考察数组基础）

操作题（考察消息队列）

箭头函数与普通函数（function）的区别是什么？构造函数（function）可以使用 new 生成实例，那么箭头函数可以吗？为什么？

ES6 代码转成 ES5 代码的实现思路是什么？

简单说说 js 中有哪几种内存泄露的情况

instanceof 的实现原理

简述执行上下文和执行栈

简述浏览器与 Node 的事件循环

谈一谈你理解的函数式编程？

什么是尾调用，使用尾调用有什么好处？

# [2021 年前端面试必读文章【超三百篇文章/赠复习导图】](https://juejin.cn/post/6844904116339261447)

执行上下文/作用域链/闭包

this/call/apply/bind

原型/继承

Promise

深浅拷贝

事件机制/Event Loop

函数式编程

Service Worker / PWA

Web Worker

常用方法

#[最近两周出去面试遇到的面试题（前端初级、长更）](https://juejin.cn/post/7073869980411887652)

什么是深拷贝和浅拷贝?以及怎么实现深拷贝和浅拷贝?

什么是原型什么是原型链?

箭头函数和普通函数有什么区别?

New 操作符做了什么事情?

说一下 eventloop

什么是闭包，闭包的作用是什么

Promise 是什么?

Set 和 Map 有什么区别？

map 和 foreach 有什么区别

说一下常见的检测数据类型的几种方式?

说一下 slice splice split 的区别?

说一下怎么把类数组转换为数组?

说一下数组如何去重,你有几种方法?

说一下怎么取出数组最多的一项？

说一下 JSON.stringify 有什么缺点？

说一下 for...in 和 for...of 的区别?

# [前端面试知识点（一）](https://juejin.cn/post/6987549240436195364)

JavaScript 是如何运行的？解释型语言和编译型语言的差异是什么？

简单描述一下 Babel 的编译过程？

JavaScript 中的数组和函数在内存中是如何存储的？

浏览器和 Node.js 中的事件循环机制有什么区别？

ES6 Modules 相对于 CommonJS 的优势是什么？

高级程序设计语言是如何编译成机器语言的？

谈谈你对大型项目的代码解耦设计理解？什么是 Ioc？一般 DI 采用什么设计模式实现？

列举你所了解的编程范式？

什么是面向切面（AOP）的编程？

什么是函数式编程？

响应式编程的使用场景有哪些？

JavaScript 中对象的属性描述符有哪些？分别有什么作用？

JavaScript 中 console 有哪些 api ?

简单对比一下 Callback、Promise、Generator、Async 几个异步 API 的优劣？

Object.defineProperty 有哪几个参数？各自都有什么作用？

Object.defineProperty 和 ES6 的 Proxy 有什么区别？

ES6 中 Symbol、Map、Decorator 的使用场景有哪些？或者你在哪些库的源码里见过这些 API 的使用？

为什么要使用 TypeScript ? TypeScript 相对于 JavaScript 的优势是什么？

TypeScript 中 const 和 readonly 的区别？枚举和常量枚举的区别？接口和类型别名的区别？

TypeScript 中 any 类型的作用是什么？

TypeScript 中 any、never、unknown 和 void 有什么区别？

TypeScript 中 interface 可以给 Function / Array / Class（Indexable）做声明吗？

TypeScript 中可以使用 String、Number、Boolean、Symbol、Object 等给类型做声明吗？

TypeScript 中的 this 和 JavaScript 中的 this 有什么差异？

TypeScript 中使用 Unions 时有哪些注意事项？

TypeScript 如何设计 Class 的声明？

TypeScript 中如何联合枚举类型的 Key?

TypeScript 中 ?.、??、!.、\_、\*\* 等符号的含义？

TypeScript 中预定义的有条件类型有哪些？

简单介绍一下 TypeScript 模块的加载机制？

简单聊聊你对 TypeScript 类型兼容性的理解？抗变、双变、协变和逆变的简单理解？

TypeScript 中对象展开会有什么副作用吗？

TypeScript 中 interface、type、enum 声明有作用域的功能吗？

TypeScript 中同名的 interface 或者同名的 interface 和 class 可以合并吗？

如何使 TypeScript 项目引入并识别编译为 JavaScript 的 npm 库包？

TypeScript 的 tsconfig.json 中有哪些配置项信息？

TypeScript 中如何设置模块导入的路径别名？

- 有点关键字 [2022 前端面试小册【腾讯 9、美团 7、百度 t5、快手 3b】的 offer](https://juejin.cn/post/

7071922989238845000.

# [「2021」高频前端面试题汇总之 JavaScript 篇（下）](https://juejin.cn/post/6941194115392634888)

对 this 对象的理解

call() 和 apply() 的区别？

实现 call、apply 及 bind 函数

异步编程的实现方式？

setTimeout、Promise、Async/Await 的区别

setTimeout

Promise

async/await

对 Promise 的理解

Promise 的基本用法

创建 Promise 对象

Promise 方法

Promise 解决了什么问题

Promise.all 和 Promise.race 的区别的使用场景

对 async/await 的理解

await 到底在等啥？

async/await 的优势

async/await 对比 Promise 的优势

async/await 如何捕获异常

并发与并行的区别？

什么是回调函数？回调函数有什么缺点？如何解决回调地狱问题？

setTimeout、setInterval、requestAnimationFrame 各有什么特点？

对象创建的方式有哪些？

对象继承的方式有哪些？

- [2022 年我的前端面试准备](https://juejin.cn/post/7072158430294704135)

- [「offer 来了」JavaScript 篇，保姆级巩固你的 js 知识体系](https://juejin.cn/post/7026502510172962829)

- [javascript 高频面试题整理](https://juejin.cn/post/6948600448388038670)

- [【刘建】2022 年前端面试题汇总](https://segmentfault.com/a/1190000041629712)

github

- 54.8k [h5bp/Front-end-Developer-Interview-Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions)

- 34.7k [yangshun/front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook)

请解释事件委托（event delegation）。

请简述 JavaScript 中的 this。

请解释原型继承（prototypal inheritance）的工作原理。

说说你对 AMD 和 CommonJS 的了解。

请解释下面代码为什么不能用作 IIFE：function foo(){ }();，需要作出哪些修改才能使其成为 IIFE？

null、undefined 和未声明变量之间有什么区别？如何检查判断这些状态值？

什么是闭包（closure），为什么使用闭包？

请说明.forEach 循环和.map()循环的主要区别，它们分别在什么情况下使用？

匿名函数的典型应用场景是什么？

你如何组织自己的代码？（使用模块模式（module pattern）还是经典继承（classical inheritance）？）

宿主对象（host objects）和原生对象（native objects）的区别是什么？

下列语句有什么区别：function Person(){}、var person = Person()和 var person = new Person()？

.call 和.apply 有什么区别？

请说明 Function.prototype.bind 的用法。

什么时候会用到 document.write()？

功能检测（feature detection）、功能推断（feature inference）和使用 UA 字符串之间有什么区别？

请尽可能详细地解释 Ajax。

使用 Ajax 的优缺点分别是什么？

请说明 JSONP 的工作原理，它为什么不是真正的 Ajax？

你使用过 JavaScript 模板吗？用过什么相关的库？

请解释变量提升（hoisting）。

请描述事件冒泡。

“attribute” 和 “property” 之间有什么区别？

为什么扩展 JavaScript 内置对象是不好的做法？

document 中的 load 事件和 DOMContentLoaded 事件之间的区别是什么？

`==`和`===`的区别是什么？

请解释关于 JavaScript 的同源策略。

请使下面的语句生效：

请说明三元表达式中“三元”这个词代表什么？

什么是"use strict";？使用它有什么优缺点？

创建一个循环，从 1 迭代到 100，3 的倍数时输出 "fizz"，5 的倍数时输出 "buzz"，同时为 3 和 5 的倍数时输出
"fizzbuzz"。

为什么不要使用全局作用域？

为什么要使用 load 事件？这个事件有什么缺点吗？你知道一些代替方案吗，为什么使用它们？

请解释单页应用是什么，如何使其对 SEO 友好。

你对 Promises 及其 polyfill 的掌握程度如何？

Promise 代替回调函数有什么优缺点？

用转译成 JavaScript 的语言写 JavaScript 有什么优缺点？

你使用什么工具和技巧调试 JavaScript 代码？

你使用什么语句遍历对象的属性和数组的元素？

请解释可变对象和不可变对象之间的区别。

请解释同步和异步函数之间的区别。

什么是事件循环？调用堆栈和任务队列之间有什么区别？

请解释 function foo() {}和 var foo = function() {}之间 foo 的用法上的区别。

使用 let、var 和 const 创建变量有什么区别？

ES6 的类和 ES5 的构造函数有什么区别？

你能给出一个使用箭头函数的例子吗，箭头函数与其他函数有什么不同？

在构造函数中使用箭头函数有什么好处？

高阶函数（higher-order）的定义是什么？

请给出一个解构（destructuring）对象或数组的例子。

ES6 的模板字符串为生成字符串提供了很大的灵活性，你可以举个例子吗？

你能举出一个柯里化函数（curry function）的例子吗？它有哪些好处？

使用扩展运算符（spread）的好处是什么，它与使用剩余参数语句（rest）有什么区别？

如何在文件之间共用代码？

什么情况下会用到静态类成员？

- 5.6k [CavsZhouyou/Front-End-Interview-Notebook](https://github.com/CavsZhouyou/Front-End-Interview-Notebook)

介绍 js 的基本数据类型。

JavaScript 有几种类型的值？你能画一下他们的内存图吗？

什么是堆？什么是栈？它们之间有什么区别和联系？

内部属性 [[Class]] 是什么？

介绍 js 有哪些内置对象？

undefined 与 undeclared 的区别？

null 和 undefined 的区别？

如何获取安全的 undefined 值？

说几条写 JavaScript 的基本规范？

JavaScript 原型，原型链？ 有什么特点？

js 获取原型的方法？

在 js 中不同进制数字的表示方式

js 中整数的安全范围是多少？

typeof NaN 的结果是什么？

isNaN 和 Number.isNaN 函数的区别？

Array 构造函数只有一个参数值时的表现？

其他值到字符串的转换规则？

其他值到数字值的转换规则？

其他值到布尔类型的值的转换规则？

{} 和 [] 的 valueOf 和 toString 的结果是什么？

什么是假值对象？

~ 操作符的作用？

解析字符串中的数字和将字符串强制类型转换为数字的返回结果都是数字，它们之间的区别是什么？

操作符什么时候用于字符串的拼接？

什么情况下会发生布尔值的隐式强制类型转换？

|| 和 && 操作符的返回值？

Symbol 值的强制类型转换？

== 操作符的强制类型转换规则？

如何将字符串转化为数字，例如 '12.3b'?

如何将浮点数点左边的数每三位添加一个逗号，如 12000000.11 转化为『12,000,000.11』?

常用正则表达式

生成随机数的各种方法？

如何实现数组的随机排序？

javascript 创建对象的几种方式？

JavaScript 继承的几种实现方式？

寄生式组合继承的实现？

Javascript 的作用域链？

谈谈 This 对象的理解。

eval 是做什么的？

什么是 DOM 和 BOM？

写一个通用的事件侦听器函数。

事件是什么？IE 与火狐的事件机制有什么区别？ 如何阻止冒泡？

三种事件模型是什么？

事件委托是什么？

["1", "2", "3"].map(parseInt) 答案是多少？

什么是闭包，为什么要用它？

javascript 代码中的 "use strict"; 是什么意思 ? 使用它区别是什么？

如何判断一个对象是否属于某个类？

instanceof 的作用？

new 操作符具体干了什么呢？如何实现？

Javascript 中，有一个函数，执行时对象查找时，永远不会去查找原型，这个函数是？

对于 JSON 的了解？

s 延迟加载的方式有哪些？

Ajax 是什么? 如何创建一个 Ajax？

谈一谈浏览器的缓存机制？

Ajax 解决浏览器缓存问题？

同步和异步的区别？

什么是浏览器的同源政策？

如何解决跨域问题？

服务器代理转发时，该如何处理 cookie？

简单谈一下 cookie ？

模块化开发怎么做？

js 的几种模块规范？

AMD 和 CMD 规范的区别？

ES6 模块与 CommonJS 模块、AMD、CMD 的差异。

requireJS 的核心原理是什么？（如何动态加载的？如何避免多次加载的？如何 缓存的？）

JS 模块加载器的轮子怎么造，也就是如何实现一个模块加载器？

ECMAScript6 怎么写 class，为什么会出现 class 这种东西?

documen.write 和 innerHTML 的区别？

DOM 操作——怎样添加、移除、移动、复制、创建和查找节点？

innerHTML 与 outerHTML 的区别？

.call() 和 .apply() 的区别？

JavaScript 类数组对象的定义？

数组和对象有哪些原生方法，列举一下？

数组的 fill 方法？

[,,,] 的长度？

JavaScript 中的作用域与变量声明提升？

如何编写高性能的 Javascript ？

简单介绍一下 V8 引擎的垃圾回收机制

哪些操作会造成内存泄漏？

需求：实现一个页面操作不会整页刷新的网站，并且能在浏览器前进、后退时正确响应。给出你的技术实现方案？

如何判断当前脚本运行在浏览器还是 node 环境中？（阿里）

把 script 标签放在页面的最底部的 body 封闭之前和封闭之后有什么区别？浏览器会如何解析它们？

移动端的点击事件的有延迟，时间是多久，为什么会有？ 怎么解决这个延时？

什么是“前端路由”？什么时候适合使用“前端路由”？“前端路由”有哪些优点和缺点？

如何测试前端代码么？ 知道 BDD, TDD, Unit Test 么？ 知道怎么测试你的前端工程么(mocha, sinon, jasmin, qUnit..)？

检测浏览器版本版本有哪些方式？

什么是 Polyfill ？

使用 JS 实现获取文件扩展名？

介绍一下 js 的节流与防抖？

Object.is() 与原来的比较操作符 “===”、“==” 的区别？

escape,encodeURI,encodeURIComponent 有什么区别？

Unicode 和 UTF-8 之间的关系？

js 的事件循环是什么？

js 中的深浅拷贝实现？

手写 call、apply 及 bind 函数

函数柯里化的实现

为什么 0.1 0.2 != 0.3？如何解决这个问题？

原码、反码和补码的介绍

toPrecision 和 toFixed 和 Math.round 的区别？

什么是 XSS 攻击？如何防范 XSS 攻击？

什么是 CSP？

什么是 CSRF 攻击？如何防范 CSRF 攻击？

什么是 Samesite Cookie 属性？

什么是点击劫持？如何防范点击劫持？

SQL 注入攻击？

什么是 MVVM？比之 MVC 有什么区别？什么又是 MVP ？

vue 双向数据绑定原理？

Object.defineProperty 介绍？

使用 Object.defineProperty() 来进行数据劫持有什么缺点？

什么是 Virtual DOM？为什么 Virtual DOM 比原生 DOM 快？

如何比较两个 DOM 树的差异？

什么是 requestAnimationFrame ？

谈谈你对 webpack 的看法

offsetWidth/offsetHeight,clientWidth/clientHeight 与 scrollWidth/scrollHeight 的区别？

谈一谈你理解的函数式编程？

异步编程的实现方式？

Js 动画与 CSS 动画区别及相应实现

get 请求传参长度的误区

URL 和 URI 的区别？

get 和 post 请求在缓存方面的区别

图片的懒加载和预加载

mouseover 和 mouseenter 的区别？

js 拖拽功能的实现

为什么使用 setTimeout 实现 setInterval？怎么模拟？

let 和 const 的注意点？

什么是 rest 参数？

什么是尾调用，使用尾调用有什么好处？

Symbol 类型的注意点？

Set 和 WeakSet 结构？

Map 和 WeakMap 结构？

什么是 Proxy ？

Reflect 对象创建目的？

require 模块引入的查找方式？

什么是 Promise 对象，什么是 Promises/A 规范？

手写一个 Promise

如何检测浏览器所支持的最小字体大小？

怎么做 JS 代码 Error 统计？

单例模式模式是什么？

策略模式是什么？

代理模式是什么？

中介者模式是什么？

适配器模式是什么？

观察者模式和发布订阅模式有什么不同？

Vue 的生命周期是什么？

Vue 的各个生命阶段是什么？

Vue 组件间的参数传递方式？

computed 和 watch 的差异？

vue-router 中的导航钩子函数

$route 和 $router 的区别？

vue 常用的修饰符？

vue 中 key 值的作用？

computed 和 watch 区别？

keep-alive 组件有什么作用？

vue 中 mixin 和 mixins 区别？

开发中常用的几种 Content-Type ？

如何封装一个 javascript 的类型判断函数？

如何判断一个对象是否为空对象？

使用闭包实现每隔一秒打印 1,2,3,4

手写一个 jsonp

手写一个观察者模式？

EventEmitter 实现

一道常被人轻视的前端 JS 面试题

如何确定页面的可用性时间，什么是 Performance API？

js 中的命名规则

js 语句末尾分号是否可以省略？

Object.assign()

Math.ceil 和 Math.floor

js for 循环注意点

一个列表，假设有 100000 个数据，这个该怎么办？

js 中倒计时的纠偏实现？

进程间通信的方式？

如何查找一篇英文文章中出现频率最高的单词？

ele.getElementsByClassName 和 ele.querySelectorAll 的区别？

- 4.6k [febobo/web-interview](https://github.com/febobo/web-interview)

说说 Javascript 中的数据类型？区别？

Javscript 数组的常用方法有哪些？

Javascript 字符串的常用方法有哪些？

谈谈 Javascript 中的类型转换机制

== 和 ===区别，分别在什么情况使用

深拷贝浅拷贝的区别？如何实现一个深拷贝？

说说你对闭包的理解

说说你对作用域链的理解

JavaScript 原型，原型链 ? 有什么特点？

Javascript 如何实现继承？

谈谈 this 对象的理解

JavaScript 中执行上下文和执行栈是什么？

说说 JavaScript 中的事件模型

typeof 与 instanceof 区别

解释下什么是事件代理？应用场景？

说说 new 操作符具体干了什么？

ajax 原理是什么？如何实现？

bind、call、apply 区别？如何实现一个 bind?

说说你对正则表达式的理解？应用场景？

说说你对事件循环的理解

DOM 常见的操作有哪些？

说说你对 BOM 的理解，常见的 BOM 对象你了解哪些？

举例说明你对尾递归的理解，有哪些应用场景

说说 JavaScript 中内存泄漏的几种情况？

Javascript 本地存储的方式有哪些？区别及应用场景？

说说你对函数式编程的理解？优缺点？

Javascript 中如何实现函数缓存？函数缓存有哪些应用场景？

说说 Javascript 数字精度丢失的问题，如何解决？

什么是防抖和节流？有什么区别？如何实现？

如何判断一个元素是否在可视区域中？

大文件上传如何做断点续传？

如何实现上拉加载，下拉刷新？

什么是单点登录？如何实现？

web 常见的攻击方式有哪些？如何防御？

- 2.1k [yisainan/web-interview](https://github.com/yisainan/web-interview)
