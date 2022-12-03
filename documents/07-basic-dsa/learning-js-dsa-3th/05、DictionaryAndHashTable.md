<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [字典 (Dictionary) 其实就是 Map](#%E5%AD%97%E5%85%B8-dictionary-%E5%85%B6%E5%AE%9E%E5%B0%B1%E6%98%AF-map)
  - [字典基础说明](#%E5%AD%97%E5%85%B8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [实现 Dictionary](#%E5%AE%9E%E7%8E%B0-dictionary)
  - [WeakSet 和 WeakMap](#weakset-%E5%92%8C-weakmap)
- [散列表 (HashTable 类，也叫 HashMap 类)](#%E6%95%A3%E5%88%97%E8%A1%A8-hashtable-%E7%B1%BB%E4%B9%9F%E5%8F%AB-hashmap-%E7%B1%BB)
  - [散列表基础说明](#%E6%95%A3%E5%88%97%E8%A1%A8%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
  - [HashTable 的实现](#hashtable-%E7%9A%84%E5%AE%9E%E7%8E%B0)
- [处理散列表中的冲突](#%E5%A4%84%E7%90%86%E6%95%A3%E5%88%97%E8%A1%A8%E4%B8%AD%E7%9A%84%E5%86%B2%E7%AA%81)
  - [1 分离链接 (HashTable Separate Chaining)](#1-%E5%88%86%E7%A6%BB%E9%93%BE%E6%8E%A5-hashtable-separate-chaining)
    - [分离链接基础说明](#%E5%88%86%E7%A6%BB%E9%93%BE%E6%8E%A5%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
    - [实现分离链接](#%E5%AE%9E%E7%8E%B0%E5%88%86%E7%A6%BB%E9%93%BE%E6%8E%A5)
  - [2 线性探查](#2-%E7%BA%BF%E6%80%A7%E6%8E%A2%E6%9F%A5)
    - [线性探查基础说明](#%E7%BA%BF%E6%80%A7%E6%8E%A2%E6%9F%A5%E5%9F%BA%E7%A1%80%E8%AF%B4%E6%98%8E)
    - [线性探查的实现](#%E7%BA%BF%E6%80%A7%E6%8E%A2%E6%9F%A5%E7%9A%84%E5%AE%9E%E7%8E%B0)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 字典 (Dictionary) 其实就是 Map

## 字典基础说明

- 在字典中，存储的是[键，值]对，其中键名是用来查询特定元素的,键名不可重复。
- 字典也称作映射、符号表或关联数组。
- 常用方法:
  - set(key,value) ：向字典中添加新元素。如果 key 已经存在，那么已存在的 value 会被新的值覆盖。
  - remove(key) ：通过使用键值作为参数来从字典中移除键值对应的数据值。
  - hasKey(key) ：如果某个键值存在于该字典中，返回 true ，否则返回 false 。
  - get(key) ：通过以键值作为参数查找特定的数值并返回。
  - clear() ：删除该字典中的所有值。
  - size() ：返回字典所包含值的数量。与数组的 length 属性类似。
  - isEmpty() ：在 size 等于零的时候返回 true ，否则返回 false 。
  - keys() ：将字典所包含的所有键名以数组形式返回。
  - values() ：将字典所包含的所有数值以数组形式返回。
  - keyValues() ：将字典中所有[键，值]对返回。
  - forEach(callbackFn) ：迭代字典中所有的键值对。 callbackFn 有两个参数： key 和 value 。
    - 该方法可以在回调函数返回 false 时被中止（和 Array 类中的 every 方法相似）。
- 应用场景:
  - 字典经常用来保存对象的引用地址。

## 实现 Dictionary

首先需要一个转换字符串的方法。在`utils.js`加入一个新方法并导出:

```js
// 转换为字符串方法
function defaultToString(item) {
  if (item === null) {
    return "NULL";
  }
  if (item === undefined) {
    return "UNDEFINED";
  }
  if (typeof item === "string" || item instanceof String) {
    return `${item}`;
  }
  return item.toString();
  // 如果 item 变量是一个对象的话，它需要实现 toString 方法，
  // 否则会导致出现异常的输出结果，如 [object Object] 。这对用户是不友好的。
}

module.exports = {
  defaultToString,
  // ...
};
```

字典代码实现(可存到单独文件，命名为`1Dictionary.js`，方便后续导入使用)：

```js
const { defaultToString } = require("../utils");

// 为了在字典中保存 value ，我们需要将 key 转化为了字符串，而为了保存信息的需要，我们同样要保存原始的 key 。
// 因此，我们不是只将 value 保存在字典中，而是要保存两个值：原始的key 和 value 。
// 为了字典能更简单地通过 toString 方法输出结果，我们同样要为 ValuePair类创建 toString 方法。
class ValuePair {
  constructor(key, value) {
    this.key = key;
    this.value = value;
  }
  toString() {
    return `[#${this.key}: ${this.value}]`;
  }
}

class Dictionary {
  constructor(toStrFn = defaultToString) {
    // 在字典中，理想的情况是用字符串作为键名，值可以是任何类型（从数、字符串等原始类型，到复杂的对象）。
    // 但是，由于 JavaScript 不是强类型的语言，不能保证键一定是字符串。
    // 因此需要把所有作为键名传入的对象转化为字符串，使得从 Dictionary 类中搜索和获取值更简单
    this.toStrFn = toStrFn;
    // 在一个 Object 的实例而不是数组中存储字典中的元素（table 属性）。
    // 将[键，值]对保存为 table[key] = {key, value} 。
    this.table = {};
  }

  // 1. 检测一个键是否存在于字典中
  hasKey(key) {
    return this.table[this.toStrFn(key)] != null;
  }
  // 2. 在字典和 ValuePair 类中设置键和值
  set(key, value) {
    if (key !== null && value !== null) {
      // 如果 key 和 value 不是 undefined 或 null ，那么我们获取表示 key 的字符串
      const tableKey = this.toStrFn(key);
      // 创建一个新的键值对并将其赋值给 table 对象上的 key属性（tableKey)
      this.table[tableKey] = new ValuePair(key, value);
      return true;
    }
    return false;
  }
  // 3. 从字典中移除一个值
  remove(key) {
    if (this.hasKey(key)) {
      delete this.table[this.toStrFn(key)];
      return true;
    }
    return false;
  }
  // 4. 从字典中检索一个值
  get(key) {
    const valuePair = this.table[this.toStrFn(key)];
    // 找不到返回undefined,找到了只返回value即可,不需要存入的原始key
    return valuePair == null ? undefined : valuePair.value;
  }
  // 5. 以数组形式返回字典中的所有 valuePair 对象(key value值)。
  keyValues() {
    return Object.values(this.table);
  }
  // 6. 返回 Dictionary 类中用于识别值的所有（原始）键名
  keys() {
    return this.keyValues().map((v) => v.key);
  }
  // 7. 返回一个字典包含的所有值构成的数组。
  values() {
    return this.keyValues().map((v) => v.value);
  }
  // 8. 用 forEach 迭代字典中的每个键值对
  forEach(callbackFn) {
    const valuePairs = this.keyValues();
    for (let i = 0; i < valuePairs.length; i++) {
      const result = callbackFn(valuePairs[i].key, valuePairs[i].value);
      if (result === false) {
        break;
      }
    }
  }
  // 9. clear、size、isEmpty 和 toString 方法
  size() {
    return Object.keys(this.table).length;
  }

  isEmpty() {
    return this.size() === 0;
  }

  clear() {
    this.table = {};
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    const valuePairs = this.keyValues();
    let objStr = `${valuePairs[0].toString()}`;
    for (let i = 1; i < valuePairs.length; i++) {
      objStr = `${objStr},${valuePairs[i].toString()}`;
    }
    return objStr;
  }
}

module.exports = {
  Dictionary,
  ValuePair,
};
```

使用示例:

```js
const dictionary = new Dictionary();
dictionary.set("Gandalf", "gandalf@email.com");
dictionary.set("John", "johnsnow@email.com");
dictionary.set("Tyrion", "tyrion@email.com");

console.log(dictionary.hasKey("Gandalf")); // true
console.log(dictionary.size()); // 3
console.log(dictionary.keys()); // ["Gandalf", "John", "Tyrion"]
console.log(dictionary.values()); // ["gandalf@email.com", "johnsnow@email.com", "tyrion@email.com"]
console.log(dictionary.get("Tyrion")); // tyrion@email.com

dictionary.remove("John");
console.log(dictionary.keys()); // [ 'Gandalf', 'Tyrion' ]
console.log(dictionary.values()); // [ 'gandalf@email.com', 'tyrion@email.com' ]
console.log(dictionary.keyValues());
/*
[
  ValuePair { key: 'Gandalf', value: 'gandalf@email.com' },
  ValuePair { key: 'Tyrion', value: 'tyrion@email.com' }
]
*/
dictionary.forEach((k, v) => {
  console.log("forEach: ", `key: ${k}, value: ${v}`);
});
/*
forEach:  key: Gandalf, value: gandalf@email.com
forEach:  key: Tyrion, value: tyrion@email.com
*/
```

## WeakSet 和 WeakMap

- 除了 Set 和 Map 这两种新的数据结构，ES2015 还增加了它们的弱化版本， WeakSet 和 WeakMap 。
- 基本上， Map 和 Set 与其弱化版本之间仅有的区别是：
  - WeakSet 或 WeakMap 类没有 entries 、 keys 和 values 等方法；
  - 只能用对象作为键。
- 创建和使用这两个类主要是为了性能。
  - WeakSet 和 WeakMap 是弱化的（用对象作为键），没有强引用的键。
  - 这使得 JavaScript 的垃圾回收器可以从中清除整个入口。
- 另一个优点是，必须用键才可以取出值。
  - 这些类没有 entries 、 keys 和 values 等迭代器方法，因此，除非你知道键，否则没有办法取出值。

# 散列表 (HashTable 类，也叫 HashMap 类)

## 散列表基础说明

- 定义:
  - 是 Dictionary (Map) 类的一种散列表
- 说明:
  - 散列算法的作用是尽可能快地在数据结构中找到一个值。
  - 在之前，如果要在数据结构中获得一个值（使用 get 方法），需要迭代整个数据结构来找到它。
  - 如果使用散列函数，就知道值的具体位置，因此能够快速检索到该值。
    - 散列函数的作用是给定一个键值，然后返回值在表中的地址。
    - 用最常见的散列函数—— lose lose 散列函数，方法是简单地将每个键值中的每个字母的 ASCII 值相加。
- 散列冲突:
  - 有时候，一些键会有相同的散列值。不同的值在散列表中对应相同位置的时候，我们称其为冲突。
  - 一般解决办法:
    - 分离链接、线性探查和双散列法。
- 简单几个方法:
  - put(key,value) ：向散列表增加一个新的项（也能更新散列表）。
  - remove(key) ：根据键值从散列表中移除值。
  - get(key) ：返回根据键值检索到的特定的值。
- 应用场景:
  - 散列表可以用来保存键和对表中记录的引用。

## HashTable 的实现

```js
const { defaultToString } = require("../utils");
const { ValuePair } = require("./1Dictionary");

class HashTable {
  constructor(toStrFn = defaultToString) {
    this.toStrFn = toStrFn;
    this.table = {};
  }

  // 1. 创建散列函数
  // 实现lose lose散列函数
  loseLoseHashCode(key) {
    if (typeof key === "number") {
      return key;
    }
    const tableKey = this.toStrFn(key);
    let hash = 0;
    for (let i = 0; i < tableKey.length; i++) {
      hash += tableKey.charCodeAt(i);
    }
    // 为了得到比较小的数值，我们会使用 hash 值和一个任意数做除法的余数(%)
    // 这可以规避操作数超过数值变量最大表示范围的风险
    return hash % 37;
  }

  hashCode(key) {
    return this.loseLoseHashCode(key);
  }

  // 2. 将键和值加入散列表
  put(key, value) {
    if (key != null && value != null) {
      const position = this.hashCode(key);
      this.table[position] = new ValuePair(key, value);
      return true;
    }
    return false;
  }

  // 3. 从散列表中获取一个值
  // HashTable 和 Dictionary 类很相似。
  // 不同之处在于在 Dictionary 类中，我们将 valuePair 保存在 table 的 key 属性中（在它被转化为字符串之后），
  // 而在 HashTable 类中，我们由 key（hash）生成一个数，并将 valuePair 保存在 hash 位置（或属性）。
  get(key) {
    const valuePair = this.table[this.hashCode(key)];
    return valuePair == null ? undefined : valuePair.value;
  }

  // 4. 从散列表中移除一个值
  remove(key) {
    // 要从 HashTable 中移除一个值，首先需要知道值所在的位置，因此我们使用 hashCode 函数来获取 hash
    const hash = this.hashCode(key);
    // 我们在 hash 的位置获取到 valuePair
    const valuePair = this.table[hash];
    // 不是 null 或 undefined ，就使用 JavaScript 的 delete 运算符将其删除
    if (valuePair != null) {
      delete this.table[hash];
      return true;
    }
    return false;
  }

  getTable() {
    return this.table;
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return Object.keys(this.table).length;
  }

  clear() {
    this.table = {};
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    const keys = Object.keys(this.table);
    let objString = `{${keys[0]} => ${this.table[keys[0]].toString()}}`;
    for (let i = 1; i < keys.length; i++) {
      objString = `${objString},{${keys[i]} => ${this.table[
        keys[i]
      ].toString()}}`;
    }
    return objString;
  }
}
```

使用示例:

```js
const hash = new HashTable();
hash.put("Gandalf", "gandalf@email.com");
hash.put("John", "johnsnow@email.com");
hash.put("Tyrion", "tyrion@email.com");

console.log(hash.hashCode("Gandalf") + " - Gandalf"); // 19 - Gandalf
console.log(hash.hashCode("John") + " - John"); // 29 - John
console.log(hash.hashCode("Tyrion") + " - Tyrion"); // 16 - Tyrion

console.log(hash.get("Gandalf")); // gandalf@email.com
console.log(hash.get("Loiane")); // undefined

hash.remove("Gandalf");
console.log(hash.get("Gandalf")); // undefined
```

# 处理散列表中的冲突

## 1 分离链接 (HashTable Separate Chaining)

### 分离链接基础说明

- 分离链接法包括为散列表的每一个位置创建一个链表并将元素存储在里面。
- 它是解决冲突的最简单的方法，但是在 HashTable 实例之外还需要额外的存储空间。
- 散列冲突:
  - 有时候，一些键会有相同的散列值。不同的值在散列表中对应相同位置的时候，我们称其为冲突。
- 一般解决办法:
  - 分离链接、线性探查和双散列法。
  - 对于分离链接和线性探查来说，只需要重写三个方法:put、get 和 remove。这三个方法在每种技术实现中都是不同的。

### 实现分离链接

这里需要用到字典和链表，所以一并导入。

```js
const { defaultToString } = require("../utils");
const { ValuePair } = require("./1Dictionary");
const { LinkedList } = require("../3LinkedList/1LinkedList");

class HashTableSeparateChaining {
  constructor(toStrFn = defaultToString) {
    this.toStrFn = toStrFn;
    this.table = {};
  }

  // 实现lose lose散列函数
  loseLoseHashCode(key) {
    if (typeof key === "number") {
      return key;
    }
    const tableKey = this.toStrFn(key);
    let hash = 0;
    for (let i = 0; i < tableKey.length; i++) {
      hash += tableKey.charCodeAt(i);
    }
    // 为了得到比较小的数值，我们会使用 hash 值和一个任意数做除法的余数(%)
    // 这可以规避操作数超过数值变量最大表示范围的风险
    return hash % 37;
  }

  hashCode(key) {
    return this.loseLoseHashCode(key);
  }

  put(key, value) {
    if (key != null && value != null) {
      const position = this.hashCode(key);
      // 验证要加入新元素的位置是否已经被占据
      if (this.table[position] == null) {
        // 如果是第一次向该位置加入元素，我们会在该位置上初始化一个 LinkedList 类的实例
        this.table[position] = new LinkedList();
      }
      // 如果已经有被占据,使用链表的push 方法向 LinkedList 实例中添加一个ValuePair 实例（键和值）
      this.table[position].push(new ValuePair(key, value));
      return true;
    }
    return false;
  }

  get(key) {
    const position = this.hashCode(key);
    const linkedList = this.table[position];
    // 如果该分离链表特定位置上存在链表且不为空
    if (linkedList != null && !linkedList.isEmpty()) {
      // 链表不为空,迭代这个链表来寻找我们需要的元素。
      // 在迭代之前先要获取链表表头的引用
      let current = linkedList.getHead();
      // 然后就可以从链表的头部迭代到尾部(最后 current.next将会是 null)。
      while (current != null) {
        // current是个含有element和next的Node(节点),而element是含有key和value的ValuePair实例
        if (current.element.key === key) {
          return current.element.value;
        }
        current = current.next;
      }
    }
    // 如果没有，则返回一个 undefined
    return undefined;
  }

  remove(key) {
    // 找到Map指定位置
    const position = this.hashCode(key);
    const linkedList = this.table[position];
    // 如果该位置不为空且位置的链表不为空
    if (linkedList != null && !linkedList.isEmpty()) {
      // 遍历该链表
      let current = linkedList.getHead();
      while (current != null) {
        // 找到该链表上ValuePair实例的key与要删除的key相同的节点
        if (current.element.key === key) {
          // 从链表中删除该节点
          linkedList.remove(current.element);
          // 如果删除节点后该链表为空,则一并删除该链表
          if (linkedList.isEmpty()) {
            delete this.table[position];
          }
          return true;
        }
        // 如果链表当前节点中没有要找的元素,迭代下一个节点
        current = current.next;
      }
    }
    return false;
  }

  getTable() {
    return this.table;
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return Object.keys(this.table).length;
  }

  clear() {
    this.table = {};
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    const keys = Object.keys(this.table);
    let objString = `{${keys[0]} => ${this.table[keys[0]].toString()}}`;
    for (let i = 1; i < keys.length; i++) {
      objString = `${objString},{${keys[i]} => ${this.table[
        keys[i]
      ].toString()}}`;
    }
    return objString;
  }
}

module.exports = {
  HashTableSeparateChaining,
};
```

测试使用：

```js
// 测试使用

// put()
const hashTable = new HashTableSeparateChaining();

hashTable.put("Ygritte", "ygritte@email.com");
hashTable.put("Jonathan", "jonathan@email.com");
hashTable.put("Jamie", "jamie@email.com");
hashTable.put("Jack", "jack@email.com");
hashTable.put("Jasmine", "jasmine@email.com");
hashTable.put("Jake", "jake@email.com");
hashTable.put("Nathan", "nathan@email.com");
hashTable.put("Athelstan", "athelstan@email.com");
hashTable.put("Sue", "sue@email.com");
hashTable.put("Aethelwulf", "aethelwulf@email.com");
hashTable.put("Sargeras", "sargeras@email.com");

console.log(hashTable.toString());
/*
// 可以明显看到散列冲突：
 {4 => [#Ygritte: ygritte@email.com]},
 {5 => [#Jonathan: jonathan@email.com],[#Jamie: jamie@email.com],[#Sue: sue@email.com],[#Aethelwulf: aethelwulf@email.com]},
 {7 => [#Jack: jack@email.com],[#Athelstan: athelstan@email.com]},
 {8 => [#Jasmine: jasmine@email.com]},
 {9 => [#Jake: jake@email.com]},
 {10 => [#Nathan: nathan@email.com],[#Sargeras: sargeras@email.com]}
*/

// get()
console.log(hashTable.get("Jamie")); // jamie@email.com
console.log(hashTable.get("Sue")); // sue@email.com
console.log(hashTable.get("Jonathan")); // jonathan@email.com
console.log(hashTable.get("Loiane")); // undefined

// remove()
console.log(hashTable.remove("Ygritte")); // true
console.log(hashTable.get("Ygritte")); // undefined
console.log(hashTable.toString());
/* 
{5 => [#Jonathan: jonathan@email.com],[#Jamie: jamie@email.com],[#Sue: sue@email.com],[#Aethelwulf: aethelwulf@email.com]},
{7 => [#Jack: jack@email.com],[#Athelstan: athelstan@email.com]},
{8 => [#Jasmine: jasmine@email.com]},
{9 => [#Jake: jake@email.com]},
{10 => [#Nathan: nathan@email.com],[#Sargeras: sargeras@email.com]}
*/

console.log(hashTable.remove("Sue")); // true
console.log(hashTable.toString());
/*
{5 => [#Jonathan: jonathan@email.com],[#Jamie: jamie@email.com],[#Aethelwulf: aethelwulf@email.com]},
{7 => [#Jack: jack@email.com],[#Athelstan: athelstan@email.com]},
{8 => [#Jasmine: jasmine@email.com]},
{9 => [#Jake: jake@email.com]},
{10 => [#Nathan: nathan@email.com],[#Sargeras: sargeras@email.com]}
*/

console.log(hashTable.remove("Jamie")); // true
console.log(hashTable.toString());
/*
{5 => [#Jonathan: jonathan@email.com],[#Aethelwulf: aethelwulf@email.com]},
{7 => [#Jack: jack@email.com],[#Athelstan: athelstan@email.com]},
{8 => [#Jasmine: jasmine@email.com]},
{9 => [#Jake: jake@email.com]},
{10 => [#Nathan: nathan@email.com],[#Sargeras: sargeras@email.com]}
*/
```

## 2 线性探查

### 线性探查基础说明

- 之所以称作线性，是因为它处理冲突的方法是将元素直接存储到表中，而不是在单独的数据结构中。
- 当想向表中某个位置添加一个新元素的时候，如果索引为 position 的位置已经被占据了，就尝试 position+1 的位置。如果 position+1 的位置也被占据了，就尝试 position+2 的位置，以此类推，直到在散列表中找到一个空闲的位置。

- 想象一下，有一个已经包含一些元素的散列表，我们想要添加一个新的键和值。我们计算这个新键的 hash ，并检查散列表中对应的位置是否被占据。如果没有，我们就将该值添加到正确的位置。如果被占据了，我们就迭代散列表，直到找到一个空闲的位置。

- 线性探查技术分为两种：
  - 第一种是软删除方法。
    - 我们使用一个特殊的值（标记）来表示键值对被删除了（惰性删除或软删除），而不是真的删除它。
    - 经过一段时间，散列表被操作过后，我们会得到一个标记了若干删除位置的散列表。
    - 这会逐渐降低散列表的效率，因为搜索键值会随时间变得更慢。
    - 能快速访问并找到一个键是我们使用散列表的一个重要原因。
  - 第二种方法需要检验是否有必要将一个或多个元素移动到之前的位置。
    - 当搜索一个键的时候，这种方法可以避免找到一个空位置。
    - 如果移动元素是必要的，我们就需要在散列表中挪动键值对。

### 线性探查的实现

以下为实现线性探查技术中上述第二种：

```js
const { defaultToString } = require("../util");
const { ValuePair } = require("./1Dictionary");

class HashTableLinearProbing {
  constructor(toStrFn = defaultToString) {
    this.toStrFn = toStrFn;
    this.table = {};
  }

  // lose lose 散列函数
  loseloseHashCode(key) {
    if (typeof key === "number") {
      return key;
    }
    const tableKey = this.toStrFn(key);
    let hash = 0;
    for (let i = 0; i < tableKey.length; i++) {
      hash += tableKey.charCodeAt(i);
    }
    return hash % 37;
  }

  // lose lose 散列函数并不是一个表现良好的散列函数，因为它会产生太多的冲突。
  // 比 lose lose 更好的散列函数是 djb2 。
  // 这并不是最好的散列函数，但这是最受社区推崇的散列函数之一。
  djb2HashCode(key) {
    // 将键转化为字符串
    const tableKey = this.toStrFn(key);
    // 初始化一个 hash 变量并赋值为一个质数
    let hash = 5381;
    // 迭代参数 key ，将 hash 与 33相乘（用作一个幻数(指直接使用的常数) ），并和当前迭代到的字符的 ASCII 码值相加
    for (let i = 0; i < tableKey.length; i++) {
      hash = hash * 33 + tableKey.charCodeAt(i);
    }
    // 最后，我们将使用相加的和与另一个随机质数相除的余数，比我们认为的散列表大小要大。
    // 在本例中，我们认为散列表的大小为 1000。
    return hash % 1013;
  }

  // 获取hash值
  hashCode(key) {
    return this.loseloseHashCode(key);
    // return this.djb2HashCode(key);
  }

  put(key, value) {
    if (key != null && value != null) {
      const position = this.hashCode(key);
      // 验证这个位置是否有元素存在
      if (this.table[position] == null) {
        // 如果没有,直接添加
        this.table[position] = new ValuePair(key, value);
      } else {
        // 如果已被占据，需要找到下一个没有被占据的位置（ position 的值是 undefined或 null ），
        // 因此我们声明一个 index 变量并赋值为 position+1 。
        let index = position + 1;
        // 然后验证该位置是否被占据），如果被占据了，继续将 index 递增
        while (this.table[index] != null) {
          index++;
        }
        // 直到找到一个没有被占据的位置。然后我们要做的，就是将值分配到该位置。(删除后的查找难点也是找准这个变动过的position)
        this.table[index] = new ValuePair(key, value);
      }
      return true;
    }
    return false;
  }

  get(key) {
    const position = this.hashCode(key);
    // 如果指定位置不为空(确定这个键存在),且需要寻找的key与存放的key匹配,返回该value
    if (this.table[position] != null) {
      if (this.table[position].key === key) {
        return this.table[position].value;
      }
      // 如果key不匹配,所有有移动过,需要迭代找到匹配的key
      let index = position + 1;
      while (this.table[index] != null && this.table[index].key !== key) {
        index++;
      }
      // 找到匹配的位置和key值之后,返回该value
      if (this.table[index] != null && this.table[index].key === key) {
        return this.table[position].value;
      }
    }

    // 如果这个键不存在，说明要查找的值不在散列表中,返回undefined
    return undefined;
  }

  /*
    在 get 方法中，当我们找到了要找的 key 后，返回它的值。
    在 remove 方法中，我们会从散列表中删除元素。可以直接从原始 hash 位置找到元素，
    如果有冲突并被处理了，我们可以在另一个位置找到元素。
    由于我们不知道在散列表的不同位置上是否存在具有相同 hash 的元素，需要验证删除操作是否有副作用。
    如果有，就需要将冲突的元素移动至一个之前的位置，这样就不会产生空位置。要完成这项工作，我们将会创建一个工具方法。
    */
  remove(key) {
    const position = this.hashCode(key);
    // 如果要删除的key存在
    if (this.table[position] != null) {
      // 且直接在对应的位置上key匹配
      if (this.table[position].key === key) {
        // 移除该元素
        delete this.table[position];
        // 为了消除直接移除元素的副作用,要专门处理一下
        this.verifyRemoveSideEffect(key, position);
        return true;
      }
      // 直接的位置上的key不匹配,迭代位置,直到找到key匹配的位置
      let index = position + 1;
      while (this.table[index] != null && this.table[index].key !== key) {
        index++;
      }
      // 找到key匹配的位置,删除该元素,并消除副作用(移动必要元素填充该位置)
      if (this.table[index] != null && this.table[index].key === key) {
        delete this.table[index];
        this.verifyRemoveSideEffect(key, index);
        return true;
      }
    }
    return false;
  }

  // 由于我们不知道在散列表的不同位置上是否存在具有相同 hash 的元素，需要验证删除操作是否有副作用。
  // 如果有，就需要将冲突的元素移动至一个之前的位置，这样就不会产生空位置。
  // 要完成这项工作，我们将会创建一个工具方法
  //      参数分别为：被删除的 key 和该 key 被删除的位置。
  verifyRemoveSideEffect(key, removedPosition) {
    // 获取被删除的 key 的 hash 值
    const hash = this.hashCode(key);
    // 会从下一个位置开始迭代散列表,直到找到一个空位置。
    // 当空位置被找到后，表示元素都在合适的位置上，不需要进行移动（或更多的移动）。
    let index = removedPosition + 1;
    // 如果不为空就需要进行移动
    while (this.table[index] != null) {
      // 当迭代随后的元素时，我们需要计算当前位置上元素的 hash 值
      const posHash = this.hashCode(this.table[index].key);
      // 如果当前元素的hash值小于或等于原始的hash值或者当前元素的hash值小于或等于removedPosition(也就是上一个被移除key的hash值)
      if (posHash <= hash || posHash <= removedPosition) {
        // 表示我们需要将当前元素移动至 removedPosition 的位置。
        this.table[removedPosition] = this.table[index];
        // 移动完成后，我们可以删除当前的元素（因为它已经被复制到 removedPosition 的位置了）。
        delete this.table[index];
        // 我们还需要将 removedPosition 更新为当前的 index ，然后重复这个过程。
        removedPosition = index;
      }
      index++;
    }
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return Object.keys(this.table).length;
  }

  clear() {
    this.table = {};
  }

  getTable() {
    return this.table;
  }

  toString() {
    if (this.isEmpty()) {
      return "";
    }
    const keys = Object.keys(this.table);
    let objString = `{${keys[0]} => ${this.table[keys[0]].toString()}}`;
    for (let i = 1; i < keys.length; i++) {
      objString = `${objString},{${keys[i]} => ${this.table[
        keys[i]
      ].toString()}}`;
    }
    return objString;
  }
}

module.exports = {
  HashTableLinearProbing,
};
```

使用测试：

```js
const hashTable = new HashTableLinearProbing();

hashTable.put("Ygritte", "ygritte@email.com");
hashTable.put("Jonathan", "jonathan@email.com");
hashTable.put("Jamie", "jamie@email.com");
hashTable.put("Jack", "jack@email.com");
hashTable.put("Jasmine", "jasmine@email.com");
hashTable.put("Jake", "jake@email.com");
hashTable.put("Nathan", "nathan@email.com");
hashTable.put("Athelstan", "athelstan@email.com");
hashTable.put("Sue", "sue@email.com");
hashTable.put("Aethelwulf", "aethelwulf@email.com");
hashTable.put("Sargeras", "sargeras@email.com");

/*
模拟一下散列表中的插入操作。【 注意，此时使用的散列函数为：loseloseHashCode()】
(1) 试着插入 Ygritte 。它的散列值是 4，由于散列表刚刚被创建，位置 4 还是空的，可以在这里插入数据。 
(2) 试着在位置 5 插入 Jonathan 。它也是空的，所以可以插入这个姓名。 
(3) 试着在位置 5 插入 Jamie ，因为它的散列值也是 5。位置 5 已经被 Jonathan 占据了，所以需要
    检查索引值为 position+1 的位置（5+1），位置 6 是空的，所以可以在位置 6 插入 Jamie 。 
(4) 试着在位置 7 插入 Jack 。它是空的，所以可以插入这个姓名，不会有冲突。 
(5) 试着在位置 8 插入 Jasmine 。它是空的，所以可以插入这个姓名，不会有冲突。 
(6) 试着在位置 9 插入 Jake 。它是空的，所以可以插入这个姓名，不会有冲突。 
(7) 试着在位置 10 插入 Nathan 。它是空的，所以可以插入这个姓名，不会有冲突。 
(8) 试着在位置 7 插入 Athelstan 。位置 7 已经被 Jack 占据了，所以需要检查索引值为
    position+1 的位置（7+1）。位置 8 也被占据了，所以迭代到下一个空位置，也就是位置 11，并插入 Athelstan 。 
(9) 试着在位置 5 插入 Sue ，位置 5 到 11 都被占据了，所以我们在位置 12 插入 Sue 。 
(10)  试着在位置 5 插入 Aethelwulf ，位置 5 到 12 都被占据了，所以我们在位置 13 插入Aethelwulf 。 
(11)  试着在位置 10 插入 Sargeras ，位置 10 到 13 都被占据了，所以我们在位置 14 插入Sargeras 。 
*/
console.log(hashTable.toString());
/* 
{4 => [#Ygritte: ygritte@email.com]},
{5 => [#Jonathan: jonathan@email.com]},
{6 => [#Jamie: jamie@email.com]},
{7 => [#Jack: jack@email.com]},
{8 => [#Jasmine: jasmine@email.com]},
{9 => [#Jake: jake@email.com]},
{10 => [#Nathan: nathan@email.com]},
{11 => [#Athelstan: athelstan@email.com]},
{12 => [#Sue: sue@email.com]},
{13 => [#Aethelwulf: aethelwulf@email.com]},
{14 => [#Sargeras: sargeras@email.com]}
*/

// 如果hansh函数使用的 djb2HashCode()，结果是：
/* 
{149 => [#Aethelwulf: aethelwulf@email.com]},
{223 => [#Nathan: nathan@email.com]},
{275 => [#Jasmine: jasmine@email.com]},
{288 => [#Jonathan: jonathan@email.com]},
{502 => [#Sue: sue@email.com]},
{619 => [#Jack: jack@email.com]},
{711 => [#Sargeras: sargeras@email.com]},
{807 => [#Ygritte: ygritte@email.com]},
{877 => [#Jake: jake@email.com]},
{925 => [#Athelstan: athelstan@email.com]},
{962 => [#Jamie: jamie@email.com]}
*/

// =======================================
// 测试 get()方法
console.log(hashTable.get("Nathan")); // nathan@email.com
console.log(hashTable.get("Loiane")); // undefined

// =======================================
// 测试 remove()方法
hashTable.remove("Jonathan");
console.log(hashTable.get("Jonathan")); // undefined
/*
演示 put 方法所创建的散列表。假设我们想要从散列表中移除 Jonathan 元素。
下面来模拟一下删除的过程。 
(1) 我们可以在位置 5 找到并删除 Jonathan 。位置 5 现在空闲了。我们将验证一下是否有副作用。 
(2) 我们来到存储 Jamie 的位置 6，现在的散列值为 5，它的散列值 5 小于等于散列值 5，
    所以要将 Jamie 复制到位置 5 并删除 Jamie 。位置 6 现在空闲了，我们来验证下一个位置。 
(3) 我们来到位置 7，这里保存了 Jack ，散列值为 7。它的散列值 7 大于散列值 5，并且散列值 7大于
    removedPosition 的值 6，所以我们不需要移动它。下一个位置也被占据了，那么我们来验证下一个位置。 
(4)  我们来到位置 8，此处保存了 Jasmine ，散列值为 8。散列值 8 大于 Jasmine 的散列值 5，
    并且散列值 8 大于 removedPosition 的值 6，因此不需要移动它。下一个位置也被占了，那么我们来验证下一个位置。 
(5) 我们来到位置 9，这里保存了 Jake ，它的散列值是 9。散列值 9 大于散列值 5，并且散列值 9 大于 
    removedPosition 的值 6，所以不需要移动它。下一个位置也被占了，那么我们来验证下一个位置。 
(6) 我们重复相同的过程，直到位置 12。 
(7) 我们来到位置 12，此处保存了 Sue ，它的散列值为 5。散列值 5 小于等于散列值 5，并且散列值 5 
    小于等于 removedPosition 的值 6，因此我们将 Sue 复制到位置 6，并删除位置 12的 Sue 。
    位置 12 现在空闲了。下一个位置也被占据了，那么我们来验证下一个位置。 
(8)  我们来到位置 13，此处保存了 Aethelwulf ，它的散列值为 5。散列值 5 小于等于散列值 5，
    并且散列值 5 小于等于 removedPosition 的值 12，因此我们需要将 Aethelwulf 复制到位置 12 
    并删除位置 13 的值。位置 13 现在空闲了。下一个位置也被占据了，那么我们来验证下一个位置。 
(9)  我们来到位置 14，此处保存了 Sargeras ，散列值为 10。散列值 10 大于 Aethelwulf的散列值 5，
    但是散列值 10 小于等于 removedPosition 的值 13，因此我们要将 Sargeras 复制到位置 13 
    并删除位置 14 的值。位置 14 现在空闲了。下一个位置也是空闲的，那么本次执行完成了。
*/
console.log(hashTable.toString());
/* 
{4 => [#Ygritte: ygritte@email.com]},
{5 => [#Jamie: jamie@email.com]},
{6 => [#Sue: sue@email.com]},
{7 => [#Jack: jack@email.com]},
{8 => [#Jasmine: jasmine@email.com]},
{9 => [#Jake: jake@email.com]},
{10 => [#Nathan: nathan@email.com]},
{11 => [#Athelstan: athelstan@email.com]},
{12 => [#Aethelwulf: aethelwulf@email.com]},
{13 => [#Sargeras: sargeras@email.com]}
*/
```
