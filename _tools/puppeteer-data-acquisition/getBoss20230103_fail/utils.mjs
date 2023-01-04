/**
【浏览器url】
指定城市、岗位关键字 的地址，可以根据输入拼接
https://www.zhipin.com/web/geek/job?query=web&city=101210100
https://www.zhipin.com/web/geek/job?query=web&city=101210100&page=3

×××××××××××××××××

之前没注意，20230103发现，有直接的【api】返回数据
岗位列表 json api：
https://www.zhipin.com/wapi/zpgeek/search/joblist.json?
scene=1&query=web&city=101210100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=1&pageSize=30

条件说明:
scene: 1
query: web                          关键字
city: 101210100                     城市代号
experience: 105,106                 工作经验
degree: 203                         学历要求
industry: 100020                    公司行业
scale: 302,303,301                  公司规模
stage: 802                          融资阶段
position: 100101                    职位类型
salary: 406                         薪资待遇
multiBusinessDistrict:330106        城市区域
page: 1                             页码
pageSize: 30                        每页数量

【对比】
地址栏的url:
https://www.zhipin.com/web/geek/job?query=web&city=101210100&experience=105,106&degree=203&scale=302,303,301&salary=406
api地址
https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=web&city=101210100&experience=105,106&degree=203&industry=&scale=302,303,301&stage=&position=&salary=406&multiBusinessDistrict=&page=1&pageSize=30

【条件数据】
热门城市站点
https://www.zhipin.com/wapi/zpgeek/common/data/citysites.json
通用【城市】信息
https://www.zhipin.com/wapi/zpCommon/data/cityGroup.json
指定城市【城市区域】划分
https://www.zhipin.com/wapi/zpgeek/businessDistrict.json?cityCode=101210100
筛选条件的【工作经验、薪资待遇、融资阶段、公司规模、学历要求】代号信息:
https://www.zhipin.com/wapi/zpgeek/search/job/condition.json
筛选条件的【公司行业】代号信息
https://www.zhipin.com/wapi/zpCommon/data/industry.json
筛选条件的【职位类型】代号信息
https://www.zhipin.com/wapi/zpCommon/data/position.json

国家代号
https://www.zhipin.com/wapi/zpuser/countryCode


【浏览器url输入的数据爬取】
打算是程序启动后，先检查本地有没有json文件，没有就去下载，有就处理城市的name和code结构放到内存，
在输入城市名称之后，获取其code，拼接url地址。如果找不到就跳过后面步骤

直接模拟页面访问的反扒机制
    如何随机
    头、代理等设置
    是点击翻页，还是直接重新输入url
    有可能会弹出登录弹窗，所以最好是登录之后再操作。使用cookie？

【直接控制pqs使用api】


    2022-01-04 结论:
    1. 用浏览器访问api地址频率不高还好，但使用http 客户端访问，则会被识别出来，得到“您的访问行为异常”的响应。
        模拟user-agent等请求头也一样，其cookie似乎不仅带有时间戳还有加盐
    2. 多访问异常几次，不仅浏览器访问api会提示IP异常暂时封禁的警告，正常访问网页也会提示输入图形验证码进行验证。
    3. 再多来几次验证之后，直接封禁IP24小时无法访问页面。
        这和我之前用puppeteer模拟浏览器访问页面是一样的结局……

    还是直接浏览器访问API之后把数据保存下来吧，这里，就当成操作浏览记录以下
 */

import fs from 'node:fs';
import { writeFile } from 'node:fs/promises';
import got, { Options } from 'got';
import puppeteer from 'puppeteer';

