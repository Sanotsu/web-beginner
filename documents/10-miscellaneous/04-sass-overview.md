# [CSS 预处理器 Sass/SCSS](https://sass-lang.com/guide)

(可能有些过时，需要看官网)

**变量声明**: 使用`$`符号,以`空格`或`逗号`分割的多个属性值，变量名可用`中划线`或`下划线`连接:  
`$basic-border: 1px solid black;`

**变量使用**: 凡是 css 属性的标准值（比如说 1px 或者 bold）可存在的地方，变量就可以使用:

```scss
$highlight-color: #f90;
$highlight-border: 1px solid $highlight-color;
.selected {
  border: $highlight-border;
}
```

**简单的嵌套**:可以像俄罗斯套娃那样在规则块中嵌套规则块,避免重复书写:

```scss
#content {
  article {
    h1 {
      color: #333;
    }
    p {
      margin-bottom: 1.4em;
    }
  }
  aside {
    background-color: #eee;
  }
}
/* 编译后 */
#content article h1 {
  color: #333;
}
#content article p {
  margin-bottom: 1.4em;
}
#content aside {
  background-color: #eee;
}
```

**父选择器的标识符`&`**: 简单嵌套的解开是**父选择器通过一个`空格`连接到子选择器的前边**形成后代选择器。  
上面的例子，父选择器`#content`，子选择器`article`和`aside`，后台选择器`#content article`和`#content aside`。  
使用嵌套规则时，父选择器标识符`&`能对于嵌套规则如何解开提供更好的控制，且`&`可以放在任何一个选择器可出现的地方。

```scss
article a {
  color: blue;
  :hover {
    color: red;
  }
}
/* 编译后 */
article a {
  color: blue;
}
article a :hover {
  color: red;
}

article a {
  color: blue;
  &:hover {
    color: red;
  }
}
/* 编译后 */
article a {
  color: blue;
}
article a:hover {
  color: red;
}
```

使用父选择器标识符`&`的，编译后`a`和`:hover`中间**没有空格**.

**群组选择器的嵌套**:sass 解开一个群组选择器规则内嵌的规则时，它会把每一个内嵌选择器的规则都正确地解出来.

```scss
.container {
  h1,
  h2,
  h3 {
    margin-bottom: 0.8em;
  }
}
nav,
aside {
  a {
    color: blue;
  }
}
/* 编译后 */
.container h1,
.container h2,
.container h3 {
  margin-bottom: 0.8em;
}
nav a,
aside a {
  color: blue;
}
```

**子组合选择器和同层组合选择器: `>`、`+`和`~`**:这三个必须和其他选择器配合使用，以指定浏览器仅选择某种特定上下文中的元素。

```scss
article {
  ~ article {
    border-top: 1px dashed #ccc;
  } // 同层全体组合选择器 ~ (不管它们之间隔了多少其他元素)
  > section {
    background: #eee;
  } // 下层相邻组合选择器 > (article下层紧邻的子元素section)
  dl > {
    dt {
      color: #333;
    }
    dd {
      color: #555;
    }
  }
  nav + & {
    margin-top: 0;
  } // 同层相邻组合选择器 + ( nav 后面紧跟着的 article元素)
}
/* 编译后 */
article ~ article {
  border-top: 1px dashed #ccc;
}
article > section {
  background: #eee;
}
article dl > dt {
  color: #333;
}
article dl > dd {
  color: #555;
}
nav + article {
  margin-top: 0;
}
```

**嵌套属性**的规则: 把属性名从中划线`-`的地方断开，在根属性后边添加一个冒号`:`，紧跟一个`{}`块，把子属性部分写在这个`{}`块中。

```scss
nav {
  border: 1px solid #ccc {
    left: 0px;
    right: 0px;
  }
}
/* 编译后 */
nav {
  border: 1px solid #ccc;
  border-left: 0px;
  border-right: 0px;
}
```

**导入 SASS 文件**: sass 的`@import`规则在**生成 css 文件时**就把相关文件导入进来。(css 中是执行到`@import`才去下载对应文件)

- 新版本已推荐使用`@use`规则从其他 Sass 样式表中加载 mixins、函数和变量，并将来自多个样式表的 CSS 组合在一起。

