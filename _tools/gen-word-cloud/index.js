const nodejieba = require('nodejieba');
const fs = require('fs');

// 生成词云数据
function wordCluod() {
    fs.readFile('./vue-faq.txt', 'utf8', function (err, data) {

        const text = nodejieba.extract(data, 200);
        // console.log("result", text);

        // 构建 https://www.wordclouds.com/ 需要的csv格式
        // 该在线词语生成器不需要登录，功能多样，推荐

        let temp = `"weight";"word";"color";"url" \n`;
        for (let i in text) {
            temp += `"${Math.ceil(text[i].weight)}";"${text[i].word}";"";"" \n`;
        }
        fs.writeFile('./wordCloud' + '.csv', temp, 'utf-8', function (err) {
            if (err) {
                console.log(err);
            }
        });
    });
}

wordCluod()

/*
// 文档示例：
var sentence = "我是拖拉机学院手扶拖拉机专业的。不用多久，我就会升职加薪，当上CEO，走上人生巅峰。";

var result;

// 没有主动调用nodejieba.load载入词典的时候，
// 会在第一次调用cut或者其他需要词典的函数时，自动载入默认词典。
// 词典只会被加载一次。
result = nodejieba.cut(sentence);
console.log(result);

result = nodejieba.cut(sentence, true);
console.log(result);

result = nodejieba.cutHMM(sentence);
console.log(result);

result = nodejieba.cutAll(sentence);
console.log(result);

result = nodejieba.cutForSearch(sentence);
console.log(result);

result = nodejieba.tag(sentence);
console.log(result);

var topN = 5;
result = nodejieba.extract(sentence, topN);
console.log(result);

result = nodejieba.textRankExtract(sentence, topN);
console.log(result);

result = nodejieba.cut("男默女泪");
console.log(result);
nodejieba.insertWord("男默女泪");
result = nodejieba.cut("男默女泪");
console.log(result);

result = nodejieba.cutSmall("南京市长江大桥", 3);
console.log(result);
*/