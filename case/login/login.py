# -*- encoding=utf8 -*-
__author__ = "song"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from utils.base import Base



class login():

    def login(self):
        #调用公共方法
        ba = Base()
        try:
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            #安装APP
            ba.install_app()
            sleep(10)
            # 启动APP
            ba.start_app()

            if not cli_setup():
                auto_setup(__file__, logdir="./case/login/log")
            sleep(2)
            print("----------------测试登錄流程開始----------------------")
            sleep(10)

            #看到手勢密碼，切換為賬號密碼登錄
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.ImageView").click()

            poco(text="更多").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[0].click()

            #輸入密碼
            poco(text="請輸入登錄密碼").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[0].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[1].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[2].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[3].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[4].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[5].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[6].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[7].child("android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup").click()
            poco(text="確定").click()

            #登錄
            poco(text="登錄").click()
            sleep(2)

            #驗證是否登錄成功

            #进入账户预览
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].click()

            #查看是否有总资产
            assert_exists(Template(r"tpl1575966345628.png",record_pos=(-0.045, -0.744), resolution=(1080, 2244)), "總資產(MOP)")
            print("登錄成功")
            print("----------------测试登錄流程結束----------------------")

            #退出app
            ba.stop_app()

        except Exception as e:
            print("-------------异常情况-------------")
            ba.log_error("登陆流程错误: \n %s"%(e))
            print(e)
            # 退出app
            ba.stop_app()





if __name__=="__main__":
    #执行
    l = login()
    l.login()
    # 生成报告
    simple_report(__file__, logpath='./case/login/log',output='./report/login.HTML')









