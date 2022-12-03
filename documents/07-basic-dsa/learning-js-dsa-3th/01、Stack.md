<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [栈(Stack)](#%E6%A0%88stack)
  - [基础说明](#%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [基于数组的 Stack 实现](#%E5%9F%BA%E4%BA%8E%E6%95%B0%E7%BB%84%E7%9A%84-stack-%E5%AE%9E%E7%8E%B0)
  - [基于对象的 Stack 实现](#%E5%9F%BA%E4%BA%8E%E5%AF%B9%E8%B1%A1%E7%9A%84-stack-%E5%AE%9E%E7%8E%B0)
  - [Stack 的应用示例](#stack-%E7%9A%84%E5%BA%94%E7%94%A8%E7%A4%BA%E4%BE%8B)
    - [1. 检验字符串中的小括号是否合法(合法即小括号成对其顺序正确)](#1-%E6%A3%80%E9%AA%8C%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E5%B0%8F%E6%8B%AC%E5%8F%B7%E6%98%AF%E5%90%A6%E5%90%88%E6%B3%95%E5%90%88%E6%B3%95%E5%8D%B3%E5%B0%8F%E6%8B%AC%E5%8F%B7%E6%88%90%E5%AF%B9%E5%85%B6%E9%A1%BA%E5%BA%8F%E6%AD%A3%E7%A1%AE)
    - [2. 从十进制到二进制](#2-%E4%BB%8E%E5%8D%81%E8%BF%9B%E5%88%B6%E5%88%B0%E4%BA%8C%E8%BF%9B%E5%88%B6)
    - [3. 进制转换算法](#3-%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2%E7%AE%97%E6%B3%95)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 栈(Stack)

## 基础说明

- 定义:
  - 栈是一种遵从后进先出（LIFO）原则的有序集合。
  - 新添加或待删除的元素都保存在栈的同一端，称作栈顶，另一端就叫栈底。在栈里，新元素都靠近栈顶，旧元素都接近栈底。
- 基本方法:
  - push(element(s)) ：添加一个（或几个）新元素到栈顶。
  - pop() ：移除栈顶的元素，同时返回被移除的元素。
  - peek() ：返回栈顶的元素，不对栈做任何修改（该方法不会移除栈顶的元素，仅仅返回它）。
  - isEmpty() ：如果栈里没有任何元素就返回 true ，否则返回 false 。
  - clear() ：移除栈里的所有元素。
  - size() ：返回栈里的元素个数。该方法和数组的 length 属性很类似。
- 生活示例:
  - 羽毛球筒
  - 桌上一叠盘子

## 基于数组的 Stack 实现

```js
class StackArray {
  constructor() {
    this.items = [];
  }

  // 向栈添加元素
  push(ele) {
    this.items.push(ele);
  }

  // 从栈移除元素
  pop() {
    return this.items.pop();
  }

  // 查看栈顶元素
  peek() {
    // 无法直接取arr[-1],所以取最大的索引
    return this.items[this.items.length - 1];
  }

  // 检查栈是否为空
  isEmpty() {
    return this.items.length === 0;
  }

  // 栈的长度
  size() {
    return this.items.length;
  }

  // 清空栈元素
  clear() {
    this.items = [];
  }
}

// 使用Stack类
const stack = new StackArray();
console.log(stack.isEmpty()); // 输出为 true
stack.push(5);
stack.push(8);
console.log(stack.peek()); // 输出 8
stack.push(11);
console.log(stack.size()); // 输出 3
console.log(stack.isEmpty()); // 输出 false
stack.push(15);
stack.pop();
stack.pop();
console.log(stack.size()); // 输出 2
console.log(stack); // StackArray { items: [ 5, 8 ] }
```

不足:

- 在使用数组时，大部分方法的时间复杂度是 **O(n)**。
- 如果数组有更多元素的话，所需的时间会更长。
- 另外，数组是元素的一个有序集合，为了保证元素排列有序，它会占用更多的内存空间。

## 基于对象的 Stack 实现

- 除了 toString 方法，创建的其他方法的复杂度均为 O(1)，可以直接找到目标元素并对其进行操作(push、pop 或 peek)。
- 能直接获取元素，占用较少的内存空间，并且仍然保证所有元素按照我们的需要排列

```js
class Stack {
  constructor() {
    this.count = 0;
    this.items = {};
  }
  // 向栈中插入元素
  push(ele) {
    this.items[this.count] = ele;
    this.count++;
  }
  // 验证一个栈是否为空
  isEmpty() {
    return this.count === 0;
  }
  // 栈的大小
  size() {
    return this.count;
  }
  // 从栈中弹出元素
  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    // 如果栈对象不为空,长度-1
    this.count--;
    // 取出栈顶值保存
    const result = this.items[this.count];
    // 删除栈顶值
    delete this.items[this.count];
    // 将保存的删除前的栈顶值返回
    return result;
  }
  // 查看栈顶的值
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }
  // 清空该栈
  clear() {
    // 要将它的值复原为构造函数中使用的值
    this.items = {};
    this.count = 0;
  }
  // 创建 toString 方法
  toString() {
    if (this.isEmpty()) {
      return "";
    }
    let objStr = `${this.Items[0]}`;
    for (let i = 1; i < this.count; i++) {
      objStr = `${objStr},${this.items[i]}`;
    }
    return objStr;
  }
}

// 使用Stack类
const stack = new Stack();
console.log(stack.isEmpty()); // 输出为 true
stack.push(5);
stack.push(8);
console.log(stack.peek()); // 输出 8
stack.push(11);
console.log(stack.size()); // 输出 3
console.log(stack.isEmpty()); // 输出 false
stack.push(15);
stack.pop();
stack.pop();
console.log(stack.size()); // 输出 2
console.log(stack); // Stack { count: 2, items: { '0': 5, '1': 8 } }
```

- 导出与导入

```js
// 因为在nodejs测试使用,如果环境不同,可以用ESM的方式导入导出   export default class Stack {...
module.exports = Stack;
// 使用时直接
const Stack = require("./Stack");

// 如果是这样导出
module.exports = { Stack };
// 引入的stack构造函数是为
const Stack = require("./Stack").Stack;
```

## Stack 的应用示例

### 1. 检验字符串中的小括号是否合法(合法即小括号成对其顺序正确)

```txt
// *   sdf(ds(ew(we)rw)rwqq)qwewe   合法
// *   (sd(qwqw)sd(sd))             合法
// *   ()()sd()(sd()fw))(           不合法
```

```js
const Stack = require("./Stack");

// 1. 检验字符串中的小括号是否合法(合法即小括号成对其顺序正确)
// *   sdf(ds(ew(we)rw)rwqq)qwewe   合法
// *   (sd(qwqw)sd(sd))             合法
// *   ()()sd()(sd()fw))(           不合法

let isLeaglBrackets = (str) => {
  const stack = new Stack();

  for (let i = 0; i < str.length; i++) {
    const e = str[i];
    // 把括号(放到栈里面去
    if (e === "(") {
      stack.push(e);
    } else if (e === ")") {
      // 如果匹配到右括号,但是没有已存在的左括号,不合法
      if (stack.isEmpty()) {
        return false;
      } else {
        // 如果匹配到右括号,已有存在的左括号,删掉一个(pop出来)
        stack.pop();
      }
    }
  }

  // 如果遍历完stack大小为0,说明合法,否则说明不合法
  return stack.size() === 0;
};

console.log(isLeaglBrackets("sdf(ds(ew(we)rw)rwqq)qwewe")); // true
console.log(isLeaglBrackets("(sd(qwqw)sd(sd))")); // true
console.log(isLeaglBrackets("()()sd()(sd()fw))(")); // false
```

### 2. 从十进制到二进制

要把十进制转化成二进制，我们可以将该十进制数除以 2（二进制是满二进一）并对商取整，直到结果是 0 为止。

```js
let decimalToBinary = (decNumber) => {
  const remStack = new Stack();
  let number = decNumber;
  let rem;
  let binaryString = "";

  // 当除法的结果不为 0 时，我们会获得一个余数，并放到栈里,然后让结果继续除以 2。
  while (number > 0) {
    rem = Math.floor(number % 2);
    remStack.push(rem);
    number = Math.floor(number / 2);
  }

  // 用 pop 方法把栈中的元素都移除，把出栈的元素连接成字符串
  while (!remStack.isEmpty()) {
    binaryString += remStack.pop().toString();
  }

  return binaryString;
};

console.log(decimalToBinary(233)); // 11101001
console.log(decimalToBinary(10)); // 1010
console.log(decimalToBinary(1000)); // 1111101000
```

### 3. 进制转换算法

修改之前的算法，使之能把十进制转换成基数为 2 ～ 36 的任意进制。除了把十进制数除以 2 转成二进制数，还可以传入其他任意进制的基数为参数

- 在将十进制转成二进制时，余数是 0 或 1；
- 在将十进制转成八进制时，余数是 0 ～ 7；
- 但是将十进制转成十六进制时，余数是 0 ～ 9 加上 A、B、C、D、E 和 F（对应 10、11、12、13、14 和 15）。
- 因此，我们需要对栈中的数字做个转化才可以（注释 {1} 和注释 {2} ）。
- 因此，从十一进制开始，字母表中的每个字母将表示相应的基数。字母 A 代表基数 11，B 代表基数 12，以此类推。

```js
let baseConverter = (decNumber, base) => {
  const remStack = new Stack();
  const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // {1}
  let number = decNumber;
  let rem;
  let baseString = "";

  // 基数需要为 2～36,否则返回空字串
  if (!base >= 2 && base <= 36) {
    return "";
  }

  while (number > 0) {
    rem = Math.floor(number % base);
    remStack.push(rem);
    number = Math.floor(number / base);
  }

  while (!remStack.isEmpty()) {
    baseString += digits[remStack.pop()]; // {2}
  }

  return baseString;
};

console.log(baseConverter(100345, 2)); // 11000011111111001
console.log(baseConverter(100345, 8)); // 303771
console.log(baseConverter(100345, 10)); // 100345
console.log(baseConverter(100345, 16)); // 187F9
console.log(baseConverter(100345, 35)); // 2BW0
```
