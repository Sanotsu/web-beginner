#!/bin/sh

#### mysql 定时备份脚本示例。放到 cron 配合使用。
DUMP=/usr/bin/mysqldump #mysqldump备份程序执行路径
OUT_DIR=/home/david/mysql_backup/mysql_data #备份文件存放路径
DB_NAME=voip #要备份的数据库名字
DB_USER=david #数据库账号 注意：非root用户要使用备份参数 --skip-lock-tables，否则可能会报错
DB_PASS=123456 #数据库密码
DAYS=7 #DAYS=7代表要删除7天前的备份，即只保留最近7天的备份
cd $OUT_DIR #进入备份存放的目录
DATE=`date +%Y%m%d%H%M%S` #获取当前系统的时间，注意：date写法
OUT_SQL=$DATE.sql #备份数据库的文件名
TAR_SQL="mysqldata_bak_$DATE.tar.gz" #最终保存的数据库备份文件名
# 如果只备份某些数据库的话，把 --all-databases 替换成指定DB_NAME即可
$DUMP -u$DB_USER -p$DB_PASS --all-databases --default-character-set=utf8 --opt -Q -R --skip-lock-tables>$OUT_SQL #执行备份命令
tar -czf $TAR_SQL ./$OUT_SQL #压缩为备份数据库文件为.tar.gz格式
rm $OUT_SQL #删除.sql格式的备份文件
find $OUT_DIR -name "mysqldata_bak*" -type f -mtime +$DAYS -exec rm {} \; #删除7天前的备份文件，注意：{} ;中间有空格