- sass 的`@import`规则并不需要指明被导入文件的全名。你可以省略`.sass`或`.scss`文件后缀
- **sass 局部文件的文件名以下划线开头**。这样，sass 就**不会**在编译时单独**编译**这个文件**输出 css**，而**只把这个文件用作导入**。
- 一般情况下，反复声明一个变量，**只有最后一处声明有效且它会覆盖前边的值**。
- 使用`!default`标签修饰变量: _如果这个变量被声明赋值了，那就用它声明的值，否则就用这个默认值。_
- **嵌套导入**: sass 允许`@import`命令写在 css 规则内。此时，生成对应的 css 文件时，**局部文件会被直接插入到 css 规则内导入它的地方**。
- **原生的 CSS 导入**:支持原生 CSS 导入，但这会造成浏览器解析 css 时的额外下载。**sass 的语法完全兼容 css，修改为`.scss`后缀名即可。**

**静默注释**: css 标准注释格式`/* ... */`的注释语法会出现在生成的 css 文件中,使用静默注释，_以`//`开头，注释内容直到行末_，则不会。

**混合器**: sass 的混合器使用`@mixin`标识符定义，通过`@include`来使用这个混合器。通过混合器实现**大段样式的重用**。

- 可以通过在`@include`混合器时给混合器传参，来*定制混合器生成的精确样式*。
  - 如果不记得参数顺序，可以使用语法`$name: value`的形式指定每个参数的值(此时就不关注参数顺序了)
  - 不必传入所有的参数，可以给参数指定一个默认值，所有未传值的参数都会被该值覆盖。

```scss
@mixin link-colors($normal, $hover, $visited) {
  color: $normal;
  &:hover {
    color: $hover;
  }
  &:visited {
    color: $visited;
  }
}
a {
  @include link-colors(blue, red, green);
}
a {
  @include link-colors($normal: blue, $visited: green, $hover: red);
}
/*编译后*/
a {
  color: blue;
}
a:hover {
  color: red;
}
a:visited {
  color: green;
}
```

**选择器继承**: 一个选择器可以继承为另一个选择器定义的所有样式。这个通过`@extend`语法实现，主要目的精简 CSS。

- **跟混合器相比，继承生成的 css 代码相对更少**。因为继承仅仅是重复选择器，而不会重复属性，所以*使用继承往往比混合器生成的 css 体积更小*。如果你非常关心你站点的速度，请牢记这一点。
- **继承遵从 css 层叠的规则**。当两个不同的 css 规则应用到同一个 html 元素上时，并且这两个不同的 css 规则对同一属性的修饰存在不同的值，css 层叠规则会决定应用哪个样式。相当直观：**通常权重更高的选择器胜出，如果权重相同，定义在后边的规则胜出。**
- 使用继承的最佳实践: **不要在 css 规则中使用后代选择器（比如.foo .bar）去继承 css 规则。**

```scss
//通过选择器继承继承样式
.error {
  border: 1px solid red;
  background-color: #fdd;
}
.seriousError {
  @extend .error;
  border-width: 3px;
}
/*编译后 .seriousError将会继承样式表中任何位置处为.error定义的所有样式。 */
.error,
.seriousError {
  border: 1px solid red;
  background-color: #fdd;
}
.seriousError {
  border-width: 3px;
}
```

如果`.seriousError @extend .error`， 那么样式表中的任何一处`.error`都用`.error .seriousError`这一选择器组进行替换。

**操作符**:Sass 支持一些有用的操作符来处理不同的值。这些包括标准的数学运算符，如`+`和`*`，以及各种其他类型的运算符。

```scss
@use "sass:math";
.container {
  display: flex;
}
article[role="main"] {
  width: math.div(600px, 960px) * 100%;
}
aside[role="complementary"] {
  width: math.div(300px, 960px) * 100%;
  margin-left: auto;
}
/**编译后 */
.container {
  display: flex;
}
article[role="main"] {
  width: 62.5%;
}
aside[role="complementary"] {
  width: 31.25%;
  margin-left: auto;
}
```

关键字入门: 预处理、变量、嵌套结构、局部文件、模块、混合器、继承、操作符

`$`变量声明，`&`父选择器标识符，`>`子组合选择器，`~`和`+`同层组合选择器，`@use`加载函数变量模块等，
`!default`修饰变量表示有默认值就用默认值没有就要新声明的值，`@mixin`声明混合器用`@include`导入使用，
`@extend`继承另一个选择器定义的样式。
