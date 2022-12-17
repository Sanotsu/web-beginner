# ES6 以来的新特性关键字

内容都应该属于基本知识了，但有些人就直接来问一句“你知道 ES6 有哪些新特性吗？”就很烦人。少量可能有补充说明。

如果 ECMAScript® 2015 称为 ES6 的话，到现在(2022-12-15)正式版本已经到 ECMAScript 2023(December 15, 2022)

## ES6

- **声明命令**: let、块级作用域、const、globalThis 顶层对象。ES6 声明变量的六种方法: var、function、let、const、import、class
- **变量的解构赋值**: 数组、对象、字符串、数值和布尔值、函数参数
  - 应用场景: 交换变量值，从函数返回多个值，定义函数参数，提取 JSON 数据，函数参数的默认值，遍历 Map 结构，输入模块的指定方法
- **字符串的扩展**: 大括号包含表示 Unicode 字符(`\u{0xXX}`或`\u{0XXX}`)；字符串遍历`for of`；模板字符串；标签模板
  - 标签模板:“标签”指的就是函数，紧跟在后面的模板字符串就是它的参数，模板字符里面有变量，则先先处理成多个参数，再调用函数。
    ```js
    console.log`hello`  等价于  console.log(['hello']) // 都输出 [ 'hello' ]
    let a = 5; let b = 10;
    tag`Hello ${ a + b } world ${ a * b }`; // 等同于
    tag(['Hello ', ' world ', ''], 15, 50); // 注意参数的位置和数量
    ```
- **字符串的新增方法**:
  - 静态方法: `String.fromCodePoint()`从 Unicode 码点返回对应字符；`String.raw()`返回一个斜杠都被转义的字符串。
  - 实例方法: codePointAt()、normalize()、repeat()、matchAll()、 includes()、startsWith()、endsWith()
