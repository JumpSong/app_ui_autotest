# -*- encoding=utf8 -*-
__author__ = "song"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.report.report import simple_report
from utils.base import Base



class Transfer():

    def transfer(self):
        # 调用公共方法
        ba = Base()
        ba.login()
        if not cli_setup():
            auto_setup(__file__, logdir="./case/p_transfer/log")

        try:
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            sleep(2)
            print("----------------同行轉賬流程開始----------------------")
            #進入同行轉賬
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[3].child("android.view.ViewGroup")[3].child("android.widget.ImageView").click()
            sleep(2)
            #選擇轉出賬戶
            poco(text="").click()
            poco(text="幣種-CNY").click()
            sleep(5)

            #轉賬10
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[3].child("android.widget.TextView")[1].click()
            poco(text="1").click()
            poco(text="0").click()
            poco(text="確定").click()
            poco(text="預覽").click()
            poco(text="確定").click()

            #測試點，驗證是否轉賬成功
            assert_exists(Template(r"tpl1575891204100.png", record_pos=(0.005, -0.299), resolution=(1080, 1920)), "轉賬成功")
            print("轉賬流程測試成功")

            #返回首頁
            poco(text="完成").click()
            print("----------------同行轉賬流程結束----------------------")

            # 退出app
            ba.stop_app()

        except Exception as e:
            print("-------------异常情况-------------")
            ba.log_error("同行转账流程错误 \n %s"%(e))
            print(e)
            # 退出app
            ba.stop_app()





if __name__=="__main__":
    # 执行
    t = Transfer()
    t.transfer()
    # 生成报告
    simple_report(__file__, logpath='./case/p_transfer/log',output='./report/transfer.HTML')



