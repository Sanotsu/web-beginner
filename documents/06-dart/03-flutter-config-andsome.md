#### [在虚拟机 ubuntu 中安装 flutter](https://flutter.cn/docs/get-started/install/linux)

不用 snap，手动安装，位置在`/home/david/SOFT/flutter`

加入环境变量，找到主目录下的`.bashrc`文件进行编辑，加入：

```
export PATH="$PATH:/home/david/SOFT/flutter/bin"
```

再更新该文件`source .bashrc`，然后重开一个终端，使用`which flutter`查看 flutter 命令是否可用。
或者使用`which flutter dart`查看 dart 的命令是否可用。

**注意**：环境变量配置文件可能位置不同，避免出现以前配置的出现干扰。例如主目录下的`.bashrc`、`.profile`、`/etc/profile`等。

#### 运行`flutter doctor`查看依赖缺失

一般情况下，需要安装 Android studio 来配置一些 Android SDK 等相关内容。

在安装 AS 的时候，注意 sdkmanager 需要选上 sdk tools 中的 adk build-tools、Command-line tools、sdk platform-tools 等

反正 flutter doctor 中有报错的，都处理掉（除非是那些开发 linux 桌面端等需求的其他报错），常见要处理的:

```sh
# 要接收安卓开发的许可：
flutter doctor --android-licenses
# 安卓sdk配置的位置不对：
flutter config --android-sdk /home/david/SOFT/AndroidSDK
# Android Studio位置不对：
flutter config --android-studio-dir /home/david/SOFT/android-studio
```

---

需要安装 java11 以上，并确保 flutter 能够识别到该环境变量。

之前在 idea 中有下载 java17，在环境变量中配置该路径即可（或者自行下载解压），操作同上，配置如下:

```sh
export JAVA_HOME=/home/david/.jdks/temurin-17.0.6
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

主页配置完也更新一下`.bashrc`文件，然后使用`java -version`查看是否生效

2023-03-31 补充：

但是，可能会出现类似的问题：Could not open settings generic class cache for settings file，[参看](https://stackoverflow.com/questions/67240279/could-not-open-settings-generic-class-cache-for-settings-file)，则需要降级 java 到 11（推荐）或 8。

猜测是因为前一段时间写的，使用的库或者版本属于较旧版本。

---
