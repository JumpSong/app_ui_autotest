# -*- encoding=utf8 -*-
__author__ = "zcq"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from utils.base import Base

'''APP二次使用，信用卡证件号登录'''
class cardLogin():

    def cardLogin(self):
        # 调用公共方法
        ba = Base()
        try:
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            # 安装APP
            ba.install_app()
            sleep(10)
            # 启动APP
            ba.start_app()

            if not cli_setup():
                auto_setup(__file__, logdir="./case/cardLogin/log")
            sleep(2)
            print("----------------测试信用卡证件号登錄流程開始----------------------")
            sleep(10)

            # 点击快捷登录
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child(
                "android.view.ViewGroup").child("android.view.ViewGroup")[1].offspring(
                "CreditCard, tab, 2 of 3").offspring("android.widget.ImageView").click()

            poco(text="快捷登錄").click()

            # 选择证件类型
            poco(text="請選擇證件類型").click()
            swipe(Template(r"tpl1576663317394.png", record_pos=(-0.004, 0.863), resolution=(1080, 2280)),
                  vector=[0.1878, -0.0851])
            touch(Template(r"tpl1576663368014.png", record_pos=(0.424, 0.458), resolution=(1080, 2280)))
            # 输入证件号码
            poco(text="請輸入證件號碼").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[4].child("android.view.ViewGroup").offspring(
                "android.widget.ImageView").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[2].child("android.view.ViewGroup")[5].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[7].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[3].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[6].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[2].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[8].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[0].child("android.view.ViewGroup")[4].child(
                "android.view.ViewGroup").click()
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup")[
                1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup")[
                2].child("android.view.ViewGroup")[3].child("android.view.ViewGroup")[0].child(
                "android.view.ViewGroup").click()
            poco(text="確定").click()
            # 输入查询密码
            poco(text="請輸入信用卡查詢密碼").click()
            poco(text="1").click()
            poco(text="2").click()
            poco(text="3").click()
            poco(text="4").click()
            poco(text="5").click()
            poco(text="6").click()
            # 点击下一步，进入短信接收页面
            poco(text="下一步").click()
            assert_exists(Template(r"tpl1576663089827.png", record_pos=(-0.004, -0.497), resolution=(1080, 2280)),
                          "发送短信成功")


            print("信用卡发送短信成功")
            print("----------------测试信用卡证件号流程結束----------------------")

            # 退出app
            ba.stop_app()

        except Exception as e:
            print("-------------异常情况-------------")
            ba.log_error("登陆流程错误: \n %s" % (e))
            print(e)
            # 退出app
            ba.stop_app()


if __name__ == "__main__":
    # 执行
    l = cardLogin()
    l.cardLogin()
    # 生成报告
    simple_report(__file__, logpath='./case/cardLogin/log', output='./report/cardLogin.HTML')
