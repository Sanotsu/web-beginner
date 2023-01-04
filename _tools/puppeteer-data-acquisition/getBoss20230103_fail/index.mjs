
/**
 * inquirer 在v9之后不允许使用commonJS语法了，因为已经完全为native esm modules。
 *      要么使用import，要么降级到v8
 * 而默认只有mjs才能export导出，应该是不能同时使用import和require
 * 
 * 所以这个脚本就都是mjs
 */
import inquirer from 'inquirer'
import { formatBasicConditions, getJoblist } from "./utils.mjs"

let conditions = formatBasicConditions()
let questions = [
    {
        name: 'query',
        message: '岗位关键字',
        default: 'web'
    },
    {
        name: 'city',
        message: '城市关键字(必须输入完整且正确)',
        default: '重庆'
    },
    {
        type: 'list',
        name: 'experience',
        message: '工作经验',
        choices: conditions.experienceList.map(x => x.name),
        default: conditions.experienceList[7].name
    },
    {
        type: 'list',
        name: 'salary',
        message: '薪资待遇',
        choices: conditions.salaryList.map(x => x.name),
        default: conditions.salaryList[4].name
    },
    {
        type: 'list',
        name: 'stage',
        message: '融资阶段',
        choices: conditions.stageList.map(x => x.name),
        default: conditions.stageList[0].name
    },
    {
        type: 'list',
        name: 'scale',
        message: '公司规模',
        choices: conditions.scaleList.map(x => x.name),
        default: conditions.scaleList[2].name
    },
    {
        type: 'list',
        name: 'degree',
        message: '学历要求',
        choices: conditions.degreeList.map(x => x.name),
        default: conditions.degreeList[5].name
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
            // 输入对象的finished属性，不是查询条件，不往下面传
            delete answers.finished

            // 输入的是name，绝大部分都需要转为code
            getJoblist(answers)
        } else {
            return getAnswers();
        }
    });
}

getAnswers()

