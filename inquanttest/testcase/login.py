#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase.public import element


class Login(unittest.TestCase):

    def test_login_mb(self):
        """
        资金账号登录方法,传入appium-driver
        APP启动时需要资金账号为登录状态时调用
        :param driver: Appium驱动
        :return: True
        """
        driver= element.Element() #实例化类
        #driver=appstart.get_driver() #调用实例方法
        driver.get_name("我的").click()
        time.sleep(2)
        driver.get_name("点击登录").click()
        time.sleep(3)
        driver.get_name("请输入手机号").send_keys("13738115595")
        time.sleep(3)
        driver.get_id("com.yingkuan.futures1:id/btn_login").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/et_login_pwd").send_keys("abc123")
        driver.get_id("com.yingkuan.futures1:id/btn_login").click()
        print('mobile_login ok')


    def test_login_zjzh(self):
        driver= element.Element()
        time.sleep(3)
        driver.get_name("交易").click()
        time.sleep(2)
        driver.get_id("com.yingkuan.futures1:id/btn_add_futures").click()
        futures=driver.get_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]")
        futuresname=futures.text
        print(futuresname)
        if futuresname=="创元期货":
            futures.click()
            driver.get_id("com.yingkuan.futures1:id/et_aaset_account").send_keys('10100229')
            driver.get_id("com.yingkuan.futures1:id/et_trades_pwd").send_keys('023414')
            driver.get_id("com.yingkuan.futures1:id/btn_trades_login").click()
            time.sleep(10)
            print("zjzh_login ok")







if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login_zjzh()"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)