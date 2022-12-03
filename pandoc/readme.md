`format-usage`是一些 pandoc 的使用，以及预设好的两个`--pdf-engine=xelatex`使用的模板配置。

`format-doc`是使用 pandoc 转为 pdf 的 md 文件，**不要格式化它**，否则排版会乱。  
最好是先在其他单文件中格式化完成之后再复制过去。

- 以 `pandoc-form` 开头的，是 12 号字体，内容较完整，用于直接查看的。
- 以 `pandoc-print` 开头的，是 10 好字体，浓缩的精华内容，可以打印出来看的。

其中

`01-pandoc-form-js-web-base.md`基本会包含项目中，基本是各子文件夹下`simplified-`开头文档的合集
`02-pandoc-print-js-web-base.md`则为其极度的精简
`03-pandoc-print-js-web-base-keywork.md`则基本只有关键内容，以便形成重点
