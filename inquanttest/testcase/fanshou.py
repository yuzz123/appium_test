#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase.public import element


class Fanshou(unittest.TestCase):
    def test_fanshou(self):#多仓反手
        driver= element.Element()
        driver.get_name("交易").click()
        time.sleep(5)
        buy=driver.get_xpath('//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.TextView[2]').text
        if str(buy)=='多':#多仓反手--下空仓
            driver.get_xpath( "//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[4]").click()
            handnum1 = driver.get_id("com.yingkuan.futures1:id/etHandNum").text
            time.sleep(2)
            if int(handnum1) == 1:
                driver.get_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)
            #空仓反手--下多仓
            driver.get_xpath( "//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[4]").click()
            handnum2 = driver.get_id("com.yingkuan.futures1:id/etHandNum").text
            time.sleep(2)
            if int(handnum2) == 1:
                driver.get_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)
        try:# 反手后锁仓
            driver.get_xpath( "//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[2]").click()
            driver.get_id('com.yingkuan.futures1:id/et_hand_num').send_keys('1')
            driver.get_name('锁仓').click()
            driver.get_id('com.yingkuan.futures1:id/dialog_sure').click()
        except Exception as e:
            print(e)




if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(("test_fanshou"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)