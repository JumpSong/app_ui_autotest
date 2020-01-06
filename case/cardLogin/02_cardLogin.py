# -*- encoding=utf8 -*-
__author__ = "zcq"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
from utils.base import Base

'''APP二次使用，信用卡号登录'''


class cardLogin2():

    def cardLogin2(self):
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
            print("----------------测试信用卡号登錄流程開始----------------------")
            sleep(10)

            # 点击快捷登录
            poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child(
                "android.view.ViewGroup").child("android.view.ViewGroup")[1].offspring(
                "CreditCard, tab, 2 of 3").offspring("android.widget.ImageView").click()

            poco(text="快捷登錄").click()
            # 切换到信用卡号登录
            poco(text="證件號登錄").click()
            swipe(Template(r"tpl1576725488897.png", record_pos=(0.006, 0.61), resolution=(1080, 2280)),
                  vector=[0.1507, 0.0809])
            touch(Template(r"tpl1576725505334.png", record_pos=(0.424, 0.455), resolution=(1080, 2280)))

            # 输入卡号
            poco(text="請輸入信用卡卡號").click()
            poco(text="6").click()
            poco(text="2").click()
            poco(text="6").click()
            poco(text="2").click()
            poco(text="9").click()
            poco(text="5").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="0").click()
            poco(text="1").click()
            poco(text="5").click()
            poco(text="4").click()

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
            assert_exists(Template(r"tpl1576725845426.png", record_pos=(0.001, -0.502), resolution=(1080, 2280)),
                          "发送短信成功")
            poco.swipe(point_a, center, direction)
            print("信用卡发送短信成功")
            print("----------------测试信用卡号流程結束----------------------")

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
    l = cardLogin2()
    l.cardLogin2()
    # 生成报告
    simple_report(__file__, logpath='./case/cardLogin/log', output='./report/cardLogin2.HTML')
