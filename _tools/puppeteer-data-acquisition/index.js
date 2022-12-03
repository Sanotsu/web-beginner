const fs = require('fs');
const puppeteer = require('puppeteer');
const moment = require('moment');



/**
 * 注意反扒机制。太频繁或者怎样，会需要验证，图片选择验证。
 *
 * 2022-04-15 问题：设置headless为true时一定会报错:
 *      滑动到页面底部失败:  Error: Execution context was destroyed, most likely because of a navigation.
 *      滑动到页面底部失败:  ProtocolError: Protocol error (Runtime.callFunctionOn): Execution context was destroyed.
 * 查不到什么原因，但设置为false时，就基本不会出现。
 *      
 *      简单分析来看，设为true的时候，执行到里面的 page.evaluate() 处就会报错。
 *          而且page.waitForNavigation()或者page.waitForSelector()会永远卡住，超时，或者永远等待。设为false则不会。
 *          但不等待，就一定出现上面 Execution context 的问题
 *      通过截图来看，是真的页面还在加载中……什么时候加载好不知道，或者永远加载不好？（false的话就没这个问题）
 * 2022-04-16 解决：headless的时候
 */

// 过滤条件
sifiConfig = {
    mainUrl: `https://www.zhipin.com`, // 这里末尾不带/，代码中拼接时有加
    city: `chongqing`,  // 目标城市，需要是拼音，url会进行拼接
    maxPage: 1,         // 需要获取的页数
    jobDesc: `web`,     // 搜索的职位、公司关键字
}

// https://www.zhipin.com/web/geek/job?query=web&city=101040100&page=2

// 网站上对应元素的selector
siteSelectorList = {
    // 职位、公司描述输入框
    jobInput: `#wrap > div.column-search-panel.search-panel-new > div > div.search-box > div.search-form > form > div.search-form-con > p > input`,
    // 首页的搜索按钮
    searchButton: `#wrap > div.column-search-panel.search-panel-new > div > div.search-box > div.search-form > form > button`,
    // 下一页按钮 （页面没有总页数，可能存在需要抓取的页数大于总页数的情况）
    // nextPage: `#main > div > div.job-list > div.page > a.next`,
    nextPage: `#wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > div > div > div > a:nth-child(10) > i`

}

/**
 * @param {*} sifiConds sifiConditions 筛选条件
 * @param {*} selectorList 页面上一些元素selector
 * 
 * 如果在trycatch中有报错的，返回false，进行重试
 */
