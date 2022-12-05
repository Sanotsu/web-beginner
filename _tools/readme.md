各文件夹小项目说明:

- min-images
  - 降低图片质量压缩大小
- gen-word-cloud
  - 读取文本拆词，用于生成词云
- `puppeteer-data-acquisition
  - 使用 puppeteer 对几个网站的简单爬虫示例
- recognize-picture-text
  - 识别图片中的文字
- get-videos-duration
  - 获取指定文件夹下所有视频的总时长

---

一点小知识：

nodejs 支持引入使用 CommonJS 和 ES 的模块，前者 `const XXX = require('xxx')`，后者 `import xxx from 'xxx'`。  
为了默认`.js`文件能使用 ESM，解决方法之一是在 package.json 中添加一句`"type": "module",`，但这会导致如果之前有使用 `require()`的 js 文件就无法使用了。  
所以，为了`require()` 和`import`可以混用，那就 js 文件使用 `require()`，要使用 `import` 的命名为.mjs 文件。

关于支持的 nodejs 版本，具体识别依据等准确信息可查看：[nodejs package 包模块](http://nodejs.cn/api/packages.html#determining-module-system)

```
以 .mjs 结尾的文件总是作为 ES 模块加载，而不管最近的父级 package.json。
以 .cjs 结尾的文件总是作为 CommonJS 加载，而不管最近的父级 package.json。
```
