js-faq 是收集了一些网上阅读量比较大的 js 面试题文章(查看时间为 2022-08-03)，

- 此部分查看[01-questions.md](./01-questions.md)

整理出关于 js 各个方面常见的问题种类

- 此部分查看[02-question-sort.md](./02-question-sort.md)

使用以下代码生成关键字，并生成词云(需要下载对应依赖)

```js
const nodejieba = require("nodejieba");
const fs = require("fs");

// 生成词云数据
function wordCluod() {
  // 把问题部分放到txt方便读取，博文标题等等就不要了，避免干扰
  fs.readFile("./questions.txt", "utf8", function (err, data) {
    const text = nodejieba.extract(data, 300);
    // console.log("result", text);

    // 构建 https://www.wordclouds.com/ 需要的csv格式
    // 该在线词语生成器不需要登录，功能多样，推荐

    let temp = `"weight";"word";"color";"url" \n`;
    for (let i in text) {
      temp += `"${Math.ceil(text[i].weight)}";"${text[i].word}";"";"" \n`;
    }
    fs.writeFile(
      "./other-question-keyowrds" + ".csv",
      temp,
      "utf-8",
      function (err) {
        if (err) {
          console.log(err);
        }
      }
    );
  });
}

wordCluod();
```

生成的图片大概如下:

![js问题高频词云](./pictures/js%E9%97%AE%E9%A2%98%E9%AB%98%E9%A2%91%E8%AF%8D%E4%BA%91.png)