let getBossZhipinJob = async (sifiConds = sifiConfig, selectorList = siteSelectorList) => {

    /******************* part 1 准备阶段，打开浏览器，输入城市和职位（更多筛选暂时没有） */
    const browser = await (puppeteer.launch({
        headless: false, //要看演示可以使用 false  // 设为ture好像要报错:  ProtocolError: Protocol error (Runtime.callFunctionOn): Execution context was destroyed.
        // dumpio:true, // 是否将浏览器进程标准输出和标准错误输入到 process.stdout 和 process.stderr 中。默认是 false
        ignoreHTTPSErrors: true, // 忽略不安全链接问题
        defaultViewport: { width: 1980, height: 1080 },
        args: [
            '--no-sandbox',
            '--window-size=2920,2080',
            // 不添加这个，intercept中response.json()或者text()时会报错：
            // ProtocolError: Could not load body for this request. This might happen if the request is a preflight request.
            "--disable-web-security",
        ],

    }));
    const page = await browser.newPage();

    // let userAgent = await browser.userAgent();
    // console.log(userAgent)
    // 2022-04-16 注意：如果设置了headless为ture，需要添加此行，才能避免顶部注释的问题。即便上一句打印能显示userAgent。
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36');


    // 进入页面
    await page.goto(`${sifiConds.mainUrl}/${sifiConds.city}`);
    // 获取页面标题
    let title = await page.title();

    console.log('1 =====> 进入首页，获取标题: ', title, ' job描述的关键字: ', sifiConds.jobDesc)

    // 点击搜索框拟人输入job描述。等待页面跳转，注意：如果 click() 触发了一个跳转，会有一个独立的 page.waitForNavigation()对象需要等待
    // 有可能一直卡住没有跳转，那只能重来。
    try {
        console.log('2 =====> 输入job描述的关键字, 等到页面跳转……')
        await page.type(selectorList.jobInput, sifiConds.jobDesc, { delay: 200 });
        // 点击搜索按钮
        await page.click(selectorList.searchButton);

        // await page.waitForSelector(`#main > div > div.job-list > ul`)
        await page.waitForNavigation({ timeout: 0 });

        console.log(' ----- 页面已经跳转,等待10秒供页面加载……')
        await page.waitForTimeout(10000)

    } catch (error) {
        console.error(' ***** 跳转到job列表页面失败: ', error)
        await page.screenshot({ path: './output/screenshot_wait_error.png', fullPage: true });
        return false;
    }


    /****************part2 如果有细则条件，需要点击筛选（不过全是下拉框，也提前不知道有哪些下拉框，可能不实现这个操作） */



    /****************part3 开始抓取数据 */

    console.log(`3 =====> 已完成等待导航栏跳转加载,开始获取数据,总共需要获取 ${sifiConds.maxPage} 页数据……`)
    let isFinishFlag = true;
    for (let i = 1; i <= sifiConds.maxPage; i++) {
        try {
            console.log(` ----- 开始把第 ${i} 页拉到底部……`)
            // 把页面滑动到最底部
            await autoScroll(page);
            // 拉到底后等待5秒，防止数据未加载完成
            console.log(` ----- 开始等待2秒供数据加载……`)
            await page.waitForTimeout(2000);

        } catch (error) {
            console.error(' ***** 滑动到页面底部失败: ', error)
            isFinishFlag = false;
            break;
        }

        console.log(` ----- 第 ${i} 页已经拉到底部并等待了2秒,开始处理页面数据…… `)

        try {
            // 单纯的job列表的ul没有样式   
            // 20220416 #main > div > div.job-list > ul
            // const JOB_LIST_SELECTOR = 'div.job-list ul';

            // 20220824 #wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > ul
            const JOB_LIST_SELECTOR = 'div.search-job-result ul';
            // 传入 sel 为 JOB_LIST_SELECTOR
            const jobList = await page.evaluate((sel) => {
                // 找到ul下每个job描述的样式
                const JobInfo = Array.from($(sel).find('li '));


                const item = JobInfo.map(v => {
                    // 获取每个职位的细项数据
                    // 20220415 #main > div > div.job-list > ul > li:nth-child(1) > div > div.info-primary > div.primary-wrapper > div > div.job-title > span.job-name
                    // const jobName = $(v).find('div.info-primary span.job-name').text().trim();

                    // 20220824 #wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > ul > li:nth-child(30) > div.job-card-body.clearfix > a > div.job-title.clearfix > span.job-name
                    const jobName = $(v).find('span.job-name').text().trim();

                    // 20220415 #main > div > div.job-list > ul > li:nth-child(1) > div > div.info-primary > div.primary-wrapper > div > div.job-title > span.job-name > a
                    // const jobDetailUrl = $(v).find('div.info-primary span.job-name a').get(0).href;

                    // 20220824 #wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > ul > li:nth-child(1) > div.job-card-body.clearfix > a
                    const jobDetailUrl = $(v).find('a.job-card-left').get(0).href;

                    // 20220824 #wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > ul > li:nth-child(1) > div.job-card-body.clearfix > a > div.job-title.clearfix > span.job-area-wrapper > span
                    const jobArea = $(v).find('span.job-area').text().trim();

                    // const salary = $(v).find('div.info-primary div.job-limit.clearfix span.red').text().trim();
                    // const yearsOfExperience = $(v).find('div.info-primary div.job-limit.clearfix p').text().trim();
                    // const companyName = $(v).find('div.info-primary div.company-text h3.name').text().trim();
                    // const companySize = $(v).find('div.info-primary div.company-text p').text().trim();

                    // const jobInfoDesc = $(v).find('div.info-append.clearfix div.info-desc').text().trim();
                    // // tag是多个,tag标签数组
                    // const jobTags = Array.from($(v).find('div.info-append.clearfix div.tags span'));
                    // let tags = [];
                    // jobTags.map(m => {
                    //     tags.push($(m).text().trim());
                    // })

                    return {
                        jobName,
                        jobDetailUrl,
                        jobArea,
                        // salary,
                        // yearsOfExperience,
                        // companyName,
                        // companySize,
                        // jobTags: tags.join(','),
                        // jobInfoDesc,
                    };
                });

                return item;
            }, JOB_LIST_SELECTOR);

            // 小瑕疵：生成的json文件因为是批次追加的，并不是完整正确的json格式，需要把 `][`替换成 `,`即可。
            appendDataToFile(jobList);
            console.log(` ----- 已完成第 ${i} 页数据解析,并保存到json。`)

        } catch (error) {
            console.error(` ***** 获取第 ${i} 页数据失败: `, error)
            isFinishFlag = false;
            break;
        }

        // 可能存在输入的需要获取的页数大于数据总页数(总数量没法从页面获取)，所以跳转下一页的条件是：当前页小于需要页数且有下一页可点击
        try {
            console.log("11111111")
            if (i < sifiConds.maxPage) {
                console.log("2222222222")
                // 注意: page.evaluate()中的console是不会生效的。
                const nextPageUrl = await page.evaluate((list) => {
                    const url = $(list.nextPage).get(0).href;
                    return url;
                }, selectorList);

                if (nextPageUrl) {
                    await page.goto(nextPageUrl, { waitUntil: 'networkidle0' });
                }
            }
        } catch (error) {
            console.error(` ***** 获取第 ${i} 页的下一页url失败: `, error)
            isFinishFlag = false;
            break;
        }
    }

    console.log(`4 =====> 数据处理流程完成,程序终止. `)
    browser.close();
    return isFinishFlag;


};