// got库配置通用头
const gotOptions = {
    prefixUrl: 'https://www.zhipin.com/wapi',
    // isStream: true,
    headers: {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Connection': 'keep-alive',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
}

// 存放条件json文件的路径
const condiyionDir = './self_conditions';
// 需要去下载的条件文件地址(got有配置prefixUrl的时候，不能以斜线开头)
const conditionUrls2 = [
    "https://www.zhipin.com/wapi/zpCommon/data/cityGroup.json",
    "https://www.zhipin.com/wapi/zpgeek/search/job/condition.json",
    "https://www.zhipin.com/wapi/zpCommon/data/industry.json",
    "https://www.zhipin.com/wapi/zpCommon/data/position.json"
]

const conditionUrls = [
    "zpCommon/data/cityGroup.json",
    "zpgeek/search/job/condition.json",
    "zpCommon/data/industry.json",
    "zpCommon/data/position.json"
]

// 岗位列表信息查询，?后面带参数
const joblistUrl = "zpgeek/search/joblist.json?"

// 默认的查询条件，后续有输入的话，替换这里的属性，然后当做参数拼接到get请求的API url中去
let queryConditions = {
    scene: 1,
    query: 'java',
    city: 101210100,
    experience: '105,106',      // 多选的值，是逗号相连的两个num，不是字符串？
    degree: 203,
    industry: '',               // 没有值的属性，不是空字符串、null、undefined，要怎么弄？
    scale: '302,303,301',       // 也是可多选的多个num？
    stage: '',
    position: '',
    salary: 406,
    multiBusinessDistrict: '',
    pageSize: 30,
    // page属性在查询调用url时在动态添加
    // page: 1,                    // 注意页数属性放在最后，可能在查询更多时会splice的时候用得到
}

/**
 * 获取准备条件
 */
let getBasicConditions = async () => {

    // 如果不存在文件夹，则创建
    try {
        if (!fs.existsSync(condiyionDir)) {
            fs.mkdirSync(condiyionDir)
        }

        // 获取数据
        conditionUrls.forEach(async (u) => {
            // body的结构是{"code": 0, "message": "Success","zpData":...}
            const { body } = await got(u, gotOptions) // 这里得到的body是个字符串没有结构了
            const { code, message, zpData } = JSON.parse(body)

            // Array.prototype.at()方法需要nodejs 16.16.0 以上版本支持
            let filename = u.split("/").at(-1)

            // 将body的zpData返回结果写入url对应的文件中去
            await writeFile(`${condiyionDir}/${filename}`, JSON.stringify(zpData));
        })

    } catch (error) {
        console.error("创建条件json文件夹失败", error)
    }
}

/** 
 * 把 experience、salary、stage、scale、degreeList几个简单的条件拼接放到全局变量去
 */
let formatBasicConditions = () => {
    try {
        let simpleConditionData = fs.readFileSync("./conditions/condition.json", 'utf-8');
        return JSON.parse(simpleConditionData)
    } catch (error) {
        console.error(error)
    }
}

/**
 * 把终端输入的条件，替换成api地址中对应的code信息，并拼接一个可用的api url
 */
let formatInputConditionObj = (obj) => {

    /**
     * 条件输入的对象是这样:
     * {  query: 'web',  city: '重庆',  experience: '5-10年',  salary: '10-20K',
     *   stage: '未融资',  scale: '20-99人',  degree: '本科',  finished: true }
     * api查询的条件属性是这样(逗号分割，没有传值的参数值为空字串):
     * scene: 1;page: 5;pageSize: 30;
     * query: web; city: 101210100;experience: 105,106;degree: 203;
     * industry: ;scale: 302,303,301;stage: ;position: ;salary: 406;multiBusinessDistrict: 330106;
     */
    try {

        // 处理简单的条件属性
        let condi = formatBasicConditions()
        let objKeys = Object.keys(obj)
        let condiKeys = Object.keys(condi)

        // 如果输入的对象的key属于条件对象的key，则对应替换其值为条件对象的code的值
        for (let i = 0; i < condiKeys.length; i++) {
            const e = condiKeys[i];
            for (let j = 0; j < objKeys.length; j++) {
                const v = objKeys[j];
                if (e.includes(v)) {
                    obj[v] = condi[e].filter(x => x.name == obj[v])[0].code
                }
            }
        }

        // 处理城市属性
        let cityGroup = fs.readFileSync("./conditions/cityGroup.json", 'utf-8');
        let cities = JSON.parse(cityGroup)
        let cityInfo = [];

        for (let i = 0; i < cities.cityGroup.length; i++) {
            const e = cities.cityGroup[i];
            // 这是把复合条件的城市信息记录下来。如果不必要，直接修改输入对象的值即可
            let fixedCitys = e.cityList.filter(v => v.name == obj.city)
            if (fixedCitys.length > 0) {
                cityInfo = cityInfo.concat(fixedCitys)
            }
        }
        obj.city = cityInfo[0].code

        // 参数合并，拼接最终查询需要的API地址
        let paramsObj = Object.assign(queryConditions, obj);
        let params = ""
        for (const key in paramsObj) {
            if (Object.hasOwnProperty.call(paramsObj, key)) {
                const val = paramsObj[key];
                if (val) {
                    params += `${key}=${val}&`
                } else {
                    params += `${key}=&`
                }
            }
        }

        // 正常来讲，最后会多一个&符号，删掉它
        return joblistUrl + params.slice(0, -1)

    } catch (error) {
        console.error("处理输入条件对象失败", error)
    }

}


let getJoblist = async (obj) => {
    let url = formatInputConditionObj(obj)

    let i = 1,
        finalUrl = url + `&page=${i}`

    console.log(`https://www.zhipin.com/wapi/` + finalUrl)

    /**
     * 直接访问地址结果会被侦测到，返回code37，您的访问行为异常
     * 尝试使用puppeteer模拟浏览器行为
     */

    await browserMockReqest(`https://www.zhipin.com/wapi/` + finalUrl)

    const { body } = await got(finalUrl, gotOptions)
    console.log('body', body)
}


// 原本希望模拟浏览器行为来绕过异常侦测，但并不行
let browserMockReqest = async (url) => {

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto(url);

    await page.screenshot({ path: `${condiyionDir}/self_screenshot.png`, fullPage: true });

    await browser.close();
}


getBasicConditions()
// formatBasicConditions()

export {
    formatBasicConditions,
    formatInputConditionObj,
    getJoblist,
}