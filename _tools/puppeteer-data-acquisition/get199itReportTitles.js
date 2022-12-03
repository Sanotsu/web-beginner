const { fail } = require('assert');
const fs = require('fs');
const puppeteer = require('puppeteer');
const moment = require('moment');


/**
 * 
 * @param {*} totalPages 需要抓取的页数
 */
let getReportMuti = async (totalPages) => {
    const browser = await (puppeteer.launch({
        // headless: false,
        ignoreHTTPSErrors: true
    }));
    const page = await browser.newPage();

    // 进入页面
    await page.goto('http://www.199it.com');

    // 获取页面标题
    let title = await page.title();
    console.log('1 需要抓取的总页数: ', totalPages, ' 已打开页面,标题: ', title)

    for (let i = 1; i <= totalPages; i++) {
        /**
         * 如果headless不是true的话，这里可能无法跳转页面，则无法继续下去。
         * 第一页和其他页url稍微不同
         * 2022-04-09 页面已知bug:
         *      直接访问整十数页码，比如 http://www.199it.com/archives/category/report/page/10，/page/20……，页面是无法加载的
         *      即便切到第9页，第11页，点击下一页 前一页，也无法加载页面。 
         */

        let flag = true, retries = 5;
        while (flag && retries > 0) {
            try {
                if (i == 1) {
                    console.log('尝试访问第 1 页……')
                    flag = false;
                    await page.goto(`http://www.199it.com/archives/category/report`, { waitUntil: 'networkidle0' });
                } else {
                    console.log(`尝试访问第 ${i} 页……`)
                    flag = false;
                    await page.goto(`http://www.199it.com/archives/category/report/page/${i}`, { waitUntil: 'networkidle0' });
                }
            } catch (error) {
                console.log(`尝试访问第 ${i} 页失败: `, error);
                flag = true;
                retries--;
                console.log(`开始重试 ${5 - retries}`);

            }
        }

        // 如果当前页重试5此都无法进入页面，则跳过该页。
        if (flag == true) {
            console.error(`------> 重试5次后依旧无法进入第 ${i} 页 ,已跳过该页。`)
            continue;
        }

        console.log(`2 已进入第 ${i} 页,开始等待页面数据加载…… `)

        // 把页面滑动到最底部
        await autoScroll(page);
        // 拉到底后等待5秒，防止数据未加载完成
        await page.waitForTimeout(5000);
        console.log(`3 第 ${i} 页已拉倒最末尾,并已经等待5秒供数据加载. `)

        console.log(`4 ----------- 开始解析 第${i} 页数据。 `)
        await singlePageDataOp(page);
        console.log(`4 ----------- 第${i} 页数据已获取完成。 `)
    }

    console.log(`数据处理完成,程序终止. `)
    browser.close();
};

// 单个页面的数据获取
let singlePageDataOp = async (page) => {
    /*
    fullXPath详情
    首页：
        url:        http://www.199it.com/archives/category/report
        title&href: /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/h2/a
        category:   /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul
        time:       /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[2]/div[1]/ul/li[2]/time
    第二页：
        url:        http://www.199it.com/archives/category/report/page/2
        title&href: /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/h2/a
        category:   /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul
        time:       /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[2]/div[1]/ul/li[2]/time
    第三页：
        url:        http://www.199it.com/archives/category/report/page/3
        title&href: /html/body/div[1]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/h2/a
        category:   /html/body/div[1]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul
        time:       /html/body/div[1]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[2]/div[1]/ul/li[2]/time
    第四页：
        url:        http://www.199it.com/archives/category/report/page/3
        title&href: /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/h2/a
        category:   /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul
        time:       /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[2]/div[1]/ul/li[2]/time
    
    结果：第一个div有区别，所以通用，div[2]取不到，再用div[1]去试。
    
    // 分类 
    // 正常分类     /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul/li[2]/a
    // 有加一的     /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul/li[3]/ul/li/a
    // 分类从简     /html/body/div[2]/div[3]/div/div/div[1]/div/div/article[1]/div[2]/aside[1]/div/ul
    */

    let normalPageXpath = `/html/body/div[2]/div[3]/div/div/div[1]/div/div/article`;
    let bakPageXpath = `/html/body/div[1]/div[3]/div/div/div[1]/div/div/article`;

    // 获取的article标签的元素数组
    let elmArr;
    // 是否成功获取article标签数组的标志
    let elmArrFlag = 'true';  // fail:取值失败，不再继续。false:正常的xpath取值失败，启用备用的。true:正常获取。
    // 成功获取article标签数组使用的xpath
    let usedPathXpath;
    // await page.$x(expression) 返回的是 数组,如果xpath表达式正确但取不到值，返回的空数组。
    try {
        elmArr = await page.$x(normalPageXpath);
        usedPathXpath = normalPageXpath;
    } catch (error) {
        console.error('未取得报告article元素:', error)
        elmArrFlag = 'false';
    }

    // console.log('**********', elmArrFlag, elmArr.length)

    if (elmArrFlag == 'false' || elmArr.length <= 0) {
        try {
            elmArr = await page.$x(bakPageXpath);
            usedPathXpath = bakPageXpath;
        } catch (error) {
            console.log('备用xpath也没取到article元素: ', error)
            elmArrFlag = 'fail';
        }
    }

    if (elmArrFlag == 'fail') {
        console.error('预设的xpath无法获取到article标签,程序终止。');
        return;
    }

    console.log(`当前页共有${elmArr.length}篇报告。`);

    let allInfo = [];
    for (let i = 1; i <= elmArr.length; i++) {
        // category
        let categorySelector = `${usedPathXpath}[${i}]/div[2]/aside[1]/div/ul`
        const categoryElementHandle = await page.$x(categorySelector);
        const categoryText = await page.evaluate(el => el.innerText, categoryElementHandle[0]);

        // title 和 href
        let selector = `${usedPathXpath}[${i}]/div[2]/h2/a`
        const elementHandle = await page.$x(selector);
        const title = await page.evaluate(el => el.innerText, elementHandle[0]);
        const href = await page.evaluate(el => el.getAttribute("href"), elementHandle[0]);
        // const html = await page.evaluate(el => el.innerHTML, elementHandle[0]);

        // time
        let timeSelector = `${usedPathXpath}[${i}]/div[2]/aside[2]/div[1]/ul/li[2]/time`
        const timeElementHandle = await page.$x(timeSelector);
        const timeText = await page.evaluate(el => el.innerText, timeElementHandle[0]);

        let reportData = {
            title,
            url: href,
            category: categoryText,
            time: timeText
        }

        allInfo.push(reportData);
    }
    appendDataToFile(allInfo);
    console.log('已完成当前页数据解析,并保存到json。')
}

// 滑动屏幕，滚至页面底部
let autoScroll = (page) => {
    return page.evaluate(() => {
        return new Promise((resolve) => {
            var totalHeight = 0;
            var distance = 100;
            // 每200毫秒让页面下滑100像素的距离
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 200);
        })
    });
}

let appendDataToFile = (data) => {
    fs.appendFileSync(`./output/199it_report_lists_${moment().format('YYYYMMDDHH')}.json`, JSON.stringify(data, undefined, 2));
}

let index = async (nums) => {
    console.time('start')
    await getReportMuti(nums)
    console.timeEnd('start')

    // 小瑕疵：生成的json文件因为是批次追加的，并不是完整正确的json格式，需要把 `][`替换成 `,`即可。

}

index(2);