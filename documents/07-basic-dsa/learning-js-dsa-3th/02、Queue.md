<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [队列(Queue)](#%E9%98%9F%E5%88%97queue)
  - [队列基础说明](#%E9%98%9F%E5%88%97%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [队列实现](#%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0)
  - [队列的应用示例](#%E9%98%9F%E5%88%97%E7%9A%84%E5%BA%94%E7%94%A8%E7%A4%BA%E4%BE%8B)
    - [击鼓传花游戏(queue)](#%E5%87%BB%E9%BC%93%E4%BC%A0%E8%8A%B1%E6%B8%B8%E6%88%8Fqueue)
- [双端队列（deque，或称 double-ended queue）](#%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97deque%E6%88%96%E7%A7%B0-double-ended-queue)
  - [双端队列基础说明](#%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [双端队列的实现](#%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97%E7%9A%84%E5%AE%9E%E7%8E%B0)
  - [双端队列的应用示例](#%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97%E7%9A%84%E5%BA%94%E7%94%A8%E7%A4%BA%E4%BE%8B)
    - [回文检查器(deque)](#%E5%9B%9E%E6%96%87%E6%A3%80%E6%9F%A5%E5%99%A8deque)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 队列(Queue)

## 队列基础说明

- 定义:
  - 队列是遵循先进先出（FIFO，也称为先来先服务）原则的一组有序的项。队列在尾部添加新元素，并从顶部移除元素。最新添加的元素必须排在队列的末尾。
- 基本方法:
  - enqueue(element(s)) ：向队列尾部添加一个（或多个）新的项。
  - dequeue() ：移除队列的第一项（即排在队列最前面的项）并返回被移除的元素。
  - peek() ：返回队列中第一个元素——最先被添加，也将是最先被移除的元素。
    - 队列不做任何变动（不移除元素，只返回元素信息——与 Stack 类的 peek 方法非常类似）。
    - 该方法在其他语言中也可以叫作 front 方法。
  - isEmpty() ：如果队列中不包含任何元素，返回 true ，否则返回 false 。
  - size() ：返回队列包含的元素个数，与数组的 length 属性类似。
  - clear() ：移除队列里的所有元素。
- 生活示例:
  - 排队

## 队列实现

Queue 类和 Stack 类非常类似。主要的区别在于 dequeue 方法和 peek 方法，这是由于先进先出和后进先出原则的不同所造成的。

```js
class Queue {
  constructor() {
    // 控制队列的大小
    this.count = 0;
    // 将要从队列前端移除元素，同样需要一个变量来协助追踪第一个元素
    this.lowestCount = 0;
    // 使用一个对象来存储我们元素
    this.items = {};
  }

  // 1. 向队列添加元素
  enqueue(element) {
    // 向队列中加入一个元素的话，我们要把 count 变量作为 items对象中的键，对应的元素作为它的值。
    // 将元素加入队列后，我们将 count 变量加 1。
    this.items[this.count] = element;
    this.count++;
  }
  // 2. 从队列移除元素
  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }
  // 3. 查看队列头元素
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }
  // 4. 检查队列是否为空
  // isEmpty() {
  //     return this.count - this.lowestCount === 0;
  // }
  isEmpty() {
    return this.size() === 0;
  }
  // 5 获取队列的长度
  //  要计算队列中有多少元素，我们只需要计算 count 和 lowestCount 之间的差值即可。
  size() {
    return this.count - this.lowestCount;
  }
  // 6. 清空队列
  clear() {
    this.items = {};
    this.lowestCount = 0;
    this.count = 0;
  }
  // 7. 创建 toString 方法
  toString() {
    if (this.isEmpty()) {
      return "";
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

// 测试
const queue = new Queue();
console.log(queue.isEmpty()); // 输出 true
queue.enqueue("John");
queue.enqueue("Jack");
console.log(queue.toString()); // John,Jack
queue.enqueue("Camila");
console.log(queue.toString()); // John, Jack, Camila
console.log(queue.size()); // 输出 3
console.log(queue.isEmpty()); // 输出 false
queue.dequeue(); // 移除 John
queue.dequeue(); // 移除 Jack
console.log(queue.toString()); // Camila

// 导出示例
module.exports = {
  Queue,
};
```

## 队列的应用示例

### 击鼓传花游戏(queue)

场景描述：

- 孩子们围成一个圆圈，把花尽快地传递给旁边的人。
- 某一时刻传花停止，这个时候花在谁手里，谁就退出圆圈、结束游戏。
  - 重复这个过程，直到只剩一个孩子（胜者）。

```js
const Queue = require("./Queue").Queue;

/**
 * 击鼓传花游戏
 * @param {*} elementList 名单
 * @param {*} num 每次传递的次数(0是自己,即最开始的那个值,从1开始即数组第二个值)
 */
let hotPotato = (elementList, num) => {
  // 实例一个队列,用于接收参与人员名单
  const queue = new Queue();
  // 记录被淘汰者
  const eliminatedList = [];

  // 得到一份名单，把里面的名字全都加入队列
  for (let i = 0; i < elementList.length; i++) {
    queue.enqueue(elementList[i]);
  }

  while (queue.size() > 1) {
    // 给定一个数字，然后迭代队列。从队列开头移除一项，再将其添加到队列末尾
    for (let i = 0; i < num; i++) {
      queue.enqueue(queue.dequeue());
    }
    eliminatedList.push(queue.dequeue());
  }

  return {
    eliminated: eliminatedList,
    winner: queue.dequeue(),
  };
};

// 测试：
const names = ["John", "Jack", "Camila", "Ingrid", "Carl"];
// 每次循环传递7次,轮到谁谁退出,继续传7次直到最后一个(第一次第一个是Jack)
const result = hotPotato(names, 7);

console.log(result);
// 输出: { eliminated: [ 'Camila', 'Jack', 'Carl', 'Ingrid' ], winner: 'John' }

// 显示过程：
result.eliminated.forEach((name) => {
  console.log(`${name}在击鼓传花游戏中被淘汰。`);
});
/*
输出：
Camila在击鼓传花游戏中被淘汰。
Jack在击鼓传花游戏中被淘汰。
Carl在击鼓传花游戏中被淘汰。
Ingrid在击鼓传花游戏中被淘汰。
*/

console.log(`胜利者： ${result.winner}`); // 胜利者： John
```

补充说明：

这其实就是个**约瑟夫环问题**，描述还例如:

- 有一个数组`A[100]`存放 0 ～ 99，要求每隔两个数删掉一个数，到末尾时循环到开头继续进行，求最后一个被删除的数。
- N 个人编号为 1，2，……，N，依次报数，每报到 M 时，杀掉那个人，求最后胜利者的编号。
  - (https://blog.csdn.net/u011500062/article/details/72855826)

使用递推公式求解也可以, 公式: `f(N,M)=(f(N−1,M)+M)%N`

- `f(N,M)`表示，N 个人报数，每报到 M 时杀掉那个人，最终胜利者的编号
- `f(N−1,M`)表示，N-1 个人报数，每报到 M 时杀掉那个人，最终胜利者的编号

有了递推公式后即可使用递归的方式实现：

```js
// 第一个问题，n个数，每隔m删除，求最后剩下的数
// 第二个问题，n个人，报m的出列，求最后未出列的
function cir(n, m) {
  let p = 0;
  for (let i = 2; i <= n; i++) {
    p = (p + m) % i;
  }
  return p + 1;
}

console.log(cir(3, 2)); // 3
console.log(cir(100, 8)); // 97
```

# 双端队列（deque，或称 double-ended queue）

## 双端队列基础说明

- 定义:
  - 一种允许同时从前端和后端添加和移除元素的特殊队列。
- 基本方法:
  - addFront(element) ：该方法在双端队列前端添加新的元素。
  - addBack(element) ：该方法在双端队列后端添加新的元素（实现方法和 Queue 类中的 enqueue 方法相同）。
  - removeFront() ：该方法会从双端队列前端移除第一个元素（实现方法和 Queue 类中的 dequeue 方法相同）。
  - removeBack() ：该方法会从双端队列后端移除第一个元素（实现方法和 Stack 类中的 pop 方法一样）。
  - peekFront() ：该方法返回双端队列前端的第一个元素（实现方法和 Queue 类中的 peek 方法一样）。
  - peekBack() ：该方法返回双端队列后端的第一个元素（实现方法和 Stack 类中的 peek 方法一样）。
  - isEmpty() ：如果队列中不包含任何元素，返回 true ，否则返回 false 。
  - size() ：返回队列包含的元素个数，与数组的 length 属性类似。
  - clear() ：移除队列里的所有元素。
- 生活示例:
  - 买电影票,一个刚买了票的人如果只是还需要再问一些简单的信息，就可以直接回到队伍的头部。另外，在队伍末尾的人如果赶时间，他可以直接离开队伍。
  - 双端队列的一个常见应用是存储一系列的撤销操作。

## 双端队列的实现

```js
// 先声明一个 Deque 类及其构造函数:
class Deque {
  constructor() {
    this.count = 0;
    this.lowestCount = 0;
    this.items = {};
  }

  // 向双端队列的前端添加元素
  addFront(element) {
    // 如果队列原本为空,在前端加和最后加是一样的.
    if (this.isEmpty()) {
      this.addBack(element);
    } else if (this.lowestCount > 0) {
      // 如果不是空队列,且一个元素已经被从双端队列的前端移除，也就是说 lowestCount >=1;
      // 因为是前端加,所以最小值索引减1,再放置该值
      this.lowestCount--;
      this.items[this.lowestCount] = element;
    } else {
      // 如果不是空队列,但 lowestCount = 0;
      /**其实可以直接移动,使用负数做key */
      // 为了便于演示，把本场景看作使用数组。要在第一位添加一个新元素，要将所有元素后移一位,空出第一个位置。
      // 由于不想丢失任何已有的值，需要从最后一位开始迭代所有的值，并为元素赋上索引值减 1 位置的值 (注释{1})。
      // 在所有的元素都完成移动后，第一位将是空闲状态，这样就可以用需要添加的新元素来覆盖它了 (注释{2})。
      for (let i = this.count; i > 0; i--) {
        // {1}
        this.items[i] = this.items[i - 1];
      }
      this.count++;
      this.lowestCount = 0;
      this.items[0] = element; // {2}
    }
  }

  addBack(element) {
    this.items[this.count] = element;
    this.count++;
  }

  removeFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  removeBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }

  peekFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }

  peekBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }

  isEmpty() {
    return this.size() === 0;
  }

  clear() {
    this.items = {};
    this.count = 0;
    this.lowestCount = 0;
  }

  size() {
    return this.count - this.lowestCount;
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}
// 测试
const deque = new Deque();
console.log(deque.isEmpty()); // 输出 true
deque.addBack("John");
deque.addBack("Jack");
console.log(deque.toString()); // John, Jack
deque.addBack("Camila");
console.log(deque.toString()); // John, Jack, Camila
console.log(deque.size()); // 输出 3
console.log(deque.isEmpty()); // 输出 false
deque.removeFront(); // 移除 John
console.log(deque.toString()); // Jack, Camila
deque.removeBack(); // Camila 决定离开
console.log(deque.toString()); // Jack
deque.addFront("John"); // John 回来询问一些信息
console.log(deque.toString()); // John, Jack

// 导出示例
module.exports = {
  Deque,
};
```

## 双端队列的应用示例

### 回文检查器(deque)

- 回文是正反都能读通的单词、词组、数或一系列字符的序列，例如 "madam" 或 "racecar"。
- 最简单的方式是将字符串反向排列并检查它和原字符串是否相同。如果两者相同，那么它就是一个回文。

```js
const Deque = require("./Queue").Deque;

let palindromeChecker = (str) => {
  // 传入str是否为空
  if (!str) {
    return false;
  }

  const deque = new Deque();
  // 将所有字母转化为小写，同时移除所有的空格
  const lowerString = str.toLocaleLowerCase().split(" ").join("");
  let isEqual = true;
  let firstChar, lastChar;
  // 把字串依次存入队列中
  for (let i = 0; i < lowerString.length; i++) {
    deque.addBack(lowerString.charAt(i));
  }
  // 如果从双端队列前端和后端取出的值不相等,则不定不是回文
  while (deque.size() > 1 && isEqual) {
    firstChar = deque.removeFront();
    lastChar = deque.removeBack();
    if (firstChar !== lastChar) {
      isEqual = false;
    }
  }
  return isEqual;
};

console.log("a", palindromeChecker("a")); // a true
console.log("aa", palindromeChecker("aa")); // aa true
console.log("kayak", palindromeChecker("kayak")); // kayak true
console.log("level", palindromeChecker("level")); // level true
console.log(
  "Was it a car or a cat I saw",
  palindromeChecker("Was it a car or a cat I saw") // Was it a car or a cat I saw true
);
console.log("Step on no pets", palindromeChecker("Step on no pets")); // Step on no pets true
```
