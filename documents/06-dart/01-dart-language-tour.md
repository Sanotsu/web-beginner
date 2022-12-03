<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [(〇)重要概念](#%E3%80%87%E9%87%8D%E8%A6%81%E6%A6%82%E5%BF%B5)
- [(一) 变量](#%E4%B8%80-%E5%8F%98%E9%87%8F)
  - [1 变量基础](#1-%E5%8F%98%E9%87%8F%E5%9F%BA%E7%A1%80)
    - [默认值](#%E9%BB%98%E8%AE%A4%E5%80%BC)
    - [late 变量](#late-%E5%8F%98%E9%87%8F)
    - [Final 和 Const](#final-%E5%92%8C-const)
  - [notes](#notes)
- [(二)内置类型](#%E4%BA%8C%E5%86%85%E7%BD%AE%E7%B1%BB%E5%9E%8B)
  - [Dart 语言支持下列内容](#dart-%E8%AF%AD%E8%A8%80%E6%94%AF%E6%8C%81%E4%B8%8B%E5%88%97%E5%86%85%E5%AE%B9)
  - [Numbers](#numbers)
  - [Strings](#strings)
  - [布尔类型](#%E5%B8%83%E5%B0%94%E7%B1%BB%E5%9E%8B)
  - [Lists](#lists)
  - [Sets](#sets)
  - [Maps](#maps)
  - [Runes 与 grapheme clusters](#runes-%E4%B8%8E-grapheme-clusters)
  - [Symbols](#symbols)
- [(三) 函数](#%E4%B8%89-%E5%87%BD%E6%95%B0)
  - [参数](#%E5%8F%82%E6%95%B0)
  - [main() 函数](#main-%E5%87%BD%E6%95%B0)
  - [函数是一级对象](#%E5%87%BD%E6%95%B0%E6%98%AF%E4%B8%80%E7%BA%A7%E5%AF%B9%E8%B1%A1)
  - [匿名函数](#%E5%8C%BF%E5%90%8D%E5%87%BD%E6%95%B0)
  - [词法作用域](#%E8%AF%8D%E6%B3%95%E4%BD%9C%E7%94%A8%E5%9F%9F)
  - [词法闭包](#%E8%AF%8D%E6%B3%95%E9%97%AD%E5%8C%85)
  - [测试函数是否相等](#%E6%B5%8B%E8%AF%95%E5%87%BD%E6%95%B0%E6%98%AF%E5%90%A6%E7%9B%B8%E7%AD%89)
  - [返回值](#%E8%BF%94%E5%9B%9E%E5%80%BC)
  - [notes](#notes-1)
- [(四)运算符](#%E5%9B%9B%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [算术运算符](#%E7%AE%97%E6%9C%AF%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [关系运算符](#%E5%85%B3%E7%B3%BB%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [类型判断运算符](#%E7%B1%BB%E5%9E%8B%E5%88%A4%E6%96%AD%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [赋值运算符](#%E8%B5%8B%E5%80%BC%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [逻辑运算符](#%E9%80%BB%E8%BE%91%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [按位和移位运算符](#%E6%8C%89%E4%BD%8D%E5%92%8C%E7%A7%BB%E4%BD%8D%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [条件表达式](#%E6%9D%A1%E4%BB%B6%E8%A1%A8%E8%BE%BE%E5%BC%8F)
  - [级联运算符](#%E7%BA%A7%E8%81%94%E8%BF%90%E7%AE%97%E7%AC%A6)
  - [其他运算符](#%E5%85%B6%E4%BB%96%E8%BF%90%E7%AE%97%E7%AC%A6)
- [(五) 控制流程语句](#%E4%BA%94-%E6%8E%A7%E5%88%B6%E6%B5%81%E7%A8%8B%E8%AF%AD%E5%8F%A5)
  - [基础控制流程语句](#%E5%9F%BA%E7%A1%80%E6%8E%A7%E5%88%B6%E6%B5%81%E7%A8%8B%E8%AF%AD%E5%8F%A5)
  - [note](#note)
- [(六) 类](#%E5%85%AD-%E7%B1%BB)
  - [使用类](#%E4%BD%BF%E7%94%A8%E7%B1%BB)
    - [使用类的成员](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E7%9A%84%E6%88%90%E5%91%98)
    - [使用构造函数](#%E4%BD%BF%E7%94%A8%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
    - [获取对象的类型](#%E8%8E%B7%E5%8F%96%E5%AF%B9%E8%B1%A1%E7%9A%84%E7%B1%BB%E5%9E%8B)
  - [实现一个类(类包含的东西)](#%E5%AE%9E%E7%8E%B0%E4%B8%80%E4%B8%AA%E7%B1%BB%E7%B1%BB%E5%8C%85%E5%90%AB%E7%9A%84%E4%B8%9C%E8%A5%BF)
    - [实例变量(Instance variables)](#%E5%AE%9E%E4%BE%8B%E5%8F%98%E9%87%8Finstance-variables)
    - [构造函数(constructors)](#%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0constructors)
      - [终值初始化](#%E7%BB%88%E5%80%BC%E5%88%9D%E5%A7%8B%E5%8C%96)
      - [默认构造函数](#%E9%BB%98%E8%AE%A4%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
      - [构造函数不被继承](#%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0%E4%B8%8D%E8%A2%AB%E7%BB%A7%E6%89%BF)
      - [命名式构造函数](#%E5%91%BD%E5%90%8D%E5%BC%8F%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
      - [调用父类非默认构造函数](#%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E9%9D%9E%E9%BB%98%E8%AE%A4%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
      - [初始化列表](#%E5%88%9D%E5%A7%8B%E5%8C%96%E5%88%97%E8%A1%A8)
      - [重定向构造函数](#%E9%87%8D%E5%AE%9A%E5%90%91%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
      - [常量构造函数](#%E5%B8%B8%E9%87%8F%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
      - [工厂构造函数](#%E5%B7%A5%E5%8E%82%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
    - [方法(Methods)](#%E6%96%B9%E6%B3%95methods)
      - [实例方法](#%E5%AE%9E%E4%BE%8B%E6%96%B9%E6%B3%95)
      - [操作符](#%E6%93%8D%E4%BD%9C%E7%AC%A6)
      - [Getter 和 Setter](#getter-%E5%92%8C-setter)
      - [抽象方法](#%E6%8A%BD%E8%B1%A1%E6%96%B9%E6%B3%95)
    - [抽象类(Abstract classes)](#%E6%8A%BD%E8%B1%A1%E7%B1%BBabstract-classes)
    - [隐式接口（Implicit interfaces）](#%E9%9A%90%E5%BC%8F%E6%8E%A5%E5%8F%A3implicit-interfaces)
    - [扩展（extends、继承）一个类](#%E6%89%A9%E5%B1%95extends%E7%BB%A7%E6%89%BF%E4%B8%80%E4%B8%AA%E7%B1%BB)
      - [重写(override)类成员](#%E9%87%8D%E5%86%99override%E7%B1%BB%E6%88%90%E5%91%98)
      - [noSuchMethod 方法](#nosuchmethod-%E6%96%B9%E6%B3%95)
    - [扩展方法(Extension methods)](#%E6%89%A9%E5%B1%95%E6%96%B9%E6%B3%95extension-methods)
    - [枚举类型](#%E6%9E%9A%E4%B8%BE%E7%B1%BB%E5%9E%8B)
      - [使用枚举](#%E4%BD%BF%E7%94%A8%E6%9E%9A%E4%B8%BE)
    - [使用 Mixin 为类添加功能](#%E4%BD%BF%E7%94%A8-mixin-%E4%B8%BA%E7%B1%BB%E6%B7%BB%E5%8A%A0%E5%8A%9F%E8%83%BD)
    - [类变量和方法(Class variables and methods)](#%E7%B1%BB%E5%8F%98%E9%87%8F%E5%92%8C%E6%96%B9%E6%B3%95class-variables-and-methods)
      - [静态变量](#%E9%9D%99%E6%80%81%E5%8F%98%E9%87%8F)
      - [静态方法](#%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95)
  - [(七) 泛型](#%E4%B8%83-%E6%B3%9B%E5%9E%8B)
    - [为什么使用泛型？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%BF%E7%94%A8%E6%B3%9B%E5%9E%8B)
    - [使用集合字面量(Using collection literals)](#%E4%BD%BF%E7%94%A8%E9%9B%86%E5%90%88%E5%AD%97%E9%9D%A2%E9%87%8Fusing-collection-literals)
    - [使用类型参数化的构造函数](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E5%9E%8B%E5%8F%82%E6%95%B0%E5%8C%96%E7%9A%84%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)
    - [泛型集合以及它们所包含的类型](#%E6%B3%9B%E5%9E%8B%E9%9B%86%E5%90%88%E4%BB%A5%E5%8F%8A%E5%AE%83%E4%BB%AC%E6%89%80%E5%8C%85%E5%90%AB%E7%9A%84%E7%B1%BB%E5%9E%8B)
    - [限制参数化类型](#%E9%99%90%E5%88%B6%E5%8F%82%E6%95%B0%E5%8C%96%E7%B1%BB%E5%9E%8B)
    - [使用泛型方法](#%E4%BD%BF%E7%94%A8%E6%B3%9B%E5%9E%8B%E6%96%B9%E6%B3%95)
  - [(八) 库和可见性(Libraries and visibility)](#%E5%85%AB-%E5%BA%93%E5%92%8C%E5%8F%AF%E8%A7%81%E6%80%A7libraries-and-visibility)
    - [使用库](#%E4%BD%BF%E7%94%A8%E5%BA%93)
    - [指定库前缀](#%E6%8C%87%E5%AE%9A%E5%BA%93%E5%89%8D%E7%BC%80)
    - [导入库的一部分](#%E5%AF%BC%E5%85%A5%E5%BA%93%E7%9A%84%E4%B8%80%E9%83%A8%E5%88%86)
    - [延迟加载(懒加载)库](#%E5%BB%B6%E8%BF%9F%E5%8A%A0%E8%BD%BD%E6%87%92%E5%8A%A0%E8%BD%BD%E5%BA%93)
  - [(九) 异步支持(Asynchrony support)](#%E4%B9%9D-%E5%BC%82%E6%AD%A5%E6%94%AF%E6%8C%81asynchrony-support)
    - [处理 Future](#%E5%A4%84%E7%90%86-future)
    - [声明异步函数](#%E5%A3%B0%E6%98%8E%E5%BC%82%E6%AD%A5%E5%87%BD%E6%95%B0)
    - [处理 Stream](#%E5%A4%84%E7%90%86-stream)
- [(十) 其他](#%E5%8D%81-%E5%85%B6%E4%BB%96)
  - [生成器](#%E7%94%9F%E6%88%90%E5%99%A8)
  - [可调用类](#%E5%8F%AF%E8%B0%83%E7%94%A8%E7%B1%BB)
  - [隔离区](#%E9%9A%94%E7%A6%BB%E5%8C%BA)
  - [Typedefs](#typedefs)
  - [元数据](#%E5%85%83%E6%95%B0%E6%8D%AE)
  - [注释](#%E6%B3%A8%E9%87%8A)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

官方[Dart 开发语言概览](https://dart.cn/guides/language/language-tour)的笔记

# (〇)重要概念

学习 Dart 语言时, 应该牢记以下几点

- 所有变量引用的都是 **对象**，每个对象都是一个 **类** 的实例。
  - 数字、函数以及 null 都是对象。除去 null 以外（如果你开启了 _空安全(Null safety)_）, 所有的类都继承于 Object 类。
- 尽管 Dart 是强类型语言，但是在声明变量时指定类型是可选的，因为 Dart 可以进行类型推断。
- 如果你开启了 _空安全_，变量在未声明为可空类型时不能为 null。
  - 你可以通过在类型后加上问号 (`?`) 将类型声明为可空。
    例如，int? 类型的变量可以是整形数字或 null。
  - 如果你 **明确知道** 一个表达式不会为空，但 Dart 不这么认为时，你可以在表达式后添加 `!` 来断言表达式不为空（为空时将抛出异常）。
    例如：`int x = nullableButNotNullInt!`
- 如果你想要显式地声明允许任意类型，使用 `Object?`（如果你 开启了空安全）、 `Object` 或者 `特殊类型 dynamic` 将检查延迟到运行时进行。
- Dart 支持泛型
  - 比如 `List<int>`（表示一组由 int 对象组成的列表）或 `List<Object>`（表示一组由任何类型对象组成的列表）。
- Dart 支持**顶级函数**（例如 main 方法），同时还支持定义属于类或对象的函数（即 静态 和 实例方法）。你还可以在函数中定义函数（嵌套 或 局部函数）。
- Dart 支持**顶级变量**，以及定义属于类或对象的变量（静态和实例变量）。实例变量有时称之为域或属性。
- Dart **没有**类似于 Java 那样的 public、protected 和 private 成员访问限定符。
  - 如果一个标识符以下划线 (`_`) 开头则表示该标识符*在库内是私有的*。
- _标识符_ 可以以字母或者下划线 (`_`) 开头，其后可跟字符和数字的组合。
- Dart 中 **表达式** 和 **语句** 是有区别的，**表达式有值而语句没有。**
  - 比如条件表达式 `expression condition ? expr1 : expr2` 中含有值 expr1 或 expr2。
  - 与 if-else 分支语句相比，if-else 分支语句则没有值。
  - _一个语句通常包含一个或多个表达式，但是一个表达式不能只包含一个语句_。
- Dart 工具可以显示 **警告** 和 **错误** 两种类型的问题。
  - 警告表明代码可能有问题但不会阻止其运行。
  - 错误分为编译时错误和运行时错误；
    - 编译时错误代码无法运行；
    - 运行时错误会在代码运行时导致*异常*。

# (一) 变量

## 1 变量基础

- 虽然 Dart 是代码类型安全的语言，但是由于其支持类型推断，因此大多数变量不需要显式地指定类型。
- 变量仅存储对象的引用。
- 通过 var 声明局部变量而非使用指定的类型。

```dart
/*
  - 这里名为 name 的变量存储了一个 String 类型对象的引用，“Bob” 则是该对象的值。
  - name 变量的类型被推断为 String，但是你可以为其指定类型。
  - 如果一个对象的引用不局限于单一的类型，可以将其指定为 Object（或 dynamic）类型。
  */
var name = 'Bob';
Object name = 'Bob';
String name = 'Bob';

var year = 1977;
var antennaDiameter = 3.7;
var flybyObjects = ['Jupiter', 'Saturn', 'Uranus', 'Neptune'];
var image = {
  'tags': ['saturn'],
  'url': '//path/to/saturn.jpg'
};
```

### 默认值

- 在 Dart 中，未初始化以及可空类型的变量拥有一个默认的初始值 null。（如果你未迁移至 空安全，所有变量都为可空类型。）即便数字也是如此，因为在 Dart 中一切皆为对象，数字也不例外。
- 如果启用 null 安全性，则必须在使用不可为 null 的变量之前初始化它们的值。
- assert() 的调用将会在生产环境的代码中被忽略掉。在开发过程中，assert(condition) 将会在 条件判断 为 false 时抛出一个异常。

```dart
int? lineCount;
assert(lineCount == null);
int lineCount = 0 ;
```

### late 变量

作用：

- 声明一个不可为空的变量，并在声明后被初始化。
- 懒惰(lazy)地初始化一个变量。

```dart
late String description;
```

### Final 和 Const

- 如果你不想更改一个变量，可以使用关键字 final 或者 const 修饰变量，
  - 这两个关键字可以替代 var 关键字或者加在一个具体的类型前。
- 一个 final 变量只可以被赋值一次；一个 const 变量是一个编译时常量（const 变量同时也是 final 的）。
- 顶层的 final 变量或者类的 final 变量在其第一次使用的时候被初始化。
- note： 实例变量 可以是 final 的但不可以是 const。
- 不能修改一个 final 变量的值。
- 使用关键字 const 修饰变量表示该变量为 编译时常量。
  - 如果使用 const 修饰类中的变量，则必须加上 static 关键字，即 static const（译者注：顺序不能颠倒）
- const 关键字不仅仅可以用来定义常量，还可以用来创建 常量值，该常量值可以赋予给任何变量。
- 常量的值不可以被修改。

```dart
final bname = 'Bob'; // Without a type annotation
final String nickname = 'Bobby';

// 如果使用初始化表达式为常量赋值可以省略掉关键字 const
const baz = []; // Equivalent to `const baz = const []`

// 没有使用 final 或 const 修饰的变量的值是可以被更改的，即使这些变量之前引用过 const 的值。
var foo = const [];

// 你可以在常量中使用 类型检查和强制类型转换 (is 和 as)、 集合中的 if 以及 展开操作符 (... 和 ...?)：
const Object i = 3; // Where i is a const Object with an int value...
const list = [i as int]; // Use a typecast.
const map = {if (i is int) i: 'int'}; // Use is and collection if.
const set = {if (list is List<int>) ...list}; // ...and a spread.

void main() {
  print('Hello, World!');
  print('变量： image is ${image}');
  print('变量： lineCount is ${lineCount}'); // 变量： lineCount is null

  description = '先声明了这个变量，但在使用的时候才给的值。';
  print(description);

  foo = [1, 2, 3]; // 之前是 const []，但因为不是使用final或者const声明，只是值为const，所以可以修改值
  print(foo); // [1, 2, 3]

  print(i); // 3
  print(list); // [3]
  print(map); // {3:int}
  print(set); // {3}
}
```

## notes

- 1 变量仅存储对象的引用。变量可以自动推断，一般不需要指定类型。如果变量不局限与一种类型，可声明为 Object 或者 dynamic 类型。
- 2 **dart 中一切皆为对象。未初始化以及可空类型的变量拥有一个默认的初始值 null**。
- 3 如果有先声明变量，lazy 地初始化，或者初始化变量成本较高地时候，可以使用 late 修饰变量。
- 4 final 修饰的变量不可修改， const 修饰的是一个编译时常量。const 变量同时也是 final。
- 4.1 可以在常量中使用类型检查（is）和类型转换（as），在常量集合（Set）中使用集合中的 if 以及 展开操作符。

# (二)内置类型

## Dart 语言支持下列内容

- Numbers (int, double)
- Strings (String)
- Booleans (bool)
- Lists (也被称为 arrays)
- Sets (Set)
- Maps (Map)
- Runes (常用于在 Characters API 中进行字符替换)
- Symbols (Symbol)
- null (Null)

其他一些类型在 Dart 语言中也有特殊的作用。

- `Object`：所有 Dart 类的超类，除了 Null。
- `Future` 和 `Stream`：在异步支持中使用。
- `Iterable`：在 for-in 循环和同步生成器函数中使用。
- `Never`：表示一个表达式永远无法成功完成评估。最常用于总是抛出一个异常的函数。
- `dynamic`：表示你想禁用静态检查。通常你应该使用 Object 或 Object?代替。
- `void`：表示一个值永远不会被使用。通常作为返回类型使用。

`Object`、`Object?`、`Null` 和 `Never` 类在类的层次结构中具有特殊的作用，正如在理解 null 安全的上下文中所描述的。

## Numbers

- `int`：整数值；长度不超过 64 位，具体取值范围 依赖于不同的平台。
- `double`：64 位的双精度浮点数字，且符合 IEEE 754 标准。
- int 和 double 都是 `num` 的子类。
  - num 中定义了一些基本的运算符(+ - \* / 等等)
  - 如果 num 及其子类不满足你的要求，可以查看 `dart:math` 库中的 API

## Strings

Dart 字符串（String 对象）包含了 UTF-16 编码的字符序列。

- 可以使用单引号或者双引号来创建字符串。
- 使用三个单引号或者三个双引号也能创建多行字符串
- **在字符串中，请以 `${表达式}` 的形式使用表达式，如果表达式是一个标识符，可以省略掉 `{}`**。
- 如果表达式的结果为一个对象，则 Dart 会调用该对象的 toString 方法来获取一个字符串。
- `==` 运算符负责判断两个对象的内容是否一样，如果两个字符串包含一样的字符编码序列，则表示相等。
- 在字符串前加上 `r` 作为前缀创建 “raw” 字符串（即不会被做任何处理（比如转义）的字符串）
- 字符串字面量是一个编译时常量，只要是编译时常量 (自注：const 的非引用类型？)(null、数字、字符串、布尔) 都可以作为字符串字面量的插值表达式

## 布尔类型

Dart 使用 bool 关键字表示布尔类型，布尔类型只有两个对象 `true` 和 `false`，两者都是编译时常量。

Dart 的类型安全不允许你使用类似` if (nonbooleanValue)` 或者 `assert (nonbooleanValue)` 这样的代码检查布尔值。相反，你应该总是显示地检查布尔值，比如像下面的代码这样：

```dart
// Check for an empty string.
var fullName = '';
assert(fullName.isEmpty);

// Check for zero.
var hitPoints = 0;
assert(hitPoints <= 0);

// Check for null.
var unicorn;
assert(unicorn == null);

// Check for NaN.
var iMeantToDoThis = 0 / 0;
assert(iMeantToDoThis.isNaN);
```

## Lists

数组 (Array) 是几乎所有编程语言中最常见的集合类型，在 Dart 中数组由 List 对象表示。通常称之为 List。

- List 的下标索引从 0 开始，第一个元素的下标为 0，最后一个元素的下标为 `list.length - 1`。
- 在 List 字面量前添加 const 关键字会创建一个编译时常量
- Dart 在 2.3 引入了 扩展操作符（`...`）和 空感知扩展操作符（`...?`），它们提供了一种将多个元素插入集合的简洁方法。

```dart
var list = [1, 2, 3];
// 这里 Dart 推断出 list 的类型为 List<int>，如果往该数组中添加一个非 int 类型的对象则会报错。
list.add("5"); // The argument type 'String' can't be assigned to the parameter type 'int'

// var list2 = [1, 2, 3, '4']; // List<Object>
var list3 = [0, ...list];
assert(list3.length == 4);  // list3現在为[0,1,2,3]

// 如果扩展操作符右边可能为 null ，你可以使用 null-aware 扩展操作符（...?）来避免产生异常：
var list4;
var list5=[0,...?list4];  // [0]
```

- Dart 还同时引入了**集合中的 if** 和 **集合中的 for** 操作，在**构建集合**时，可以使用条件判断 (if) 和循环 (for)。

```dart
// 集合中的 if 来创建一个 List 的示例，它可能包含 3 个或 4 个元素
var nav = [
  'Home',
  'Furniture',
  'Plants',
  if (promoActive) 'Outlet'
];

// 集合中的 for 将列表中的元素修改后添加到另一个列表中的示例
  var listOfInts = [1, 2, 3];
  var listOfStrings = ['#0', for (var i in listOfInts) '#$i'];
  print(listOfStrings); // [#0, #1, #2, #3]

```

_List 类中有许多用于操作 List 的便捷方法，你可以查阅 `泛型Generics` 和 `集合Collections` 获取更多与之相关的信息。_

更多查看[List API](https://api.dart.cn/stable/2.16.2/dart-core/List-class.html)

## Sets

在 Dart 中，set 是一组**特定元素的无序集合**。 Dart 支持的集合由`集合的字面量(set literals)`和 Set 类提供。

_尽管 **Set 类型(type)** 一直都是 Dart 的一项核心功能，但是 **Set 字面量(literals)** 是在 Dart 2.2 中才加入的。_

```dart
// 使用 Set 字面量来创建一个 Set 集合的方法：
var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};

// 创建空的set
var names = <String>{};
// Set<String> names = {}; // This works, too.
// var names = {}; // Creates a map, not a set. 因为先有的 Map 字面量语法，所以 {} 默认是 Map 类型。
```

**从 Dart 2.3 开始，Set 可以像 List 一样支持使用扩展操作符（`...` 和 `...?`）以及 集合中 `if` 和 `for` 操作。**

- 使用 `add()` 方法或 `addAll()` 方法向已存在的 Set 中添加项目。
- 使用 `.length` 可以获取 Set 中元素的数量。
- 可以在 Set 变量前添加 const 关键字创建一个 Set 编译时常量。

更多查看[Set API](https://api.dart.cn/stable/2.16.2/dart-core/Set-class.html)

```dart
final constantSet = const {
  'fluorine',
  'chlorine',
  'bromine',
  'iodine',
  'astatine',
};
// constantSet.add('helium'); // This line will cause an error.
```

## Maps

- 通常来说，Map 是用来关联 keys 和 values 的对象。其中键和值都可以是任何类型的对象。
- 每个 `key(键)` 只能出现一次但是 `value(值)` 可以重复出现多次。
- Dart 中 Map 提供了 Map 字面量以及 Map 类型两种形式的 Map。

**使用 Map 字面量创建 Map：**

```dart
// Dart 将 gifts 变量的类型推断为 Map<String, String>，而将 nobleGases 的类型推断为 Map<int, String>。
// 如果你向这两个 Map 对象中添加不正确的类型值，将导致运行时异常。
var gifts = {
  // Key:    Value
  'first': 'partridge',
  'second': 'turtledoves',
  'fifth': 'golden rings'
};

var nobleGases = {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};
```

**也可以使用 Map 的构造器创建 Map：**

- _也许你想使用 `new Map()` 构造 Map 对象。但是在 Dart 中，`new` 关键词是可选的。(译者注：且不被建议使用)_

```dart
// 在 Dart 中，new 关键词是可选的，且不被建议使用。
var gifts = Map<String, String>();
gifts['first'] = 'partridge';
gifts['second'] = 'turtledoves';
gifts['fifth'] = 'golden rings';

var nobleGases = Map<int, String>();
nobleGases[2] = 'helium';
nobleGases[10] = 'neon';
nobleGases[18] = 'argon';
```

在一个 Map 字面量前添加 const 关键字可以创建一个 Map 编译时常量：

```dart
final constantMap = const {
  2: 'helium',
  10: 'neon',
  18: 'argon',
};

// constantMap[2] = 'Helium'; // This line will cause an error.
```

Map 可以像 List 一样支持使用扩展操作符（`...` 和 `...?`）以及集合的 `if` 和 `for` 操作。

**list、set、map 的许多操作和 js 中的类似**

## Runes 与 grapheme clusters

在 Dart 中，`runes` 公开了字符串的 Unicode 码位。使用 `characters` 包 来访问或者操作用户感知的字符，也被称为 Unicode (扩展) `grapheme clusters`。

```dart
import 'package:characters/characters.dart';
...
var hi = 'Hi 🇩🇰';
print(hi);
print('The end of the string: ${hi.substring(hi.length - 1)}');
print('The last character: ${hi.characters.last}\n');
```

## Symbols

Symbol 表示 Dart 中声明的操作符或者标识符。

- 几乎不会需要 Symbol，但是它们对于那些通过名称引用标识符的 API 很有用，因为代码压缩后，尽管标识符的名称会改变，但是它们的 Symbol 会保持不变。

可以使用在标识符前加 # 前缀来获取 Symbol：

```dart
#radix
#bar
```

Symbol 字面量是编译时常量。

---

_**综合起来看，基本的类型和方法与 js 中的类似。**_

# (三) 函数

- Dart 是一种真正面向对象的语言，所以即便函数也是对象并且类型为 Function。
  - 这意味着函数可以被赋值给变量或者作为其它函数的参数。
  - 你也可以像调用函数一样调用 Dart 类的实例。
- `=>` (胖箭头) 简写语法用于仅包含一条语句的函数。该语法在将匿名函数作为参数传递时非常有用。
  - 语法 `=> 表达式` 是 `{ return 表达式; }` 的简写， `=>` 有时也称之为 **箭头函数**。

```dart
// 建议 为每个函数的参数以及返回值都指定类型
int fibonacci(int n) {
  if (n == 0 || n == 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}


// 在 => 与 ; 之间的只能是 表达式 而非 语句。
bool isEven(int number) => number % 2 == 0;

```

## 参数

- 必要参数 和 可选参数
  - **必要参数定义在参数列表前面，可选参数则定义在必要参数后面**。
  - 可选参数可以是 `命名的` 或 `位置的`。
- （简单理解：不是可选的位置参数就是必要参数）

- 命名参数

  - 定义函数时，使用 `{参数 1, 参数 2, …}` 来指定命名参数。
  - **命名参数默认为可选参数，除非他们被特别标记为 required**。

- 可选的位置参数

  - **使用 `[]` 将一系列参数包裹起来作为位置参数**。
  - 不用[]或者{}那就是必填的位置参数了。

- 默认参数值

  - 可以用 `=` 为函数的命名参数和位置参数定义默认值。
  - 默认值必须为编译时常量，没有指定默认值的情况下默认值为 null。
  - `List` 或 `Map` 同样也可以作为默认值。

- 可选位置参数和可选命名参数不能混合在一起使用，因为可选参数列表只能位于整个函数形参列表的最后。

```dart
void main(List<String> args) {
  print(say('111', '222', 'phone'));
  // 111 says 222 with a phone action is Smile
}

String say(String from, String msg, [String? device, String? action = "Smile"]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device action is $action';
  }
  return result;
}

```

## main() 函数

每个 Dart 程序都必须有一个 main() 顶级函数作为程序的入口， main() 函数返回值为 void 并且有一个 `List<String>` 类型的可选参数。

```dart
void main(List<String> arguments) {
  print(arguments);

  assert(arguments.length == 2);
  assert(int.parse(arguments[0]) == 1);
  assert(arguments[1] == 'test');
}
/*
将此部分代码保存为test.dart之后，在该文件的终端命令运行，例如
`dart .\test.dart 1 test`
则会输出参数数组：[1, test]
*/
```

## 函数是一级对象

- 可以将函数作为参数传递给另一个函数。
- 也可以将函数赋值给一个变量。

```dart
// 最常用的函数作为参数：forEach的参数
void printElement(int element) {
 print(element);
}
```

## 匿名函数

- 大多数函数都是有名字的，比如 `main()` 或 `printElement()`。
- 可以创建一个没有名字的函数，称之为 `匿名函数`、 `Lambda 表达式` 或 `Closure 闭包`。
  - 可以将匿名函数赋值给一个变量然后使用它，比如将该变量添加到集合或从中删除。
- 匿名函数看起来与命名函数类似，在括号之间可以定义参数，参数之间用逗号分割。
  - **如果函数体内只有一行返回语句，你可以使用胖箭头缩写法。**

后面大括号中的内容则为函数体：

```
([[类型] 参数[, …]]) {
  函数体;
};
```

```dart
// 定义了只有一个参数 item 且没有参数类型的匿名方法。
// List 中的每个元素都会调用这个函数，打印元素位置和值的字符串
const list = ['apples', 'bananas', 'oranges'];

list.forEach((item) {
  print('${list.indexOf(item)}: $item');
});
```

## 词法作用域

- Dart 是词法有作用域语言，变量的作用域在写代码的时候就确定了，大括号内定义的变量只能在大括号内访问，与 Java 类似。

```dart
bool topLevel = true;

void main() {
  var insideMain = true;

  void myFunction() {
    var insideFunction = true;

    void nestedFunction() {
      var insideNestedFunction = true;

      print(topLevel);
      print(insideMain);
      print(insideFunction);
      print(insideNestedFunction);
    }

    nestedFunction(); // 打印4个 true
  }

  myFunction();
}
//  nestedFunction() 函数可以访问包括顶层变量在内的所有的变量。
```

## 词法闭包

- 闭包 即一个函数对象，即使函数对象的调用在它原始作用域之外，依然能够访问在它词法作用域内的变量。
- 函数可以封闭定义到它作用域内的变量。

```dart
// 函数 makeAdder() 捕获了变量 addBy。
// 无论函数在什么时候返回，它都可以使用捕获的 addBy 变量。
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

void main() {
  // Create a function that adds 2.
  var add2 = makeAdder(2);

  // Create a function that adds 4.
  var add4 = makeAdder(4);

  print(add2(3) == 5);
  print(add4(3) == 7);
}
```

## 测试函数是否相等

下面是顶级函数(top-level functions)，静态方法(static methods)和实例方法(instance methods)相等性的测试示例。

```dart
void foo() {} // 一个顶级函数

class A {
  static void bar() {} // 一个静态方法
  void baz() {} // 一个实例方法
}

void main() {
  Function x;

  // 比较顶级方法。
  x = foo;
  print('1: ${foo == x}'); // 1: true

  // 比较静态方法。
  x = A.bar;
  print(A.bar == x); // true

  // 比较实例方法。
  var v = A(); // Instance #1 of A
  var w = A(); // Instance #2 of A
  var y = w;
  x = w.baz;

  // 这些闭包引用同一个实例（#2），因此它们是相等的。
  print(y.baz == x);

  // 这些闭包引用不同的实例，因此它们是不相等的。
  print(v.baz != w.baz);
}
```

## 返回值

- 所有的函数都有返回值。没有显示返回语句的函数最后一行默认为执行 `return null;`。

## notes

- 1 和 js 的函数基本类似，注意函数的命名参数和可选位置参数不能同时用。
- 2 每个函数都有返回值，如果是 `void`，则是省略了 `return null;`。
- 3 也是有闭包，注意闭包的两个主要目的即可：
  - 一个是可以在全局作用域中读取内部函数的的变量，
  - 另一个就是可以让闭包中引用的变量始终保存在内存中。
- 4 每个 Dart 程序都必须有一个` main()` 顶级函数作为程序的入口。

# (四)运算符

## 算术运算符

| 运算符  | 描述                                       |
| ------- | ------------------------------------------ |
| +       | 加                                         |
| –       | 减                                         |
| -表达式 | 一元负, 也可以作为反转（反转表达式的符号） |
| \*      | 乘                                         |
| /       | 除                                         |
| ~/      | 除并取整                                   |
| %       | 取模                                       |
| ++var   | var = var + 1 (表达式的值为 var + 1)       |
| var++   | var = var + 1 (表达式的值为 var)           |
| --var   | var = var – 1 (表达式的值为 var – 1)       |
| var--   | var = var – 1 (表达式的值为 var)           |

## 关系运算符

| 运算符 | 描述     |
| ------ | -------- |
| ==     | 相等     |
| !=     | 不等     |
| \>     | 大于     |
| \<     | 小于     |
| >=     | 大于等于 |
| <=     | 小于等于 |

**要判断两个对象(objects) x 和 y 是否表示相同的事物使用 `==` 即可。**

`==` 运算符的一些规则:

- 当 x 和 y 同时为空时返回 true，而只有一个为空时返回 false。
- 返回对 x 调用 `==` 方法的结果，参数为 y。（像 `==` 这样的操作符是对左侧内容进行调用的。)

## 类型判断运算符

`as`、`i`s、`is!` 运算符是在运行时判断对象类型的运算符。
| 运算符 | 描述 |
| ------ | -------- |
| as| 类型转换（也用作指定 类前缀)）|
| is| 如果对象是指定类型则返回 true|
| is!| 如果对象是指定类型则返回 false|

当且仅当 `obj` 实现了 T 的接口，`obj is T` 才是 true。

例如 `obj is Object` 总为 true，因为所有类都是 Object 的子类。  
仅当你确定这个对象是该类型的时候，你才可以使用 `as` 操作符可以把对象转换为特定的类型。

```dart
(employee as Person).firstName = 'Bob';

// 如果你不确定这个对象类型是不是 T，请在转型前使用 is T 检查类型。

if (employee is Person) {
  // Type check
  employee.firstName = 'Bob';
}

// 上述两种方式是有区别的：如果 employee 为 null 或者不为 Person 类型，则第一种方式将会抛出异常，而第二种不会。
```

## 赋值运算符

可以使用 `=` 来赋值，同时也可以使用 `??=` 来为值为 null 的变量赋值。

```dart
// Assign value to a
a = value;
// Assign value to b if b is null; otherwise, b stays the same
// b为null则赋值为value，否则还是b
b ??= value;
```

**`+=` 这样的赋值运算符将算数运算符和赋值运算符组合在了一起**  
| | | | | |
| ------ | -------- |-------- |-------- |-------- |
|= |\*= |%=| >>>=| ^=|
|+=| /=| <<=| &= |=|
|-=| ~/=| >>=|

eg:  
**`a op= b` ==> `a = a op b`**  
`a += b` ==> `a = a + b`

## 逻辑运算符

| 运算符  | 描述                                                      |
| ------- | --------------------------------------------------------- |
| !表达式 | 对表达式结果取反（即将 true 变为 false，false 变为 true） |
| \|\|    | 逻辑或                                                    |
| &&      | 逻辑与                                                    |

## 按位和移位运算符

在 Dart 中，二进制位运算符可以操作二进制的某一位，**但仅适用于整数**。
| 运算符 | 描述 |
| ------- | ----|
|& |按位与|
|\| |按位或|
|^| 按位异或|
|~表达式| 按位取反（即将 “0” 变为 “1”，“1” 变为 “0”）|
|<<| 位左移|
|>> |位右移|
|>>> |无符号右移|

**`>>>` 操作符在 2.14 以上的 Dart 版本 中可用。**

## 条件表达式

_条件 ? 表达式 1 : 表达式 2_  
如果条件为 true，执行表达式 1 并返回执行结果，否则执行表达式 2 并返回执行结果。

_表达式 1 ?? 表达式 2_  
如果表达式 1 为非 null 则返回其值，否则执行表达式 2 并返回其值。

```dart
// 根据布尔表达式确定赋值时，请考虑使用 ? 和 :
var visibility = isPublic ? 'public' : 'private';

// 如果赋值是根据判定是否为 null 则考虑使用 ??。
String playerName(String? name) => name ?? 'Guest';
```

## 级联运算符

级联运算符 (**`..`** 和 **`?..`**) 可以**在同一个对象上连续调用多个对象的变量或方法。**

```dart
var paint = Paint()
  ..color = Colors.black
  ..strokeCap = StrokeCap.round
  ..strokeWidth = 5.0;

// 构造函数Paint()返回一个Paint对象。级联符号后面的代码对该对象进行操作，忽略任何可能返回的值。
// 等价于：
var paint = Paint();
paint.color = Colors.black;
paint.strokeCap = StrokeCap.round;
paint.strokeWidth = 5.0;
```

## 其他运算符

| 运算符 | 名字         | 描述                                                                                                                   |
| ------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| ()     | 使用方法     | 代表调用一个方法                                                                                                       |
| []     | 访问 List    | 访问 List 中特定位置的元素                                                                                             |
| ?[]    | 判空访问     | List 左侧调用者不为空时，访问 List 中特定位置的元素                                                                    |
| .      | 访问成员     | 成员访问符                                                                                                             |
| ?.     | 条件访问成员 | 与上述成员访问符类似，但是左边的操作对象不能为 null。<br/>例如 `foo?.bar`，如果 foo 为 null 则返回 null ，否则返回 bar |

# (五) 控制流程语句

## 基础控制流程语句

- if else
  - 不同于 JavaScript，Dart 的 if 语句中的条件必须是布尔值而不能为其它类型。
- for、
  - for 循环中的闭包会自动捕获循环的 索引值 以避免 JavaScript 中一些常见的陷阱。
- for in
  - 如果要遍历的对象是一个可迭代对象（例如 List 或 Set），并且你不需要知道当前的遍历索引，则可以使用 for-in 方法进行 遍历。
- forEach
  - 可迭代对象同时可以使用 forEach() 方法作为另一种选择。
- while
  - while 循环会在执行循环体前先判断条件。
  - do-while 循环则会 先执行一遍循环体 再判断条件。
- Break 和 Continue
  - 使用 break 可以中断循环。
  - 使用 continue 可以跳过本次循环直接进入下一次循环。
- Switch 和 Case
  - Dart 中的 Switch 语句仅适用于有限的情况，比如使用解释器和扫描器的场景。
  - 每一个非空的 case 子句都必须有一个 break 语句，也可以通过 continue、throw 或者 return 来结束非空 case 语句。
- 断言 Assert
  - 在开发过程中，可以在条件表达式为 false 时使用 _`assert(条件, 可选信息);`_ 语句来打断代码的执行。
  - assert 的第一个参数可以是值为布尔值的任何表达式。
    - 如果表达式的值为 true，则断言成功，继续执行。
    - 如果表达式的值为 false，则断言失败，抛出一个 `AssertionError` 异常。
- 异常
  - Dart 的所有异常都是非必检异常，方法不必声明会抛出哪些异常，并且你也不必捕获任何异常。
  - Dart 提供了 `Exception` 和 `Error` 两种类型的异常以及它们一系列的子类，也可以定义自己的异常类型。
  - `throw` 异常
  - `try on catch finally` 异常
  - `rethrow` 异常

```dart
void baseControlTest() {
  var year = 2021;
  var number = 100;
  var flybyObjects = [1, 2, 3];

// Dart 的 if 语句中的条件必须是布尔值而不能为其它类型。
  if (year >= 2001) {
    print('21st century');
  } else if (year >= 1901) {
    print('20th century');
  }

// 基本for循环
  // for (int month = 1; month <= 12; month++) {
  //   print(month);
  // }

// 在 Dart 语言中，for 循环中的闭包会自动捕获循环的 索引值 以避免 JavaScript 中一些常见的陷阱。
// 这个代码在js会打印2 2
  var callbacks = [];
  for (var i = 0; i < 2; i++) {
    callbacks.add(() => print(i));
  }
  callbacks.forEach((c) => c());

// 遍历的对象是一个可迭代对象（例如 List 或 Set），并且你不需要知道当前的遍历索引，可以使用for in
  for (final object in flybyObjects) {
    print(object);
  }

// while 循环会在执行循环体前先判断条件：
  while (year < 2016) {
    year += 1;
  }
  print("year is $year"); // 2021

// do-while 循环则会 先执行一遍循环体 再判断条件
  do {
    number += 1;
  } while (number < 60);

  print("year is $number"); // 101

// 使用 break 可以中断循环
// 使用 continue 可以跳过本次循环直接进入下一次循环
  for (int i = 0; i < 100; i++) {
    if (i < 5) {
      continue;
    }
    if (i >= 10) {
      break;
    }
    print("i is $i"); // 5 6 7 8 9
  }

  // Switch 语句在 Dart 中使用 == 来比较整数、字符串或编译时常量，
  // 比较的两个对象必须是同一个类型且不能是子类并且没有重写 == 操作符。
  // 枚举类型非常适合在 Switch 语句中使用。

  // 每一个非空的 case 子句都必须有一个 break 语句，
  // 也可以通过 continue、throw 或者 return 来结束非空 case 语句。
  // 不匹配任何 case 语句的情况下，会执行 default 子句中的代码。
  var command = 'OPEN';
  switch (command) {
    case 'CLOSED': // 支持空的 case 语句，允许其以 fall-through 的形式执行。
    // break;               // 如果输入的是CLOSED，有break，直接返回。沒有break，返回PENDING的执行。
    case 'PENDING':
      print("executePending()");
      break;
    case 'APPROVED': // 非空 case 语句中想要实现 fall-through 的形式，可以使用 continue 语句配合 label 的方式实现:
      print("executeApproved()");
      continue nowApproved;
    case 'DENIED':
      print("executeDenied()");
      break;
    nowApproved:
    case 'OPEN': // Runs for both APPROVED and OPEN.
      print("executeOpen()");
      break;
    default:
      print("executeUnknown()");
  }

  // 在开发过程中，可以在条件表达式为 false 时使用 — assert(条件, 可选信息); — 语句来打断代码的执行。
  // 第二个参数可以为其添加一个字符串消息。
  var text, num, urlString;
  // Make sure the variable has a non-null value.
  assert(text != null);

// Make sure the value is less than 100.
  assert(num < 100);

// Make sure this is an https URL.
  assert(urlString.startsWith('https'),
      'URL ($urlString) should start with "https".');

  // assert 的第一个参数可以是值为布尔值的任何表达式。如果表达式的值为 true，则断言成功，继续执行。
  // 如果表达式的值为 false，则断言失败，抛出一个 AssertionError 异常。
}

// Dart 代码可以抛出和捕获异常。
// 与 Java 不同的是，Dart 的所有异常都是非必检异常，方法不必声明会抛出哪些异常，并且你也不必捕获任何异常。
void distanceTo(int other) => throw UnimplementedError("异常信息");

void misbehave() {
  try {
    dynamic foo = true;
    print(foo++); // Runtime error
  } on NoSuchMethodError catch (e) {
    // 使用 on 来指定异常类型，使用 catch 来捕获异常对象，两者可同时使用。
    print('NoSuchMethodError: $e');
    // 关键字 rethrow 可以将捕获的异常再次抛出
    rethrow; // Allow callers to see the exception.
  } catch (e) {
    // 如果 catch 语句没有指定异常类型则表示可以捕获任意异常类型(在上面已经catch了，就不会到这里了)
    print('misbehave() partially handled ${e.runtimeType}.');
    // 关键字 rethrow 可以将捕获的异常再次抛出
    rethrow; // Allow callers to see the exception.
  } finally {
    // 无论是否抛出异常，finally 语句始终执行，
    // 如果没有指定 catch 语句来捕获异常，则异常会在执行完 finally 语句后抛出
    print("无论如何，都会执行在finally");
  }
}

void main() {
  baseControlTest();
  var text;
  assert(text != null);

  try {
    misbehave();
  } catch (e) {
    print('main() finished handling ${e.runtimeType}.');
  }
}
```

## note

- 和在 js 中的常用控制语句用法基本一致，沒什么特殊的。

# (六) 类

## 使用类

- Dart 是支持基于 mixin 继承机制的面向对象语言。
- 所有对象都是一个类的实例，而除了 Null 以外的所有的类都继承自 Object 类。
- `基于 mixin 的继承` 意味着尽管每个类（顶层类 `Object?` 除外）都只有一个超类。
- 一个类的代码可以在其它多个类继承中重复使用。

- 扩展方法(Extension methods) 是一种在不更改类或创建子类的情况下向类添加功能的方式。

### 使用类的成员

- 对象的 成员 由函数和数据（即 `方法(methods)` 和 `实例变量(instance variables)`）组成。
- 方法的 调用 要通过对象来完成，这种方式可以访问对象的函数和数据。
- 使用（`.`）来访问对象的实例变量或方法。
- 使用 `?.` 代替 `.` 可以避免因为左边表达式为 null 而导致的问题

```dart
var p = Point(2, 2);

// Get the value of y.
assert(p.y == 2);

// Invoke distanceTo() on p [调用实例p上的distanceTo()方法].
double distance = p.distanceTo(Point(4, 4));
// If p is non-null, set a variable equal to its y value.
var a = p?.y;
```

### 使用构造函数

可以使用 **构造函数** 来创建一个对象。构造函数的命名方式可以为 _`类名`_ 或 _`类名.标识符`_ 的形式。例如下述代码分别使用 `Point()` 和 `Point.fromJson()` 两种构造器创建了 Point 对象：

```dart
var p1 = Point(2, 2);
var p2 = Point.fromJson({'x': 1, 'y': 2});
```

以下代码具有相同的效果，但是*构造函数名前面的的 new 关键字是可选的*(最好不用)：

```dart
var p1 = new Point(2, 2);
var p2 = new Point.fromJson({'x': 1, 'y': 2});
```

一些类提供了【**常量构造函数**】(如果类生成的对象都是不变的，可以在生成这些对象时就将其变为编译时常量。)。使用常量构造函数，在构造函数名之前加 const 关键字，来创建编译时常量时：

```dart
var p = const ImmutablePoint(2, 2);
```

两个使用相同构造函数相同参数值构造的编译时常量是同一个对象：

```dart
var a = const ImmutablePoint(1, 1);
var b = const ImmutablePoint(1, 1);

assert(identical(a, b)); // They are the same instance!
```

**在 _常量上下文_ 场景中，你可以省略掉构造函数或字面量前的 const 关键字。**

例如下面的例子中我们创建了一个常量 Map：

```dart
// Lots of const keywords here.
const pointAndLine = const {
  'point': const [const ImmutablePoint(0, 0)],
  'line': const [const ImmutablePoint(1, 10), const ImmutablePoint(-2, 11)],
};
// 根据上下文，你可以只保留第一个 const 关键字，其余的全部省略：

// Only one const, which establishes the constant context.
const pointAndLine = {
  'point': [ImmutablePoint(0, 0)],
  'line': [ImmutablePoint(1, 10), ImmutablePoint(-2, 11)],
};
```

**但是如果无法根据上下文判断是否可以省略 const，则不能省略掉 const 关键字，否则将会创建一个 非常量对象**。

例如：

```dart
var a = const ImmutablePoint(1, 1); // Creates a constant
var b = ImmutablePoint(1, 1); // Does NOT create a constant

assert(!identical(a, b)); // NOT the same instance!
```

### 获取对象的类型

可以使用 `Object 对象的 runtimeType 属性`在运行时获取一个对象的类型，该对象类型是 Type 的实例。

```dart
print('The type of a is ${a.runtimeType}');
```

在生产环境使用**类型判断运算符**：

- `as`[类型转换（也用作指定 类前缀)）]、
- `is`[如果对象是指定类型则返回 true]、
- `is!`[如果对象是指定类型则返回 false]。

运算符是在运行时判断对象类型的运算符。

## 实现一个类(类包含的东西)

### 实例变量(Instance variables)

下面是声明实例变量的示例：

```dart
class Point {
  double? x; // Declare instance variable x, initially null.
  double? y; // Declare y, initially null.
  double z = 0; // Declare z, initially 0.
}
```

**所有未初始化的实例变量其值均为 null。**  
**所有实例变量均会隐式地声明一个 Getter 方法。**
**非终值(non-final)的实例变量和 late final 声明但未声明初始化的实例变量还会隐式地声明一个 Setter 方法。**

```dart
void main() {
  var point = Point();
  point.x = 4; // Use the setter method for x.
  assert(point.x == 4); // Use the getter method for x.
  assert(point.y == null); // Values default to null.
}
```

如果实例变量是 `final` 的，那就必须初始化。  
在声明时，使用构造函数参数或使用构造函数的初始化器列表初始化 `final`、`non-late` 实例变量。

```dart
class ProfileMark {
  final String name;
  final DateTime start = DateTime.now();    // 直接初始化

  ProfileMark(this.name);
  ProfileMark.unnamed() : name = '';    // 使用构造函数初始化列表 （constructor’s initializer list）初始化
}
```

### 构造函数(constructors)

- 声明一个与类名一样的函数即可声明一个构造函数
- （对于命名式构造函数 还可以添加额外的标识符）。
- 大部分的构造函数形式是生成式构造函数，**其用于创建一个类的实例**。

#### 终值初始化

Dart 则提供了一种特殊的语法糖来简化该步骤。
构造中初始化的参数可以用于初始化非空或 final 修饰的变量，它们都必须被初始化或提供一个默认值。

```dart
class Point {
  double x = 0;
  double y = 0;

/*
// 使用 this 关键字引用当前实例
  Point(double x, double y) {
    this.x = x;
    this.y = y;
  }
  */
// 语法糖方式
   Point(this.x, this.y);
}
```

#### 默认构造函数

如果你没有声明构造函数，那么 Dart 会自动生成一个无参数的构造函数并且该构造函数会调用其父类的无参数构造方法。

#### 构造函数不被继承

子类不会继承父类的构造函数，如果子类没有声明构造函数，那么只会有一个默认无参数的构造函数。

#### 命名式构造函数

可以为一个类声明多个命名式构造函数来表达更明确的意图。

```dart
const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  double x = 0;
  double y = 0;

  Point(this.x, this.y);

  // Named constructor
  Point.origin()
      : x = xOrigin,
        y = yOrigin;
}
```

构造函数是不能被继承的，这将意味着子类不能继承父类的命名式构造函数，  
如果你想在子类中提供一个与父类命名构造函数名字一样的命名构造函数，则需要在子类中显式地声明。

#### 调用父类非默认构造函数

**默认情况下，子类的构造函数会调用父类的匿名无参数构造方法**，并且该调用会在子类构造函数的函数体代码执行前，  
如果子类构造函数还有一个 初始化列表，那么该初始化列表会在调用父类的该构造函数之前被执行，  
总的来说，这三者的调用顺序如下：

- 初始化列表
- 父类的无参数构造函数
- 当前类的构造函数

**如果父类没有匿名无参数构造函数，那么子类必须调用父类的其中一个构造函数。**

- _为子类的构造函数指定一个父类的构造函数只需在构造函数体前使用（:）指定。_

```dart
class Person {
  String? firstName;

  Person.fromJson(Map data) {
    print('in Person');
  }
}

class Employee extends Person {
  // Person does not have a default constructor;
  // you must call super.fromJson(data).
  // 为子类的构造函数指定一个父类的构造函数，在子类构造函数加个 【： 父类构造函数】 即可
  Employee.fromJson(Map data) : super.fromJson(data) {
    print('in Employee');
  }
}

void main() {
  var employee = Employee.fromJson({});
  print(employee);
  // Prints:
  // in Person
  // in Employee
  // Instance of 'Employee'
}
```

**请注意:**

传递给父类构造函数的参数不能使用 this 关键字。

- 因为在参数传递的这一步骤，子类构造函数尚未执行，子类的实例对象也就还未初始化，因此所有的实例成员都不能被访问，但是类成员可以。

#### 初始化列表

除了调用父类构造函数之外，还可以在构造函数体执行之前初始化实例变量。每个实例变量之间使用逗号分隔。

```dart
// Initializer list sets instance variables before
// the constructor body runs.
Point.fromJson(Map<String, double> json)
    : x = json['x']!,
      y = json['y']! {
  print('In Point.fromJson(): ($x, $y)');
}
```

**请注意:**

初始化列表表达式 = 右边的语句不能使用 this 关键字。

```dart
// 使用初始化列表设置 final 字段非常方便，下面的示例中就使用初始化列表来设置了三个 final 变量的值。
import 'dart:math';

class Point {
  final double x;
  final double y;
  final double distanceFromOrigin;

  Point(double x, double y)
      : x = x,
        y = y,
        distanceFromOrigin = sqrt(x * x + y * y);
}

void main() {
  var p = Point(2, 3);
  print(p.distanceFromOrigin);  // 3.605551275463989
}
```

#### 重定向构造函数

有时候**类中的构造函数仅用于调用类中其它的构造函数**，  
此时该构造函数没有函数体，只需**在函数签名后使用（:）指定需要重定向到的其它构造函数 (使用 this 而非类名)**：

```dart
class Point {
  double x, y;

  // The main constructor for this class.
  Point(this.x, this.y);

  // Delegates to the main constructor.
  // 委托给主构造函数。
  Point.alongXAxis(double x) : this(x, 0);
}
```

#### 常量构造函数

如果类生成的对象都是不变的，可以在生成这些对象时就将其变为编译时常量。  
可以在类的构造函数前加上 const 关键字并确保所有实例变量均为 final 来实现该功能。

```dart
class ImmutablePoint {
  static const ImmutablePoint origin = ImmutablePoint(0, 0);

  final double x, y;

  const ImmutablePoint(this.x, this.y);
}
```

#### 工厂构造函数

使用 `factory` 关键字标识类的构造函数将会令该构造函数变为工厂构造函数，这将意味着使用该构造函数构造类的实例时并非总是会返回新的实例对象。

**在工厂构造函数中无法访问 this。**

例如，工厂构造函数可能会从缓存中返回一个实例，或者返回一个子类型的实例。

```dart
class Logger {
  final String name;
  bool mute = false;

  // _cache 是私有变量，因为前缀 _ 的缘故。
  static final Map<String, Logger> _cache = <String, Logger>{};

 // Logger 的工厂构造函数从缓存中返回对象，和 Logger.fromJson 工厂构造函数从 JSON 对象中初始化一个最终变量。
  factory Logger(String name) {
    return _cache.putIfAbsent(
        name, () => Logger._internal(name));
  }

  factory Logger.fromJson(Map<String, Object> json) {
    return Logger(json['name'].toString());
  }

  Logger._internal(this.name);

  void log(String msg) {
    if (!mute) print(msg);
  }
}
```

### 方法(Methods)

方法是为对象提供行为的函数(Methods are functions that provide behavior for an object.)。

#### 实例方法

对象的实例方法可以访问实例变量和 this。

```dart
import 'dart:math';

class Point {
  double x = 0;
  double y = 0;

  Point(this.x, this.y);

  // distanceTo() 方法就是一个实例方法
  double distanceTo(Point other) {
    var dx = x - other.x;
    var dy = y - other.y;
    return sqrt(dx * dx + dy * dy);
  }
}
```

#### 操作符

运算符是有着特殊名称的实例方法。

Dart 允许使用以下名称定义运算符:
| | |||
| :----: | :----: |:----: |:----: |
|< |+| \| |>>>|
|> |/| ^ |[]|
|<= |~/| & |[]=|
|>= |\*| <<| ~|
|– |%| >>| ==|

**为了表示重写操作符，使用 `operator` 标识来进行标记。**

```dart
class Vector {
  final int x, y;

  Vector(this.x, this.y);

// 把+ - 重寫为向量的+ -
  Vector operator +(Vector v) => Vector(x + v.x, y + v.y);
  Vector operator -(Vector v) => Vector(x - v.x, y - v.y);

  // Operator == and hashCode not shown.
  // ···
}

void main() {
  final v = Vector(2, 3);
  final w = Vector(2, 2);

  assert(v + w == Vector(4, 5));
  assert(v - w == Vector(0, 1));
}
```

#### Getter 和 Setter

- `Getter` 和 `Setter` 是一对用来读写对象属性的特殊方法，
- 实例对象的每一个属性都有一个隐式的 `Getter` 方法，如果为非 `final` 属性的话还会有一个 Setter 方法，
- 可以使用 `get` 和 `set` 关键字为额外的属性添加 `Getter` 和 `Setter` 方法。
  - 使用 `Getter` 和 `Setter` 的好处是，你可以先使用你的实例变量，过一段时间过再将它们包裹成方法且不需要改动任何代码，即先定义后更改且不影响原有逻辑。
  - 像自增（`++`）这样的操作符不管是否定义了 `Getter` 方法都会正确地执行。
  - 为了避免一些不必要的异常情况，运算符只会调用 `Getter` 一次，然后将其值存储在一个临时变量中。

```dart
class Rectangle {
  double left, top, width, height;

  Rectangle(this.left, this.top, this.width, this.height);

  // Define two calculated properties: right and bottom.
  double get right => left + width;
  set right(double value) => left = value - width;
  double get bottom => top + height;
  set bottom(double value) => top = value - height;
}

void main() {
  var rect = Rectangle(3, 4, 20, 15);
  assert(rect.left == 3);
  rect.right = 12;
  assert(rect.left == -8);
}
```

#### 抽象方法

抽象方法就是以 abstract 修饰的方法，这种方法只声明返回的数据类型、方法名称和所需的参数，没有方法体，也就是说**抽象方法只需要声明而不需要实现**。

**当一个方法为抽象方法时，意味着这个方法必须被子类的方法所重写，否则其子类的该方法仍然是 abstract 的**，而这个子类也必须是抽象的，即声明为 abstract。

- 实例方法、Getter 方法以及 Setter 方法都可以是抽象的，
- 定义一个接口方法而不去做具体的实现让实现它的类去实现该方法，
- **抽象方法只能存在于*抽象类*中**,
- 直接使用分号（`;`）替代方法体即可声明一个抽象方法

```dart
abstract class Doer {
  // Define instance variables and methods...

  void doSomething(); // Define an abstract method.
}

class EffectiveDoer extends Doer {
  void doSomething() {
    // Provide an implementation, so the method is not abstract here...
  }
}
```

### 抽象类(Abstract classes)

- 使用关键字 `abstract` 标识类可以让该类成为 抽象类，
- 抽象类将无法被实例化。
- 抽象类常用于声明接口方法、有时也会有具体的方法实现。
- 如果想让抽象类同时可被实例化，可以为其定义 工厂构造函数。
- 抽象类常常会包含抽象方法。

```dart
// 该类被声明为抽象类，因此无法实例化。
abstract class AbstractContainer {
  // Define constructors, fields, methods...

  void updateChildren(); // 抽象方法。
}
```

### 隐式接口（Implicit interfaces）

- **每一个类都隐式地定义了一个接口并实现了该接口，这个接口包含所有这个类的实例成员以及这个类所实现的其它接口。**
  - 也就是说，当我们定义了一个类的时候，同时就会产生一个和此类同名的接口，而且此接口包含了我们定义的类中所有的方法，以及它的成员变量。
- 如果想要创建一个 A 类支持调用 B 类的 API 且不想继承 B 类，则可以实现 B 类的接口。
- 一个类可以通过关键字 `implements` 来**实现一个或多个接口并实现每个接口定义的 API**。
  - 如果需要**实现多个类接口**，可以使用逗号分割每个接口类。

```dart
/**
 * 隐式接口
 *
 * 库和可见性(Libraries and visibility)说明：
 * import 和 library 关键字可以帮助你创建一个模块化和可共享的代码库。
 * 代码库不仅只是提供 API 而且还起到了封装的作用：以下划线（_）开头的成员仅在代码库中可见。
 * 每个 Dart 程序都是一个库，即便没有使用关键字 library 指定。
 */

// Person类，隐式接口 greet().
class Person {
  // 库中可见的私有变量 _name
  final String _name;

  // 构造函数
  Person(this._name);

  // 库中的方法
  String greet(String who) => 'Hello, $who. I am $_name.';
}

// An implementation of the Person interface.Person接口的实现。
class Impostor implements Person {
  String get _name => '';
  String greet(String who) => 'Hi $who. Do you know who I am?';
}

String greetBob(Person person) => person.greet('Bob');

void main() {
  var p = Person('张三'); // 张三
  print(p._name);
  print(p.greet("李四")); // Hello, 李四. I am 张三.

  print(greetBob(Person('Kathy'))); // Hello, Bob. I am Kathy.
  print(greetBob(Impostor())); // Hi Bob. Do you know who I am?
}
```

### 扩展（extends、继承）一个类

**Dart 支持单继承。**

使用 extends 关键字来创建一个子类，并可使用 super 关键字引用一个父类

```dart
class Television {
  void turnOn() {
    _illuminateDisplay();
    _activateIrSensor();
  }
  // ···
}

class SmartTelevision extends Television {
  void turnOn() {
    super.turnOn();
    _bootNetworkInterface();
    _initializeMemory();
    _upgradeApps();
  }
  // ···
}
```

#### 重写(override)类成员

- 子类可以重写父类的实例方法（包括 操作符）、 Getter 以及 Setter 方法。
  - 可以使用 `@override` 注解来表示你重写了一个成员.
- 一个重写方法的声明必须在几个方面与它所重新的方法（或方法）相匹配:
  - **返回类型**必须与被重写方法的返回类型相同（或为其子类型）。
  - **参数类型**必须与被重写方法的参数类型相同（或者是超类型）。
  - 如果被重写的方法接受 **n 个位置参数**，那么被重写的方法也必须接受 n 个位置参数。
  - 一个泛型方法不能重写一个非泛型方法，而一个非泛型方法也不能重写一个泛型方法。
- **注意：如果重写 `==` 操作符，必须同时重写对象 hashCode 的 Getter 方法。**
- 可以使用 `covariant` 关键字 来缩小代码中那些符合 `类型安全` 的方法参数或实例变量的类型。

```dart
class Television {
  // ···
  set contrast(int value) {...}
}

class SmartTelevision extends Television {
  @override
  set contrast(num value) {...}
  // ···
}
```

#### noSuchMethod 方法

如果调用了对象上不存在的方法或实例变量将会触发 `noSuchMethod` 方法。

可以重写 `noSuchMethod` 方法来追踪和记录这一行为。

```dart
class A {
  // 除非重写noSuchMethod，否则使用不存在的成员会导致NoSuchMethodError。
  @override
  void noSuchMethod(Invocation invocation) {
    print('You tried to use a non-existent member: '
        '${invocation.memberName}');
  }
}
```

**只有下面其中一个条件成立时，你才能调用一个未实现的(unimplemented)方法：**

- 接收方(receiver)是静态的 `dynamic` 类型。
- 接收方(receiver)具有静态类型，定义了未实现的方法（抽象亦可），并且接收方的动态类型实现了 `noSuchMethod` 方法且具体的实现与 `Object` 中的不同。

### 扩展方法(Extension methods)

**扩展方法是向现有库添加功能的一种方式。** 可能已经在不知道它是扩展方法的情况下使用了它。

[Extension methods](https://dart.dev/guides/language/extension-methods)

### 枚举类型

枚举类型是一种特殊的类型，也称为 `enumerations` 或 `enums`，用于定义一些固定数量的常量值。

#### 使用枚举

- 使用关键字 `enum` 来定义枚举类型
  - 可以在声明枚举类型时使用 尾随逗号(最后一个值后面加了逗号)
- 每一个枚举值都有一个名为 `index` 成员变量的 `Getter` 方法，该方法将会返回以 `0` 为基准索引的位置值。
- 想要获得全部的枚举值，使用枚举类的 `values` 方法获取包含它们的列表。
- 可以在 `Switch` 语句中使用枚举
  - 但是需要注意的是必须处理枚举值的每一种情况，即每一个枚举值都必须成为一个 case 子句，不然会出现警告。

```dart
enum Color { red, green, blue }

var aColor = Color.blue;

switch (aColor) {
  case Color.red:
    print('Red as roses!');
    break;
  case Color.green:
    print('Green as grass!');
    break;
  default: // Without this, you see a WARNING.
    print(aColor); // 'Color.blue'
}
```

**枚举类型有如下两个限制**：

- 枚举不能成为子类，也不可以 `mix in`，你也不可以实现一个枚举。
- 不能显式地实例化一个枚举类。

### 使用 Mixin 为类添加功能

Mixin 是一种在多重继承中复用某个类中代码的方法模式。  
（dart 是单继承多实现，使用 mixin 可以多重继承）

使用 `with` 关键字并在其后跟上 Mixin 类的名字来使用 Mixin 模式

```dart
class Musician extends Performer with Musical {
  // ···
}

class Maestro extends Person with Musical, Aggressive, Demented {
  Maestro(String maestroName) {
    name = maestroName;
    canConduct = true;
  }
}
```

想要实现一个 Mixin，请创建**一个继承自 `Object` 且未声明构造函数的类**。

- 除非想让该类与普通的类一样可以被正常地使用，否则请使用关键字 `mixin` 替代 `class`。

```dart
mixin Musical {
  bool canPlayPiano = false;
  bool canCompose = false;
  bool canConduct = false;

  void entertainMe() {
    if (canPlayPiano) {
      print('Playing piano');
    } else if (canConduct) {
      print('Waving hands');
    } else {
      print('Humming to self');
    }
  }
}
```

可以使用关键字 `on` 来指定哪些类可以使用该 `Mixin` 类。

```dart
// 只有扩展或实现Musician类的类才能使用MusicalPerformer这个混合器(mixin)。
// 因为SingerDancer扩展(extends)了Musician，所以SingerDancer可以混入MusicalPerformer。
class Musician {
  // ...
}
mixin MusicalPerformer on Musician {
  // ...
}
class SingerDancer extends Musician with MusicalPerformer {
  // ...
}
```

### 类变量和方法(Class variables and methods)

使用关键字 `static` 可以声明类变量或类方法(静态变量或静态方法)。

#### 静态变量

静态变量（即类变量）常用于声明类范围内所属的状态变量和常量。  
**静态变量在其首次被使用的时候才被初始化**。

```dart
class Queue {
  static const initialCapacity = 16;
  // ···
}

void main() {
  assert(Queue.initialCapacity == 16);
}
```

#### 静态方法

静态方法（即类方法）不能对实例进行操作，因此不能使用 `this`。但是他们可以访问静态变量。

可以将静态方法作为编译时常量。例如，你可以将静态方法作为一个参数传递给一个常量构造函数。

```dart
import 'dart:math';

class Point {
  double x, y;
  Point(this.x, this.y);

  static double distanceBetween(Point a, Point b) {
    var dx = a.x - b.x;
    var dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
  }
}

void main() {
  var a = Point(2, 2);
  var b = Point(4, 4);
    // 可以在一个类上直接调用静态方法
  var distance = Point.distanceBetween(a, b);
  assert(2.8 < distance && distance < 2.9);
  print(distance);
}
```

## (七) 泛型

如果查看数组的 API 文档，会发现数组 `List` 的实际类型为` List<E>`。

- `<…>` 符号表示数组是一个 `泛型(generic)`（或 `参数化类型(parameterized)）`, **通常使用一个字母来代表类型参数**，比如 E、T、S、K 和 V 等等。

### 为什么使用泛型？

泛型常用于需要要求类型安全的情况，但是它也会对代码运行有好处：

- 适当地指定泛型可以更好地帮助代码生成。
- 使用泛型可以减少代码重复。

### 使用集合字面量(Using collection literals)

List、Set 以及 Map 字面量也可以是参数化的。

- 定义参数化的 List 只需在中括号前添加 `<type>`；
- 定义参数化的 Map 只需要在大括号前添加 `<keyType, valueType>`：

```dart
var names = <String>['Seth', 'Kathy', 'Lars'];
var uniqueNames = <String>{'Seth', 'Kathy', 'Lars'};
var pages = <String, String>{
  'index.html': 'Homepage',
  'robots.txt': 'Hints for web robots',
  'humans.txt': 'We are people, not machines'
};
```

### 使用类型参数化的构造函数

调用构造方法时也可以使用泛型，只需在类名后用尖括号（`<...>`）将一个或多个类型包裹即可：

```dart
var nameSet = Set<String>.from(names);
// 下面代码创建了一个键为 Int 类型，值为 View 类型的 Map 对象：
var views = Map<int, View>();
```

### 泛型集合以及它们所包含的类型

Dart 的泛型类型是 **固化的(reified)**，这意味着即便在运行时也会保持类型信息。

```dart
var names = <String>[];
names.addAll(['Seth', 'Kathy', 'Lars']);
print(names is List<String>); // true
```

> 与 Java 不同的是，Java 中的泛型是类型 **擦除(erasure)** 的，这意味着泛型类型会在运行时被移除。在 Java 中你可以判断对象是否为 List 但不可以判断对象是否为 `List<String>`。

### 限制参数化类型

有时**使用泛型**的时候，可能会想**限制可作为参数的泛型范围**，也就是参数必须是指定类型的子类，这时候**可以使用 `extends` 关键字**。

- 一种常见的非空类型处理方式，是将子类限制继承 `Object` （而不是默认的 `Object?`）。
- 除了对象之外，还可以将扩展与其他类型一起使用。

```dart
// 子类限制继承 `Object`
class Foo<T extends Object> {
  // Any type provided to Foo for T must be non-nullable.
}
// 下面是一个扩展SomeBaseClass的示例，以便可以在T类型的对象上调用SomeBaseClass的成员
class Foo<T extends SomeBaseClass> {
  // Implementation goes here...
  String toString() => "Instance of 'Foo<$T>'";
}
class Extender extends SomeBaseClass {...}

// 这时候就可以使用 SomeBaseClass 或者它的子类来作为泛型参数：
var someBaseClassFoo = Foo<SomeBaseClass>();
var extenderFoo = Foo<Extender>();
```

### 使用泛型方法

起初 Dart 只支持在类的声明时指定泛型，现在同样也可以在方法上使用泛型，称之为 泛型方法(generic methods)。

```dart
T first<T>(List<T> ts) {
  // Do some initial work or error checking, then...
  T tmp = ts[0];
  // Do some additional checking or processing...
  return tmp;
}
/*
方法 first<T> 的泛型 T 可以在如下地方使用：
    函数的返回值类型 (T)。
    参数的类型 (List<T>)。
    局部变量的类型 (T tmp)。
*/
```

## (八) 库和可见性(Libraries and visibility)

`import` 和 `library` 关键字可以帮助你创建一个模块化和可共享的代码库。  
代码库不仅只是提供 API 而且还起到了封装的作用：以下划线（\_）开头的成员仅在代码库中可见。  
每个 Dart 程序都是一个库，即便没有使用关键字 library 指定。  
Dart 的库可以使用 包工具(packages) 来发布和部署。

### 使用库

使用 `import` 来指定命名空间以便其它库可以访问。

- import 的唯一参数是用于指定代码库的 URI，
  - 对于 Dart 内置的库，使用 `dart:xxxxxx` 的形式。
  - 而对于其它的库，你可以使用一个文件系统路径或者以 `package:xxxxxx` 的形式。
    - `package:xxxxxx` 指定的库通过包管理器（比如 pub 工具）来提供

```dart
import 'dart:html';
import 'package:test/test.dart';
```

URI 代表统一资源标识符。  
URL（统一资源定位符）是一种常见的 URI。

### 指定库前缀

如果导入的两个代码库有冲突的标识符，可以为其中一个指定前缀。

```dart
// 比如如果 library1 和 library2 都有 Element 类
import 'package:lib1/lib1.dart';
import 'package:lib2/lib2.dart' as lib2;

// Uses Element from lib1.
Element element1 = Element();

// Uses Element from lib2.
lib2.Element element2 = lib2.Element();
```

### 导入库的一部分

如果只想使用代码库中的一部分，可以有选择地导入代码库。关键字 `show` 和 `hide`。

```dart
// Import only foo.
import 'package:lib1/lib1.dart' show foo;

// Import all names EXCEPT foo.
import 'package:lib2/lib2.dart' hide foo;
```

### 延迟加载(懒加载)库

可能使用到延迟加载的场景：

- 为了减少应用的初始化时间。
- 处理 A/B 测试，比如测试各种算法的不同实现。
- 加载很少会使用到的功能，比如可选的屏幕和对话框。

使用 `deferred as` 关键字来标识需要延时加载的代码库。  
当实际需要使用到库中 API 时先调用 `loadLibrary` 函数加载库。

- `loadLibrary` 函数可以调用多次也没关系，代码库只会被加载一次。

```dart
import 'package:greetings/hello.dart' deferred as hello;

Future<void> greet() async {
  // 使用 await 关键字暂停代码执行直到库加载完成。
  await hello.loadLibrary();
  hello.printGreeting();
}
```

延迟加载注意事项：

- 延迟加载的代码库中的常量需要在代码库被加载的时候才会导入，未加载时是不会导入的。
- 导入文件的时候无法使用延迟加载库中的类型。如果你需要使用类型，则考虑把接口类型转移到另一个库中然后让两个库都分别导入这个接口库。
- Dart 会隐式地将 `loadLibrary()` 导入到使用了 `deferred as` 命名空间 的类中。 `loadLibrary()` 函数返回的是一个 `Future`。

[实现库](https://dart.cn/guides/libraries/create-library-packages)

## (九) 异步支持(Asynchrony support)

Dart 代码库中有大量返回 `Future` 或 `Stream` 对象的函数，这些函数都是 异步 的，它们会在耗时操作（比如 I/O）执行完毕前直接返回而不会等待耗时操作执行完毕。

`async` 和 `await` 关键字用于实现异步编程，并且让代码看起来就像是同步的一样。

### 处理 Future

可以通过下面两种方式，获得 Future 执行完成的结果：

- 使用 `async` 和 `await`;
- 使用 `Future API`.

使用 `async` 和 `await` 的**代码是异步**的，但是**看起来有点像同步代码**。

- 必须在带有 `async` 关键字的 **异步函数** 中使用 `await`。

```dart
Future<void> checkVersion() async {
  var version = await lookUpVersion();
  // Do something with version
}
```

> 尽管异步函数可以处理耗时操作，但是它并不会等待这些耗时操作完成，异步函数执行时会在其遇到第一个 `await` 表达式（代码行）时返回一个 `Future` 对象，然后等待 `await` 表达式执行完毕后继续执行。

使用 `try、catch` 以及 `finally` 来处理使用 `await` 导致的异常。

```dart
try {
  version = await lookUpVersion();
} catch (e) {
  // React to inability to look up the version
}
```

可以在异步函数中多次使用 await 关键字。

```dart
var entrypoint = await findEntryPoint();
var exitCode = await runExecutable(entrypoint, args);
await flushThenExit(exitCode);
```

> `await` 表达式的返回值通常是一个 `Future` 对象；如果不是的话也会自动将其包裹在一个 `Future` 对象里。 `Future` 对象代表一个“promise”， `await` 表达式会阻塞直到需要的对象返回。

> 如果在使用 `await` 时导致编译错误，请确保 `await` 在一个异步函数中使用。

### 声明异步函数

**异步函数** 是函数体由 `async` 关键字标记的函数。

- 将关键字 async 添加到函数并让其返回一个 `Future` 对象。

```dart
Future<String> lookUpVersion() async => '1.0.0';
```

> 函数体不需要使用 `Future API`。如有必要，Dart 会创建 `Future` 对象。  
> 如果函数没有返回有效值，需要设置其返回类型为 `Future<void>`。

[异步编程：使用 Future 和 async-await](https://dart.cn/codelabs/async-await)

### 处理 Stream

如果想从 `Stream` 中获取值，可以有两种选择：

- 使用 `async` 关键字和一个 `异步循环`（使用 `await for` 关键字标识）。
- 使用 `Stream API`

> 在使用 `await for` 关键字前，确保其可以令代码逻辑更加清晰并且是真的需要等待所有的结果执行完毕。  
> 例如，通常不应该在 UI 事件监听器上使用 `await for` 关键字，因为 UI 框架发出的事件流是无穷尽的。

```dart
await for (varOrType identifier in expression) {
  // Executes each time the stream emits a value.
}
```

表达式(expression) 的类型必须是 Stream。执行流程如下：

- 1 等待直到 Stream 返回一个数据。
- 2 使用 1 中 Stream 返回的数据执行循环体。
- 3 重复 1、2 过程直到 Stream 数据返回完毕。

使用 `break` 和 `return` 语句可以停止接收 Stream 数据，这样就跳出了循环并取消注册监听 Stream。

**如果在实现异步 for 循环时遇到编译时错误，请检查确保 await for 处于异步函数中。**

```dart
void main() async {
  // ...
  await for (final request in requestServer) {
    handleRequest(request);
  }
  // ...
}
```

# (十) 其他

## 生成器

当你需要延迟地生成一连串的值时，可以考虑使用 生成器函数。Dart 内置支持两种形式的生成器方法：

- **同步** 生成器：返回一个 Iterable 对象。
- **异步** 生成器：返回一个 Stream 对象。

通过在函数上加 `sync*` 关键字并将返回值类型设置为 _Iterable_ 来实现一个 **同步** 生成器函数，在函数中使用 _yield_ 语句来传递值。
实现 **异步** 生成器函数与同步类似，只不过关键字为 `async*` 并且返回值为 _Stream_。
如果生成器是递归调用的，可是使用 `yield*` 语句提升执行性能。

```dart
Iterable<int> naturalsDownFrom(int n) sync* {
  if (n > 0) {
    yield n;
    yield* naturalsDownFrom(n - 1);
  }
}
```

## 可调用类

通过实现类的 call() 方法，允许使用类似函数调用的方式来使用该类的实例。

## 隔离区

大多数计算机中，甚至在移动平台上，都在使用多核 CPU。
为了有效利用多核性能，开发者一般使用共享内存的方式让线程并发地运行。
然而，多线程共享数据通常会导致很多潜在的问题，并导致代码运行出错。

为了解决多线程带来的并发问题，Dart 使用 `isolate` 替代线程，所有的 Dart 代码均运行在一个 `isolate` 中。
每一个 `isolate` 有它自己的堆内存以确保其状态不被其它 `isolate` 访问。

**所有的 Dart 代码都是在一个 isolate 中运行，而非线程。**
**每个 isolate 都有一个单独的执行线程，并且不与其他的 isolate 共享任何可变对象。**

## Typedefs

**类型别名**是引用某一类型的简便方法，因为其使用关键字 `typedef`，因此通常被称作 `typedef`。

下面是一个使用 IntList 来声明和使用类型别名的例子:

```dart
typedef IntList = List<int>;
IntList il = [1, 2, 3];
```

类型别名可以有类型参数:

```dart
typedef ListMapper<X> = Map<X, List<X>>;

Map<String, List<String>> m1 = {}; // 声明类型比较冗长
ListMapper<String> m2 = {}; // 这样更简洁的方式
```

针对函数，在大多数情况下，我们推荐使用 内联函数类型 替代 typedefs。

## 元数据

使用元数据可以为代码增加一些额外的信息。元数据注解以 `@` 开头，其后紧跟一个编译时常量（比如 deprecated）或者调用一个常量构造函数。

Dart 中有三个注解是所有代码都可以使用的： `@deprecated`、`@Deprecated` 和 `@override`。也可以自定义元数据注解。

下面的示例定义了一个带有两个参数的 `@todo` 注解：

```dart
library todo;

class Todo {
  final String who;
  final String what;

  const Todo(this.who, this.what);
}
```

使用 @Todo 注解的示例：

```dart
import 'todo.dart';

@Todo('seth', 'make this do something')
void doSomething() {
  print('do something');
}
```

元数据可以在 library、class、typedef、type parameter、 constructor、factory、function、field、parameter 或者 variable 声明之前使用，也可以在 import 或 export 之前使用。
可使用反射在运行时获取元数据信息。

## 注释

单行注释

- 单行注释以 `//` 开始。所有在 `//` 和该行结尾之间的内容均被编译器忽略。

多行注释

- 多行注释以 `/*` 开始，以 `*/` 结尾。
- 所有在 `/*` 和 `*/` 之间的内容均被编译器忽略（不会忽略文档注释），多行注释可以嵌套。

文档注释
// 文档注释可以是多行注释，也可以是单行注释，文档注释以 `///` 或者 `/**` 开始。
// 在连续行上使用 `///` 与多行文档注释具有相同的效果。
// 在文档注释中，除非用中括号括起来，否则分析器会忽略所有文本。
// 使用中括号可以引用类、方法、字段、顶级变量、函数和参数。
// 括号中的符号会在已记录的程序元素的词法域中进行解析。
