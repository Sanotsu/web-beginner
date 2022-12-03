参看 [Pandoc+TeXLive 实现 Markdown 转 PDF](https://zhuanlan.zhihu.com/p/444440478)

```sh
pandoc --pdf-engine=xelatex -V CJKmainfont="Microsoft YaHei" -V CJKmonofont="Times New Roman" --highlight-style tango -H form.tex -N --toc --toc-depth=5 05-simplified-ts.md -o README.pdf
```

查看支持中文的字体:

```sh
fc-list :lang=zh
```

说明

`-V CJKmainfont="Microsoft YaHei" -V CJKmonofont="Times New Roman"` 设置字体.使用 CJKmainfont 选项指定支持中文的字体。
`--highlight-style tango` 指定代码高亮(就这个好一点，代码区域有底色)
`-H form.tex` 使用其他配置文件
`-N ` 给各级标题前面添加编号(生成的目录中不会有)
`--toc --toc-depth=5` 在最前面生成目录,指定层级 5 层
`05-simplified-ts.md -o README.pdf` 指定 md 文件输出为指定 pdf 文件

正文中换行:

```
\newpage
```

不要使用新型图片格式，例如 svg、webp
图片太大可能会报错，先压缩质量
要使用换行，尤其是表格、图片之前，否则会编程一行，不要相信 puppeteer 的输出，不一样的
图片指定占位宽度，否则可能显示不全 `![image](./images/image.png){width=70%}`

美中不足，对于表格，显示不是很好
指定 table column 宽度，正文中`<div style="width:[长度]">[单元格文本]</div>` (但不会变)

章节标题层级大于 3，则不生效了。
尝试在该标题下方使用一个 \ ，在 pandoc 生成文档中为空一行，则可以分开标题和正文，
注意下一行马上跟上文字，否则 markdown 文档预览则多一个反斜线字符。
如果四级五级标题下方马上是个 `-` 或者 `1.` 这样的列表，则会自动换行

md 正文中的表格

```txt
%% 表示文档内容开始
\begin{document}
%% 添加表格
\begin{longtable}{|c|c|r|r|r|r|r|r|r|l|}
    \caption{caption}       %% 表格标题
    \label{table:label}  \\ %% 添加表格标签
    \hline                  %% 添加水平线
    line1   &   line2   &   $t_1$   &   $t_{12}$    &   $t_2$       &   $r$(\%)&    $D$(GB)&    $D_{nc}(GB)$&$G_t$(\%)&Station\\
    \hline
    % 每行的数据
    10      &   2       &   0:22:00 &   9:46:00 &   2:00:00 &   80.49   &   159.18  &   302.25  &   89.88   &   Cours Dillon    \\
    204     &   205     &   2:01:00 &   2:57:00 &   1:11:00 &   47.97   &   95.21   &   138.43  &   45.38   &   Ayguevives Collège  \\
    % 更多数据
    \hline
\end{longtable}
%% 表示文档内容结束
\end{document}
```

表格中的换行，md 原本使用`<br>`就好，但是 pandoc 不能识别，需要使用 \newline，前后的文字需要有个空格

表格中分割行里面的-------------------------的长度就是各个栏位占比宽度。如果用了格式化，比例就变得很奇怪，一定最后手动调整

同样的，*斜体*格式化之后变成 _斜体_，同样 pandoc 转换是不生效的

把字体设置放到 .tex 文件之后

把一些 pandoc 配置放在专门的 tex 文件中，然后使用，例如:

```sh
pandoc --pdf-engine=xelatex --highlight-style tango -H form.tex --toc --toc-depth=5 02-simplified-vue-pandoc.md -o pandoc-pdf/02-simplified-vue-pandoc.pdf
```

`form-print.tex`和`form.tex`都是是标准 A4，窄边框，前者 10 号字体，没有页首页脚文字，只有页码；后者 12 号字体，有页首页脚章节文字。

带目录的 form:

pandoc --pdf-engine=xelatex --highlight-style tango -H ../pandoc-usage/form.tex --toc --toc-depth=5 01-pandoc-form-js-web-base.md -o pandoc-pdf/01-pandoc-form-js-web-base.pdf

不带目录的 print:

pandoc --pdf-engine=xelatex --highlight-style tango -H ../pandoc-usage/form-print.tex 02-pandoc-print-js-web-base.md -o pandoc-pdf/02-pandoc-print-js-web-base.pdf

pandoc --pdf-engine=xelatex --highlight-style tango -H ../pandoc-usage/form-print.tex \
03-pandoc-print-js-web-base-keyword.md -o pandoc-pdf/03-pandoc-print-js-web-base-keyword.pdf
