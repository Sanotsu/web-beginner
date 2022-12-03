文档中使用到的工具函数汇整：

`utils.js`

```js
// 比较结果
const Compare = {
  LESS_THAN: -1,
  BIGGER_THAN: 1,
  EQUALS: 0,
};
// 不存在常量
const DOES_NOT_EXIST = -1;

// 小于等于方法
function lesserEquals(a, b, compareFn) {
  const comp = compareFn(a, b);
  return comp === Compare.LESS_THAN || comp === Compare.EQUALS;
}
// 大于等于方法
function biggerEquals(a, b, compareFn) {
  const comp = compareFn(a, b);
  return comp === Compare.BIGGER_THAN || comp === Compare.EQUALS;
}
// 默认的比较方法
function defaultCompare(a, b) {
  if (a === b) {
    return Compare.EQUALS;
  }
  return a < b ? Compare.LESS_THAN : Compare.BIGGER_THAN;
}
// 相等
function defaultEquals(a, b) {
  return a === b;
}
// 装换为字符串方法
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
// 数组内指定索引两个数的交换
function swap(array, a, b) {
  /* const temp = array[a];
  array[a] = array[b];
  array[b] = temp; */
  [array[a], array[b]] = [array[b], array[a]];
}

// 翻转比较
function reverseCompare(compareFn) {
  return (a, b) => compareFn(b, a);
}
// 求数值的差值方法
function defaultDiff(a, b) {
  return Number(a) - Number(b);
}

//-----------------
// 红黑树节点的颜色
const Colors = {
  RED: 0,
  BLACK: 1,
};

function findMaxValue(array, compareFn = defaultCompare) {
  if (array && array.length > 0) {
    let max = array[0];
    for (let i = 1; i < array.length; i++) {
      if (compareFn(max, array[i]) === Compare.LESS_THAN) {
        max = array[i];
      }
    }
    return max;
  }
  return undefined;
}
function findMinValue(array, compareFn = defaultCompare) {
  if (array && array.length > 0) {
    let min = array[0];
    for (let i = 1; i < array.length; i++) {
      if (compareFn(min, array[i]) === Compare.BIGGER_THAN) {
        min = array[i];
      }
    }
    return min;
  }
  return undefined;
}

module.exports = {
  Compare,
  Colors,
  DOES_NOT_EXIST,
  lesserEquals,
  biggerEquals,
  defaultCompare,
  defaultEquals,
  defaultToString,
  swap,
  reverseCompare,
  defaultDiff,
  findMinValue,
  findMaxValue,
};
```
