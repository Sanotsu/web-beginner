# 说明

关于前端 web 开发的一些学习记录，整理部分一般都会有参考地址，希望对以后的发展有所裨益。此外还有一些小工具脚本等，作为记录，以便后续使用。

**<font color=green>当然，这都是笔者自己的学习路线中的总结，不具有通用性，请注意甄别。</font>**

文件夹结构:

![文件夹结构](pic-mind-map/文件夹结构.png)

<!-- ```txt
.
├── documents               - 存放直接使用的md文件，可以快捷键格式化，下层为各种主题的分类
│   ├── 01-javascript           - 分类以下内容可自订再细分,含部分CSS、HTML內容
│   │   ├── base-js             - 基础知识学习部分
│   │   ├── js-faq              - 常见问题(不一定有答案)
│   │   └── rxjs
│   ├── 02-vue
│   ├── 03-nodejs
│   ├── 04-engineered       - 前端工程化相关内容，也包括性能等
│   │   └── webpack
│   ├── 05-typescript
│   ├── 06-dart
│   ├── 07-basic-dsa        - 基本的数据结构与算法
│   ├── 08-arc-design       - 系统设计相关(设计模式、系统架构之类的)
│   ├── 09-scripts-and-commands - 一些常用的脚本或者命令
│   ├── 10-miscellaneous    - 其他杂项(HTTP、缓存、跨域、web安全、mysql基础、一些后台工具介绍等……)
│   └── 11-others           - 掘金上写的博文主要放在这里
├── pandoc                  - 一般是刻意整理的总结性md文件，目的是使用xelatex转成指定格式的pdf
│   ├── format-doc              - 不要轻易格式化md文件，否则转换的pdf排版会乱
│   ├── pandoc-usage
│   └── readme.md
├── pic-mind-map            - 一些简单的脑图导出来的图片，做参看。
└── _tools                  - 一些nodejs或者python脚本小工具，用于某些简单的需求
``` -->

- 如果有需要自己制作作成 pdf，可以把对应的 md 文件的内容抽出来，使用 pandoc 配合 Latex 格式(需要安装相应工具)使用。

