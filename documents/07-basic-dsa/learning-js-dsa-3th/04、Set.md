<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [集合 (Set）](#%E9%9B%86%E5%90%88-set)
  - [基础说明](#%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [使用 Object 实现的 Set](#%E4%BD%BF%E7%94%A8-object-%E5%AE%9E%E7%8E%B0%E7%9A%84-set)
  - [使用原始 js Set 模拟简单集合运算](#%E4%BD%BF%E7%94%A8%E5%8E%9F%E5%A7%8B-js-set-%E6%A8%A1%E6%8B%9F%E7%AE%80%E5%8D%95%E9%9B%86%E5%90%88%E8%BF%90%E7%AE%97)
    - [1 使用函数实现](#1-%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0%E5%AE%9E%E7%8E%B0)
    - [2 使用扩展运算符实现](#2-%E4%BD%BF%E7%94%A8%E6%89%A9%E5%B1%95%E8%BF%90%E7%AE%97%E7%AC%A6%E5%AE%9E%E7%8E%B0)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 集合 (Set）

## 基础说明

- 定义:
  - 集合是由一组无序且唯一（即不能重复）的项组成的。
- 说明:
  - 该数据结构使用了与有限集合相同的数学概念，但应用在计算机科学的数据结构中。
  - 在数学中，集合是一组不同对象的集。
  - 在数学中，集合也有并集、交集、差集等基本运算。
- ECMAScript 2015 介绍了 Set 类是 JavaScript API 的一部分。原生 ES2015 没有提供的集合运算，例如并集、交集和差集。
- 空集:
  - 就是不包含任何元素的集合。
- 简单集合运算:
  - 并集 `A∪B` ：对于给定的两个集合，返回一个包含两个集合中所有元素的新集合。
  - 交集 `A∩B` ：对于给定的两个集合，返回一个包含两个集合中共有元素的新集合。
  - 差集 `A-B` ：对于给定的两个集合，返回一个包含所有存在于第一个集合且不存在于第二个集合的元素的新集合。
  - 子集 `A⊆B` ：验证一个给定集合是否是另一集合的子集(或集合 B 包含集合 A)。
- 与数组:
  - 可以把集合想象成一个既没有重复元素，也没有顺序概念的数组。
- 基本方法:
  - add(element) ：向集合添加一个新元素。
  - delete(element) ：从集合移除一个元素。
  - has(element) ：如果元素在集合中，返回 true ，否则返回 false 。
  - clear() ：移除集合中的所有元素。
  - size() ：返回集合所包含元素的数量。它与数组的 length 属性类似。
  - values() ：返回一个包含集合中所有值（元素）的数组。
- 应用场景:
  - 在计算机科学中的主要应用之一是数据库。集合被用于查询的设计和处理。

## 使用 Object 实现的 Set

```js
class MySet {
  constructor() {
    this.items = {};
  }

  // 检验某个元素是否存在于集合中
  has(element) {
    // 如果指定的属性在指定的对象或其原型链中，则in 运算符返回true。
    // in左边为一个字符串类型或者 symbol 类型的属性名或者数组索引（非symbol类型将会强制转为字符串）。
    // in右操作数必须是一个对象值。
    // return element in items;

    // 有更好的实现
    // 该方法返回一个表明对象是否具有特定属性的布尔值。in运算符则返回表示对象在原型链上是否有特定属性的布尔值。
    return Object.prototype.hasOwnProperty.call(this.items, element);
  }
  // 添加元素
  add(element) {
    if (!this.has(element)) {
      // 添加一个 element 的时候，把它同时作为键和值保存，因为这样有利于查找该元素。
      this.items[element] = element;
      return true;
    }
    return false;
  }
  // 删除元素
  delete(element) {
    if (this.has(element)) {
      // 删除对应的属性使用delete
      delete this.items[element];
      return true;
    }
    return false;
  }

  // 清空集合
  clear() {
    this.items = {};
  }

  // 集合中元素数量
  size() {
    // 使用Object.keys()可能只有在现代浏览器中使用
    return Object.keys(this.items).length;
  }

  // 手动提取 items 对象的每一个属性，记录属性的个数并返回这个数。
  // 可以在任何浏览器上运行，和之前的代码是等价的。 和size()方法一样的
  sizeLegacy() {
    let count = 0;
    // 迭代 items 对象的所有属性
    for (let key in this.items) {
      // 检查它们是否是对象自身的属性（避免重复计数)
      if (this.items.hasOwnProperty(key)) {
        count++;
      }
      return count;
    }
  }

  // 查看集合内所有元素
  values() {
    // Object.values() 方法返回了一个包含给定对象所有属性值的数组。
    return Object.values(this.items);
  }

  // 不会修改当前的 Set 类实例或是作为参数传入的 otherSet 。没有副作用的方法和函数被称为纯函数。
  // 集合并集
  union(otherSet) {
    const unionSet = new MySet();
    this.values().forEach((value) => unionSet.add(value));
    otherSet.values().forEach((value) => unionSet.add(value));
    return unionSet;
  }

  // 集合交集
  // 找到当前 Set 实例中所有也存在于给定 Set 实例（otherSet）中的元素。
  // 不足:迭代次数为调用者集合的元素数量,如果调用者集合元素过多,迭代次数也多
  // (可以减少一些迭代次数 < 比较调用者集合元素和被调用者集合元素哪一个数量较小,就迭代哪个> )
  intersection1(otherSet) {
    const intersectionSet = new MySet();
    const values = this.values();
    for (let i = 0; i < values.length; i++) {
      if (otherSet.has(values[i])) {
        intersectionSet.add(values[i]);
      }
    }
    return intersectionSet;
  }

  intersection(otherSet) {
    const intersectionSet = new MySet();
    // 取出比较的两个set的所有元素
    const values = this.values();
    const otherValues = otherSet.values();

    // 比较调用者集合元素数量和被调用者元素数量的大小
    let biggerSet = values;
    let smallSet = otherValues;
    if (otherValues.length - values.length > 0) {
      biggerSet = otherValues;
      smallSet = values;
    }
    // 对较少元素集合进行迭代
    smallSet.forEach((value) => {
      if (biggerSet.includes(value)) {
        intersectionSet.add(value);
      }
    });

    return intersectionSet;
  }

  // 集合差集
  difference(otherSet) {
    const differenceSet = new MySet();
    this.values().forEach((value) => {
      if (!otherSet.has(value)) {
        differenceSet.add(value);
      }
    });
    return differenceSet;
  }

  // 集合子集
  // (说明: A.isSubsetOf(B),A是被比较者集合,B是比较者集合)
  isSubsetOf(otherSet) {
    // 如果传入的集合(比较者)元素数量小于被比较者元素数量,则不可能是比较者的子集
    if (otherSet.size() < this.size()) {
      return false;
    }
    let isSubset = true;
    this.values().every((value) => {
      // 如果被比较者有存在与比较者不同的元素,则不可能是子集,返回false并退出迭代
      if (!otherSet.has(value)) {
        isSubset = false;
        return false;
      }
      return true;
    });

    return isSubset;
  }

  isEmpty() {
    return this.size() === 0;
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    const values = this.values();
    let objString = `${values[0]}`;
    for (let i = 1; i < values.length; i++) {
      objString = `${objString},${values[i].toString()}`;
    }
    return objString;
  }
}

module.exports = {
  Set: MySet,
};
```

使用示例：

```js
const set = new MySet();

set.add(1);
console.log(set.values()); // 输出[1]
console.log(set.has(1)); // 输出 true
console.log(set.size()); // 输出 1

set.add(2);
console.log(set.values()); // 输出[1, 2]
console.log(set.has(2)); // 输出 true
console.log(set.size()); // 输出 2

set.delete(1);
console.log(set.values()); // 输出[2]

set.delete(2);
console.log(set.values()); // 输出[]

// 并集测试
const setA = new MySet();
setA.add(1);
setA.add(2);
setA.add(3);
setA.add(5);

const setB = new MySet();
setB.add(3);
setB.add(4);
setB.add(5);
setB.add(6);

// 并集
const unionAB = setA.union(setB);
console.log(unionAB.values()); // [ 1, 2, 3, 4, 5, 6 ] (重复的只会保留一个)
// 交集
const intersectionAB = setA.intersection(setB);
console.log(intersectionAB.values()); // [ 3, 5 ]
// 差集(存在于A但不存在与B)
const differenceAB = setA.difference(setB);
console.log(differenceAB.values()); // [ 1, 2 ]
// 子集
const setC = new MySet();
setC.add(3);
setC.add(6);

console.log(setC.isSubsetOf(setA)); // false
console.log(setC.isSubsetOf(setB)); // true
```

## 使用原始 js Set 模拟简单集合运算

### 1 使用函数实现

```js
// 并集
const union = (setA, setB) => {
  const unionAB = new Set();
  setA.forEach((v) => unionAB.add(v));
  setB.forEach((v) => unionAB.add(v));
  return unionAB;
};

// 交集(也可以先找出较小set进行迭代)
const intersection = (setA, setB) => {
  const intersectionSet = new Set();
  setA.forEach((v) => {
    if (setB.has(v)) {
      intersectionSet.add(v);
    }
  });
  return intersectionSet;
};

// 差集
const difference = (setA, setB) => {
  const differenceSet = new Set();
  setA.forEach((v) => {
    if (!setB.has(v)) {
      differenceSet.add(v);
    }
  });
  return differenceSet;
};

// 测试
const setAA = new Set();
setAA.add(1);
setAA.add(2);
setAA.add(3);

const setBB = new Set();
setBB.add(2);
setBB.add(3);
setBB.add(4);

console.log(union(setAA, setBB)); // Set { 1, 2, 3, 4 }
console.log(intersection(setAA, setBB)); // Set { 2, 3 }
console.log(difference(setAA, setBB)); // Set { 1 }
```

### 2 使用扩展运算符实现

```js
// 并集
console.log(new Set([...setAA, ...setBB])); // Set { 1, 2, 3, 4 }
// 交集
console.log(new Set([...setAA].filter((x) => setBB.has(x)))); // Set { 2, 3 }
// 差集
console.log(new Set([...setAA].filter((x) => !setBB.has(x)))); // Set { 1 }
```

在数学中，有一个叫作多重集的概念，它允许我们向集合中插入之前已经添加过的元素。

多重集（或袋）在计算集合中元素的出现次数时很有用。它也在数据库系统中得到了广泛运用。
