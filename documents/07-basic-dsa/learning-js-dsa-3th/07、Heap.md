<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [堆(Heap) 也叫作 二叉堆](#%E5%A0%86heap-%E4%B9%9F%E5%8F%AB%E4%BD%9C-%E4%BA%8C%E5%8F%89%E5%A0%86)
  - [堆基础说明](#%E5%A0%86%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [类的实现](#%E7%B1%BB%E7%9A%84%E5%AE%9E%E7%8E%B0)
    - [最小堆类的实现](#%E6%9C%80%E5%B0%8F%E5%A0%86%E7%B1%BB%E7%9A%84%E5%AE%9E%E7%8E%B0)
    - [最大堆类的实现](#%E6%9C%80%E5%A4%A7%E5%A0%86%E7%B1%BB%E7%9A%84%E5%AE%9E%E7%8E%B0)
  - [堆排序算法](#%E5%A0%86%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 堆(Heap) 也叫作 二叉堆

## 堆基础说明

- 定义:
  - 是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵完全二叉树的数组对象。
- 特征:
  - 1 堆不是最小堆就是最大堆；
    - 所有的节点都大于等于（最大堆）或小于等于（最小堆）每个它的子节点。这叫作堆特性。
  - 2 堆总是一棵完全二叉树。
    - 表示树的每一层都有左侧和右侧子节点（除了最后一层的叶节点），并且最后一层的叶节点尽可能都是左侧子节点，这叫作结构特性。
- 完全二叉树:
  - 一棵深度为 k 的有 n 个结点的二叉树，对树中的结点按从上至下、从左到右的顺序进行编号，
  - 如果编号为 i（1≤i≤n）的结点与满二叉树中编号为 i 的结点在二叉树中的位置相同，则这棵二叉树称为完全二叉树。
- 注意:
  - 尽管二叉堆是二叉树，但并不一定是二叉搜索树（BST）。
  - 在二叉堆中，每个子节点都要大于等于父节点（最小堆）或小于等于父节点（最大堆）。
  - 然而在二叉搜索树中，左侧子节点总是比父节点小，右侧子节点也总是更大。
- 主要操作:
  - insert(value) ：这个方法向堆中插入一个新的值。如果插入成功，它返回 true ，否则返回 false 。
  - extract() ：这个方法移除最小值（最小堆）或最大值（最大堆），并返回这个值。
  - findMinimum() ：这个方法返回最小值（最小堆）或最大值（最大堆）且不会移除这个值。

## 类的实现

### 最小堆类的实现

首先，需要一些新的工具函数，在`utils.js`加入新方法并导出:

```js
// 翻转比较
function reverseCompare(compareFn) {
  return (a, b) => compareFn(b, a);
}

// 数组内指定索引两个数的交换
function swap(array, a, b) {
  /* const temp = array[a];
  array[a] = array[b];
  array[b] = temp; */
  [array[a], array[b]] = [array[b], array[a]];
}

module.exports = {
  reverseCompare,
  swap,
  // ...
};
```

最小堆的实现代码：

```js
const { Compare, reverseCompare, defaultCompare, swap } = require("../util");

class MinHeap {
  constructor(compareFn = defaultCompare) {
    this.compareFn = compareFn;
    // 会使用数组来存储数据
    this.heap = [];
  }

  /* 二叉树有两种表示方式。
    // 第一种是使用一个动态的表示方式，也就是指针（用节点表示）。
                 1  (0)
               /   \
        (2)  2      3 (3)
            / \     /  \
       (3) 4  5(4) 6(5) 7 (6)
    
    // 第二种是使用一个数组，通过索引值检索父节点、左侧和右侧子节点的值。
    ┌────┬────┬────┬────┬────┬────┬────┐
    │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │
    └────┴────┴────┴────┴────┴────┴────┘
     (0)  (1)  (2)  (3)  (4)  (5)  (6)
    
    要访问使用普通数组的二叉树节点，我们可以用下面的方式操作 index 。 
    对于给定位置 index 的节点： 
     它的左侧子节点的位置是 2 * index + 1 （如果位置可用）； 
     它的右侧子节点的位置是 2 * index + 2 （如果位置可用）； 
     它的父节点位置是 index / 2 （如果位置可用）。 
    */

  // 获取左节点位置
  getLeftIndex(index) {
    return 2 * index + 1;
  }
  // 获取右节点位置
  getRightIndex(index) {
    return 2 * index + 2;
  }
  // 获取父节点位置
  getParentIndex(index) {
    if (index === 0) {
      return undefined;
    }
    return Math.floor((index - 1) / 2);
  }

  // 2. 向堆中插入值
  // 向堆中插入值是指将值插入堆的底部叶节点（数组的最后一个位置）再执行siftUp 方法，
  // 表示我们将要将这个值和它的父节点进行交换，直到父节点小于这个插入的值。
  // 这个上移操作也被称为 up head、percolate up、bubble up、heapify up 或 cascade up。
  insert(value) {
    if (value != null) {
      // 把值添加到堆的底部叶子节点
      this.heap.push(value);
      // 执行shftUp(),调整节点的正确位置
      this.siftUp(this.heap.length - 1);
      return true;
    }
    return false;
  }

  // 上移操作(将指定索引的值与其父节点值比较,如果小(最小堆),则交换两者位置)
  // siftUp 方法接收插入值的位置作为参数。
  siftUp(index) {
    // 需要获取其父节点的位置
    let parent = this.getParentIndex(index);
    // 注意,书上有错,应该是===判断的大小,书上是 >
    while (
      index > 0 &&
      this.compareFn(this.heap[parent], this.heap[index]) ===
        Compare.BIGGER_THAN
    ) {
      // 新叶子节点值小于其父节点,将两者交换
      swap(this.heap, parent, index);
      // 新要进行处理的节点索引为原父节点的索引
      index = parent;
      // 新的父节点为原父节点的父节点(一直往上比较交换,直到符合条件)
      // 重复这个过程直到堆的根节点也经过了交换节点和父节点位置的操作
      parent = this.getParentIndex(index);
    }
  }

  // 3. 从堆中找到最小值或最大值
  // 在最小堆中，最小值总是位于数组的第一个位置（堆的根节点）,最大堆同理。
  size() {
    return this.heap.length;
  }
  isEmpty() {
    return this.size() === 0;
  }
  findMinimum() {
    return this.isEmpty() ? undefined : this.heap[0];
  }
  clear() {
    this.heap = [];
  }

  // 4. 导出堆中的最小值或最大值(从堆中移除根节点,并将剩下的构建一个新的堆)
  // 移除最小值（最小堆）或最大值（最大堆）表示移除数组中的第一个元素（堆的根节点）。
  // 在移除后，我们将堆的最后一个元素移动至根部并执行 siftDown 函数，表示我们将交换元素直到堆的结构正常。
  // 这个下移操作也被称为 sink down、percolate down、bubble down、heapify down或 cascade down。
  extract() {
    // 如果堆为空，也就是没有值可以导出，返回 undefined
    if (this.isEmpty()) {
      return undefined;
    }
    // 如果堆中只有一个值，直接移除并返回它
    if (this.size() === 1) {
      return this.heap.shift();
    }
    // 如果堆中有不止一个值，将第一个值移除，存储到一个临时变量中以便在执行完下移操作后返回它
    const removedValue = this.heap[0];
    // 在移除后，我们将堆的最后一个元素移动至根部并执行 siftDown 函数
    this.heap[0] = this.heap.pop();
    this.siftDown(0);
    return removedValue;
  }
  // 下移操作（堆化）
  // siftDown 方法接收移除元素的位置作为参数。
  siftDown(index) {
    // 将 index 复制到 element 变量中。同样要获取左侧子节点和右侧子节点的值。
    let element = index;
    const left = this.getLeftIndex(index);
    const right = this.getRightIndex(index);
    const size = this.size();

    // 如果元素比左侧子节点要小（且 index 合法），我们就交换元素和它的左侧子节点。
    if (
      left < size &&
      this.compareFn(this.heap[element], this.heap[left]) ===
        Compare.BIGGER_THAN
    ) {
      element = left;
    }
    // 如果元素小于它的右侧子节点（且 index 合法），我们就交换元素和它的右侧子节点。
    if (
      right < size &&
      this.compareFn(this.heap[element], this.heap[right]) ===
        Compare.BIGGER_THAN
    ) {
      element = right;
    }

    // 在找到最小子节点的位置后，检验它的值是否和 element 相同（传入 siftDown 方法——和自己交换是没有意义的！
    // 如果不是，就将它和最小的 element 交换，并且重复这个过程直到 element 被放在正确的位置上。
    if (index !== element) {
      swap(this.heap, index, element);
      this.siftDown(element);
    }
  }

  // heapify 函数和我们创建的 siftDown 方法有相同的代码。
  // 不同之处是我们会将堆本身、堆的大小和要使用的比较函数传入作为参数。
  // 这是因为我们不会直接使用堆数据结构，而是使用它的逻辑来开发 heapSort 算法。
  heapify(array) {
    if (array) {
      this.heap = array;
    }
    const maxIndex = Math.floor(this.size() / 2) - 1;
    for (let i = 0; i <= maxIndex; i++) {
      this.siftDown(i);
    }
    return this.heap;
  }

  getAsArray() {
    return this.heap;
  }
}
module.exports = {
  MinHeap,
};
```

### 最大堆类的实现

MaxHeap 类的算法和 MinHeap 类的算法一模一样。不同之处在于我们要把所有 > （大于）的比较换成 < （小于）的比较。

```js
// 创建最大堆类
// MaxHeap 类的算法和 MinHeap 类的算法一模一样。不同之处在于我们要把所有 > （大于）的比较换成 < （小于）的比较。
class MaxHeap extends MinHeap {
  constructor(compareFn = defaultCompare) {
    super(compareFn);
    // 在需要时进行反向的比较。要将比较反转，不将 a 和 b 进行比较，而是将 b 和 a 进行比较
    this.compareFn = reverseCompare(compareFn);
  }
}
module.exports = {
  MaxHeap,
};
```

测试使用：

```js
// 测试最小堆
const heap = new MinHeap();

heap.insert(2);
heap.insert(3);
heap.insert(4);
heap.insert(5);
heap.insert(1);

console.log(heap);
/*
MinHeap {
  compareFn: [Function: defaultCompare],
  heap: [ 1, 2, 4, 5, 3 ]
}
因为:
     它的左侧子节点的位置是 2 * index + 1 （如果位置可用）；
     它的右侧子节点的位置是 2 * index + 2 （如果位置可用）；
     它的父节点位置是 index / 2 （如果位置可用）。
上最小堆即:
            1
           / \
          2   4
         / \
        5   3

*/
console.log("Heap size: ", heap.size()); // Heap size:  5
console.log("Heap is empty: ", heap.isEmpty()); // Heap is empty:  false
console.log("Heap min value: ", heap.findMinimum()); // Heap min value:  1

// 测试移除最小值
heap2 = new MinHeap();
for (let i = 1; i < 10; i++) {
  heap2.insert(i);
}
console.log(heap2);
/*
MinHeap {
  compareFn: [Function: defaultCompare],
  heap: [
    1, 2, 3, 4, 5,
    6, 7, 8, 9
  ]
}
*/
console.log("Extract minimum: ", heap2.extract()); // Extract minimum:  1
console.log(heap2);
/*
MinHeap {
  compareFn: [Function: defaultCompare],
  heap: [
    2, 4, 3, 8,
    5, 6, 7, 9
  ]
}
*/
/*
从 heap: [1, 2, 3, 4, 5, 6, 7, 8, 9]
            1
          /   \
        2       3
       / \     / \
      4   5   6   7
     / \
    8   9
变为 heap: [2, 3, 4, 5, 6, 7, 8, 9]
            2
          /   \
        4       3
       / \     / \
      8   5   6   7
     / 
    9  
*/

// 测试最大堆
const maxHeap = new MaxHeap();

maxHeap.insert(2);
maxHeap.insert(3);
maxHeap.insert(4);
maxHeap.insert(5);
maxHeap.insert(1);

console.log("Heap size: ", maxHeap.size()); // Heap size:  5
console.log("Heap min value: ", maxHeap.findMinimum()); // Heap min value:  5
console.log(maxHeap); // MaxHeap { compareFn: [Function (anonymous)], heap: [ 5, 4, 3, 2, 1 ] }
console.log(maxHeap.extract()); // 5
console.log(maxHeap); // MaxHeap { compareFn: [Function (anonymous)], heap: [ 4, 2, 3, 1 ] }
```

## 堆排序算法

- 它包含下面三个步骤：
  - (1) 用数组创建一个最大堆用作源数据。
  - (2) 在创建最大堆后，最大的值会被存储在堆的第一个位置。我们要将它替换为堆的最后一个值，将堆的大小减 1
    - (每次堆大小-1 就是存放排好序的值,直到堆大小为 1 之后,全部排完)。
  - (3) 最后，我们将堆的根节点下移并重复步骤 2 直到堆的大小为 1。
- 用最大堆得到一个升序排列的数组（从最小到最大）。想要这个数组按降序排列，可以用最小堆代替。

代码实现：

```js
onst { defaultCompare, swap } = require('../utils');

// 要构建最大堆，可以使用下面的函数
function buildMaxHeap(array, compareFn) {
    for (let i = Math.floor(array.length / 2); i >= 0; i -= 1) {
        heapify(array, i, array.length, compareFn);
    }
    return array;
}

// heapify 函数和我们创建的 siftDown 方法有相同的代码。
// 不同之处是我们会将堆本身、堆的大小和要使用的比较函数传入作为参数。
// 这是因为我们不会直接使用堆数据结构，而是使用它的逻辑来开发 heapSort 算法。
function heapify(array, index, heapSize, compareFn) {
    let largest = index;
    const left = (2 * index) + 1;
    const right = (2 * index) + 2;
    if (left < heapSize && compareFn(array[left], array[index]) > 0) {
        largest = left;
    }
    if (right < heapSize && compareFn(array[right], array[largest]) > 0) {
        largest = right;
    }
    if (largest !== index) {
        swap(array, index, largest);
        heapify(array, largest, heapSize, compareFn);
    }
}

function heapSort(array, compareFn = defaultCompare) {
    let heapSize = array.length;
    buildMaxHeap(array, compareFn); // 步骤 1
    while (heapSize > 1) {
        // 最大堆函数会重新组织数组的顺序。
        // 归功于要进行的所有比较，我们只需要对后半部分数组执行 heapify （下移）函数
        // （前半部分会被自动排好序，所以不需要对已经知道排好序的部分执行函数）。
        swap(array, 0, --heapSize); // 步骤 2
        heapify(array, 0, heapSize, compareFn); // 步骤 3
    }
    return array;
}

// 堆排序测试：
const array = [7, 6, 3, 5, 4, 1, 2];

console.log('Before sorting: ', array); // Before sorting: [7, 6, 3, 5, 4, 1, 2 ]
console.log('After sorting: ', heapSort(array)); // After sorting: [1, 2, 3, 4, 5, 6, 7 ]
```
