const { createWorker, createScheduler } = require('tesseract.js');

/*
[tesseract.js](https://github.com/naptha/tesseract.js#tesseractjs)  
Pure Javascript OCR for more than 100 Languages  
识别图片中的文字

亲测：

中文：  
一般间隔的文字图片，中文识别率极低，不仅扫描的 pdf 截图无法识别，原本数字版的 pdf 截图也无法识别。（000,111）  
识别的准确率和图片中文字的大小个间隔及其相关。同样的图片，放大数倍的截图，识别率明显提升。（222,333）  
但模糊、不平整、有旋转偏移污点等，会被认定为一个整体，无法正确识别。（444）  
整体识别效率较低。

英文：  
英文数字版 pdf 截图识别率还行，与中文同等水平大小但中文无法识别，英文也能识别。（555）  
比较清晰的扫描版本英文 pdf 截图识别率也还好。（666） 
*/


let cnPicPath = "./input/222.png"
let engPicPath = "./input/666.png"

// const worker = createWorker({
//     logger: m => console.log(m)
// });

const worker = createWorker();

const scheduler = createScheduler();
const worker1 = createWorker();
const worker2 = createWorker();

/**
 * 都是官方示例简单改动
 */
// (async () => {
//     await worker.load();
//     await worker.loadLanguage('eng+chi_sim');
//     await worker.initialize('chi_sim');
//     const { data: { text } } = await worker.recognize(cnCicPath);
//     console.log(text);
//     await worker.terminate();
// })();

/**
 * 单个worker处理一张图片
 * @param {*} loadLanguage 
 * @param {*} initialize 
 * @param {*} picPath 
 */
let recognizeIndex = async (loadLanguage, initialize, picPath) => {
    console.time('start')

    await worker.load();
    await worker.loadLanguage(loadLanguage);
    await worker.initialize(initialize);
    const { data: { text } } = await worker.recognize(picPath);
    console.log(text);
    await worker.terminate();

    console.timeEnd('start')
}

/**
    官方的 with multiple workers to speed up (^2.0.0-beta.1)
    但没看懂哪里有加速，明明更慢了
 */
let multiJobRecognizeIndex = async (loadLanguage, initialize, picPath) => {

    console.time('start')

    await worker1.load();
    await worker2.load();
    await worker1.loadLanguage(loadLanguage);
    await worker2.loadLanguage(loadLanguage);
    await worker1.initialize(initialize);
    await worker2.initialize(initialize);
    scheduler.addWorker(worker1);
    scheduler.addWorker(worker2);

    /** Add 10 recognition jobs */
    // 2022-03-23 实测这10个job都在各自处理同一个图片，处理出10份一模一样的结果，也没speed up 啊？
    const results = await Promise.all(Array(10).fill(0).map(() => (
        scheduler.addJob('recognize', picPath)
    )));

    // console.log(results);
    /*
    results是包含以下对象的数组，数组数量与job数量一致:
    {
        jobId: 'Job-25-b1bba',
        data: {
        text: '5.08 Table Layout\n' +`……`,
        hocr: `<div class='ocr_page' id='page_1' title='image ""; bbox 0 0 765 257; ppageno 0'>\n` +,
        tsv: '1\t1\t0\t0\t0\t0\t0\t0\t765\t257\t-1\t\n…………' ,
        box: null,
        unlv: null,
        osd: null,
        confidence: 90,
        blocks: [Array],
        psm: 'SINGLE_BLOCK',
        oem: 'DEFAULT',
        version: '4.1.1-56-gbe45',
        paragraphs: [Array],
        lines: [Array],
        words: [Array],
        symbols: [Array]
        }
    }
    其中 data.text就是图片中文字。
    */
    // console.log(results.map(r => r.data.text));

    // 以上重复显示了10次，只显示第一个的就好
    const { data: { text } } = results[0]
    console.log(text);

    await scheduler.terminate(); // It also terminates all workers.

    console.timeEnd('start') // start: 73364.364ms
};

// recognizeIndex('eng+chi_sim', 'chi_sim', cnPicPath)

// 同一张图片，时间差很多：
// recognizeIndex('eng', 'eng', engPicPath)      // start: 13940.321ms
multiJobRecognizeIndex('eng', 'eng', engPicPath) // start: 74979.289ms
