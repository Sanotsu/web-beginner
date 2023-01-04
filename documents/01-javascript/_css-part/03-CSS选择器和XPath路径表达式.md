<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [CSS 选择器与 XPath 路径表达式](#css-%E9%80%89%E6%8B%A9%E5%99%A8%E4%B8%8E-xpath-%E8%B7%AF%E5%BE%84%E8%A1%A8%E8%BE%BE%E5%BC%8F)
  - [CSS 选择器](#css-%E9%80%89%E6%8B%A9%E5%99%A8)
  - [XPath 路径表达式](#xpath-%E8%B7%AF%E5%BE%84%E8%A1%A8%E8%BE%BE%E5%BC%8F)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## CSS 选择器与 XPath 路径表达式

### CSS 选择器

**1. 选择器是什么**

CSS 中，选择器用来**指定网页上想要样式化的 HTML 元素**。CSS 选择器是 CSS 规则的第一部分。选择器所选择的元素，叫做“选择器的对象”。

**2. 选择器列表**

有**多个使用相同样式的 CSS 选择器**，那么这些单独的选择器**可以被混编为一个“选择器列表”**，这样，规则就可以应用到所有的单个选择器上:

```css
h1 {
  color: blue;
}
.special {
  color: blue;
}

/* 组合为选择器列表=> */
h1,
.special {
  color: blue;
}
```

使用选择器列表时，如果*任何一个*选择器*无效* (存在语法错误)，那么*整条规则*都会*被忽略*。

**3. 选择器的种类**

<!--
| -------------- | ------------------- | ---------------------------------------------------------------------------- |
-->

| 选择器         | 示例                | 备注                                                                                         |
| -------------- | ------------------- | -------------------------------------------------------------------------------------------- |
| 类型选择器     | `h1 { }`            | 语法: `元素 {样式声明 }`                                                                     |
| 通配选择器     | `* { }`             | 在 CSS 中，一个星号就是一个通配选择器 ，可以和命名空间组合使用                               |
| 类选择器       | `.box { }`          | 语法: `.类名 {样式声明 }`                                                                    |
| ID 选择器      | `#unique { }`       | 语法: `#id 属性值 {样式声明 }`                                                               |
| 标签属性选择器 | `a[title] { }`      | 通过已经存在的*属性名*或*属性值*匹配元素 。`a[href*="example"] {}`                           |
| 伪类选择器     | `p:first-child { }` | 伪类是添加到选择器的关键字，用于*指定所选元素的特殊状态*。例如`:hover`                       |
| 伪元素选择器   | `p::first-line { }` | 伪元素是一个附加至选择器末的关键词，允许*对被选择元素的特定部分修改样式*。                   |
| 后代选择器     | `article p`         | 如果第二个选择器匹配的元素具有与第一个选择器匹配的祖先元素，则它们将被选择。                 |
| 子代选择器     | `article > p`       | 只会匹配那些作为第一个元素的*直接后代*(子元素) 的第二元素。                                  |
| 相邻兄弟选择器 | `h1 + p`            | 第二个元素**紧跟**第一个元素之后且两个元素都属于同一个父元素的子元素，第二个元素将被选中。   |
| 通用兄弟选择器 | `h1 ~ p`            | 两个选择器分开并匹配第二个选择器的所有迭代元素，位置**无须紧邻**，只须有**相同的父级元素**。 |

```css
/*【标签选择器】存在 title 属性的<a> 元素 */
a[title] {
  color: purple;
}

/*【标签选择器】存在 href 属性并且属性值匹配"https://example.org"的<a> 元素 */
a[href="https://example.org"]
{
  color: green;
}

/* 标签选择器】存在 href 属性并且属性值包含"example"的<a> 元素 */
a[href*="example"] {
  font-size: 2em;
}

/*【标签选择器】存在 href 属性并且属性值结尾是".org"的<a> 元素 */
a[href$=".org"] {
  font-style: italic;
}

/*【标签选择器】存在 class 属性并且属性值包含以空格分隔的"logo"的<a>元素 */
a[class~="logo"] {
  padding: 2px;
}

/*【伪类选择器】用户的指针悬停在其上的任何按钮变为蓝色 */
button:hover {
  color: blue;
}

/*【伪元素选择器】对p标签内第一行使用绿色和全大写字母 */
p::first-line {
  color: blue;
  text-transform: uppercase;
}

/*【后代选择器】作为 "my-things" 列表的后代的列表项目 */
ul.my-things li {
  margin: 2em;
}

/*【相邻兄弟选择器】图片后面紧跟着的段落将被选中 */
img + p {
  font-weight: bold;
}

/*【相邻兄弟选择器 + 伪类选择器】在 一组li兄弟元素中其类型的第一个元素之后的第一个li，即li列表的第二个li元素 */
li:first-of-type + li {
  color: red;
}

/*【通用兄弟选择器】在任意图像后的兄弟段落 */
img ~ p {
  color: red;
}
```

### XPath 路径表达式

什么是 XPath?

- XPath 使用路径表达式在 XML 文档中进行导航
- XPath 包含一个标准函数库
- XPath 是 XSLT 中的主要元素
- XPath 是一个 W3C 标准

XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。

XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。

在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点（或称为根节点）。

**1. 选取节点**

XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。

| 表达式     | 描述                                                       | 示例              | 说明                                                                                        |
| ---------- | ---------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------- |
| `nodename` | 选取此节点的所有子节点。                                   | `bookstore`       | 选取 bookstore 元素的所有子节点。                                                           |
| `/`        | 从根节点选取。                                             | `bookstore/book`  | 选取属于 bookstore 的子元素的所有 book 元素。                                               |
| `//`       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 | `/bookstore`      | 选取根元素 bookstore。注释：假如路径起始于正斜杠(`/`)，则此路径始终代表到某元素的绝对路径！ |
| `.`        | 选取当前节点。                                             | `//book `         | 选取所有 book 子元素，而不管它们在文档中的位置。                                            |
| `..`       | 选取当前节点的父节点。                                     | `bookstore//book` | 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。    |
| `@`        | 选取属性。                                                 | `//@lang`         | 选取名为 lang 的所有属性。                                                                  |

**2. 选取未知节点**

XPath 通配符可用来选取未知的 XML 元素。

| 通配符   | 描述                 | 路径表达式     | 结果                              |
| -------- | -------------------- | -------------- | --------------------------------- |
| `*`      | 匹配任何元素节点。   | `/bookstore/*` | 选取 bookstore 元素的所有子元素。 |
| `@*`     | 匹配任何属性节点。   | `//*`          | 选取文档中的所有元素。            |
| `node()` | 匹配任何类型的节点。 | `//title[@*]`  | 选取所有带有属性的 title 元素。   |

**3. 谓语（Predicates）**

谓语用来查找某个特定的节点或者包含某个指定的值的节点。_谓语被嵌在方括号中_。

|                                      |                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------- |
| `/bookstore/book[1]`                 | 选取属于 bookstore 子元素的第一个 book 元素。                                             |
| `/bookstore/book[last()]`            | 选取属于 bookstore 子元素的最后一个 book 元素。                                           |
| `/bookstore/book[last()-1]`          | 选取属于 bookstore 子元素的倒数第二个 book 元素。                                         |
| `/bookstore/book[position()<3]`      | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。                                 |
| `//title[@lang]`                     | 选取所有拥有名为 lang 的属性的 title 元素。                                               |
| `//title[@lang='eng']`               | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。                                |
| `/bookstore/book[price>35.00]`       | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。                |
| `/bookstore/book[price>35.00]/title` | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

**4. 选取若干路径**

通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

| 路径表达式             | 结果          |
| ---------------------- | ------------- | ----------------------------------------------------------------------------------- |
| `//book/title          | //book/price` | 选取 book 元素的所有 title 和 price 元素。                                          |
| `//title               | //price`      | 选取文档中的所有 title 和 price 元素。                                              |
| `/bookstore/book/title | //price`      | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。 |

XPath 示例:

`//*[@id="main"]/div/div[1]/div/div[1]/dl[5]/dd/a[2]`

- 在当前文档中选择了 id 名为"main" 的元素下 div 后第 1 个 div 后 div 下第 1 个 div 下第 5 个 dl 元素下 dd 之后的第 2 个 a 标签元素。
- 表达式的`[x]`就是第 x 个元素，不是从 0 开始计数的。

---

ref:

- MDN [CSS 选择器](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)
- MDN [XPath](https://developer.mozilla.org/en-US/docs/Web/XPath)
- [xpath-tester](https://extendsclass.com/xpath-tester.html)
- W3School [XPath 语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)
