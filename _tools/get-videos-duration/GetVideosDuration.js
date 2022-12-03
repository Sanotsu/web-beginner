const fs = require('fs')
const os = require('os')
const path = require('path')
const { getVideoDurationInSeconds } = require('get-video-duration')

/**
 * 为了使得整个过程同步，先递归找到所有文件夹和符合条件的文件，
 * 再一个一个的读取文件信息，拼接时长
 */

// 常见视频后缀
let defaultVideoFormats = [
    ".avi", ".wmv", ".mpeg", ".mp4", "mkv", "mpg",
    ".m4v", ".mov", ".asf", ".flv",
    ".f4v", ".rmvb", ".rm", ".3gp",
    ".vob"
]

// 如果当前路径含有忽略的文件夹关键字（例如系统内容、无权限文件夹）
let ingoreDirKeywords = [
    "System Volume Information",
    "Documents and Settings",
    "WindowsApp",
    "$RECYCLE",
    "$Recycle",
    "Windows",
    "Program Files",
    "node_modules",
    "_cacache",
    ".tmp",
    ".sys",
    ".exe",
]
// 忽略以下内容开头的文件夹
let ingoreDirStartWithKeywords = [
    ".",
    "~",
    "$",
    "#",
]

// 输出的文件名
let scannedFileLog = "scanned-files-info.log"
let scannedVideoLog = "scanned-videos-info.log"
let scannedIngoreDirLog = "scanned-ingore-info.log"

// 所有文件夹下的视频总时长
let allTotalDuration = 0

/**
 * 将秒数转为`x小时x分钟x秒`的结构
 * @param {*} seconds 秒数
 * @returns 
 */
let formatSecond = (seconds) => {
    var h = Math.floor(seconds / 3600);
    var m = Math.floor((seconds / 60 % 60));
    var s = Math.floor((seconds % 60));
    return h + "小时" + m + "分钟" + s + "秒";
}

/**
 * 递归读取文件夹,并获取视频文件信息
 *      把每个扫描的文件，都写到日志里去
 * @param {*} dir 当前扫描的路径
 * @param {*} fmts 需要匹配的视频格式
 * @returns 
 */
let readFileList = async (dir, fmts) => {
    // 同步读取指定文件夹
    // 在终端显示当前文件夹
    process.stdout.write(`当前文件夹: ${dir}\r`)

    const files = fs.readdirSync(dir)

    // 遍历当前路径所有内容
    for (let index = 0; index < files.length; index++) {
        const item = files[index];
        // 当前路径
        const fullPath = path.join(dir, item)

        // 如果文件夹在各个层级中，以. ~ 等开始的文件夹
        // 或者当前路径含有忽略的文件夹关键字（例如系统内容、无权限文件夹）则跳过
        let temp = fullPath.split(path.sep)

        if (temp.filter(p => p.startsWith(".")).length > 0
            || temp.filter(p => p.startsWith("$")).length > 0
            || temp.filter(p => p.startsWith("#")).length > 0
            || temp.filter(p => p.startsWith("~")).length > 0
            || ingoreDirKeywords.filter(v => fullPath.includes(v)).length > 0
        ) {

            // console.log("被忽略的路径: ", fullPath)
            fs.appendFileSync(scannedIngoreDirLog, fullPath + os.EOL, 'utf8')

            continue
        }

        // 获取当前路径的类型
        const stat = fs.statSync(fullPath)

        // 如果当前路径为文件夹,递归读取文件
        if (stat.isDirectory()) {
            readFileList(path.join(dir, item), fmts)
        } else {

            // 在终端显示当前文件
            process.stdout.write(`当前文件: ${fullPath}\r`)

            // 如果是文件，写入日志，并判断类别
            fs.appendFileSync(scannedFileLog, fullPath + os.EOL, 'utf8')

            let isVideoArr = fmts.filter(f => fullPath.toLowerCase().endsWith(f));
            // 如果视频文件
            if (isVideoArr.length > 0) {

                // 如果是视频文件，获取其时长，写入日志
                let duration = await getVideoDurationInSeconds(fullPath)
                allTotalDuration += parseFloat(duration)

                // 将需要的数据写入文件(时长 文件名 路径)
                let temp = "当前" + (duration + "秒").padEnd(16, " ")
                    + "约为" + formatSecond(duration).padEnd(16, " ")
                    + "累计" + formatSecond(allTotalDuration).padEnd(20, " ")
                    + fullPath + os.EOL;

                fs.appendFileSync(scannedVideoLog, temp, 'utf8');

            }
        }
    }
}

// 执行扫描的入口
let indexExec = async (dir, fmts) => {
    try {
        console.time('start')
        await readFileList(dir, fmts);
        console.timeEnd('start')
    } catch (error) {
        console.error("扫描文件出错:", error)
    }
}

module.exports = {
    indexExec: indexExec,
    formatSecond: formatSecond,
    defaultVideoFormats: defaultVideoFormats
}

