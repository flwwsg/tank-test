### 启动步骤 

#### 软件环境
软件名 | 命令 | 描述 
--- | --- |---
nodejs for windows| 从官网下载|运行appium
android studio for windows | 从官网下载（需要翻墙） | 安装 android sdk，avd 虚拟机
java jdk 8(not jre 8) | 从官网下载 | 运行uiautomator2需要

#### steps for windows
ref: http://appium.io/docs/en/drivers/android-uiautomator2/index.html#requirements-and-support

以下配置虚拟机
- 设置环境变量 JAVA_HOME。 复制 “控制面板\系统和安全\系统” 到文件管理器地址栏中(不包含引号)在"高级系统设置->系统变量"中添加变量JAVA_HOME指向安装的 jdk8 路径
- 安装 android sdk (api版本26)，"高级系统设置->系统变量"添加变量 ANDROID_HOME 指向安装好的 sdk 路径
- 在android studio 中打开 avd 管理器，添加一个 android 8 的虚拟机。

启动测试 appium
- 安装appium。npm install -g appium
- 启动 appium。用管理员权限启动 powershell，输入 appium.cmd，启动appium

### 启动 android emulator

**所有操作需要管理员权限**

列出虚拟机 %username% 是当前用户名。
- cd C:\Users\%username%\AppData\Local\Android\Sdk\emulator -list-avds
- 从列出的虚拟中选择其中一个虚拟机名。C:\Users\%username%\AppData\Local\Android\Sdk\emulator -avd 选择的虚拟机名字