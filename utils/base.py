# -*- encoding=utf8 -*-
import shutil

from airtest.core.android import *
from airtest.core.android.adb import *
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from configparser import ConfigParser


from config.logger import Logger



# 獲取配置信息
cp = ConfigParser()
cp.read("./config/config.ini")
section = cp.sections()[0]
device = cp.get(section, "device1")
package = cp.get(section, "package")

logger = Logger(logger='Base').getlog()

# 获得当前设备列表
adb = ADB()
devicesList = adb.devices()
# 连几台基本上是知道的,也可以判断一下是否满足需要,如果不够就报个错
devicesNum = len(devicesList) > 0
assert_equal(devicesNum,True,"设备连接数量至少为2")
android = Android()
adb = ADB()

#公共类
class Base():

    #测试错误时记录日志到log目录下:error:日志信息
    def log_error(self,error):
        return logger.error(error)

    #自动连接设备
    def get_device(self):
         if not cli_setup():
             auto_setup(__file__, logdir=False, devices=[
                 device,
             ])

    #获取app包名
    def get_package(self):
        return package

    #登录
    def login(self):
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        try:
            print("----------------登錄----------------------")
            # 启动APP
            self.start_app()
            sleep(10)

            # 看到手勢密碼，切換為賬號密碼登錄
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child(
                "android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child(
                "android.view.ViewGroup").child("android.widget.ScrollView").child("android.view.ViewGroup").child(
                "android.view.ViewGroup")[0].child("android.widget.ImageView").click()

            poco(text="更多").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child(
                "android.view.ViewGroup").child("android.view.ViewGroup")[0].click()

            # 輸入密碼
            poco(text="請輸入登錄密碼").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[0].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[1].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[2].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[3].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[4].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[5].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[6].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[7].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child(
                "android.view.ViewGroup").click()
            poco(text="確定").click()
            sleep(2)
            # 登錄
            poco(text="登錄").click()

        except Exception as e:
            print("---------------登录异常------------------")
            self.log_error("登陆错误 \n %s"%(e))
            print(e)

    #启动app
    def start_app(self):
        return start_app(self.get_package())

    #关闭app
    def stop_app(self):
        return stop_app(self.get_package())

    #清除设备上目标应用程序的数据
    def clern_app(self):
        return clear_app(self.get_package())

    #唤醒屏幕
    def wake(self):
        return wake()

    #返回目标设备的主屏幕
    def home(self):
        return home()

    #安装APP
    def install_app(self):
        try:
            android.check_app(self.get_package())
            logger.info(self.get_package() + "——设备已安装")
        except AirtestError:
            # 安装应用,是否同意覆盖安装,默认否
            filePath = './res/app/'
            dirs = os.listdir(filePath)
            for file in dirs:
                logger.info(filePath+file)
                android.install_app(filePath+file, False)

    def clean_log(self):
        shutil.rmtree('要清空的文件夹名')
        os.mkdir('要清空的文件夹名')






