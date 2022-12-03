<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [链表 (Linked List）](#%E9%93%BE%E8%A1%A8-linked-list)
  - [链表基础说明](#%E9%93%BE%E8%A1%A8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [链表的实现](#%E9%93%BE%E8%A1%A8%E7%9A%84%E5%AE%9E%E7%8E%B0)
- [双向链表 (Doubly Linked List）](#%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8-doubly-linked-list)
  - [双向链表基础说明](#%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [双向链表的实现](#%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8%E7%9A%84%E5%AE%9E%E7%8E%B0)
- [循环链表 (Circular Linked List）](#%E5%BE%AA%E7%8E%AF%E9%93%BE%E8%A1%A8-circular-linked-list)
  - [循环链表基础说明](#%E5%BE%AA%E7%8E%AF%E9%93%BE%E8%A1%A8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [循环链表的实现](#%E5%BE%AA%E7%8E%AF%E9%93%BE%E8%A1%A8%E7%9A%84%E5%AE%9E%E7%8E%B0)
- [有序链表 (Sorted Linked List）](#%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8-sorted-linked-list)
  - [有序链表基础说明](#%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [有序链表的实现](#%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8%E7%9A%84%E5%AE%9E%E7%8E%B0)
- [用链表实现栈(Stack)](#%E7%94%A8%E9%93%BE%E8%A1%A8%E5%AE%9E%E7%8E%B0%E6%A0%88stack)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 链表 (Linked List）

## 链表基础说明

- 定义:
  - 链表存储有序的元素集合，但不同于数组，链表中的元素在内存中并不是连续放置的。
  - 每个元素由一个存储元素本身的节点和一个指向下一个元素的引用（也称指针或链接）组成。
- 与数组:
  - 相对于传统的数组，链表的一个好处在于，添加或移除元素的时候不需要移动其他元素。
  - 然而，链表需要使用指针，因此实现链表时需要额外注意。
  - 在数组中，我们可以直接访问任何位置的任何元素，
  - 而要想访问链表中间的一个元素，则需要从起点（表头）开始迭代链表直到找到所需的元素。
- 基本方法:
  - push(element) ：向链表尾部添加一个新元素。
  - insert(element, position) ：向链表的特定位置插入一个新元素。
  - getElementAt(index) ：返回链表中特定位置的元素。如果链表中不存在这样的元素，则返回 undefined 。
  - remove(element) ：从链表中移除一个元素。
  - indexOf(element) ：返回元素在链表中的索引。如果链表中没有该元素则返回 -1 。
  - removeAt(position) ：从链表的特定位置移除一个元素。
  - isEmpty() ：如果链表中不包含任何元素，返回 true ，如果链表长度大于 0 则返回 false 。
  - size() ：返回链表包含的元素个数，与数组的 length 属性类似。
  - toString() ：返回表示整个链表的字符串。
    - 由于列表项使用了 Node 类，就需要重写继承自 JavaScript 对象默认的 toString 方法，让其只输出元素的值。
- 生活示例:
  - 康加舞队、寻宝游戏、火车

## 链表的实现

首先需要用到一个判等的方法，所以可以新建一个`utils.js`文件，用来存放共用方法。后续其他数据结构也要用到其他辅助工具类或方法。

文件名`utils.js`:

```js
// 相等
function defaultEquals(a, b) {
  return a === b;
}

// 导出
module.exports = {
  defaultEquals,
};
```

链表代码实现(可存到单独文件，命名为`1LinkedList.js`，方便后续导入使用)：

```js
const { defaultEquals } = require("../utils");

// 链表节点类（存储元素和指向下一个元素的引用）
class Node {
  constructor(element, next) {
    this.element = element;
    // 当一个 Node 实例被创建时，它的 next 指针总是 undefined 。
    // 这没问题，因为我们知道它会是链表的最后一项。
    // this.next = undefined;
    this.next = next;
  }
}

// 链表结构
class LinkedList {
  constructor(equalsFn = defaultEquals) {
    // 存储链表中的元素数量
    this.count = 0;
    // 由于链表是对待的,所以需要将第一个元素的引用保存下来
    this.head = undefined;
    // 要比较链表中的元素是否相等，我们需要使用一个内部调用的函数，名为 equalsFn
    this.equalsFn = equalsFn;
  }

  // 链表最后一个节点的下一个元素始终是 undefined 或 null 。

  // 1. 向链表尾部添加元素
  push(element) {
    // 实例化一个节点
    // 当一个 Node 实例被创建时，它的 next 指针总是 undefined 。
    // 这没问题，因为我们知道它会是链表的最后一项。
    const node = new Node(element);
    // 指向链表中当前项的变量
    let current;
    // 链表为空，添加的是第一个元素；
    if (this.head == null) {
      this.head = node;
    } else {
      // 链表不为空，向其追加元素。
      // 只有第一个元素的引用，因此需要循环访问列表，直到找到最后一项。
      current = this.head;
      while (current.next != null) {
        // 找到当前节点的下一个节点为null,说明当前节点就是链表尾端,最后一项
        current = current.next;
      }
      // 将其 next 赋为新元素，建立链接
      current.next = node;
    }
    // 节点添加成功,链表总数量+1
    this.count++;
  }

  // 2. 从链表特定位置移除一个元素（ removeAt ）
  removeAt(index) {
    // 检查越界值
    if (index >= 0 && index < this.count) {
      let current = this.head;

      // 移除第一项
      if (index === 0) {
        // 把头结点指向原节点的下一个节点即可(不要去想原节点会怎样,该节点就会被丢弃在计算机内存中，等着被垃圾回收器清除。)
        this.head = current.next; // 也可以直接把 head 赋为 head.next,因为后面用到了current变量,所以没有这么做
      } else {
        /*
                // 记录前一个节点的变量
                let previous;
                // 要移除链表的最后一个或者中间某个元素。为此，需要迭代链表的节点，直到到达目标位置
                // 一个重要细节是： current 变量总是为对所循环列表的当前元素的引用(初始是指定的head,所以才跌代到指定位置)。
                // 我们还需要一个对当前元素的前一个元素的引用，它被命名为 previous。 
                for (let i = 0; i < index; i++) {
                    previous = current;
                    // 迭代到目标位置之后， current 变量会持有我们想从链表中移除的节点()
                    current = current.next;
                }
                // 将 previous 与 current 的下一项链接起来：跳过 current，从而移除它 (前一个的下一个是当前的下一个,当前就被跳过了)
                // 该节点就会被丢弃在计算机内存中，等着被垃圾回收器清除。
                previous.next = current.next;
                */

        // 使用getElementAt()重构
        const previous = this.getElementAt(index - 1);
        current = previous.next;
        previous.next = current.next;
      }
      //移除成功,链表总数量-1
      this.count--;
      // 将被移除的节点的元素返回
      return current.element;
    }
    // 如果传入的值超过链表大小(不是链表有效位置),直接返回undefined
    return undefined;
  }

  // 3. 循环迭代链表直到目标位置(返回链表指定位置的节点)
  getElementAt(index) {
    if (index >= 0 && index <= this.count) {
      // 声明变量指定第一个节点
      // 初始化 node 变量，该变量会从链表的第一个元素 head开始，迭代整个链表。
      let current = this.head;
      // 遍历,得到需要获取元素的节点
      for (let i = 0; i < index && current != null; i++) {
        current = current.next;
      }
      // 返回指定节点
      return current;
    }
    // 无效位置返回undefined
    return undefined;
  }

  // 4. 在任意位置插入元素
  /*
    tip 使用变量引用我们需要控制的节点非常重要，这样就不会丢失节点之间的链接。
    我们可以只使用一个变量（ previous ），但那样会很难控制节点之间的链接。  
    因此，最好声明一个额外的变量来帮助我们处理这些引用。 
    */
  insert(element, index) {
    if (index >= 0 && index <= this.count) {
      const node = new Node(element);
      // 在第一个位置添加
      if (index === 0) {
        // current 变量是对链表中第一个元素的引用。
        const current = this.head;
        // 把 node.next 的值设为 current （链表中第一个元素，或简单地设为 head ）。
        node.next = current;
        // 现在 head 和 node.next 都指向了 current 。接下来把 head 的引用改为 node ,这样链表中就有了一个新元素。
        this.head = node;
      } else {
        // 记录前一个节点
        const previous = this.getElementAt(index - 1);
        // 记录原本的当前节点
        const current = previous.next;
        // node就是新的当前节点,原本的当前节点变为新节点的下一个
        node.next = current;
        // 前一个节点的下一个就是新的当前节点
        previous.next = node;
      }
      // 更新链表长度
      this.count++;
      // 插入成功
      return true;
    }
    // 指定位置无效,插入返回 false
    return false;
  }

  // 5. indexOf 方法：返回一个元素的位置
  indexOf(element) {
    // 需要一个变量来帮助循环访问列表。的初始值是 head
    let current = this.head;
    for (let i = 0; i < this.count && current != null; i++) {
      // 在每次迭代时，将验证 current 节点的元素和目标元素是否相等,相等返回位置,不等遍历下一个节点
      if (
        this.equalsFn(
          element,
          current.element /**或者直接用 element === current.element */
        )
      ) {
        return i;
      }
      current = current.next;
    }
    return -1;
  }

  // 6. 从链表中移除元素
  remove(element) {
    // 找到指定元素位置
    const index = this.indexOf(element);
    // 移除该位置节点,
    return this.removeAt(index);
  }

  // toString 方法
  toString() {
    if (this.head == null) {
      return "";
    }
    let objStr = `${this.head.element}`;
    let current = this.head.next;
    for (let i = 1; i < this.size() && current != null; i++) {
      objStr = `${objStr},${current.element}`;
      current = current.next;
    }
    return objStr;
  }

  size() {
    return this.count;
  }

  isEmpty() {
    return this.size() === 0;
  }

  getHead() {
    return this.head;
  }

  clear() {
    this.head = undefined;
    this.count = 0;
  }
}

// 导出节点(其他类型的链表也会用到Node类)和链表
module.exports = {
  Node,
  LinkedList,
};
```

使用测试：

```js
// 使用示例
const list = new LinkedList();
list.push(1);
list.push(2);
list.push(3);
console.log(list);
/* 上面输出
LinkedList {
  count: 3,
  head: Node { element: 1, next: Node { element: 2, next: [Node] } },
  equalsFn: [Function]
}
*/
console.log(list.getElementAt(1)); // Node { element: 2, next: Node { element: 3, next: undefined } }
console.log(list.removeAt(1)); // 2
list.push(4);
list.push(5);
list.push(6);
console.log(list.remove(4)); // 4
console.log(list.indexOf(3)); // 1
console.log(list.size()); // 4
console.log(list.insert(7, 3)); // true
console.log(list.insert(7, 10)); // false
console.log(list.toString()); // 1,3,5,7,6
console.log(list.isEmpty()); // false
console.log(list.size()); // 5
console.log(list.getHead());
/*
Node {
  element: 1,
  next: Node { element: 3, next: Node { element: 5, next: [Node] } }
}
*/
```

# 双向链表 (Doubly Linked List）

## 双向链表基础说明

- 定义:
  - 双向链表和普通链表的区别在于，在链表中，一个节点只有链向下一个节点的链接；
  - 而在双向链表中，链接是双向的：一个链向下一个元素，另一个链向前一个元素.
- 双向链表提供了两种迭代的方法：从头到尾，或者从尾到头。
  - 在单向链表中，如果迭代时错过了要找的元素，就需要回到起点，重新开始迭代。这是双向链表的一个优势。

## 双向链表的实现

双向链表代码实现(可存到单独文件，命名为`2DoublyLinkedList.js`，方便后续导入使用)：

```js
const { LinkedList, Node } = require("./1LinkedList");
const { defaultEquals } = require("../utils");

// 双向链表的节点结构
class DoublyNode extends Node {
  constructor(element, next, prev) {
    super(element, next);
    // 一个特定节点前一个元素。
    this.prev = prev;
  }
}

// 双向链表类
class DoublyLinkedList extends LinkedList {
  constructor(equalsFn = defaultEquals) {
    // 调用 LinkedList 的构造函数，它会初始化 count 和 head 属性。
    // 不使用equalsFn,简单比较直接使用表达式
    super(equalsFn);
    // 保存对链表最后一个元素的引用
    this.tail = undefined;
  }

  push(element) {
    const node = new DoublyNode(element);
    if (this.head == null) {
      this.head = node;
      this.tail = node; // NEW
    } else {
      // attach to the tail node // NEW
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.count++;
  }

  // 向任意位置插入一个新元素的算法。
  insert(element, index) {
    if (index >= 0 && index <= this.count) {
      const node = new DoublyNode(element);
      let current;
      // 如果插入的是首位置
      if (index === 0) {
        // 如果头引用为空
        if (this.head == null) {
          // 空链表,首位节点都是新插入的这一个
          this.head = node;
          this.tail = node;
        } else {
          // 如果不是空链表
          current = this.head;
          //新加节点为head,它执行的下一个节点就是原本的head
          node.next = this.head;
          // current存的是原本的head,现在是第二个节点,它的前一个就是新加的节点
          current.prev = node;
          // 在构造函数已经完成
          // node.prev=undefined
          // 当前的head就是新加的节点
          this.head = node;
        }
      } else if (index == this.count) {
        // 如果是尾部插入
        // 存储原本的尾节点
        current = this.tail;
        // 原尾节点的下一个节点就是新加的节点
        current.next = node;
        //新节点的前一个节点就是原本的尾节点
        node.prev = current;
        // 在构造函数已经完成
        // node.next=undefined
        // 新的尾节点就是新加的节点
        this.tail = node;
      } else {
        // 不是加在首位,就是加在中间
        // 取得指定位置的原本节点的前一个
        const previous = this.getElementAt(index - 1);
        // 原本的当前节点就是原本节点的前一个节点的后一个
        current = previous.next;
        // 新的当前节点是新加的节点,它的后一个节点就是原本的当前节点
        node.next = current;
        // 原本前一个节点的后一个节点现在是新的当前节点
        previous.next = node;
        // 原本节点的前一个节点也就是新的当前节点
        current.prev = node;
        // 新的当前节点的前一个节点依旧是原本的前一个节点
        node.prev = previous;
      }
      // 插入成功,链表长度+1,返回true
      this.count++;
      return true;
    }
    // 不在链表范围内
    return false;
  }

  // 从任意位置移除元素
  removeAt(index) {
    if (index >= 0 && index < this.count) {
      let current;
      // 如果是移除第一项
      if (index === 0) {
        current = this.head;
        this.head = current.next;
        // 如果只有一项,需要更新tail
        if (this.count === 1) {
          this.tail = undefined;
        } else {
          this.head.prev = undefined;
        }
      } else if (index === this.count - 1) {
        // 如果是移除最后一项
        current = this.tail;
        this.tail = current.prev;
        this.tail.next = undefined;
      } else {
        // 移除的是中间的
        // 需要被移除的节点
        current = this.getElementAt(index);
        // 前一个节点是将要被移除的节点的前一个
        const previous = current.prev;
        // 前一个节点的下一个节点为将要被移除节点的下一个
        previous.next = current.next;
        // 将要被移除的节点的后一个节点的前一个节点,现在为将要被移除节点的前一个节点
        current.next.prev = previous;
      }
      // 移除成功长度-1,返回true
      this.count--;
      return current.element;
    }
    return undefined;
  }

  indexOf(element) {
    let current = this.head;
    let index = 0;
    while (current != null) {
      if (this.equalsFn(element, current.element)) {
        return index;
      }
      index++;
      current = current.next;
    }
    return -1;
  }

  getHead() {
    return this.head;
  }

  getTail() {
    return this.tail;
  }

  clear() {
    super.clear();
    this.tail = undefined;
  }

  toString() {
    if (this.head == null) {
      return "";
    }
    let objString = `${this.head.element}`;
    let current = this.head.next;
    while (current != null) {
      objString = `${objString},${current.element}`;
      current = current.next;
    }
    return objString;
  }

  inverseToString() {
    if (this.tail == null) {
      return "";
    }
    let objString = `${this.tail.element}`;
    let previous = this.tail.prev;
    while (previous != null) {
      objString = `${objString},${previous.element}`;
      previous = previous.prev;
    }
    return objString;
  }
}

// 导出
module.exports = {
  DoublyNode,
  DoublyLinkedList,
};
```

使用测试：

```js
// 双向链表使用示例
let dlist = new DoublyLinkedList();

dlist.insert(1, 0);
dlist.insert(2, 1);
dlist.insert(3, 2);
dlist.insert(5, 1);
console.log(dlist.toString()); // 输出:1,5,2,3
dlist.removeAt(2); // 移除第三个节点
console.log(dlist.toString()); // 输出:1,5,3
dlist.push(6);
console.log(dlist.indexOf(3)); // 2
console.log(dlist.getHead());
/*
DoublyNode {
  element: 1,
  next: DoublyNode {
    element: 5,
    next: DoublyNode { element: 3, next: [DoublyNode], prev: [Circular] },
    prev: [Circular]
  },
  prev: undefined
}
*/
console.log(dlist.getTail());
/*
DoublyNode {
  element: 6,
  next: undefined,
  prev: DoublyNode {
    element: 3,
    next: [Circular],
    prev: DoublyNode { element: 5, next: [Circular], prev: [DoublyNode] }
  }
}
*/
console.log(dlist.getElementAt(2));
/*
DoublyNode {
  element: 3,
  next: DoublyNode { element: 6, next: undefined, prev: [Circular] },
  prev: DoublyNode {
    element: 5,
    next: [Circular],
    prev: DoublyNode { element: 1, next: [Circular], prev: undefined }
  }
}
*/
console.log(dlist.toString()); // 1,5,3,6
console.log(dlist.inverseToString()); // 6,3,5,1
```

# 循环链表 (Circular Linked List）

## 循环链表基础说明

- 定义:
  - 循环链表可以像链表一样只有单向引用，也可以像双向链表一样有双向引用。
- 循环链表和链表之间唯一的区别在于，最后一个元素指向下一个元素的指针(tail.next)不是引用 undefined,而是指向第一个元素(head);
  - 双向循环链表有指向 head 元素的 tail.next 和指向 tail 元素的 head.prev 。

## 循环链表的实现

```js
const { LinkedList, Node } = require("./1LinkedList");
const { defaultEquals } = require("../utils");

class CircularLinkedList extends LinkedList {
  // 不需要额外的属性
  constructor(equalsFn = defaultEquals) {
    super(equalsFn);
  }

  // 在任意位置插入新元素
  insert(element, index) {
    if (index >= 0 && index <= this.count) {
      const node = new Node(element);
      let current;
      // 如果插在头部
      if (index === 0) {
        // 如果原为空链表
        if (this.head === null) {
          this.head = node;
          // 单个节点,自己指向自己
          node.next = this.head;
        } else {
          // 新插入的节点为头节点,所以原头结点变为新头结点的next
          current = this.head;
          node.next = current;
          // 将尾节点赋值给current
          current = this.getElementAt(this.size());
          // 新传入节点为新的头结点
          this.head = node;
          // 尾节点的next指向头结点
          current.next = this.head;
        }
      } else {
        // 未插在头部
        // 记录需要插入节点的前一个节点
        const previous = this.getElementAt(index - 1);
        // 新节点的后一个就是原本位置的节点(即原节点前一个节点的后一个)
        node.next = previous.next;
        // 新节点的前一个就是原节点的前一个
        previous.next = node;
      }
      this.count++;
      return true;
    }
    return false;
  }

  // 从任意位置移除元素
  removeAt(index) {
    if (index >= 0 && index < this.count) {
      let current;
      // 如果删除头结点
      if (index === 0) {
        // 如果只有一个节点
        if (this.size() === 1) {
          this.head = undefined;
        } else {
          // 记录将要被移除的原头结点(用于返回)
          const removed = this.head;
          // 记录原本的尾节点(书上有错,总数-1才是尾节点的索引)
          current = this.getElementAt(this.size() - 1);
          // 新的头结点就是原本头结点的后一个
          this.head = this.head.next;
          // 尾节点的next指向新的头结点
          current.next = this.head;
          // 把被移除的节点赋值给current,供外部返回
          current = removed;
        }
      } else {
        // 删除中间的节点,就只需把被删除的前一个节点的next指向被删除节点的next
        const previous = this.getElementAt(index - 1);
        current = previous.next;
        previous.next = current.next;
      }
      // 删除成功,长度-1
      this.count--;
      return current.element;
    }
    return undefined;
  }

  push(element) {
    const node = new Node(element);
    let current;
    if (this.head == null) {
      this.head = node;
    } else {
      current = this.getElementAt(this.size() - 1);
      current.next = node;
    }
    // set node.next to head - to have circular list
    node.next = this.head;
    this.count++;
  }
}

// 导出
module.exports = {
  CircularLinkedList,
};
```

# 有序链表 (Sorted Linked List）

## 有序链表基础说明

- 定义:
  - 有序链表是指保持元素有序的链表结构。
- 除了使用排序算法之外，我们还可以将元素插入到正确的位置来保证链表的有序性。

## 有序链表的实现

首先，需要一些新的工具，在`utils.js`加入

```js
// 比较结果
const Compare = {
  LESS_THAN: -1,
  BIGGER_THAN: 1,
  EQUALS: 0,
};

// 默认的比较方法
function defaultCompare(a, b) {
  if (a === b) {
    return Compare.EQUALS;
  }
  return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
}

// 现在导出
module.exports = {
  defaultEquals,
  Compare, // +
  defaultCompare, // +
};
``;
```

有序链表的实现：

```js
const { LinkedList } = require("./1LinkedList");
const { Compare, defaultCompare, defaultEquals } = require("../utils");

// // 排序使用到的比较结果
// const Compare = {
//     LESS_THAN: -1,
//     BIGGER_THAN: 1
// }
// // 预设的比较函数
// function defaultCompare(a, b) {
//     if (a === b) {
//         return 0;
//     }
//     return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
// }

// 有序链表类
class SortedLinkedList extends LinkedList {
  /*
    SortedLinkedList 类会从 LinkedList 类中继承所有的属性和方法，
    但是由于这个类有特别的行为，我们需要一个用来比较元素的函数。因此，还需要声明 compareFn，用来比较元素。
    该函数会默认使用 defaultCompare 。
    如果用于比较的元素更复杂一些，我们可以创建自定义的比较函数并将它传入 SortedLinkedList 类的构造函数中。
    */
  constructor(equalsFn = defaultEquals, compareFn = defaultCompare) {
    super(equalsFn);
    this.equalsFn = equalsFn;
    this.compareFn = compareFn;
  }

  push(element) {
    if (this.isEmpty()) {
      super.push(element);
    } else {
      const index = this.getIndexNextSortedElement(element);
      super.insert(element, index);
    }
  }

  // 有序插入元素
  // 不想允许在任何位置插入元素，我们要给 index 参数设置一个默认值
  insert(element, index = 0) {
    // 因为插入元素的位置是内部控制的。我们这么做的原因是不想重写整个LinkedList 类的方法，
    // 我们只需要覆盖 insert 方法的行为。

    // 如果有序链表为空，我们可以直接调用 LinkedList 的 insert 方法并传入 0 作为 index
    // 如果有序链表不为空，我们会知道插入元素的正确位置并调用 LinkedList的 insert 方法，传入该位置来保证链表有序
    if (this.isEmpty()) {
      // 有传位置的话以传位置的为准(书上没改)
      return super.insert(element, index === 0 ? index : 0);
    }
    const pos = this.getIndexNextSortedElement(element);
    return super.insert(element, pos);
  }

  // 找到有序链表插入的正确位置
  getIndexNextSortedElement(element) {
    // 迭代整个有序链表直至找到需要插入元素的位置，或是迭代完所有的元素。
    let current = this.head;
    let i = 0;
    for (; i < this.size() && current; i++) {
      const comp = this.compareFn(element, current.element);
      if (comp === Compare.LESS_THAN) {
        return i;
      }
      current = current.next;
    }
    return i;
  }
}

// 导出
module.exports = {
  SortedLinkedList,
};
```

# 用链表实现栈(Stack)

还可以使用 LinkedList 类及其变种作为内部的数据结构来创建其他数据结构，例如栈、队列和双向队列。

此示例为用链表实现 Stack:

```js
const { DoublyLinkedList } = require("./2DoublyLinkedList");

class StackLinkedList {
  constructor() {
    this.items = new DoublyLinkedList();
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items.removeAt(this.size() - 1);
  }

  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items.getElementAt(this.size() - 1).element;
  }
  isEmpty() {
    return this.items.isEmpty();
  }
  size() {
    return this.items.size();
  }
  clear() {
    this.items.clear();
  }
  toString() {
    return this.items.toString();
  }
}

module.exports = {
  StackLinkedList,
};
```
