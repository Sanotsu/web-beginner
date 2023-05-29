<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [flutter 开发时一些环境建置的问题(持续更新)](#flutter-%E5%BC%80%E5%8F%91%E6%97%B6%E4%B8%80%E4%BA%9B%E7%8E%AF%E5%A2%83%E5%BB%BA%E7%BD%AE%E7%9A%84%E9%97%AE%E9%A2%98%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0)
  - [启动虚拟机报错：avd manager the emulator process was killed](#%E5%90%AF%E5%8A%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E6%8A%A5%E9%94%99avd-manager-the-emulator-process-was-killed)
  - [启动虚拟机报窗口信息：could not automatically detect an adb binary ……](#%E5%90%AF%E5%8A%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E6%8A%A5%E7%AA%97%E5%8F%A3%E4%BF%A1%E6%81%AFcould-not-automatically-detect-an-adb-binary-)
  - [linux 下启动 Android Studio 的模拟器失败：grant current user access to /dev/kvm](#linux-%E4%B8%8B%E5%90%AF%E5%8A%A8-android-studio-%E7%9A%84%E6%A8%A1%E6%8B%9F%E5%99%A8%E5%A4%B1%E8%B4%A5grant-current-user-access-to-devkvm)
  - [卡在: Running Gradle task 'assembleDebug'...](#%E5%8D%A1%E5%9C%A8-running-gradle-task-assembledebug)
  - [在虚拟机中运行虚拟机会弹窗警告](#%E5%9C%A8%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%E8%BF%90%E8%A1%8C%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%BC%9A%E5%BC%B9%E7%AA%97%E8%AD%A6%E5%91%8A)
  - [虚拟机内部无法上網，导致網絡請求不可用](#%E8%99%9A%E6%8B%9F%E6%9C%BA%E5%86%85%E9%83%A8%E6%97%A0%E6%B3%95%E4%B8%8A%E7%B6%B2%E5%AF%BC%E8%87%B4%E7%B6%B2%E7%B5%A1%E8%AB%8B%E6%B1%82%E4%B8%8D%E5%8F%AF%E7%94%A8)
  - [为什么明明设定 `1080*1920` 的分辨率，结果显示是 `360*600` 左右](#%E4%B8%BA%E4%BB%80%E4%B9%88%E6%98%8E%E6%98%8E%E8%AE%BE%E5%AE%9A-10801920-%E7%9A%84%E5%88%86%E8%BE%A8%E7%8E%87%E7%BB%93%E6%9E%9C%E6%98%BE%E7%A4%BA%E6%98%AF-360600-%E5%B7%A6%E5%8F%B3)
  - [网页调试时，http 请求报错 XMLHttpRequest error](#%E7%BD%91%E9%A1%B5%E8%B0%83%E8%AF%95%E6%97%B6http-%E8%AF%B7%E6%B1%82%E6%8A%A5%E9%94%99-xmlhttprequest-error)
  - [项目启动出现：Could not receive a message from the daemon.](#%E9%A1%B9%E7%9B%AE%E5%90%AF%E5%8A%A8%E5%87%BA%E7%8E%B0could-not-receive-a-message-from-the-daemon)
  - [D8: Cannot fit requested classes in a single dex file (# methods: 69584 > 65536)](#d8-cannot-fit-requested-classes-in-a-single-dex-file--methods-69584--65536)
  - [Do not use BuildContexts across async gaps](#do-not-use-buildcontexts-across-async-gaps)
  - [更新 Android Gradle 遇到的一些问题](#%E6%9B%B4%E6%96%B0-android-gradle-%E9%81%87%E5%88%B0%E7%9A%84%E4%B8%80%E4%BA%9B%E9%97%AE%E9%A2%98)
  - [在组件中修改状态出现类似报错: The widget on which setState() or markNeedsBuild() was called was:](#%E5%9C%A8%E7%BB%84%E4%BB%B6%E4%B8%AD%E4%BF%AE%E6%94%B9%E7%8A%B6%E6%80%81%E5%87%BA%E7%8E%B0%E7%B1%BB%E4%BC%BC%E6%8A%A5%E9%94%99-the-widget-on-which-setstate-or-markneedsbuild-was-called-was)
  - [使用一些功能组件（示例为 image_picker）依赖时报错包含:`Duplicate class androidx.lifecycle.ViewModelLazy  ……`](#%E4%BD%BF%E7%94%A8%E4%B8%80%E4%BA%9B%E5%8A%9F%E8%83%BD%E7%BB%84%E4%BB%B6%E7%A4%BA%E4%BE%8B%E4%B8%BA-image_picker%E4%BE%9D%E8%B5%96%E6%97%B6%E6%8A%A5%E9%94%99%E5%8C%85%E5%90%ABduplicate-class-androidxlifecycleviewmodellazy--)
  - [类似`Unhandled Exception: PlatformException`错误](#%E7%B1%BB%E4%BC%BCunhandled-exception-platformexception%E9%94%99%E8%AF%AF)
  - [windows 查看端口占用](#windows-%E6%9F%A5%E7%9C%8B%E7%AB%AF%E5%8F%A3%E5%8D%A0%E7%94%A8)
  - [一直弹窗显示“adb.exe 已经停止运作”，`flutter doctor`检测设备连接报错:](#%E4%B8%80%E7%9B%B4%E5%BC%B9%E7%AA%97%E6%98%BE%E7%A4%BAadbexe-%E5%B7%B2%E7%BB%8F%E5%81%9C%E6%AD%A2%E8%BF%90%E4%BD%9Cflutter-doctor%E6%A3%80%E6%B5%8B%E8%AE%BE%E5%A4%87%E8%BF%9E%E6%8E%A5%E6%8A%A5%E9%94%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# flutter 开发时一些环境建置的问题(持续更新)

---

## 启动虚拟机报错：avd manager the emulator process was killed

可能需要根据 Android API 版本更新一下 Android Emulator 。

[参看](https://stackoverflow.com/questions/36841461/error-android-emulator-gets-killed)

## 启动虚拟机报窗口信息：could not automatically detect an adb binary ……

这是没有自动检测 ADB binary，可以在虚拟机左侧的 settings -> General 选项中关闭自动检测，然后手动指定 ADB 路径。

[参看](https://blog.csdn.net/hou09tian/article/details/120339542)

---

## linux 下启动 Android Studio 的模拟器失败：grant current user access to /dev/kvm

给当前的`/dev/kvm`授权

可以在 Android Studio 的 Terminal 里面输入

```
sudo chown <uname> -R /dev/kvm
```

这里的 `<uname>`就是你当前用户用户名

[参看 1](https://blog.csdn.net/qq_36949176/article/details/92839527)、[参看 2](https://stackoverflow.com/questions/37300811/android-studio-dev-kvm-device-permission-denied)

---

## 卡在: Running Gradle task 'assembleDebug'...

这个一般是网络不佳或者首次运行是比较多，最好是使用`flutter run -v`打印运行日志，确定为什么卡住。

大多数时候是因为国内的网下载依赖非常慢，可以修改对应的源到国内，例如修改 flutter 项目中的`android/build.gradle`文件

```
repositories {
// 这里做了修改，使用国内阿里的代理
// google()
// jcenter()
 maven { url 'https://maven.aliyun.com/repository/google' }
 maven { url 'https://maven.aliyun.com/repository/jcenter' }
 maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }
 }
```

对应 flutter sdk 中有修改的地方类似：

```
C:\flutter\packages\flutter_tools\gradle
resolve_dependencies.gradle
flutter.gradle
```

[参看](https://juejin.cn/post/6844904142511538184)

---

## 在虚拟机中运行虚拟机会弹窗警告

类似提示 `Emulator is running using nested virtualization. This is not recommended. It may not work at all. And typically the performance is not quite good.`

A：虚拟机里面跑 AVD，那不就是嵌套的虚拟化了，不管他就好。

## 虚拟机内部无法上網，导致網絡請求不可用

1 要宿主机有網

2 app 要有上网权限：`android/app/src/main/AndroidManifest.xml`中添加

```
<uses-permission android:name="android.permission.INTERNET"/>
```

3 还不行，则双清虚拟机再试，类似：

```
C:\Users\UN\AppData\Local\Android\Sdk\emulator> .\emulator -avd Nexus_5X_API_28 -wipe-data
```

[参看](https://github.com/flutter/flutter/issues/27883)

---

## 为什么明明设定 `1080*1920` 的分辨率，结果显示是 `360*600` 左右

A：因为前者是 px，后者是 dp 单位不同，需要以后者參考布局。参看[flutter_screenutil](https://pub.dev/packages/flutter_screenutil)查看的使用。

---

觉得太卡了要清除数据后启动

```
/development/AndroidSdk/emulator$ ./emulator -avd xiaomi6_API_30 -wipe-data -dns-server 8.8.8.8,114.114.114.114
正常启动就：（这是因为本虚拟机的/etc/resove.conf里面的nameserver第一个不能上网）
/development/AndroidSdk/emulator$ ./emulator -avd xiaomi6_API_30 -dns-server 8.8.8.8,114.114.114.114
/development/AndroidSdk/emulator/emulator -avd xiaomi6_API_30 -dns-server 8.8.8.8,114.114.114.114
```

---

## 网页调试时，http 请求报错 XMLHttpRequest error

可能单纯是 Uri 的方法使用错了，例如使用 `Uri.parse(url)`代替了 `Uri.https('urlPath', 'callPath')`。

[参看](https://stackoverflow.com/questions/71157863/dart-flutter-http-request-raises-xmlhttprequest-error)

---

## 项目启动出现：Could not receive a message from the daemon.

A：網上都說是 vmware 虛擬機或者 windows 的熱點问题，关掉就可以了。但是台式机没有热点、也没有 vm 虚拟机也会出现此问题。

---

## D8: Cannot fit requested classes in a single dex file (# methods: 69584 > 65536)

A：https://stackoverflow.com/questions/55591958/flutter-firestore-causing-d8-cannot-fit-requested-classes-in-a-single-dex-file

---

## Do not use BuildContexts across async gaps

出现类似的警告：

```sh
Don't use 'BuildContext's across async gaps.Try rewriting the code to not reference the 'BuildContext'
```

---

A：在警告处检查组件是否挂载完成:

```dart
if (!mounted) return;
```

[参看](https://stackoverflow.com/questions/68871880/do-not-use-buildcontexts-across-async-gaps)

## 更新 Android Gradle 遇到的一些问题

出现类似警告信息:

```sh
Warning: Mapping new ns http://schemas.android.com/repository/android/common/02 to old ns http://schemas.android.com/repository/android/common/01
Warning: Mapping new ns http://schemas.android.com/repository/android/generic/02 to old ns http://schemas.android.com/repository/android/generic/01
Warning: Mapping new ns http://schemas.android.com/sdk/android/repo/addon2/02 to old ns http://schemas.android.com/sdk/android/repo/addon2/01
```

---

A: 是因为 gradle 版本太旧了，需要升级一下。[参看](https://stackoverflow.com/questions/68600352/build-warning-mapping-new-ns-to-old-ns)

**要特别注意 jdk 和 maven 的 gradle 以及 android gradle 版本的对应关系。**

2023-05-17 更新本项目对应是 ：`jdk 11.0.18  - AGP 7.4.2 - gradle 7.6`，参看[更新 Gradle](https://developer.android.google.cn/studio/releases/gradle-plugin?hl=zh-cn)

修改`android/build.gradle`文件

```
buildscript {
    repositories {
        google()
        mavenCentral()
    }

    dependencies {
        classpath 'com.android.tools.build:gradle:7.4.2' # Update this line,我之前是4.1.0
        ...
    }
}
```

和`android/gradle/wrapper/gradle-wrapper.properties`文件

```s
distributionUrl=https\://services.gradle.org/distributions/gradle-7.6-all.zip # Update this line 我之前是6.7
```

注意，**更新之后可能出现类似错误**:

```sh
Using insecure protocols with repositories, without explicit opt-in, is unsupported. Switch Maven repository 'maven3(http://maven.aliyun.com/nexus/content/groups/public)' to redirect to a secure protocol (like HTTPS) or allow insecure protocols.
```

这应该是修改了默认 maven 仓库地址，需要修改`android/build.gradle`文件中自定义的 maven 地址，忽略不安全协议：

```s
# 之前:
maven {
    url 'https://maven.aliyun.com/repository/google'
}
# 改为:
maven {
    allowInsecureProtocol = true
    url 'https://maven.aliyun.com/repository/google'
}
```

**注意，慎重直接修改到最新版本，可能出现兼容问题**，类似：

```sh
Android Gradle plugin requires Java 17 to run. You are currently using Java 11.
[        ]       Your current JDK is located in /home/david/.jdks/temurin-11.0.18
```

这是因为我的 jdk 是 11 版本，直接使用的`com.android.tools.build:gradle:8.0.1`时就报错了，因为它[最低要求 jdk17](https://developer.android.com/build/releases/gradle-plugin#jdk-17-agp)，所以又改回来了。

**注意，升级 AGP 也要注意插件的兼容性。**

例如 AGP 升级到 7.4.2，`image_gallery_saver: ^1.7.1` 需要`org.jetbrains.kotlin:kotlin-gradle-plugin:1.3.72`这个版本，但前者只支持`1.5.20`或更高。这就导致要么降级，要么升级插件。如果插件本身就很久没更新了，那就得重写功能业务代码了。

**如果继续出现类似错误**:

```sh
 Script '/home/david/SOFT/flutter/packages/flutter_tools/gradle/flutter.gradle' line: 1151
[        ] * What went wrong:
[        ] Execution failed for task ':app:compileFlutterBuildDebug'.
[        ] > Process 'command '/home/david/SOFT/flutter/bin/flutter'' finished with non-zero exit value 1
[        ] * Try:
[        ] > Run with --debug option to get more log output.
[        ] > Run with --scan to get full insights.
[        ] * Exception is:
[        ] org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':app:compileFlutterBuildDebug'.
[        ]      at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.lambda$executeIfValid$1(ExecuteActionsTaskExecuter.java:142)
[        ]      at org.gradle.internal.Try$Failure.ifSuccessfulOrElse(Try.java:282)
```

则更新一下依赖:

```sh
flutter clean
flutter pub get
```

## 在组件中修改状态出现类似报错: The widget on which setState() or markNeedsBuild() was called was:

```sh
This _InheritedProviderScope<AudioInList?> widget cannot be marked as needing to build because the framework is already in the process of building widgets. A widget can be marked as needing to be built during the build phase only if one of its ancestors is currently building. This exception is allowed because the framework builds parent widgets before children, which means a dirty descendant will always be built. Otherwise, the framework might not visit this widget during this build phase.
The widget on which setState() or markNeedsBuild() was called was: _InheritedProviderScope<AudioInList?>
```

---

A：我这里是使用了 provider 库，在使用 notifyListeners()时，在重建它之前，等待构建方法完成

```
WidgetsBinding.instance.addPostFrameCallback((_) {
  notifyListeners();
});
```

[参看](https://stackoverflow.com/questions/60852896/widget-cannot-be-marked-as-needing-to-build-because-the-framework-is-already-in)第二个答案

---

## 使用一些功能组件（示例为 image_picker）依赖时报错包含:`Duplicate class androidx.lifecycle.ViewModelLazy  ……`

```sh
 Duplicate class androidx.lifecycle.ViewModelLazy found in modules jetified-lifecycle-viewmodel-ktx-2.3.1-runtime (androidx.lifecycle:lifecycle-viewmodel-ktx:2.3.1) and lifecycle-viewmodel-2.5.1-runtime (androidx.lifecycle:lifecycle-viewmodel:2.5.1)
```

参看: https://issuetracker.google.com/issues/242384116#comment4 。对应修改 build.gradle 中的相关参数

## 类似`Unhandled Exception: PlatformException`错误

输出日志类似：

```sh
 [ERROR:flutter/runtime/dart_vm_initializer.cc(41)] Unhandled Exception: PlatformException(channel-error, Unable to establish connection on channel., null, null)
```

可能是依赖过时，可尝试更新：

```
flutter pub outdated
```

Then upgrade the outdated packages one by one like this:

```
flutter pub upgrade outdated_package
```

After you're finished:

```
flutter clean
```

and

```
flutter pub get
```

[参看](https://stackoverflow.com/questions/72880037/unhandled-exception-platformexceptionchannel-error-unable-to-establish-connec)

---

## windows 查看端口占用

A: windows 查看端口占用:`netstat -aon|findstr "8080"`，得到 pid，再使用 `tasklist|findstr "<pid>"` 获取任务信息。如下

```
C:\Users\davidsu> netstat -aon|findstr "5037"
  TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       4828
C:\Users\davidsu> tasklist|findstr "4828"
adb.exe                       4828 Console                    1     24,108 K
```

---

## 一直弹窗显示“adb.exe 已经停止运作”，`flutter doctor`检测设备连接报错:

总是报错：

```sh
X Exception: Unable to run "adb", check your Android SDK installation and ANDROID_SDK_ROOT environment variable: C:\AndroidSdk\platform-tools\adb.exe
```

但实际上该位置有 adb.exe 且正常运行

```sh
C:\Users\davidsu>C:\AndroidSdk\platform-tools\adb.exe --version
Android Debug Bridge version 1.0.41
Version 33.0.3-8952118
Installed as C:\AndroidSdk\platform-tools\adb.exe
```

找不到解决办法，有类似的 issue：https://github.com/flutter/flutter/issues/55267
