# -*- encoding=utf8 -*-
__author__ = "dell"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from utils.base import Base

class Logout():

    def logout(self):
        # 调用公共方法
        ba = Base()
        ba.login()

        if not cli_setup():
            auto_setup(__file__, logdir='./case/logout/log')
        try:
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

            # script content
            sleep(2)
            print("-------------登出流程开始----------------")
            #點擊我的
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].offspring("MineHome, tab, 3 of 3").offspring("android.widget.ImageView").click()
            #點擊設置
            poco(text="設置").click()
            #登出
            poco(text="退出登錄").click()
            poco(text="確定").click()
            print("登出成功")
            print("-------------登出流程结束----------------")

            # 退出app
            ba.stop_app()

        except Exception as e:
            print("-------------异常情况-------------")
            ba.log_error("登出流程错误: \n %s"%(e))
            print(e)
            # 退出app
            ba.stop_app()


if __name__=="__main__":
    #执行
    lo = Logout()
    lo.logout()
    #生成报告
    simple_report(__file__, logpath='./case/logout/log', output='./report/logout.HTML')