以下都有整理到`《web 前端基础知识汇整(精简版)》`部分。最近也在 [掘金](https://juejin.cn/user/1591748568036765/posts)上整理 web 相关的系列文章，有兴趣可以去看看。

---

**分类如下(加粗的应对面试可能有裨益，写得比较用心)** ：

## 前端基础知识汇整的 pdf

你也可以直接找到对应的 md 文件使用例如 Latex 工具转换成 pdf 文件，所有内容自行确认。

- [web 前端基础知识汇整-500+页](pandoc/format-doc/pandoc-pdf/01-pandoc-form-js-web-base-20230516.pdf)
- **[web 前端基础知识汇整(精简版)-100 页左右](pandoc/format-doc/pandoc-pdf/02-pandoc-print-js-web-base-20230516.pdf)**
  - 我是希望自己能够彻底弄懂这一百多页的各类总结。
- [web 前端基础知识汇整(关键字-几页)](pandoc/format-doc/pandoc-pdf/03-pandoc-print-js-web-base-keyword-20230516.pdf)

## 简单的思维导图

- [个人用到的基本 web 相关知识关键字 ](pic-mind-map/基本web相关知识关键字map.png)
- [某系统架构使用的组件说明](pic-mind-map/某系统架构使用的组件说明.png)

## HTML、CSS、JavaScript

### HTML

- **[web 开发 7 年，不止为了面试 —— 万字 HTML 重点基础知识分享](documents/11-others/web-base-html-part1.md)**

### CSS

- **[01-CSS 布局与响应式布局简述](documents/01-javascript/_css-part/01-CSS布局与响应式布局简述.md)**
- [02-CSS 的动画、变换、过渡简介(animation-transform-transition)](documents/01-javascript/_css-part/02-CSS-animation-transform-transition.md)
- [03-CSS 选择器与 XPath 路径表达式](documents/01-javascript/_css-part/03-CSS选择器和XPath路径表达式.md)
- **[Web 开发 7 年，一文总结 CSS 常见面试点和基础教程](documents/11-others/web-base-css-part1.md)**
  - [掘金版本](documents/11-others/web-base-css-part1-掘金版本.md)

### JS

#### 基础知识

- [01-基本概念：什么是 JavaScript](documents/01-javascript/base-js/01、基本概念：什么是JavaScript.md)
- [02-语言基础](documents/01-javascript/base-js/02、语言基础.md)
- [03-变量、作用域与内存](documents/01-javascript/base-js/03、变量、作用域与内存.md)
- [04-基本引用类型](documents/01-javascript/base-js/04、基本引用类型.md)
- [05-集合引用类型](documents/01-javascript/base-js/05、集合引用类型.md)
- [06-迭代器与生成器](documents/01-javascript/base-js/06、迭代器与生成器.md)
- [07-对象、类与面向对象编程(上)](<documents/01-javascript/base-js/07、对象、类与面向对象编程(上).md>)
- [08-对象、类与面向对象编程(下)](<documents/01-javascript/base-js/08、对象、类与面向对象编程(下).md>)
- [09-代理与反射](documents/01-javascript/base-js/09、代理与反射.md)
- [10-函数](documents/01-javascript/base-js/10、函数.md)
- [11-Promises 和异步函数](documents/01-javascript/base-js/11、Promises和异步函数.md)
- [12-MDN 的 Canvas 基础](documents/01-javascript/base-js/12、MDN的Canvas基础.md)
- [13-MDN 的 WebGL 基础教程概述](documents/01-javascript/base-js/13、MDN的WebGL基础教程概述.md)
- **[Web 开发 7 年，3 万字分享 JavaScript 常用重要知识点](documents/11-others/web-base-js-part1.md)**

#### 常见问题

- [js-FAQs(纯题目收集)](documents/01-javascript/js-faq/readme.md)
- **[js 常用技巧](documents/01-javascript/js-faq/03-javascript-tricks.md)**
- [ES6 以来的新特性关键字(更新到 ES2023)](documents/01-javascript/js-faq/04-es6-new-features.md)

#### RxJS

- [01-rxjs7-basic](documents/01-javascript/rxjs/01-rxjs7-basic.md)

## Vue

- [01-vue 常见问题(纯问题转存)](documents/02-vue/01-vue-faq.md)
- **[02-vue-FAQs](documents/02-vue/02-vue-simplification-FAQs.md)**
- **[03-vuejs 设计与实现总结](documents/02-vue/03-vuejs设计与实现总结.md)**
- **[04-vue 响应式原理](documents/02-vue/04-vue响应式原理.md)**
- [05-vue3 新特性关键字](documents/02-vue/05-vue3-new-features.md)

## Node.js

- [01-nodejs_interview_questions](documents/03-nodejs/01-nodejs_interview_questions_en-cn.md)
- **[02-nodejs-FAQs](documents/03-nodejs/02-node-faq.md)**

## 前端工程化

- **[01-前端工程化概述](documents/04-engineered/01-frontend-engineered-overview.md)**
- **[02-渲染页面:浏览器的工作原理](documents/04-engineered/02-渲染页面:浏览器的工作原理.md)**
- **[03-web 性能指标及优化](documents/04-engineered/03-web性能指标及优化.md)**
- **[web 开发 7 年，浅谈前端架构设计与工程化](documents/11-others/frontend-architecture-design-and-engineering.md)**
- **[web 开发 7 年，Chrome 开发工具 Performance 使用实战](documents/11-others/web-base-chrome-performance-devtool.md)**
- [「前端性能优化」之 nginx 启用 br 压缩和 h2 的配置](documents/04-engineered/04-前端性能优化之nginx启用br和h2的配置.md)
- **[Web 开发 7 年，长文浅谈一下浏览器的工作原理](documents/11-others/web-base-browser-working.md)**

## TypeScript

- [01-typescript 官方手册概述](documents/05-typescript/01-typescript-handbook概述.md)

## Dart

- [01-dart 官方教程概述](documents/06-dart/01-dart-language-tour.md)
- [02-flutter 架构简介](documents/06-dart/02-flutter-resource.md)
- [03-ubuntu 下配置 flutter 环境的简述](documents/06-dart/03-flutter-config-andsome.md)
- [04-flutter 开发时一些环境建置的问题(持续更新)](documents/06-dart/04-flutter-dev-env-issue.md)

## 数据结构与算法(入门内容)

#### 《学习 JavaScript 数据结构与算法(第 3 版)》笔记

- [01-栈](documents/07-basic-dsa/learning-js-dsa-3th/01、Stack.md)
- [02-队列](documents/07-basic-dsa/learning-js-dsa-3th/02、Queue.md)
- [03-链表](documents/07-basic-dsa/learning-js-dsa-3th/03、LinkedList.md)
- [04-集合](documents/07-basic-dsa/learning-js-dsa-3th/04、Set.md)
- [05-字典与哈希表](documents/07-basic-dsa/learning-js-dsa-3th/05、DictionaryAndHashTable.md)
- [06-树](documents/07-basic-dsa/learning-js-dsa-3th/06、Tree.md)
- [07-堆](documents/07-basic-dsa/learning-js-dsa-3th/07、Heap.md)
- [08-图](documents/07-basic-dsa/learning-js-dsa-3th/08、Graph.md)
- [09-基础的排序与搜索算法](documents/07-basic-dsa/learning-js-dsa-3th/09、SortingAndSearchingAlgorithms.md)
- [10-算法设计与技巧](documents/07-basic-dsa/learning-js-dsa-3th/10、AlgorithmDesignAndTechniques.md)

#### 算法题与技巧("他山之玉")

- [01-极简的基础数据结构与算法介绍](documents/07-basic-dsa/01-simplified-dsa-dp.md)
- [02-常见基础算法技巧题解(leetcode 题解)](documents/07-basic-dsa/02-simplified-simple-aps.md)
  - 推荐看他人更具体有效的内容，比如[youngyangyang04/leetcode-master](https://github.com/youngyangyang04/leetcode-master)，这里只是列举个人在意的基础的算法题，没有普遍性。

## 架构设计

- [01-设计模式概述](documents/08-arc-design/01-design-patterns.md)

## 杂项

- [01-前端基础杂项简述(css、网络相关、浏览器相关、性能问题、前端编译、数据库相关)](documents/10-miscellaneous/01-other-web-faq.md)
- [02-mysql 常见问题](documents/10-miscellaneous/02-mysql-faq.md)
- [03-后端常用工具简介](documents/10-miscellaneous/03-backend-common-tools.md)
- [04-sass 简介](documents/10-miscellaneous/04-sass-overview.md)
- [05-http 基础](documents/10-miscellaneous/05-http-basic.md) - 已合到 10
- **[06-http 缓存](documents/10-miscellaneous/06-http-cache.md)**
- **[07-跨源资源共享 cors](documents/10-miscellaneous/07-cors.md)**
- **[08-web 安全](documents/10-miscellaneous/08-web-secure.md)**
- [09-http 方法和常见响应码介绍](documents/10-miscellaneous/09-http-methods.md) - 已合到 10
- **[10-Web 前端八股整理：比较全面的初级 HTTP、HTTPS 和 TLS 知识点分享](documents/11-others/web-base-https-part1.md)**

## 脚本命令等

- [配合 cron 的 mysql 备份脚本](documents/09-scripts-and-commands/scripts/mysqlbak.sh)
- [linux 常用的命令](documents/09-scripts-and-commands/commands/linux-command.md)
- [k8s 常用的命令](documents/09-scripts-and-commands/commands/k8s-command.md)
- [gitlab-ce 的一些命令](documents/09-scripts-and-commands/configs/gitlab-ce-simple-usage.md)
- [pandoc 转 pdf 文件使用的 LaTeX 配置](pandoc/pandoc-usage/form.tex)
  - 代码都有注释，已经覆盖了常见的配置需求

## 其他

- [工作经验(updating)](documents/11-others/work-ex-just-read-updating.md)
  - 笔者的近期经验，不具备参看性，看个乐。
- **[干了 7 年 web 开发工作，混吃等死的日子可能到头了](documents/11-others/web-development-work-experience-summary.md)**
- [说干就干不如不干？3 个月开发 flutter 项目的实践经验分享](documents/11-others/experience-sharing/说干就干不如不干？3个月开发flutter项目的实践经验分享.md)

---

《web 前端基础知识汇整》pdf 文件截图:

![pdf截图1](pandoc/format-doc/pictures/pdf-screenshots-1.png)

![pdf截图2](pandoc/format-doc/pictures/pdf-screenshots-2.png)
