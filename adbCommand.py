import os
import re


def TwoDevices():#解决有两个模拟器问题（offine devices）
    os.system('adb kill-server')
    os.system('adb start-server')
    out = os.popen('adb devices').read()
    devices=out
    return devices
def getFocusedPackageAndActivity():
    pattern = re.compile( r"(.+?)/[a-zA-Z0-9\.]+")  # 这里使用了正则表达式，对输出的内容做了限制，只会显示类似"com.mediatek.factorymode/com.mediatek.factorymode.FactoryMode"的字符串
    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()  # window下使用findstr
    list = pattern.findall(out)
    component = list[0]  # 输出列表中的第一条字符串
    return component
print(TwoDevices())
print(getFocusedPackageAndActivity())
def install():
    os.system('adb unistall ')
