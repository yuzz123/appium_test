#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase.public import element


class buysale(unittest.TestCase):
    def test_buy(self):#买入开仓
        driver= element.Element()
        driver.get_name("交易").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/btn_trades_order").click()
        time.sleep(2)
        sousuo=driver.get_id("com.yingkuan.futures1:id/edit_search")
        sousuo.send_keys("C1905")
        time.sleep(3)
        driver.get_xpath('//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout').click()
        driver.get_id('com.yingkuan.futures1:id/et_hand_num').send_keys('1')
        driver.get_name('买多').click()
        driver.get_id('com.yingkuan.futures1:id/dialog_sure').click()



    def test_sale(self):#卖出开仓
        driver= element.Element()
        driver.get_name("交易").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/btn_trades_order").click()
        time.sleep(2)
        sousuo=driver.get_id("com.yingkuan.futures1:id/edit_search")
        sousuo.send_keys("C1905")
        time.sleep(3)
        driver.get_xpath('//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout').click()
        driver.get_id('com.yingkuan.futures1:id/et_hand_num').send_keys('1')
        driver.get_name('卖空').click()
        driver.get_id('com.yingkuan.futures1:id/dialog_sure').click()






if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    #suite.addTest("test_buy")
    suite.addTest("test_sale")
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)