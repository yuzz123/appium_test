#! /usr/bin/env python
# coding=utf-8
import time
import unittest
from appium import webdriver
import HTMLTestRunner

class Test111(unittest.TestCase):
    def setupclass(self):
        print('setup准备环境')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'  # 测试机Android版本
        desired_caps['deviceName'] = '127.0.0.1:62001'  # 测试机序列号 adb devices
        desired_caps['appPackage'] = 'com.yingkuan.futures1'  # 被测app包名
        desired_caps['appActivity'] = 'com.yingkuan.futures.model.SplashActivity'  # app启动的activity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(20)

    def tearDownclass(self):
        self.driver.quit()
        print
        "print('teardown清理环境')!"
        time.sleep(5)

    def test011(self):
        #未登录手机号，需先登录手机号，已登录直接跳至交易页面,登录期货账号
        try:
            self.driver.find_element_by_name("交易").click()
            self.driver.find_element_by_name("已有帐号，马上添加").click()
            self.driver.find_element_by_name("请输入手机号").send_keys("13738115595")
            self.driver.find_element_by_name("下一步").click()
            self.driver.find_element_by_id("com.yingkuan.futures1:id/et_login_pwd").send_keys("123456a")
            self.driver.find_element_by_id("com.yingkuan.futures1:id/btn_login").click()
            time.sleep(10)
            self.driver.find_element_by_id("com.yingkuan.futures1:id/et_trades_pwd").send_keys("023414")
            self.driver.find_element_by_id("com.yingkuan.futures1:id/btn_trades_login").click()
            time.sleep(10)
            items = self.driver.find_elements_by_id("com.yingkuan.futures1:id/recyclerView")
            if items is not None:  # 判断列表是否为空
                # 操作快平
                self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
                handnum = self.driver.find_element_by_id("com.yingkuan.futures1:id/etHandNum").text
                time.sleep(2)
                if int(handnum) == 1:
                    self.driver.find_element_by_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)
        except Exception as e:
            print(e)

    def test022(self):
        self.driver.find_element_by_name("交易").click()
        self.driver.find_element_by_id("com.yingkuan.futures1:id/btn_trades_order").click()
        self.driver.find_element_by_id("com.yingkuan.futures1:id/edit_search").send_keys("玉米1901")
        self.driver.find_elements_by_xpath( "//android.support.v7.widget.RecyclerView/com.yingkuan.futures1:id/itemLayout[1]").click()
        time.sleep(5)

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Test111("test011"))
    suite.addTest(Test111("test022"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)