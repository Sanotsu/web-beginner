# js 常用技巧

- **1. 数组相关**

  - **数组去重**: ES6 引入了 Set 对象和延展（spread）语法`…`

  ```js
  const uniqueArray = [...new Set([1, 1, 2, 3, 5, 5, 1])]; // [1, 2, 3, 5]
  // 截取数组，slice()的运行速度比重新定义数组的 length 属性快
  let array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  array.length = 4;
  console.log(array); // [ 0, 1, 2, 3 ]
  console.log([0, 1, 2, 3, 4, 5, 6, 7, 8, 9].slice(0, 4)); // [ 0, 1, 2, 3 ]
  console.log([0, 1, 2, 3, 4, 5, 6, 7, 8, 9].slice(-4)); // [ 6, 7, 8, 9 ]
  ```

  - **在循环中缓存数组长度**

  ```js
  // 从性能方面来看，即使数组变得很大，也不需要花费额外的运行时重复计算 array.length。
  for (let i = 0, length = array.length; i < length; i++) {...}
  ```

  - **使用 Boolean 过滤数组中的所有假值**

  ```js
  const compact = (arr) => arr.filter(Boolean);
  compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]); // 结果值为: [ 1, 2, 3, 'a', 's', 34 ]
  ```

  - **数组元素转化为数字**

  ```js
  const array2 = ["12", "1", "3.1415", "-10.01"];
  console.log(array2.map(Number)); // [12, 1, 3.1415, -10.01]
  ```

  - **将数组平铺到指定深度**

  ```js
  const flatten = (arr, depth = 1) =>
    depth != 1
      ? arr.reduce(
          (a, v) => a.concat(Array.isArray(v) ? flatten(v, depth - 1) : v),
          []
        )
      : arr.reduce((a, v) => a.concat(v), []);
  console.log(flatten([1, [2], 3, 4])); // [1, 2, 3, 4]
  console.log(flatten([1, [2, [3, [4, 5], 6], 7], 8], 2)); // [1, 2, 3, [4, 5], 6, 7, 8]
  ```

  - **返回数组中最大值**

  ```js
  const maxElementFromArray = (array, number = 1) =>
    [...array].sort((x, y) => y - x).slice(0, number);
  console.log(
    maxElementFromArray([1, 4, 3, 6, 7]),
    maxElementFromArray([7, 8, 9, 9, 9])
  ); // [7] [9]
  ```

- **2. 字符串相关**

  - 数字转换成字符串: `strval = numval + ""`； 字符串转成数字: `~~strnum`，一个波浪号表示**按位取反**操作，`~15` 等于`-16`。

  ```js
  console.log(+"15", typeof +"15"); // 输出: 15 number
  // 在某些情况下，+运算符会被解析成连接操作，而不是加法操作。对于这种情况，可以使用两个波浪号：~~
  console.log(~15, ~"15", ~~"15", typeof ~~"15"); // 输出都是number类型: -16 -16 15 number
  ```

  - **格式化 JSON.stringify() 输出的字符串**

  该方法接受两个额外的参数，一个是函数，用于过滤要显示的 JSON；另一个是空格个数，也可以是一个字符串。

  ```js
  console.log(JSON.stringify({ alpha: "A", beta: "B" })); // 挤在了一行输出
  console.log(JSON.stringify({ alpha: "A", beta: "B" }, null, "\t")); // 有格式的输出
  ```

  - **string 强制转换为数字**

  用`*1`来转化为数字(实际上是调用`.valueOf` 方法)，也可以使用`+`来转化字符串为数字。

  ```js
  console.log(
    "32" * 1,
    "ds" * 1,
    null * 1,
    undefined * 1,
    1 * { valueOf: () => "3" }
  ); // 32 NaN 0 NaN 3
  console.log(+"123", +"ds", +"", +null, +undefined, +{ valueOf: () => "3" }); // 123 NaN 0 0 NaN 3
  ```

  - **字符串反转**

  ```js
  const reverseStr = (string) => [...string].reverse().join("");
  console.log(reverseStr("hello"), reverseStr("1234")); // "olleh" "4321"
  ```

- **3. 对象等结构相关**

  - **object 强制转化为 string**

  使用 `字符串 + Object` 的方式来转化对象为字符串，也可以覆盖对象的 toString 和 valueOf 方法来自定义对象的类型转换。

  ```js
  // 输出: Math转字符串:[object Math] JSON字符串:[object JSON]
  console.log("Math转字符串:" + Math, "JSON字符串:" + JSON);
  console.log(2 * { valueOf: () => "3" }, "J" + { toString: () => "S" }); // 输出: 6 "JS"
  ```

  - **对象动态声明属性**

  ```js
  const dynamic = "color";
  let item = { brand: "Ford", [dynamic]: "Blue" };
  console.log(item); // { brand: "Ford", color: "Blue" }
  ```

