
/**
 * inquirer 在v9之后不允许使用commonJS语法了，因为已经完全为native esm modules。
 *      要么使用import，要么降级到v8
 * 而默认只有mjs才能export导出，应该是不能同时使用import和require
 * 
 * 把本小脚本项目单独拿出来用时，才使用此内部的package.json
 */

const inquirer = require('inquirer')
const { resolve } = require('path')
const { indexExec, defaultVideoFormats } = require("./GetVideosDuration.js")

let questions = [
    {
        name: 'path',
        message: '需要查询的文件夹(默认为当前文件夹)',
        default: resolve('./')
    },
    {
        name: 'videoFormats',
        message: '需要筛选的视频格式(多个用逗号分开，如:mp4,avi): ',
        default: defaultVideoFormats
    },
    {
        type: "confirm",
        name: "finished",
        message: "是否确认输入正确?",
    },
]

let getAnswers = () => {
    return inquirer.prompt(questions).then(answers => {
        if (answers.finished) {

            // 格式化输入的视频格式
            let fmtStr = (answers.videoFormats + "").toLowerCase();
            // 如果有输入.的后缀就直接用，否则就加上.在前面
            let fmts = fmtStr.split(",").map(v => v.startsWith(".") ? v : `.${v}`)

            indexExec(answers.path, fmts)
        } else {
            return getAnswers();
        }
    }).catch(function (err) {
        console.error("getAnswers输入处理出错:", err);
    })
}

getAnswers()