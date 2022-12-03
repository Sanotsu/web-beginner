const fs = require('fs');
const puppeteer = require('puppeteer');

// 打开电商首页，输入想要的商品名称，点击搜索按钮，跳转至相应的商品列表页，然后一页页浏览，从而找到心仪的商品，这大概就是我们平时网购的样子。
// 那么如何让浏览器自动执行以上步骤，同时还能抽空爬取每页的商品信息，顺便将信息导出至文件呢？
// 有些操作的延迟时间比较大，模拟人员输入，避免拦截
// 这么多await但是没有trycatch

/*
page.title() 获取页面标题
page.type(selector, text[, options]) 获取输入框焦点并输入内容
page.click(selector[, options]) 点击要选择的元素
page.waitForNavigation([options]) 等待页面跳转
page.waitFor(selectorOrFunctionOrTimeout[, options[, ...args]]) 页面等待时间
fs.createWriteStream 对文件流进行写入
window.scrollBy(xnum, ynum) 页面向右、向下滑动的像素值
*/

// 本次模拟获取苏宁易购的数据，来抓取在售的所有笔记本电脑信息~
(async () => {
    const browser = await (puppeteer.launch({ headless: false }));
    const page = await browser.newPage();

    // 进入页面
    // await page.goto('https://search.suning.com/笔记本电脑/');
    await page.goto('https://www.suning.com');

    // 获取页面标题
    let title = await page.title();
    console.log('1 已打开页面,标题: ', title)

    // 等待页面跳转，注意：如果 click() 触发了一个跳转，会有一个独立的 page.waitForNavigation()对象需要等待
    // 2022-04-15 promise.all是并发的，但实际需要是依次执行的
    // await Promise.all([
    //     // 点击搜索框拟人输入“笔记本电脑”
    //     page.type('#searchKeywords', '笔记本电脑', { delay: 500 }),
    //     // 点击搜索按钮
    //     // await page.click('.search-btn btn-new');
    //     page.click('#searchSubmit'),
    //     page.waitForNavigation({ timeout: 0 }),
    // ]);

    // 点击搜索框拟人输入“笔记本电脑”
    await page.type('#searchKeywords', '笔记本电脑', { delay: 500 });
    // 点击搜索按钮
    // await page.click('.search-btn btn-new');
    await page.click('#searchSubmit');
    // await page.waitForNavigation({ timeout: 0 });

    await page.waitForTimeout(3000);

    console.log('2 已完成等待导航栏跳转')

    // 获取当前搜索项商品最大页数，为节约爬取时间，暂只爬取前5页数据
    // const maxPage = await page.evaluate(() => {
    //     return Number($('#bottomPage').attr('max'));
    // })
    const maxPage = 2;

    console.log('maxpage', maxPage)

    let allInfo = [];
    for (let i = 0; i < maxPage; i++) {
        // 因为苏宁页面的商品信息用了懒加载，所以需要把页面滑动到最底部，保证所有商品数据都加载出来
        await autoScroll(page);

        console.log(`3 第${i}页已拉倒最末尾 `)

        // 保证每个商品信息都加载出来
        await page.waitForTimeout(5000);

        console.log(`4 第${i}页 已完成等待5秒钟供商品加载。 `)

        // 获取每个
        const SHOP_LIST_SELECTOR = 'ul.general.clearfix';
        const shopList = await page.evaluate((sel) => {
            const shopBoxs = Array.from($(sel).find('li div.res-info'));
            const item = shopBoxs.map(v => {
                // 获取每个商品的名称、品牌、价格
                const title = $(v).find('div.title-selling-point').text().trim();
                const brand = $(v).find('b.highlight').text().trim();
                const price = $(v).find('span.def-price').text().trim();
                return {
                    title,
                    brand,
                    price,
                };
            });
            return item;
        }, SHOP_LIST_SELECTOR);
        allInfo = [...allInfo, ...shopList];

        appendDataToFile(shopList);
        console.log(`5 第${i}页 已完成商品数据的获取 ${shopList.length}。 当前总数量：`, allInfo.length)

        // 当当前页面并非最大页的时候，跳转到下一页
        if (i < maxPage - 1) {
            const nextPageUrl = await page.evaluate(() => {
                const url = $('#nextPage').get(0).href;
                return url;
            });
            await page.goto(nextPageUrl, { waitUntil: 'networkidle0' });
            // waitUntil对应的参数如下：
            // load - 页面的load事件触发时
            // domcontentloaded - 页面的 DOMContentLoaded 事件触发时
            // networkidle0 - 不再有网络连接时触发（至少500毫秒后）
            // networkidle2 - 只有2个网络连接时触发（至少500毫秒后）
        }
    }

    console.log(`6 已获取完既定的数据。共获取到${allInfo.length}台笔记本电脑信息`)

    // 将笔记本电脑信息写入文件
    writerStream = fs.createWriteStream('./output/notebook.json');
    writerStream.write(JSON.stringify(allInfo, undefined, 2), 'UTF8');
    writerStream.end();

    browser.close();

    console.log(`7 已完成数据写入json文件,并关闭浏览器,操作完成。`)

    // 滑动屏幕，滚至页面底部
    function autoScroll(page) {
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

    function appendDataToFile(data) {
        fs.appendFileSync(`./output/notebook-list.json`, JSON.stringify(data, undefined, 2));
    }

})();

