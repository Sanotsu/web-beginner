---
puppeteer:
  landscape: false
  format: "A4"
  printBackground: true

# pandoc生成标题信息时用到
# title: "web前端基础知识汇整（关键字）"
# author: David Su | callmedavidsu@gmail.com
# date: \today

# 正文字体，默认最大是12pt，要更大需要其他包(常见字号: 四号14pt 小四12pt 五号10.5pt 小五9pt)
fontsize: 10pt
# 配合form.tex的hyperref设置链接颜色
boxlinks: true
# 设置双面模式，以便.tex文件中能区分左右页眉页脚
classoption: twoside,symmetric
# 添加此可以让pandoc生成的toc新起一页，而不是接续在首页。目录页面从1开始编号
include-before:
  - '`\newpage{}`{=latex}'
  - \setcounter{page}{1}
# 样式调整好后，一定不要shift+alt+f去自动格式化，会让很多设置失效
#   例如 *斜体* 变为 _斜体_，pandoc不能识别。表格分割线----- 长度变化，但是各个栏位占比不对
---

<!-- % 画一条横线：\rule[水平高度]{长度}{粗细} -->
<!-- A4 宽21cm，左右边距0.8cm，线长19.4cm -->
<!-- \rule[0pt]{19.4cm}{0.03em} -->

# Vue 3 迁移指南(新特性)

直接看官网[Vue 3 迁移指南](https://v3-migration.vuejs.org/zh/)，都有说明的。

**Vue 3 中需要关注的一些新特性**

- `*` [组合式 API](https://cn.vuejs.org/guide/extras/composition-api-faq.html)
  - v2.7 以上内置，更好的逻辑复用，更灵活的代码组织，更好的类型推导，更小的生产包体积
- `*` [单文件组件中的组合式 API 语法糖 (`<script setup>`)](https://cn.vuejs.org/api/sfc-script-setup.html)
  - `<script setup>` 是在单文件组件 (SFC) 中使用组合式 API 的编译时语法糖
- 内置组件: [Teleport 组件](https://cn.vuejs.org/guide/built-ins/teleport.html)
  - 可以将一个组件内部的一部分模板“传送”到该组件的 DOM 结构外层的位置去。
- [Fragments 片段节点类型](https://v3-migration.vuejs.org/zh/new/fragments.html)
  - Vue 3 现在正式支持了多根节点的组件。(不用在 template 中用 div 包裹多个根节点组件了)
- `**` [emits 组件选项](https://cn.vuejs.org/api/options-state.html#emits)- 类似 props 一样，有了单独的 emits 选项。
- 来自 `@vue/runtime-core` 的 [createRenderer](https://cn.vuejs.org/api/custom-renderer.html) API 用来创建自定义渲染函数
- `*` [单文件组件中的状态驱动的 CSS 变量 (\<style>中的 v-bind)](https://cn.vuejs.org/api/sfc-css-features.html#v-bind-in-css)
  - 单文件组件和`<script setup>`的 `<style>` 标签支持使用 `v-bind` CSS 函数将 CSS 的值链接到动态的组件状态
- [SFC \<style scoped> 新增全局规则和针对插槽内容的规则](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0023-scoped-styles-changes.md)
  - 深度选择器，v2 `::v-deep xxx`；v3 `v-deep(xxx)`，缩写 `:deep(xxx)`
- 实验性内置组件[Suspense](https://cn.vuejs.org/guide/built-ins/suspense.html)

`*` 现在也支持在 Vue 2.7 中使用；`**` Vue 2.7 中支持，但仅用于类型推断

**新的框架级别推荐(默认建议)**

- 新版本的 Router, Devtools & test utils 来支持 Vue 3
- 构建工具链: Vue CLI `->` [Vite](https://cn.vitejs.dev/)
- 状态管理: Vuex `->` [Pinia](https://pinia.vuejs.org/zh/index.html)
- IDE 支持: Vetur `->` [Volar](https://marketplace.visualstudio.com/items?itemName=vue.volar)
- 新的 TypeScript 命令行工具: [vue-tsc](https://github.com/johnsoncodehk/volar/tree/master/vue-language-tools/vue-tsc)
- 静态网站生成: VuePress `->` [VitePress](https://vitepress.vuejs.org/)
- JSX: `@vue/babel-preset-jsx` `->` [`@vue/babel-plugin-jsx`](https://github.com/vuejs/babel-plugin-jsx)

**非兼容性改变**

- 全局 API
  - 全局 Vue API 更改为使用应用程序实例
  - vue2 没有“app”的概念，我定义的应用只是通过 `new Vue()` 创建的根 Vue 实例。从同一个 Vue 构造函数创建的**每个根实例共享相同的全局配置**。既影响其他测试，又没办法实现不共用全局配置。
    vue3 调用 `createApp` 返回一个应用实例(vue3 新概念)。应用实例暴露了 Vue 2 全局 API 的一个子集，经验法则是，_任何全局改变 Vue 行为的 API 现在都会移动到应用实例上_。
  - 全局和内部 API 都经过了重构，现已支持 TreeShaking （摇树优化）
- 模板指令
  - v-model 指令在组件上的使用已经被重新设计，替换掉了 `v-bind.sync`
  - 在`<template v-for>` 和没有 v-for 的节点身上使用 key 发生了变化
  - v-if 和 v-for 在同一个元素身上使用时的优先级发生了变化
  - `v-bind="object"` 现在是顺序敏感的
  - `v-on:event.native` 事件修饰符已经被移除
- 组件
  - 函数式组件只能通过纯函数进行创建
  - 单文件组件 (SFC) `<template>` 标签的 `functional` attribute 和函数式组件的 `functional` 选项已被移除
  - 异步组件现在需要通过 `defineAsyncComponent` 方法进行创建
  - 组件事件现在应该使用 `emits` 选项进行声明
- 渲染函数
  - 渲染函数 API 更改: h 现在是全局导入，而不是作为参数传递给渲染函数。
    - `render(h){return h('div')} -> import { h } from 'vue'; render(){return h('div')}`。
  - `$scopedSlots` property 已移除，所有插槽都通过 `$slots` 作为函数暴露
  - `$listeners` 被移除或整合到 `$attrs`
  - `$attrs` 现在包含 `class` 和 `style` attribute
- 被移除的 API
  - `keyCode` 作为 `v-on` 修饰符的支持
  - `$on`、`$off` 和 `$once` 实例方法
  - 过滤器 (filter)
  - 内联模板 attribute
  - `$children` 实例 property
  - `propsData` 选项
  - `$destroy` 实例方法。用户不应该再手动管理单个 Vue 组件的生命周期。
  - 全局函数 `set` 和 `delete` 以及实例方法 `$set` 和 `$delete`。基于代理的变化检测已经不再需要它们了。
- 自定义元素
  - 自定义元素检测现在在模板编译时执行
  - 特殊的 is attribute 的使用被严格限制在被保留的 \<component> 标签中
- [其他小改动](https://v3-migration.vuejs.org/breaking-changes/#other-minor-changes)

---

- ref [Vue 3 迁移指南](https://v3-migration.vuejs.org/zh/)