- **4. 语法相关**

  - **短路求值**: `||`

  ```js
  let one = 1,
    two = 2,
    three = 3;
  console.log(one && two && three); // 3
  console.log(0 && null); // 0
  ```

  - 转换成布尔值: **使用`!`**

  在 JavaScript 中，除了 0、空字符串、null、undefined、NaN 和 false 是假值之外，其他的都是真值。

  ```js
  console.log(!"hello", !0, typeof true, !typeof true); // false true "boolean" false
  ```

  - 快速幂运算`**`，比使用`Math.pow()`更快: `console.log(Math.pow(2, 3) == 2 ** 3) // true`

  - 快速取整: **使用位或运算符 `|`** 比 Math.floor()、Math.ceil()或 Math.round()更快。

  ```js
  console.log(23.9 | 0, -23.9 | 0); // 位运算符，正数向下取整，负数向上取整，输出: 23 -23
  console.log(Math.floor(23.9), Math.ceil(-23.9)); // 输出: 23 -23
  console.log(1553 / 100, (1553 / 100) | 0); // // 移除整数尾部数字,输出: 15.53, 15
  ```

  - **判断奇偶数 `& 1`**

  ```js
  const num = 3;
  console.log(!!(num & 1), !!(num % 2)); // true true
  ```

  - **给多个变量赋值**

  ```js
  let [a, b, c] = [5, 8, 12];
  console.log(a, b, c); // 5 8 12
  ```

  - **交换两个变量**

  ```js
  let x = "Hello",
    y = 55;
  console.log(x, y); // Hello 55
  [x, y] = [y, x];
  console.log(x, y); // 55 Hello
  ```

  - **多条件检查**

  对于多个值匹配，我们可以将所有的值放到数组中，然后使用 indexOf() 或 includes() 方法。

  ```js
  if (value === 1 || value === "one" || value === 2 || value === "two") {...}
  if ([1, "one", 2, "two"].indexOf(value) >= 0) {  ...}
  if ([1, "one", 2, "two"].includes(value)) {...}
  ```

  - **仅在变量为 true 的情况下才调用函数**，则可以使用 `&&` 运算符

  ```js
  if (test1) {
    callMethod();
  }
  test1 && callMethod();
  ```

  - **在 return 语句中使用比较**

  ```js
  function checkReturn() {
    return test || callMe("test");
  }
  ```

- **5. 工具方法**

  - **数组洗牌**

  ```js
  const shuffleArray = (arr) => arr.sort(() => Math.random() - 0.5);
  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  console.log(shuffleArray(arr)); // 每次输出都不一样
  ```

  - **生成随机颜色字符串**

  ```js
  const generateRandomHexColor = () =>
    `#${Math.floor(Math.random() * 0xffffff).toString(16)}`;
  console.log(generateRandomHexColor()); // 输出类似: #7a40e7
  ```

  - **缩短 console.log()**

  ```js
  // 在nodejs使用 globalThis，看环境使用window、document等
  const cc = console.log.bind(globalThis);
  cc(996, "hello world", new Date()); // 996 hello world 2022-12-15T07:02:08.567Z
  ```

---

ref: 实际上，这些大部分的所谓技巧都是 ES6 以来新特性的用法，有几个实用的工具方法到还有点用

- 2019-05-27 \* [11 JavaScript Tricks You Won’t Find in Most Tutorials](https://bretcameron.medium.com/12-javascript-tricks-you-wont-find-in-most-tutorials-a9c9331f169d)
- 2019-09-05 [学会这些 JS 小技巧，提升编码幸福度](https://www.infoq.cn/article/wF1PorTPQiW0*Q2Jc2XU)
- 2020-11-02 [JavaScript shorthand tips and tricks that will save your time](https://javascript.plainenglish.io/20-javascript-shorthand-techniques-that-will-save-your-time-f1671aab405f)
- 2018-11-06 [JavaScript 复杂判断的更优雅写法](https://juejin.cn/post/6844903705058213896)
- 2020-11-11 [25 JavaScript Tricks You Need To Know About](https://medium.com/before-semicolon/25-javascript-code-solutions-utility-tricks-you-need-to-know-about-3023f7ed993e)
- 2022-02-13 \* [7 Killer One-Liners in JavaScript](https://tapajyoti-bose.medium.com/7-killer-one-liners-in-javascript-33db6798f5bf)
- 2021-03-10 [新老手必备的 34 种 JavaScript 简写优化技术](https://mp.weixin.qq.com/s/WJLLtXEVhmk5m2DHkK4U_g)
- 2021-12-08 \* [20+个超级实用的 JavaScript 开发技巧](https://juejin.cn/post/7039142750503534599)
- 2022-04-20 \* [面向 Web 开发人员的 58 个 JavaScript 技巧](https://juejin.cn/post/7088527867037876255)
- 2020-03-19 [上次 24 个实用 ES6 方法受到好评，这次再来 10 个](https://www.toutiao.com/article/6805704151348019715/)
