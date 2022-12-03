<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [Promise 与异步函数](#promise-%E4%B8%8E%E5%BC%82%E6%AD%A5%E5%87%BD%E6%95%B0)
  - [异步编程](#%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B)
    - [同步与异步](#%E5%90%8C%E6%AD%A5%E4%B8%8E%E5%BC%82%E6%AD%A5)
  - [Promise](#promise)
    - [Promise 基础](#promise-%E5%9F%BA%E7%A1%80)
      - [Promise 状态机 (The Promise State Machine)](#promise-%E7%8A%B6%E6%80%81%E6%9C%BA-the-promise-state-machine)
      - [解决值、拒绝理由及 Promise 用例 (Resolved Values, Rejection Reasons, and Utility of Promises)](#%E8%A7%A3%E5%86%B3%E5%80%BC%E6%8B%92%E7%BB%9D%E7%90%86%E7%94%B1%E5%8F%8A-promise-%E7%94%A8%E4%BE%8B-resolved-values-rejection-reasons-and-utility-of-promises)
      - [通过执行函数控制 Promise 状态 (Controlling Promise State with the Executor)](#%E9%80%9A%E8%BF%87%E6%89%A7%E8%A1%8C%E5%87%BD%E6%95%B0%E6%8E%A7%E5%88%B6-promise-%E7%8A%B6%E6%80%81-controlling-promise-state-with-the-executor)
      - [Promise.resolve()](#promiseresolve)
      - [Promise.reject()](#promisereject)
      - [同步/异步执行的二元性](#%E5%90%8C%E6%AD%A5%E5%BC%82%E6%AD%A5%E6%89%A7%E8%A1%8C%E7%9A%84%E4%BA%8C%E5%85%83%E6%80%A7)
    - [Promise 的实例方法](#promise-%E7%9A%84%E5%AE%9E%E4%BE%8B%E6%96%B9%E6%B3%95)
      - [非重入 Promise 方法(Non-Reentrant Promise Methods)](#%E9%9D%9E%E9%87%8D%E5%85%A5-promise-%E6%96%B9%E6%B3%95non-reentrant-promise-methods)
      - [邻近处理程序的执行顺序](#%E9%82%BB%E8%BF%91%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F%E7%9A%84%E6%89%A7%E8%A1%8C%E9%A1%BA%E5%BA%8F)
      - [传递解决值和拒绝理由](#%E4%BC%A0%E9%80%92%E8%A7%A3%E5%86%B3%E5%80%BC%E5%92%8C%E6%8B%92%E7%BB%9D%E7%90%86%E7%94%B1)
      - [拒绝 Promise 与拒绝错误处理](#%E6%8B%92%E7%BB%9D-promise-%E4%B8%8E%E6%8B%92%E7%BB%9D%E9%94%99%E8%AF%AF%E5%A4%84%E7%90%86)
    - [Promise 连锁与 Promise 合成 (Promise Chaining and Composition)](#promise-%E8%BF%9E%E9%94%81%E4%B8%8E-promise-%E5%90%88%E6%88%90-promise-chaining-and-composition)
      - [Promise 连锁](#promise-%E8%BF%9E%E9%94%81)
      - [Promise 图(Promise Graphs)](#promise-%E5%9B%BEpromise-graphs)
      - [Promise.all()和 Promise.race()](#promiseall%E5%92%8C-promiserace)
      - [串行 Promise 合成 (Serial Promise Composition)](#%E4%B8%B2%E8%A1%8C-promise-%E5%90%88%E6%88%90-serial-promise-composition)
    - [Promise 扩展 (Promise Extensions)](#promise-%E6%89%A9%E5%B1%95-promise-extensions)
    - [补充：Promise 的静态方法和实例方法概述](#%E8%A1%A5%E5%85%85promise-%E7%9A%84%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95%E5%92%8C%E5%AE%9E%E4%BE%8B%E6%96%B9%E6%B3%95%E6%A6%82%E8%BF%B0)
      - [Promise 取消 (Promise Canceling)](#promise-%E5%8F%96%E6%B6%88-promise-canceling)
      - [Promise 进度通知 (Promise Progress Notifications)](#promise-%E8%BF%9B%E5%BA%A6%E9%80%9A%E7%9F%A5-promise-progress-notifications)
  - [异步函数 (ASYNC FUNCTIONS)](#%E5%BC%82%E6%AD%A5%E5%87%BD%E6%95%B0-async-functions)
    - [异步函数基础 (Async Function Basics)](#%E5%BC%82%E6%AD%A5%E5%87%BD%E6%95%B0%E5%9F%BA%E7%A1%80-async-function-basics)
      - [async](#async)
      - [await](#await)
    - [停止和恢复执行 (Halting and Resuming Execution)](#%E5%81%9C%E6%AD%A2%E5%92%8C%E6%81%A2%E5%A4%8D%E6%89%A7%E8%A1%8C-halting-and-resuming-execution)
    - [异步函数策略 (Strategies for Async Functions)](#%E5%BC%82%E6%AD%A5%E5%87%BD%E6%95%B0%E7%AD%96%E7%95%A5-strategies-for-async-functions)
      - [实现 sleep()](#%E5%AE%9E%E7%8E%B0-sleep)
      - [利用平行执行 (Maximizing Parallelization)](#%E5%88%A9%E7%94%A8%E5%B9%B3%E8%A1%8C%E6%89%A7%E8%A1%8C-maximizing-parallelization)
      - [串行执行 Promise (Serial Promise Execution)](#%E4%B8%B2%E8%A1%8C%E6%89%A7%E8%A1%8C-promise-serial-promise-execution)
      - [栈追踪与内存管理 (Stack Traces and Memory Management)](#%E6%A0%88%E8%BF%BD%E8%B8%AA%E4%B8%8E%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86-stack-traces-and-memory-management)
  - [小结](#%E5%B0%8F%E7%BB%93)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

# Promise 与异步函数

本章内容

- 异步编程
- Promise
- 异步函数

感觉 MDN 的[Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)讲解更易懂。

同时参看[async 函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function) 和 [await](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/await)。

## 异步编程

- 同步行为和异步行为的对立统一是计算机科学的一个基本概念。
- 特别是在 JavaScript 这种单线程事件循环模型中，同步操作与异步操作更是代码所要依赖的核心机制。
- 异步行为是为了优化因计算量大而时间长的操作。如果在等待其他操作完成的同时，即使运行其他指令，系统也能保持稳定，那么这样做就是务实的。
- 重要的是，异步操作并不一定计算量大或要等很长时间。只要你不想为等待某个异步操作而阻塞线程执行，那么任何时候都可以使用。

### 同步与异步

**同步行为**对应内存中顺序执行的处理器指令。

- _每条指令都会严格按照它们出现的顺序来执行_，而每条指令执行后也能立即获得存储在系统本地（如寄存器或系统内存）的信息。
- 这样的执行流程容易分析程序在执行到代码任意位置时的状态（比如变量的值）。
  - 首先，操作系统会在栈内存上分配一个存储浮点数值的空间，然后针对这个值做一次数学计算，再把计算结果写回之前分配的内存中。
  - 所有这些指令都是在单个线程中按顺序执行的。在低级指令的层面，有充足的工具可以确定系统状态。

**异步行为**类似于系统中断，即当前进程外部的实体可以触发代码执行。

- 异步操作经常是必要的，因为强制进程等待一个长时间的操作通常是不可行的（同步操作则必须要等）。
- 如果代码要访问一些高延迟的资源，比如向远程服务器发送请求并等待响应，那么就会出现长时间的等待。

## Promise

Promise 是对尚不存在结果的一个替身。

书中翻译为期约，不太习惯，保留 promise 的说法。

### Promise 基础

- ECMAScript 6 新增的引用类型 `Promise` ，可以通过 `new` 操作符来实例化。创建新 Promise 时需要传入执行器（executor）函数作为参数。

#### Promise 状态机 (The Promise State Machine)

- Promise 是一个有状态的对象，可能处于如下 3 种状态之一：
  - 待定（pending）
  - 兑现（fulfilled，有时候也称为“解决”，resolved）
  - 拒绝（rejected）
- 说明
  - 待定（pending）是 Promise 的最初始状态。
  - 在待定状态下，Promise 可以落定（settled）为代表成功的兑现（fulfilled）状态，或者代表失败的拒绝（rejected）状态。
  - 无论落定为哪种状态都是不可逆的。只要从待定转换为兑现或拒绝，Promise 的状态就不再改变。
  - 而且，也不能保证 Promise 必然会脱离待定状态。
- Promise 的状态是私有的，不能直接通过 JavaScript 检测到。
- Promise 的状态也不能被外部 JavaScript 代码修改。
  - 这与不能读取该状态的原因是一样的：Promise 故意将异步行为封装起来，从而隔离外部的同步代码。

```js
// 开发中的实际例子：
let genCanvasBgSync = async () => {
  return new Promise((resolve, reject) => {
    fabric.Image.fromURL(this.imageData, (img, loadErrFlag) => {
      // 如果加载图片出错
      if (loadErrFlag) {
        reject(false);
      }
      // 没报错进行的业务处理
      this.canvas.setBackgroundImage(
        img,
        this.canvas.renderAll.bind(this.canvas),
        {
          opaity: 1,
          angle: 0,
        }
      );
      // 成功执行后返回
      resolve(true);
    });
  });
};

await genCanvasBgSync();
```

#### 解决值、拒绝理由及 Promise 用例 (Resolved Values, Rejection Reasons, and Utility of Promises)

- Promise 主要有两大用途:
  - 首先是抽象地表示一个异步操作。
    - Promise 的状态代表 Promise 是否完成。“待定”表示尚未开始或者正在执行中。“兑现”表示已经成功完成，而“拒绝”则表示没有成功完成。
  - 在另外一些情况下，Promise 封装的异步操作会实际生成某个值，而程序期待 Promise 状态改变时可以访问这个值。
    - ，如果 Promise 被拒绝，程序就会期待 Promise 状态改变时可以拿到拒绝的理由。(resolve() 和 reject() 的返回值)
- 因此，每个 Promise 只要状态切换为兑现，就会有一个私有的内部值（value）。类似地， 每个 Promise 只要状态切换为拒绝，就会有一个私有的内部理由（reason）。
- 无论是值还是理由，都是包含原 始值或对象的不可修改的引用。二者都是可选的，而且默认值为 `undefined` 。
- 在 Promise 到达某个落定状态时执行的异步代码始终会收到这个值或理由。

#### 通过执行函数控制 Promise 状态 (Controlling Promise State with the Executor)

- 由于 Promise 的状态是私有的，所以只能在内部进行操作。内部操作在 Promise 的执行器函数中完成。
- **执行器函数主要有两项职责：初始化 Promise 的异步行为和控制状态的最终转换。**
  - 其中，控制 Promise 状态的转换是通过调用它的两个函数参数实现的。这两个函数参数通常都命名为 resolve() 和 reject() 。
    - 调用 resolve() 会把状态切换为兑现，调用 reject() 会把状态切换为拒绝。另外，调用 reject() 也会抛出错误。
- 在初始化 Promise 时，执行器函数已经改变了每个 Promise 的状态。
  - 这里的关键在于，**执行器函数是同步执行的。**这是因为执行器函数是 Promise 的初始化程序。
- 无论 resolve() 和 reject() 中的哪个被调用，状态转换都不可撤销了。

```js
new Promise(() => setTimeout(console.log, 0, "executor")); // executor
setTimeout(console.log, 0, "promise initialized"); // promise initialized

// 添加 setTimeout 可以推迟切换状态：
let p = new Promise((resolve, reject) => setTimeout(resolve, 1000));
// 在 console.log 打印Promise实例的时候，还不会执行超时回调（即 resolve()）
setTimeout(console.log, 0, p); // Promise <pending>

// 无论 resolve() 和 reject() 中的哪个被调用，状态转换都不可撤销了。于是继续修改状态会静默失败。
let p2 = new Promise((resolve, reject) => {
  resolve(true);
  reject(false); // 没有效果
});

setTimeout(console.log, 0, p2); // Promise { true }

// 为避免Promise卡在待定状态，可以添加一个定时退出功能。
let p3 = new Promise((resolve, reject) => {
  // 通过 setTimeout 设置一个10 秒钟后无论如何都会拒绝Promise的回调：
  setTimeout(reject, 10000); // 10 秒后调用 reject()
  // 执行函数的逻辑
});

setTimeout(console.log, 0, p3); // Promise <pending>
setTimeout(console.log, 11000, p3); // 11 秒后再检查状态
// (After 10 seconds) Uncaught error
// (After 11 seconds) Promise { <rejected> undefined }
```

#### Promise.resolve()

- Promise 并非一开始就必须处于待定状态，然后通过执行器函数才能转换为落定状态。通过调用 `Promise.resolve()` 静态方法，可以实例化一个解决的 Promise。
- 对这个静态方法而言，如果传入的参数本身是一个 Promise，那它的行为就类似于一个空包装。因此，`Promise.resolve()` 可以说是一个幂等方法.

  ```js
  let p4 = Promise.resolve(7);

  setTimeout(console.log, 0, p4 === Promise.resolve(p4)); // true
  setTimeout(console.log, 0, p4 === Promise.resolve(Promise.resolve(p4))); // true
  ```

  - 这个幂等性会保留传入 Promise 的状态。

    ```js
    let p5 = new Promise(() => {});

    setTimeout(console.log, 0, p5); // Promise <pending>
    setTimeout(console.log, 0, Promise.resolve(p5)); // Promise <pending>
    setTimeout(console.log, 0, p5 === Promise.resolve(p5)); // true
    ```

#### Promise.reject()

- Promise.reject() 会实例化一个拒绝的 Promise 并抛出一个异步错误
  - （这个错误不能通过 try / catch 捕获，而只能通过拒绝处理程序捕获）。
- Promise.reject() 并没有照搬 Promise.resolve() 的幂等逻辑。如果给它传一个 Promise 对象，则这个 Promise 会成为它返回的拒绝 Promise 的理由。

```js
setTimeout(console.log, 0, Promise.reject(Promise.resolve()));
// Promise { <rejected> Promise { undefined } }
```

#### 同步/异步执行的二元性

- Promise 真正的异步特性：它们是同步对象（在同步执行模式中使用），但也是异步执行模式的媒介。

```js
// 以下同步代码里没有在try catch中捕获到promise的异常
try {
  Promise.reject(new Error("bar"));
} catch (e) {
  console.log(e);
}
// Uncaught (in promise) Error: bar
```

- 拒绝 Promise 的错误并没有抛到执行同步代码的线程里，而是通过浏览器异步消息队列来处理的。因此， try / catch 块并不能捕获该错误。
  - 代码一旦开始以异步模式执行，则唯一与之交互的方式就是使用异步结构——更具体地说，就是 Promise 的方法。

### Promise 的实例方法

- **Promise.prototype.catch()**
  - 为 promise 添加一个被拒绝状态的回调函数，并返回一个新的 promise，
  - 若回调函数被调用，则兑现其返回值，否则兑现原来的 promise 兑现的值。
- **Promise.prototype.then()**
  - 为 promise 添加被兑现和被拒绝状态的回调函数，其以回调函数的返回值兑现 promise。
  - 若不处理已兑现或者已拒绝状态（例如，onFulfilled 或 onRejected 不是一个函数），则返回 promise 被敲定时的值。
- **Promise.prototype.finally()**
  - 为 promise 添加一个回调函数，并返回一个新的 promise。
  - 这个新的 promise 将在原 promise 被兑现时兑现。而传入的回调函数将在原 promise 被敲定（无论被兑现还是被拒绝）时被调用。

补充说明:

- 在 ECMAScript 暴露的异步结构中，任何对象都有一个 then() 方法。这个方法被认为实现了 `Thenable` 接口。
  - ECMAScript 的 Promise 类型实现了 Thenable 接口。这个简化的接口跟 TypeScript 或其他包中的接口或类型定义不同，它们都设定了 Thenable 接口更具体的形式。

#### 非重入 Promise 方法(Non-Reentrant Promise Methods)

- **当 Promise 进入落定状态时，与该状态相关的处理程序仅仅会被排期，而非立即执行。跟在添加这个处理程序的代码之后的同步代码一定会在处理程序之前先执行。**
  - 这个特性由 JavaScript 运行时保证，被称为“非重入”（non-reentrancy）特性。

```js
// 在这个例子中，即使Promise状态变化发生在添加处理程序之后，处理程序也会等到运行的消息队列让它出列时才会执行。
let synchronousResolve;

// 创建一个Promise并将解决函数保存在一个局部变量中
let p8 = new Promise((resolve) => {
  synchronousResolve = function () {
    console.log("1: invoking resolve()");
    resolve();
    console.log("2: resolve() returns");
  };
});

p8.then(() => console.log("4: then() handler executes"));

synchronousResolve();
console.log("3: synchronousResolve() returns");

// 实际的输出：
// 1: invoking resolve()
// 2: resolve() returns
// 3: synchronousResolve() returns
// 4: then() handler executes
```

- 非重入适用于 onResolved / onRejected 处理程序、 catch() 处理程序和 finally() 处理程序。

```js
let p1 = Promise.resolve();
p1.then(() => console.log("p1.then() onResolved"));
console.log("p1.then() returns");

let p2 = Promise.reject();
p2.then(null, () => console.log("p2.then() onRejected"));
console.log("p2.then() returns");

let p3 = Promise.reject();
p3.catch(() => console.log("p3.catch() onRejected"));
console.log("p3.catch() returns");

let p4 = Promise.resolve();
p4.finally(() => console.log("p4.finally() onFinally"));

console.log("p4.finally() returns");

// 实际输出顺序：
// p1.then() returns
// p2.then() returns
// p3.catch() returns
// p4.finally() returns
// p1.then() onResolved
// p2.then() onRejected
// p3.catch() onRejected
// p4.finally() onFinally
```

#### 邻近处理程序的执行顺序

- 如果给 Promise 添加了多个处理程序，当 Promise 状态变化时，相关处理程序会按照添加它们的顺序依次执行。
  - 无论是 then() 、 catch() 还是 finally() 添加的处理程序都是如此。

```js
let p1 = Promise.resolve();
let p2 = Promise.reject();

p1.then(() => setTimeout(console.log, 0, 1));
p1.then(() => setTimeout(console.log, 0, 2));
// 1
// 2

p2.then(null, () => setTimeout(console.log, 0, 3));
p2.then(null, () => setTimeout(console.log, 0, 4));
// 3
// 4

p2.catch(() => setTimeout(console.log, 0, 5));
p2.catch(() => setTimeout(console.log, 0, 6));
// 5
// 6

p1.finally(() => setTimeout(console.log, 0, 7));
p1.finally(() => setTimeout(console.log, 0, 8));
// 7
// 8 let p1 = Promise.resolve();
let p2 = Promise.reject();

p1.then(() => setTimeout(console.log, 0, 1));
p1.then(() => setTimeout(console.log, 0, 2));
// 1
// 2

p2.then(null, () => setTimeout(console.log, 0, 3));
p2.then(null, () => setTimeout(console.log, 0, 4));
// 3
// 4

p2.catch(() => setTimeout(console.log, 0, 5));
p2.catch(() => setTimeout(console.log, 0, 6));
// 5
// 6

p1.finally(() => setTimeout(console.log, 0, 7));
p1.finally(() => setTimeout(console.log, 0, 8));
// 7
// 8
```

#### 传递解决值和拒绝理由

- 到了落定状态后，Promise 会提供其解决值（如果兑现）或其拒绝理由（如果拒绝）给相关状态的处理程序。拿到返回值后，就可以进一步对这个值进行操作。
- 在执行函数中，解决的值和拒绝的理由是分别作为 resolve() 和 reject() 的第一个参数往后传的。
  - 然后，这些值又会传给它们各自的处理程序，作为 onResolved 或 onRejected 处理程序的唯一参数。

```js
let p1 = new Promise((resolve, reject) => resolve("foo"));
p1.then((value) => console.log(value)); // foo

let p2 = new Promise((resolve, reject) => reject("bar"));
p2.catch((reason) => console.log(reason)); // bar
```

- Promise.resolve() 和 Promise.reject() 在被调用时就会接收解决值和拒绝理由。
  - 同样地，它们返回的 Promise 也会像执行器一样把这些值传给 onResolved 或 onRejected 处理程序。

```js
let p1 = Promise.resolve("foo");
p1.then((value) => console.log(value)); // foo

let p2 = Promise.reject("bar");
p2.catch((reason) => console.log(reason)); // bar
```

#### 拒绝 Promise 与拒绝错误处理

- 拒绝 Promise 类似于 throw() 表达式，因为它们都代表一种程序状态，即需要中断或者特殊处理。
  - 在 Promise 的执行函数或处理程序中抛出错误会导致拒绝，对应的错误对象会成为拒绝的理由。
- then() 和 catch() 的 onRejected 处理程序在语义上相当于 try / catch 。出发点都是捕获错误之后将其隔离，同时不影响正常逻辑执行。
  - 为此， onRejected 处理程序的任务应该是在捕获异步错误之后返回一个解决的 Promise。

```js
// 对比了同步错误处理与异步错误处理
console.log("begin synchronous execution");
try {
  throw Error("foo");
} catch (e) {
  console.log("caught error", e);
}
console.log("continue synchronous execution");

// begin synchronous execution
// caught error Error: foo
// continue synchronous execution

new Promise((resolve, reject) => {
  console.log("begin asynchronous execution");
  reject(Error("bar"));
})
  .catch((e) => {
    console.log("caught error", e);
  })
  .then(() => {
    console.log("continue asynchronous execution");
  });

// begin asynchronous execution
// caught error Error: bar
// continue asynchronous execution
```

### Promise 连锁与 Promise 合成 (Promise Chaining and Composition)

- 多个 Promise 组合在一起可以构成强大的代码逻辑。这种组合可以通过两种方式实现：Promise 连锁与 Promise 合成。
  - **前者就是一个 Promise 接一个 Promise 地拼接，后者则是将多个 Promise 组合为一个 Promise**。

#### Promise 连锁

- 之所以可以把 Promise 逐个串联起来，是因为每个 Promise 实例的方法（ then() 、 catch() 和 finally() ）都会返回一个新的 Promise 对象，而这个新 Promise 又有自己的实例方法。这样连缀方法调用就可以构成所谓的“Promise 连锁”
- 要真正执行异步任务，让每个执行器都返回一个 Promise 实例。这样就可以让每个后续 Promise 都等待之前的 Promise，也就是串行化异步任务。
- 每个后续的处理程序都会等待前一个 Promise 解决，然后实例化一个新 Promise 并返回它。
  - 这种结构可以简洁地将异步任务串行化，解决之前依赖回调的难题。

```js
// 把生成Promise的代码提取到一个工厂函数中
function delayedResolve(str) {
  return new Promise((resolve, reject) => {
    console.log(str);
    setTimeout(resolve, 1000);
  });
}

// 让每个Promise在一定时间后解决(resolve)：
delayedResolve("p1 executor")
  .then(() => delayedResolve("p2 executor"))
  .then(() => delayedResolve("p3 executor"))
  .then(() => delayedResolve("p4 executor"));

// p1 executor（1 秒后）
// p2 executor（2 秒后）
// p3 executor（3 秒后）
// p4 executor（4 秒后）
```

- 因为 then() 、 catch() 和 finally() 都返回 Promise，所以串联这些方法也很直观。

```js
let p = new Promise((resolve, reject) => {
  console.log("initial promise rejects");
  reject();
});

p.catch(() => console.log("reject handler"))
  .then(() => console.log("resolve handler"))
  .finally(() => console.log("finally handler"));

// initial promise rejects
// reject handler
// resolve handler
// finally handler
```

#### Promise 图(Promise Graphs)

- 因为一个 Promise 可以有任意多个处理程序，所以 Promise 连锁可以构建有向非循环图的结构。
  - 这样，每个 Promise 都是图中的一个节点，而使用实例方法添加的处理程序则是有向顶点。
  - 因为图中的每个节点都会等待前一个节点落定，所以图的方向就是 Promise 的解决或拒绝顺序。
- 有向非循环图是体现 Promise 连锁可能性的最准确表达。

```js
//         A
//       /   \
//      B     C
//     / \   / \
//    D   E F   G

let A = new Promise((resolve, reject) => {
  console.log("A");
  resolve();
});

let B = A.then(() => console.log("B"));
let C = A.then(() => console.log("C"));

B.then(() => console.log("D"));
B.then(() => console.log("E"));
C.then(() => console.log("F"));
C.then(() => console.log("G"));

// 日志的输出语句是对二叉树的层序遍历:
// A
// B
// C
// D
// E
// F
// G

// Promise的处理程序是按照它们添加的顺序执行的。由于Promise的处理程序是先添加到消息队列，然后才逐个执行，因此构成了层序遍历。
```

#### Promise.all()和 Promise.race()

1. **Promise.all()**
   - Promise.all() 静态方法创建的 Promise 会在一组 Promise 全部解决之后再解决。这个静态方法接收一个可迭代(iterable)对象，返回一个新 Promise。
     - 注：Array，Map，Set 都属于 ES6 的 iterable 类型。
   - **合成的 Promise 只会在每个包含的 Promise 都解决之后才解决。**
   - **如果至少有一个包含的 Promise 待定，则合成的 Promise 也会待定。如果有一个包含的 Promise 拒绝，则合成的 Promise 也会拒绝。**
   - 如果所有 Promise 都成功解决，则合成 Promise 的解决值就是所有包含 Promise 解决值的数组，按照迭代器顺序。
   - 如果有 Promise 拒绝，则第一个拒绝的 Promise 会将自己的理由作为合成 Promise 的拒绝理由。之后再拒绝的 Promise 不会影响最终 Promise 的拒绝理由。

```js
// 虽然只有第一个Promise的拒绝理由会进入拒绝处理程序，第二个Promise的拒绝也会被静默处理，不会有错误跑掉
let p = Promise.all([
  Promise.resolve(1),
  Promise.reject(3),
  new Promise((resolve, reject) => setTimeout(reject("出错了"), 1000)),
]);

p.catch((reason) => setTimeout(console.log, 0, reason)); // 3
```

2. **Promise.race()**

- **Promise.race() 静态方法返回一个包装 Promise，是一组集合中最先解决或拒绝的 Promise 的镜像**。这个方法接收一个可迭代对象，返回一个新 Promise。
  - 一旦迭代器中的某个 promise 解决或拒绝，返回的 promise 就会解决或拒绝。
- Promise.race() 不会对解决或拒绝的 Promise 区别对待。无论是解决还是拒绝，只要是第一个落定的 Promise， Promise.race() 就会包装其解决值或拒绝理由并返回新 Promise。
- 如果传的迭代是空的，则返回的 promise 将永远等待。
- 与 Promise.all()类似，合成的 Promise 会静默处理所有包含 Promise 的拒绝操作。

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, "one");
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, "two");
});

Promise.race([promise1, promise2]).then((value) => {
  console.log(value);
  // Both resolve, but promise2 is faster
});
// expected output: "two"
```

#### 串行 Promise 合成 (Serial Promise Composition)

- 基于后续 Promise 使用之前 Promise 的返回值来串联 Promise 是 Promise 的基本功能。这很像函数合成，即将多个函数合成为一个函数。

```js
function addTwo(x) {
  return x + 2;
}
function addThree(x) {
  return x + 3;
}
function addFive(x) {
  return x + 5;
}

// 提炼出一个通用函数，可以把任意多个函数作为处理程序合成一个连续传值的Promise连锁。
function compose(...fns) {
  // 使用 Array.prototype.reduce() 可以写成更简洁的形式
  return (x) =>
    fns.reduce((promise, fn) => promise.then(fn), Promise.resolve(x));
}

let addTen = compose(addTwo, addThree, addFive);

addTen(8).then(console.log); // 18
```

### Promise 扩展 (Promise Extensions)

很多第三方 Promise 库实现中具备而 ECMAScript 规范却未涉及的两个特性：Promise 取消和进度追踪。

> ES6 不支持取消 Promise 和进度通知，一个主要原因就是这样会导致 Promise 连锁和 Promise 合成过度复杂化。
> 比如在一个 Promise 连锁中，如果某个被其他 Promise 依赖的 Promise 被取消了或者发出了通知，那么接下来应该发生什么完全说不清楚。

### 补充：Promise 的静态方法和实例方法概述

- 构造函数

  - **Promise()**
    - 创建一个新的 Promise 对象。该构造函数主要用于包装还没有添加 promise 支持的函数。

- 静态方法
  - **Promise.all(iterable)**
    - 这个方法返回一个新的 promise 对象，等到所有的 promise 对象都成功或有任意一个 promise 失败。
    - 如果所有的 promise 都成功了，它会把一个包含 iterable 里所有 promise 返回值的数组作为成功回调的返回值。顺序跟 iterable 的顺序保持一致。
    - 一旦有任意一个 iterable 里面的 promise 对象失败则立即以该 promise 对象失败的理由来拒绝这个新的 promise。
  - **Promise.allSettled(iterable)**
    - 等到所有 promise 都已敲定（每个 promise 都已兑现或已拒绝）。
    - 返回一个 promise，该 promise 在所有 promise 都敲定后完成，并兑现一个对象数组，其中的对象对应每个 promise 的结果。
  - **Promise.any(iterable)**
    - 接收一个 promise 对象的集合，当其中的任意一个 promise 成功，就返回那个成功的 promise 的值。
  - **Promise.race(iterable)**
    - 等到任意一个 promise 的状态变为已敲定。
    - 当 iterable 参数里的任意一个子 promise 成功或失败后，父 promise 马上也会用子 promise 的成功返回值或失败详情作为参数调用父 promise 绑定的相应处理函数，并返回该 promise 对象。
  - **Promise.reject(reason)**
    - 返回一个状态为已拒绝的 Promise 对象，并将给定的失败信息传递给对应的处理函数。
  - **Promise.resolve(value)**
    - 返回一个状态由给定 value 决定的 Promise 对象。如果该值是 thenable（即，带有 then 方法的对象），返回的 Promise 对象的最终状态由 then 方法执行结果决定；否则，返回的 Promise 对象状态为已兑现，并且将该 value 传递给对应的 then 方法。
    - 通常而言，如果你不知道一个值是否是 promise 对象，使用 Promise.resolve(value) 来返回一个 Promise 对象，这样就能将该 value 以 promise 对象形式使用。
- 实例方法
  - **Promise.prototype.catch()**
    - 为 promise 添加一个被拒绝状态的回调函数，并返回一个新的 promise，若回调函数被调用，则兑现其返回值，否则兑现原来的 promise 兑现的值。
  - **Promise.prototype.then()**
    - 为 promise 添加被兑现和被拒绝状态的回调函数，其以回调函数的返回值兑现 promise。若不处理已兑现或者已拒绝状态（例如，onFulfilled 或 onRejected 不是一个函数），则返回 promise 被敲定时的值。
  - **Promise.prototype.finally()**
    - 为 promise 添加一个回调函数，并返回一个新的 promise。这个新的 promise 将在原 promise 被兑现时兑现。而传入的回调函数将在原 promise 被敲定（无论被兑现还是被拒绝）时被调用。

#### Promise 取消 (Promise Canceling)

- ES6 Promise 被认为是“激进的”：只要 Promise 的逻辑开始执行，就没有办法阻止它执行到完成。
- 可以在现有实现基础上提供一种临时性的封装，以实现取消 Promise 的功能。

```js
// 下面是 CancelToken 类的一个基本实例：
class CancelToken {
  constructor(cancelFn) {
    this.promise = new Promise((resolve, reject) => {
      cancelFn(resolve);
    });
  }
}
/*
这个类包装了一个Promise，把解决方法暴露给了 cancelFn 参数。
这样，外部代码就可以向构造函数中传入一个函数，从而控制什么情况下可以取消Promise。
这里Promise是令牌类的公共成员，因此可以给它添加处理程序以取消Promise。 
*/
```

#### Promise 进度通知 (Promise Progress Notifications)

ECMAScript 6 Promise 并不支持进度追踪，但是可以通过扩展来实现。

- 有一种实现方式是扩展 Promise 类，为它添加 notify() 方法:

```js
// 扩展 Promise 类，为它添加 notify() 方法
class TrackablePromise extends Promise {
  constructor(executor) {
    const notifyHandlers = [];

    super((resolve, reject) => {
      return executor(resolve, reject, (status) => {
        notifyHandlers.map((handler) => handler(status));
      });
    });

    this.notifyHandlers = notifyHandlers;
  }

  notify(notifyHandler) {
    this.notifyHandlers.push(notifyHandler);
    return this;
  }
}

// 实例化一个扩展后的Promise
// 这个Promise会连续 5 次递归地设置 1000 毫秒的超时。每个超时回调都会调用 notify() 并传入状态值。
let p = new TrackablePromise((resolve, reject, notify) => {
  function countdown(x) {
    if (x > 0) {
      notify(`${20 * x}% remaining`);
      setTimeout(() => countdown(x - 1), 1000);
    } else {
      resolve();
    }
  }
  countdown(5);
});

// 调用notify()方法
p.notify((x) => setTimeout(console.log, 0, "progress:", x));
p.then(() => setTimeout(console.log, 0, "completed"));

// （约 1 秒后）80% remaining
// （约 2 秒后）60% remaining
// （约 3 秒后）40% remaining
// （约 4 秒后）20% remaining
// （约 5 秒后）completed
```

## 异步函数 (ASYNC FUNCTIONS)

- 异步函数，也称为“async/await”（语法关键字），是 ES6 Promise 模式在 ECMAScript 函数中的应用。
- async/await 是 ES8 规范新增的。这个特性从行为和语法上都增强了 JavaScript，让以同步方式写的代码能够异步执行。

### 异步函数基础 (Async Function Basics)

#### async

- `async` 关键字用于声明异步函数。这个关键字可以用在函数声明、函数表达式、箭头函数和方法上。
- 使用 `async` 关键字可以让函数具有异步特征，但总体上其代码仍然是同步求值的。而在参数或闭包方面，异步函数仍然具有普通 JavaScript 函数的正常行为。
- 异步函数如果使用 `return` 关键字返回了值（如果没有 `return` 则会返回 `undefined` ），这个值会被 `Promise.resolve()` 包装成一个 Promise 对象。
  - 异步函数始终返回 Promise 对象。在函数外部调用这个函数可以得到它返回的 Promise。
- 异步函数的返回值期待（但实际上并不要求）一个实现 `thenable` 接口的对象，但常规的值也可以。
  - 如果返回的是实现 `thenable` 接口的对象，则这个对象可以由提供给 `then()` 的处理程序“解包”。
  - 如果不是，则返回值就被当作已经解决的 Promise。
- 与在 Promise 处理程序中一样，在异步函数中抛出错误会返回拒绝的 Promise。
  - 不过，拒绝 Promise 的错误不会被异步函数捕获。

#### await

- 因为异步函数主要针对不会马上完成的任务，所以自然需要一种暂停和恢复执行的能力。
  - 使用 `await` 关键字可以暂停异步函数代码的执行，等待 Promise 解决。
- `await` 关键字会暂停执行异步函数后面的代码，让出 JavaScript 运行时的执行线程。
  - 这个行为与生成器函数中的 yield 关键字是一样的。
  - `await` 关键字同样是尝试“解包”对象的值，然后将这个值传给表达式，再异步恢复异步函数的执行。
- `await` 关键字期待（但实际上并不要求）一个实现 `thenable` 接口的对象，但常规的值也可以。
  - 如果是实现 `thenable` 接口的对象，则这个对象可以由 `await` 来“解包”。
  - 如果不是，则这个值就被当作已经解决的 Promise。
- 单独的 `Promise.reject()` 不会被异步函数捕获，而会抛出未捕获错误。
  - 不过，对拒绝的 Promise 使用 `await` 则会释放（unwrap）错误值（将拒绝 Promise 返回）。
- await 的限制
  - **`await` 关键字必须在异步函数中使用**。
  - 此外，异步函数的特质不会扩展到嵌套函数。
    - 因此， `await` 关键字也只能直接出现在异步函数的定义中。在同步函数内部使用 `await` 会抛出 `SyntaxError` 。

### 停止和恢复执行 (Halting and Resuming Execution)

- 使用 await 关键字之后的区别其实比看上去的还要微妙一些。

```js
async function foo() {
  console.log(await Promise.resolve("foo"));
}

async function bar() {
  console.log(await "bar");
}

async function baz() {
  console.log("baz");
}

foo();
bar();
baz();
// 执行顺序和调用顺序有异：
// baz
// bar
// foo
```

- **async/await 中真正起作用的是 await**。 async 关键字，无论从哪方面来看，都不过是一个标识符。
  - 毕竟，异步函数如果不包含 await 关键字，其执行基本上跟普通函数没有什么区别。
- JavaScript 运行时在碰到 await 关键字时，会记录在哪里暂停执行。等到 await 右边的值可用了，JavaScript 运行时会向消息队列中推送一个任务，这个任务会恢复异步函数的执行。
  - 因此，即使 await 后面跟着一个立即可用的值，函数的其余部分也会被异步求值。

```js
async function foo() {
  console.log(2);
  await null;
  console.log(4);
}

console.log(1);
foo();
console.log(3);

// 1
// 2
// 3
// 4
/*
控制台中输出结果的顺序很好地解释了运行时的工作过程： 
(1)  打印 1； 
(2)  调用异步函数 foo() ； 
(3) （在 foo() 中）打印 2； 
(4) （在 foo() 中） await 关键字暂停执行，为立即可用的值 null 向消息队列中添加一个任务； 
(5)  foo() 退出； 
(6)  打印 3； 
(7)  同步线程的代码执行完毕； 
(8)  JavaScript 运行时从消息队列中取出任务，恢复异步函数执行； 
(9) （在 foo() 中）恢复执行， await 取得 null 值（这里并没有使用）； 
(10)（在 foo() 中）打印 4； 
(11) foo() 返回。 
*/
```

- 如果 await 后面是一个 Promise，为了执行异步函数，实际上会有两个任务被添加到消息队列并被异步求值。

```js
async function foo() {
  console.log(2);
  console.log(await Promise.resolve(8));
  console.log(9);
}

async function bar() {
  console.log(4);
  console.log(await 6);
  console.log(7);
}

console.log(1);
foo();
console.log(3);
bar();
console.log(5);

// 输出 1 2 3 4 5 8 9 6 7

// TC39 对 await 后面是Promise的情况如何处理做过一次修改。
// 修改后，本例中的 Promise.resolve(8) 只会生成一个异步任务。因此在新版浏览器中，这个示例的输出结果为 123458967 。
// 实际开发中，对于并行的异步操作我们通常更关注结果，而不依赖执行顺序。
```

### 异步函数策略 (Strategies for Async Functions)

#### 实现 sleep()

```js
async function sleep(delay) {
  return new Promise((resolve) => setTimeout(resolve, delay));
}

async function foo() {
  const t0 = Date.now();
  await sleep(1500); // 暂停约 1500 毫秒
  console.log(Date.now() - t0);
}
foo();
```

#### 利用平行执行 (Maximizing Parallelization)

```js
// 顺序等待了5个随机的超时：
async function randomDelay(id) {
  // 延迟 0~1000 毫秒
  const delay = Math.random() * 1000;
  return new Promise((resolve) =>
    setTimeout(() => {
      console.log(`${id} finished`);
      resolve();
    }, delay)
  );
}

async function foo() {
  const t0 = Date.now();
  for (let i = 0; i < 5; ++i) {
    await randomDelay(i);
  }

  console.log(`${Date.now() - t0}ms elapsed`);
}

// 就算这些Promise之间没有依赖，异步函数也会依次暂停，等待每个超时完成。这样可以保证执行顺序，但总执行时间会变长。
foo();
```

如果顺序不是必需保证的，那么可以先一次性初始化所有 Promise，然后再分别等待它们的结果。

```js
// 如果顺序不是必需保证的，那么可以先一次性初始化所有Promise，然后再分别等待它们的结果。
async function randomDelay(id) {
  // 延迟 0~1000 毫秒
  const delay = Math.random() * 1000;
  return new Promise((resolve) =>
    setTimeout(() => {
      console.log(`${id} finished`);
      resolve(id);
    }, delay)
  );
}

async function foo() {
  const t0 = Date.now();

  const promises = Array(5)
    .fill(null)
    .map((_, i) => randomDelay(i));

  for (const p of promises) {
    console.log(`awaited ${await p}`);
  }

  console.log(`${Date.now() - t0}ms elapsed`);
}
// 虽然Promise没有按照顺序执行，但 await 按顺序收到了每个Promise的值
foo();
// 每次输出的顺序可能不一样，但耗时比上面顺序执行的要短
// 2 finished
// 0 finished
// awaited 0
// 4 finished
// 3 finished
// 1 finished
// awaited 1
// awaited 2
// awaited 3
// awaited 4
// 628ms elapsed
```

#### 串行执行 Promise (Serial Promise Execution)

- 使用 async/await，Promise 连锁会变得很简单。

```js
async function addTwo(x) {
  return x + 2;
}
async function addThree(x) {
  return x + 3;
}
async function addFive(x) {
  return x + 5;
}

async function addTen(x) {
  for (const fn of [addTwo, addThree, addFive]) {
    x = await fn(x);
  }
  return x;
}

addTen(9).then(console.log); // 19
```

#### 栈追踪与内存管理 (Stack Traces and Memory Management)

- Promise 与异步函数的功能有相当程度的重叠，但它们在内存中的表示则差别很大。

```js
// 注意，以下在浏览器的console中运行才是这个结果，如果是nodejs环境运行，报错是一样的：
// (node:16075) UnhandledPromiseRejectionWarning: bar
// ...

// 即便如此，实际浏览器中报错和书中的还是有点区别：

// Promise报错
function fooPromiseExecutor(resolve, reject) {
  setTimeout(reject, 1000, "bar");
}

function foo() {
  new Promise(fooPromiseExecutor);
}

foo();
// Uncaught (in promise) bar
//   setTimeout (async)
//   fooPromiseExecutor
//   foo
//   (anonymous)
```

以上示例：

- 栈追踪信息应该相当直接地表现 JavaScript 引擎当前栈内存中函数调用之间的嵌套关系。
  - 在超时处理程序执行时和拒绝 Promise 时，我们看到的错误信息包含嵌套函数的标识符，那是被调用以创建最初 Promise 实例的函数。
  - 可是，我们知道这些函数已经返回了，因此栈追踪信息中不应该看到它们。
- 答案很简单，这是因为 **JavaScript 引擎会在创建 Promise 时尽可能保留完整的调用栈。**
  - 在抛出错误时，调用栈可以由运行时的错误处理逻辑获取，因而就会出现在栈追踪信息中。
  - 当然，**这意味着栈追踪信息会占用内存，从而带来一些计算和存储成本。**

```js
// 异步函数的报错
function fooPromiseExecutor(resolve, reject) {
  setTimeout(reject, 1000, "bar");
}

async function foo() {
  await new Promise(fooPromiseExecutor);
}
foo();

// Uncaught (in promise) bar
//   foo
//   async function (async)
//   (anonymous)
```

- 这样修改后，栈追踪信息就准确地反映了当前的调用栈。
  - fooPromiseExecutor() 已经返回，所以它不在错误信息中。但 foo() 此时被挂起了，并没有退出。
  - JavaScript 运行时可以简单地在嵌套函数中存储指向包含函数的指针，就跟对待同步函数调用栈一样。
  - 这个指针实际上存储在内存中，可用于在出错时生成栈追踪信息。
  - 这样就不会像之前的例子那样带来额外的消耗，因此**在重视性能的应用中是可以优先考虑的**。

## 小结

- 随着 ES6 新增了 Promise 和 ES8 新增了异步函数(async/await)，ECMAScript 的异步编程特性有了长足的进步。
- Promise 的主要功能是为异步代码提供了清晰的抽象。
  - 可以用 Promise 表示异步执行的代码块，也可以用 Promise 表示异步计算的值。
  - 在需要串行异步代码时，Promise 的价值最为突出。
  - 作为可塑性极强的一种结构，Promise 可以被序列化、连锁使用、复合、扩展和重组。
- 异步函数是将 Promise 应用于 JavaScript 函数的结果。
  - 异步函数可以暂停执行，而不阻塞主线程。
  - 无论是编写基于 Promise 的代码，还是组织串行或平行执行的异步代码，使用异步函数都非常得心应手。
  - 异步函数可以说是现代 JavaScript 工具箱中最重要的工具之一。