// 滑动屏幕，滚至页面底部（两个都有效）
let autoScroll = (page) => {
    return page.evaluate(() => {
        return new Promise((resolve) => {
            let totalHeight = 0;
            let distance = 100;
            // 每200毫秒让页面下滑100像素的距离
            let timer = setInterval(() => {
                let scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 500);
        })
    });
}


let autoScroll2 = (page) => {
    return page.evaluate(() => {
        return new Promise((resolve, reject) => {
            try {
                const maxScroll = Number.MAX_SAFE_INTEGER;
                let lastScroll = 0;
                const interval = setInterval(() => {
                    window.scrollBy(0, 100);
                    const scrollTop = document.documentElement.scrollTop;
                    if (scrollTop === maxScroll || scrollTop === lastScroll) {
                        clearInterval(interval);
                        resolve();
                    } else {
                        lastScroll = scrollTop;
                    }
                }, 100);
            } catch (err) {
                console.log(err);
                reject(err.toString());
            }
        });
    });
}


let appendDataToFile = (data) => {
    fs.appendFileSync(`./output/bosszhipin_job_list_${moment().format('YYYYMMDDHH')}.json`, JSON.stringify(data, undefined, 2));
}

let index = async () => {
    console.time('getBossZhipinJob')

    let isFinished = await getBossZhipinJob();

    console.log('------------------------------------------------------------------')

    if (!isFinished) {
        console.warn(`第一次执行失败 ${isFinished} ,开始重试…… `)
    }

    // 如果一次执行报错超过5次，也强行终止，不再继续尝试。
    let retryTimes = 0;
    while (!isFinished && retryTimes < 2) {

        isFinished = await getBossZhipinJob()
        retryTimes++;
        console.log(`进行了第 ${retryTimes} 次重试，执行结果(isFinished): `, isFinished)
    }

    console.log('final isFinished: ', isFinished)
    console.log('------------------------------------------------------------------')
    console.timeEnd('getBossZhipinJob')
}

index();