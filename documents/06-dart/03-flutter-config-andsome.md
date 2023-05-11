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
# openjdk环境
# export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  ## 这里要注意目录要换成自己解压的jdk 目录
# 使用的ieda下载的java17，如果卸载了idea，注意看还在不在
# export JAVA_HOME=/home/david/.jdks/temurin-17.0.6
export JAVA_HOME=/home/david/.jdks/temurin-11.0.18
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

export PATH="$PATH:/home/david/SOFT/flutter/bin"
export ANDROID_SDK_ROOT=/home/david/SOFT/AndroidSDK
export ANDROID_SDK_HOME=/home/david/SOFT/AndroidSDK/platform-tools
export PATH="$PATH:$ANDROID_SDK_HOME"
```

主页配置完也更新一下`.bashrc`文件，然后使用`java -version`查看是否生效

2023-03-31 补充：

但是，可能会出现类似的问题：Could not open settings generic class cache for settings file，[参看](https://stackoverflow.com/questions/67240279/could-not-open-settings-generic-class-cache-for-settings-file)，则需要降级 java 到 11（推荐）或 8。

猜测是因为前一段时间写的，使用的库或者版本属于较旧版本。

---

#### 记录的一些问题

Q: windows 查看端口占用
A: windows 查看端口占用:`netstat -aon|findstr "8080"`，得到 pid，再使用 `tasklist|findstr "<pid>"` 获取任务信息。如下

```
C:\Users\davidsu> netstat -aon|findstr "5037"
  TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       4828
C:\Users\davidsu> tasklist|findstr "4828"
adb.exe                       4828 Console                    1     24,108 K
```

---

Q:一直弹窗显示“adb.exe 已经停止运作”，`flutter doctor`检测设备连接报错:

X Exception: Unable to run "adb", check your Android SDK installation and ANDROID_SDK_ROOT environment variable: C:\AndroidSdk\platform-tools\adb.exe

但实际上该位置有 adb.exe 且正常运行

```sh
C:\Users\davidsu>C:\AndroidSdk\platform-tools\adb.exe --version
Android Debug Bridge version 1.0.41
Version 33.0.3-8952118
Installed as C:\AndroidSdk\platform-tools\adb.exe
```

找不到解决办法，有类似的 issue：https://github.com/flutter/flutter/issues/55267

---

Q: 启动虚拟机报错：avd manager the emulator process was killed
A: https://stackoverflow.com/questions/36841461/error-android-emulator-gets-killed

---

Q：启动虚拟机报窗口信息：could not automatically detect an adb binary ……
A：https://blog.csdn.net/hou09tian/article/details/120339542

---

Q：linux 下启动 Android Studio 的模拟器失败：grant current user access to /dev/kvm
A https://blog.csdn.net/qq_36949176/article/details/92839527

---

Q：卡在: Running Gradle task 'assembleDebug'...
A：https://juejin.cn/post/6844904142511538184
maven { url 'https://maven.aliyun.com/repository/google' }
maven { url 'https://maven.aliyun.com/repository/jcenter' }
maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }

---

Q：在虛擬機中运行 AVD 时，会提示 Emulator is running using nested virtualization. This is not recommended. It may not work at all. And typically the performance is not quite good.
A：虚拟机里面跑安卓虛擬機，那不就是嵌套的虚拟化了，不管他就好。

---

Q：Android Studio: /dev/kvm device permission denied
A：https://stackoverflow.com/questions/37300811/android-studio-dev-kvm-device-permission-denied

---

Q：虚拟机内部无法上網，导致網絡請求不可用
A： step1 要宿主机有網
step2 https://stackoverflow.com/questions/54551198/how-to-solve-socketexception-failed-host-lookup-www-xyz-com-os-error-no-ad/55548864#55548864
step3 https://www.jianshu.com/p/cb738ad177ac
https://github.com/flutter/flutter/issues/27883 xai1983kbu 的回答

---

Q：为什么明明设定 1080*1920 的分辨率，结果显示是 360*600 左右
A：因為前者是 px，后者是 dp 单位不同，需要以后者參考布局

---

觉得太卡了要清除数据后启动

```
/development/AndroidSdk/emulator$ ./emulator -avd xiaomi6_API_30 -wipe-data -dns-server 8.8.8.8,114.114.114.114
正常启动就：（这是因为本虚拟机的/etc/resove.conf里面的nameserver第一个不能上网）
/development/AndroidSdk/emulator$ ./emulator -avd xiaomi6_API_30 -dns-server 8.8.8.8,114.114.114.114
/development/AndroidSdk/emulator/emulator -avd xiaomi6_API_30 -dns-server 8.8.8.8,114.114.114.114
```

---

Q：网页调试时，http 请求报错 XMLHttpRequest error
A：https://stackoverflow.com/questions/71157863/dart-flutter-http-request-raises-xmlhttprequest-error

---

Q：项目启动出现：Could not receive a message from the daemon.
A：網上都說是 vmware 虛擬機或者 windows 的熱點问题，关掉就可以了。但是台式机没有热点、也没有 vm 虚拟机也会出现此问题。

---

Q：D8: Cannot fit requested classes in a single dex file (# methods: 69584 > 65536)
A：https://stackoverflow.com/questions/55591958/flutter-firestore-causing-d8-cannot-fit-requested-classes-in-a-single-dex-file

---

flutter sdk 中有修改的地方
C:\flutter\packages\flutter_tools\gradle
resolve_dependencies.gradle
flutter.gradle
