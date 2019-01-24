#! /usr/bin/env python
# coding=utf-8
import time
import unittest
from testcase.public import element


class kuaiping(unittest.TestCase):
    def test_kuaiping(self):  # 平多仓
        driver = element.Element()  # 实例化类
        driver.get_name("交易").click()
        buy = driver.get_xpath('//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.TextView[2]').text
        if str(buy) == '多':
            driver.get_xpath("//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
            handnum1 = driver.get_id("com.yingkuan.futures1:id/etHandNum").text
            time.sleep(2)
            if int(handnum1) == 1:
                driver.get_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)
        #平空仓
        try:
            driver.get_xpath( "//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
            handnum1 = driver.get_id("com.yingkuan.futures1:id/etHandNum").text
            time.sleep(2)
            if int(handnum1) == 1:
                driver.get_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)
        except Exception as e:
                print(e)



if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    # suite.addTest(login.Loginmobile("test_zjzh_login"))
    suite.addTest(kuaiping("test_kuaiping"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)