- **正则的扩展**:
  - 变更 RegExp 构造函数入参：允许首参数为正则对象，尾参数为正则修饰符(返回的正则表达式会忽略原正则表达式的修饰符)
  - 字符串的实例方法 match()、replace()、search()和 split()在语言内部全部调用 RegExp 的实例方法
  - 正则表达式添加了 `u` 修饰符，含义为“Unicode 模式”，用来正确处理大于`\uFFFF` 的 Unicode 字符
  - [`y`修饰符](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#advanced_searching_with_flags): 与 g 修饰符类似也是全局匹配，执行“粘性 (sticky)”搜索，匹配从目标字符串的当前位置开始。
- **数值的扩展**: 二进制和八进制表示法(前缀`0b`和`0o`)
  - Number 对象新增方法: isFinite()、isNaN()、parseInt()、parseFloat()、isInteger()、isSafeInteger()
    - 一个极小的常量`Number.EPSILON`，**js 能够表示的最小精度**。误差如果小于这个值，可以认为已经没有意义，即不存在误差。
    - `Number.MAX_SAFE_INTEGER === Math.pow(2, 53)-1` 和 `Number.MIN_SAFE_INTEGER === -(2^53-1)`
  - Math 对象新增方法: ES6 在 Math 对象上新增了 17 个与数学相关的方法，trunc()、sign()、cbrt()等
- **函数的扩展**: 参数默认值(指定了默认值后，函数的 length 属性将失真)；rest 参数`...`；函数的 name 属性；箭头函数；尾调用尾递归。
  - 只要函数参数使用了默认值、解构赋值、或者扩展运算符，那么函数内部就不能显式设定为严格模式，否则会报错。
- **数组的扩展**: 扩展运算符`...`，应用于复制数组、合并数组、与解构赋值结合、字符串转字符数组、实现了 Iterator 接口的对象。
  - 静态方法: `Array.from()`类数组和可迭代对象转数组；`Array.of()`将一组值转数组。
  - 实例方法: copyWithin()、find()，findIndex()，findLast() 和 findLastIndex()、fill()、entries()，keys() 和 values()、flat() 和 flatMap()。ES5 对空位的处理很不一致，大多数情况下会忽略空位。ES6 则是明确将数组空位转为 undefined。别有空位。
- **对象的扩展**: 对象属性、方法可简写；用表达式作为对象的属性名；方法的 name 属性；属性的可枚举性和遍历；super 关键字。
  - 静态方法:is()、assign()、setPrototypeOf()、getPrototypeOf()、Object.keys()、fromEntries()
- **新的原始数据类型 Symbol**: 表示独一无二的值，通过 Symbol()函数生成。不支持语法`new Symbol()`。
- **新的数据结构 Set、WeakSet、Map、WeakMap**；
- **新的对象 Proxy、Reflect、Promise**
- **迭代器 Iterator 和 for...of 循环**: 迭代器为各种不同的数据结构提供统一的访问机制。
- **Generator 对象**: 生成器函数，用`function*`声明，返回一个 Generator 对象。是一种异步编程解决方案。

  - 形式上，Generator 函数是一个普通函数，但是有两个特征。
    - 一是，function 关键字与函数名之间有一个星号；二是，函数体内部使用 yield 表达式，定义不同的内部状态。

- **Class 类**: 定义、原理、方法和关键字、属性、静态属性和方法、继承、super、实例、表达式、this 指向、`new.target`
- **Module**: export、import 命令；ES6 的模块自动采用严格模式。
  - ES6 模块与 CommonJS 模块三个重大差异:
    - CommonJS 模块输出的是一个**值的拷贝**，ES6 模块输出的是**值的引用**。
    - CommonJS 模块是**运行时加载**，ES6 模块是**编译时输出接口**。
    - CommonJS 模块的 require()是**同步加载**模块，ES6 模块的 import 命令是**异步加载**，有一个独立的模块依赖的解析阶段。
      - 语法上: CommonJS 模块使用 `require()`和 `module.exports`，ES6 模块使用 `import` 和 `export`。
      - node13.2 版本开始默认打开 ES6 模块支持(模块采用`.mjs`后缀文件名或项目 package.json 指定`"type":"module"`)

## ES2016

- **数组扩展**: 实例方法 `includes()`；**指数运算符** `**`(可与其他某些运算符一起用)

## ES2017

- **字符串扩展**: padStart()、padEnd()；**对象扩展**: Object.getOwnPropertyDescriptors()、Object.values()、Object.entries()
- **函数扩展**: 允许函数最后一个参数有尾逗号；**引入 SharedArrayBuffer**，允许 Worker 线程与主线程共享同一块内存。
- **引入了 `async` 函数**，使得异步操作变得更加方便。是 Generator 函数的语法糖，返回一个 Promise 对象。
  - 正常情况下，`await` 命令后面是一个 Promise 对象，返回该对象的结果。如果不是 Promise 对象，就直接返回对应的值。

## ES2018

- **字符串扩展**: 放松对标签模板里字符串转义的限制：遇到不合法的字符串转义返回 undefined，并且从 raw 上可获取原字符串。
- **对象扩展**: 扩展运算符`...`：转换对象为用逗号分隔的参数序列`{ ...obj }`。
- **正则扩展**: s 修饰符、dotAll、后行断言、后行否定断言、Unicode 属性转义、具名组匹配(为每组匹配指定名字)。
- **Promise 扩展**: 实例方法`finally()`：指定不管最后状态如何都会执行的回调函数。
- **async 扩展**: 异步迭代器`for-await-of`：循环等待每个 Promise 对象变为 resolved 状态才进入下一步。

## ES2019

- **字符串扩展**: 直接输入`U+2028`和`U+2029`；`JSON.stringify()`改造；实例方法`trimStart()`、`trimEnd()`。
- **对象扩展**: `Object.fromEntries()`：返回以键和值组成的对象(`Object.entries()`的逆操作)。
- **数组扩展**: `sort()`排序默认要稳定实现。实例方法`flat()`、`flatMap()`。
- **函数扩展**: `toString()`改造，返回函数原始代码；`catch()`中的参数可省略。
- **Symbol 扩展**: 实例属性`description`，返回 Symbol 值的描述。

## ES2020

- **声明**: `globalThis`，作为顶层对象，指向全局环境下的 this。浏览器是`window`，nodejs 是`global`，webworker 是`self`。
- **数值扩展**: `BigInt` 是一种内置对象(数据类型)，表示大于`2^53-1`的整数，表示任意大的整数。定义方式: 整数字面量后面加 `n`。
  - 该对象有静态方法`asIntN()`、`asUintN()`，实例方法`toLocaleString()`、`toString()`、`valueOf()`。
  - 全局方法`parseInt()` 会将 BigInt 转换为 Number，并在这个过程中失去了精度(因为拖尾的非数字值，包括 "n"，会被丢弃)。
- **对象扩展**: 链判断操作符`?.`是否存在对象属性，不存在返回 undefined；空判断操作符`??`是否值为 undefined 或 null，是则使用默认值。
- **正则扩展**: `matchAll()`：返回所有匹配的遍历器。
- **Module**: `import()`函数，动态加载模块(返回 Promise)。
- **Iterator**: `for-in`遍历顺序，不同的引擎已就如何迭代属性达成一致，从而使行为标准化。
  **Promise 扩展**: `Promise.allSettled()`参数数组的*所有 Promise 对象都发生状态变更*，返回的 Promise 对象才会发生状态变更。

## ES2021

- **字符串扩展**: `String.prototype.replaceAll()`；
- **逻辑赋值运算符** `||=`、`&&=`、`??=`。例如`opts.baz ?? (opts.baz = 'qux');  简写->  opts.baz ??= 'qux';`
- **数字分隔符** 是一个有用的工具，它在数字中用下划线 (`_`)分隔数字，从而使长数字文字更具可读性。
- **Promise 扩展**: `Promise.any()`接受一个可迭代的 Promise 对象数组，在数组中任意一个 Promise resolve 时，即 resolve。
  - 如果所有 Promise 都没有 resolve，则会抛出一种新类型的异常 `AggregateError`，将错误以对象数组的形式组合为一个错误数组。
- **弱引用 WeakRef**: `WeakRef`直接创建对象的弱引用；
- **FinalizationRegistry** 对象可以让你在对象被垃圾回收时请求一个回调。

## ES2022

- **Class 类**: 类字段只能在构造函数之外声明；使用`#`声明私有字段和成员；为类声明静态字段和静态私有方法；允许在创建类时定义只执行一次的静态块；支持使用 in 运算符检查一个对象中是否有一个特定的私有字段；
- **Top-level `await`**(不限定只在 async 中使用)；
- 数组，字符串和 TypedArray 对象现在也有 **`at()`** 方法，访问末尾的第 N 个元素。
- **RegExp 匹配索引**: 指定一个 `d`修饰符标志，来获取匹配开始和结束的两个索引。
- **Object.hasOwn()** 方法，如果指定的属性是对象的直接属性，则返回 true。否则返回 false。
- **错误原因**: Error 对象新增了 `cause` 属性表示错误原因

## ES2023

- **数组扩展**: `findLast()` 和 `findLastIndex()` 方法； **Hashbang Grammar**

---

ref：

- 阮一峰 [ECMAScript 6 入门教程](https://es6.ruanyifeng.com/)
- [T39 Finished Proposals](https://github.com/tc39/proposals/blob/HEAD/finished-proposals.md) - 已完成的提案就是新特性了
- 掘金 [1.5 万字概括 ES6 全部特性(已更新 ES2020)](https://juejin.cn/post/6844903959283367950)
- 掘金 [ES6、ES7、ES8 特性一锅炖(ES6、ES7、ES8 学习指南)](https://juejin.cn/post/6844903679976275976)
- 掘金 [从 ES6 到 ES10 的新特性万字大总结（不得不收藏）](https://juejin.cn/post/6844904023787569159)
- 掘金 [ES2021 激动人心的新特性](https://juejin.cn/post/6969016993215152136)
- 掘金 [ES2022 新特性必知必会](https://juejin.cn/post/7074469494063628301)
- 掘金 [ECMAScript 2023 将新增这 9 个数组方法](https://juejin.cn/post/7143445585784209445)
- [ECMAScript® 2015 Language Specification](https://262.ecma-international.org/6.0/)
- [ECMAScript® 2023 Language Specification](https://tc39.es/ecma262/multipage/)
