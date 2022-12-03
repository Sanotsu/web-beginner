<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!-- **Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)* -->

- [修改 root 帐号密码：](#%E4%BF%AE%E6%94%B9-root-%E5%B8%90%E5%8F%B7%E5%AF%86%E7%A0%81)
- [安装 openssh-server 并启用 ssh 可连：](#%E5%AE%89%E8%A3%85-openssh-server-%E5%B9%B6%E5%90%AF%E7%94%A8-ssh-%E5%8F%AF%E8%BF%9E)
- [修改左边启动器到底部：](#%E4%BF%AE%E6%94%B9%E5%B7%A6%E8%BE%B9%E5%90%AF%E5%8A%A8%E5%99%A8%E5%88%B0%E5%BA%95%E9%83%A8)
- [文件夹目录树状](#%E6%96%87%E4%BB%B6%E5%A4%B9%E7%9B%AE%E5%BD%95%E6%A0%91%E7%8A%B6)
- [安裝 deb 软件：](#%E5%AE%89%E8%A3%9D-deb-%E8%BD%AF%E4%BB%B6)
- [ubuntu 创建、删除文件及文件夹：](#ubuntu-%E5%88%9B%E5%BB%BA%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6%E5%8F%8A%E6%96%87%E4%BB%B6%E5%A4%B9)
- [设置为系统默认 JDK：](#%E8%AE%BE%E7%BD%AE%E4%B8%BA%E7%B3%BB%E7%BB%9F%E9%BB%98%E8%AE%A4-jdk)
- [安裝的桌面](#%E5%AE%89%E8%A3%9D%E7%9A%84%E6%A1%8C%E9%9D%A2)
- [安装 MATE 桌面](#%E5%AE%89%E8%A3%85-mate-%E6%A1%8C%E9%9D%A2)
- [卸载 MATE 桌面 Remove MATE desktop from Ubuntu](#%E5%8D%B8%E8%BD%BD-mate-%E6%A1%8C%E9%9D%A2-remove-mate-desktop-from-ubuntu)
- [vs code 搜索栏跑到下面或右边：](#vs-code-%E6%90%9C%E7%B4%A2%E6%A0%8F%E8%B7%91%E5%88%B0%E4%B8%8B%E9%9D%A2%E6%88%96%E5%8F%B3%E8%BE%B9)
- [桌面显示垃圾桶图标](#%E6%A1%8C%E9%9D%A2%E6%98%BE%E7%A4%BA%E5%9E%83%E5%9C%BE%E6%A1%B6%E5%9B%BE%E6%A0%87)
- [查看硬盘容量占用](#%E6%9F%A5%E7%9C%8B%E7%A1%AC%E7%9B%98%E5%AE%B9%E9%87%8F%E5%8D%A0%E7%94%A8)
- [硬盘分析工具](#%E7%A1%AC%E7%9B%98%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7)
- [sh 腳本設定權限](#sh-%E8%85%B3%E6%9C%AC%E8%A8%AD%E5%AE%9A%E6%AC%8A%E9%99%90)
- [linux 下停止 job](#linux-%E4%B8%8B%E5%81%9C%E6%AD%A2-job)
- [安裝 docker:](#%E5%AE%89%E8%A3%9D-docker)
- [docker 安裝 mariadb 示例：](#docker-%E5%AE%89%E8%A3%9D-mariadb-%E7%A4%BA%E4%BE%8B)
- [安裝 nginx](#%E5%AE%89%E8%A3%9D-nginx)
- [nvm 安装 nodejs](#nvm-%E5%AE%89%E8%A3%85-nodejs)
- [git warning: push.default 尚未设置](#git-warning-pushdefault-%E5%B0%9A%E6%9C%AA%E8%AE%BE%E7%BD%AE)
- [查看端口占用](#%E6%9F%A5%E7%9C%8B%E7%AB%AF%E5%8F%A3%E5%8D%A0%E7%94%A8)
- [压缩虚拟机硬盘大小](#%E5%8E%8B%E7%BC%A9%E8%99%9A%E6%8B%9F%E6%9C%BA%E7%A1%AC%E7%9B%98%E5%A4%A7%E5%B0%8F)
- [vbox 文件夹挂载后,需要将当期登录用户加入到 vboxsf 组](#vbox-%E6%96%87%E4%BB%B6%E5%A4%B9%E6%8C%82%E8%BD%BD%E5%90%8E%E9%9C%80%E8%A6%81%E5%B0%86%E5%BD%93%E6%9C%9F%E7%99%BB%E5%BD%95%E7%94%A8%E6%88%B7%E5%8A%A0%E5%85%A5%E5%88%B0-vboxsf-%E7%BB%84)
- [本虚拟机安装的 Dgraph 的学习镜像：](#%E6%9C%AC%E8%99%9A%E6%8B%9F%E6%9C%BA%E5%AE%89%E8%A3%85%E7%9A%84-dgraph-%E7%9A%84%E5%AD%A6%E4%B9%A0%E9%95%9C%E5%83%8F)
- [gradle 7 之后转换 gradle 项目为 maven 项目](#gradle-7-%E4%B9%8B%E5%90%8E%E8%BD%AC%E6%8D%A2-gradle-%E9%A1%B9%E7%9B%AE%E4%B8%BA-maven-%E9%A1%B9%E7%9B%AE)
- [查看指定文件夹大小](#%E6%9F%A5%E7%9C%8B%E6%8C%87%E5%AE%9A%E6%96%87%E4%BB%B6%E5%A4%B9%E5%A4%A7%E5%B0%8F)
- [查看 ubuntu 版本](#%E6%9F%A5%E7%9C%8B-ubuntu-%E7%89%88%E6%9C%AC)
- [把终端执行命令显示内容写到文件](#%E6%8A%8A%E7%BB%88%E7%AB%AF%E6%89%A7%E8%A1%8C%E5%91%BD%E4%BB%A4%E6%98%BE%E7%A4%BA%E5%86%85%E5%AE%B9%E5%86%99%E5%88%B0%E6%96%87%E4%BB%B6)
- [cron 定时任务](#cron-%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1)
- [查看 CPU 型号](#%E6%9F%A5%E7%9C%8B-cpu-%E5%9E%8B%E5%8F%B7)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 修改 root 帐号密码：

`sudo passwd root`

需要 ssh 远程可用 root 帐号：  
修改配置文件  
`sudo nano /etc/ssh/sshd_config`  
找到被注释的`PermitRootLogin`，修改为`PermitRootLogin yes`  
然后重新启动 ssh 服务即可：  
`sudo /etc/init.d/ssh restart` 或  
`sudo systemctl restart ssh`

### 安装 openssh-server 并启用 ssh 可连：

`sudo apt-get install openssh-server`  
修改配置文件：  
`sudo nano /etc/ssh/sshd_config`  
找到 GSSAPI options 这一节，将下面两行注释掉：

```
#GSSAPIAuthentication yes
#GSSAPIDelegateCredentials no
```

然后重新启动 ssh 服务即可：  
`sudo /etc/init.d/ssh restart` 或  
`sudo systemctl restart ssh`

### 修改左边启动器到底部：

`gsettings set com.canonical.Unity.Launcher launcher-position Bottom`

- 从底部还原到左侧：

`gsettings set com.canonical.Unity.Launcher launcher-position Left`

### 文件夹目录树状

導出文件夾目錄結構爲樹狀（linux）  
`tree -a > list.txt`
導出文件夾目錄結構爲樹狀（windows）  
`tree /a /f > list.txt`

### 安裝 deb 软件：

`sudo dpkg -i [gitkraken-amd64.deb](app name)`

### ubuntu 创建、删除文件及文件夹：

`mkdir 目录名` => 创建一个目录  
`rmdir 空目录名` => 删除一个空目录  
`rm 文件名 文件名` => 删除一个文件或多个文件  
`rm –rf 非空目录名` => 删除一个非空目录下的一切  
`touch 文件名` => 创建一个空文件

### 设置为系统默认 JDK：

```
sudo update-alternatives --install /usr/bin/java java /opt/java/jdk1.8.0_162/bin/java 300
sudo update-alternatives --install /usr/bin/javac javac /opt/java/jdk1.8.0_162/bin/javac 300
sudo update-alternatives --install /usr/bin/jar jar /opt/java/jdk1.8.0_162/bin/jar 300
sudo update-alternatives --install /usr/bin/javah javah /opt/java/jdk1.8.0_162/bin/javah 300
sudo update-alternatives --install /usr/bin/javap javap /opt/java/jdk1.8.0_162/bin/javap 300
```

百度地图应用 ak V8cdAESqe5GFeCp7POaAeldIRVK2bSG8

https://stackoverflow.com/questions/52189713/regular-expression-for-cron-expression-in-javascript

### 安裝的桌面

```
sudo apt-get install gnome-session-flashback GNOME Classic（Metacity）
sudo apt-get install gnome-flashback
sudo apt install xfce4
```

### 安装 MATE 桌面

```
sudo apt update && sudo apt upgrade -y
sudo apt install ubuntu-mate-desktop
```

### 卸载 MATE 桌面 Remove MATE desktop from Ubuntu

```
sudo apt remove -y ubuntu-mate-desktop mate-* ubuntu-mate-* plymouth-theme-ubuntu-mate-* lightdm  # 升级到18.04之后执行这个,机器就无法启动了
sudo apt autoremove -y
sudo apt install --reinstall -y gdm3
```

### vs code 搜索栏跑到下面或右边：

把设置里的 "search.location": "panel" 去掉 或者改成"search.location": "sidebar"

### 桌面显示垃圾桶图标

```
gsettings set org.gnome.nautilus.desktop trash-icon-visible true
```

### 查看硬盘容量占用

`df -hl`

- 当前文件夹大小
  `du -h`

### 硬盘分析工具

`sudo baobab`  
系统自带的,如果没有,则需安装  
`sudo apt-get install baobab`

### sh 腳本設定權限

`chmod +x test.sh`  
然後直接 ./test.sh 執行

### linux 下停止 job

ctrl+z  
需要繼續  
fg

ng serve --host 192.168.28.39 --port 4200

### 安裝 docker:

```
sudo sh -c "$(curl -fsSL https://get.docker.com)" 或 curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker $USER
```

### docker 安裝 mariadb 示例：

1、公共倉庫拉取鏡像到本地  
`docker pull mariadb`  
2、創建一個 mariadb 容器，並映射端口  
`docker run --name my-mariadb -e MYSQL_ROOT_PASSWORD=root -p3307:3306 -d mariadb:latest`  
3、訪問容器內部 mariadb 配置文件  
可以直接使用 docker exec -it my-mariadb bash 進入容器內部執行命令  
或者在 vscode 中安裝 docker 和 docker-container 插件，在 vscode 中打開容器內部文件/夾

### 安裝 nginx

```
sudo apt-get update
apt-get install nginx
```

配置文件位置: /etc/nginx/(sites-available/default)

### nvm 安装 nodejs

安装 nvm  
`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash`  
安装 nodejs  
`nvm install <version>`  
设置为默认  
`nvm alias default <version>`  
使用某一版本  
`nvm use <version>`  
查看已安装的版本  
`nvm ls`  
查看远端可用版本  
`nvm ls-remote`

### git warning: push.default 尚未设置

warning: push.default 尚未设置，它的默认值在 Git 2.0 已从 'matching'
变更为 'simple'。若要不再显示本信息并保持传统习惯，进行如下设置：

git config --global push.default matching

若要不再显示本信息并从现在开始采用新的使用习惯，设置：

git config --global push.default simple

当 push.default 设置为 'matching' 后，git 将推送和远程同名的所有
本地分支。

从 Git 2.0 开始，Git 默认采用更为保守的 'simple' 模式，只推送当前
分支到远程关联的同名分支，即 'git push' 推送当前分支。

### 查看端口占用

`sudo lsof -i:3307`

### 压缩虚拟机硬盘大小

```
1、 填 0 操作（如果是多个盘，请分别执行）
sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY
2、 vbox 导出虚拟机 ova,再导入(导出时会自行压缩,但导出导入非常耗时,没事的时候干)
```

### vbox 文件夹挂载后,需要将当期登录用户加入到 vboxsf 组

`sudo usermod -aG vboxsf $(whoami)`

### 本虚拟机安装的 Dgraph 的学习镜像：

`docker run --rm -it -p 8000:8000 -p 8180:8080 -p 9080:9080 dgraph/standalone:v20.11.2`  
浏览器访问 http://localhost:8000 DB 可视化界面

### gradle 7 之后转换 gradle 项目为 maven 项目

```
1 在 build.gradle 中加入
apply plugin: 'maven-publish'

2 在项目根目录下终端运行：
gradle publishToMavenLocal
```

注意：gradle 7 之后已经没有 maven 插件，改为了 maven-publish；gradle install 也没用了，而是 gradle publishToMavenLocal。

删除在本地 maven 仓库下.lastUpdated 文件：

```
find ./  -name "*.lastUpdated" -exec grep -q "Could not transfer" {} \; -print -exec rm {} \;
```

### 查看指定文件夹大小

进入该文件夹下，执行 `du -sh`

### 查看 ubuntu 版本

```
cat /etc/issue （简单）
cat /etc/lsb-release（具体）
uname -a（内核）
```

### 把终端执行命令显示内容写到文件

```
ls | tee ls.txt
```

追加到文本

```
ls | tee -a ls.txt
```

### cron 定时任务

编辑文件位置：`/var/spool/cron/crontabs`  
内容格式：`30 9 * * * gitlab-backup create`  
启动或暂停

```
service crond start
service crond stop
或
/etc/init.d/cron stop
/etc/init.d/cron start
```

### 查看 CPU 型号

```
sudo more /proc/cpuinfo | grep -i "model name"

```

### 复制文件夹

```
sudo cp -r <文件夹名> <目标位置文件夹名>
```

### 删除指定文件夹 30 天前的文件的脚本

编写脚本，内容为：

```sh
#!/bin/sh

find ./<需要删除的文件夹位置> -type f -ctime +30 | xargs rm -rf
```

保存在 shell 文件，并赋权限:

```sh
chmod +x <本sh文件>
```

或者放到 crontab 中，做定时任务

### 修改固定 IP

1 查看网卡名称

```
ip a
```

2 如果是 ubuntu20 以上，配置文件应该在`/etc/netplan/00-xxx.yaml`。补入以下内容：

注意 enp7s0 和 ens33，要对应替换成自己的网卡名称，也就是`ip a`里面看到的。

```yaml
network:
  ethernets:
    ens33: # 网卡名称，ip a 可见
      dhcp4: no # 不开启dhcp
      addresses: [192.168.1.100/24] # 固定ip
      optional: true
      gateway4: 192.168.1.1 # 网关
      nameservers:
        addresses: [114.114.114.114, 8.8.8.8] # nds
  version: 2
```

如果是 16.04，配置文件在`/etc/network/interfaces`,补入以下内容：

```
auto enp7s0 // 使用的网络接口，之前查询接口是为了这里
iface enp7s0 inet static // enp7s0这个接口，使用静态ip设置
address 10.0.208.222 // 设置ip地址
netmask 255.255.240.0 // 设置子网掩码
gateway 10.0.208.1 // 设置网关
dns-nameservers 10.0.208.1 // 设置dns服务器地址
```

3 应用配置：

20.04 新版本：

```
sudo netplan apply
```

16.04 旧版本

```
sudo ip addr flush enp7s0
sudo systemctl restart networking.service
```

### kill 进程

查看 pid 是否被占用：

`sudo lsof -p <pid号码>`

杀掉该进程：

`sudo kill -9 <pid号码>`

### 批量删除进程

rtprecv 为需要关闭的进程名关键字

```sh
$ ps -ef | grep rtprecv | grep -v grep | awk '{print $2}' | xargs kill -9

```

ps -ef 用于获取当前系统所有进程，如上图所示。  
grep rtprecv 过滤出与“rtprecv”字符相关的数据（以行为单位）。  
grep -v grep 的作用是除去本次操作所造成的影响，-v 表示反向选择。  
awk '{print $2}' 表示筛选出我们所关注的进程号，$2 表示每行第二个变量，在这个例子中就是进程号。所以如果你使用 ps 工具不一样，或者 ps 带的参数不一样，那需要关注的就可能不是$2，可能是$1 。  
xargs kill -9 中的 xargs 命令表示用前面命令的输出结果（也就是一系列的进程号）作为 kill -9 命令的参数，-9 表示强制终止，不是必须的。

上面是用 kill 配合过滤操作来完成，实际上还有更简单的方法——使用 killall 命令。killall 通过进程名字终止所有进程，用法如下：`killall -9 <process_name>` 。

https://blog.csdn.net/lu_embedded/article/details/53590815