import re
import os

from InstallSoft import appLocation

appPackageAdb = list(os.popen('aapt dump badging ' + appLocation ).readlines())
appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0][0])
import os, re


# 检查apk版本号等信息
def getAppBaseInfo(parm_aapt_path, parm_apk_path):
    get_info_command = "%s dump badging %s" % (parm_aapt_path, parm_apk_path)  # 使用命令获取版本信息  aapt命令介绍可以相关博客


output = os.popen(get_info_command).read()  # 执行命令，并将结果以字符串方式返回
match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(
    output)  # 通过正则匹配，获取包名，版本号，版本名称
if not match:
    print
    output
raise Exception("can't get packageinfo")

packagename = match.group(1)
versionCode = match.group(2)
versionName = match.group(3)
print
u" 包名：%s \n 版本号：%s \n 版本名称：%s " % (packagename, versionCode, versionName)

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__)) + "\\"
aapt_path = path + "tools\\aapt.exe"  # 解析工具aapt.exe地址
apk_path = path + "publish_files\\TrunkingHome.apk"  # apk地址
getAppBaseInfo(aapt_path, apk_path)
