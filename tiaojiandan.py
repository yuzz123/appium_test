#! /usr/bin/env python3
# coding=utf-8


import time
import unittest
from testcase.public import element


class TiaoJianDan(unittest.TestCase):
    #设置买入开仓实时触发条件单
    def test_buyopen(self):
        driver = element.Element()
        driver.get_name("交易").click()
        driver.get_name("条件单").click()
        driver.get_name("+创建条件单").click()
        driver.get_id("com.yingkuan.futures1:id/edit_search").send_keys("玉米1905")
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/itemLayout").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/switchTriggerTime").click() #关闭时间
        driver.get_id("com.yingkuan.futures1:id/ivHighPrice").click()
        driver.get_id("com.yingkuan.futures1:id/ivLowPrice").click()
        driver.get_name("确认").click()
        time.sleep(5)
        driver.get_name("继续").click()
        time.sleep(10)


    #设置卖出开仓实时触发条件单
    def test_sellopen(self):
        driver = element.Element()
        driver.get_name("交易").click()
        driver.get_name("条件单").click()
        driver.get_name("+创建条件单").click()
        driver.get_id("com.yingkuan.futures1:id/edit_search").send_keys("玉米1905")
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/itemLayout").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/switchTriggerTime").click() #关闭时间
        driver.get_name("卖出").click()
        driver.get_name("确认").click()
        time.sleep(5)
        driver.get_name("继续").click()
        time.sleep(10)



    #设置买入平仓实时触发条件单
    def test_buyclose(self):
        driver = element.Element()
        driver.get_name("交易").click()
        driver.get_name("条件单").click()
        driver.get_name("+创建条件单").click()
        driver.get_id("com.yingkuan.futures1:id/edit_search").send_keys("玉米1905")
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/itemLayout").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/switchTriggerTime").click() #关闭时间
        driver.get_id("com.yingkuan.futures1:id/ivHighPrice").click()
        driver.get_id("com.yingkuan.futures1:id/ivLowPrice").click()
        driver.get_name("平仓").click()
        driver.get_name("确认").click()
        time.sleep(5)
        driver.get_name("继续").click()
        time.sleep(10)



    #设置卖出平仓实时触发条件单
    def test_sellclose(self):
        driver = element.Element()
        driver.get_name("交易").click()
        driver.get_name("条件单").click()
        driver.get_name("+创建条件单").click()
        driver.get_id("com.yingkuan.futures1:id/edit_search").send_keys("玉米1905")
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/itemLayout").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/switchTriggerTime").click() #关闭时间
        driver.get_name("卖出").click()
        driver.get_name("平仓").click()
        driver.get_name("确认").click()
        time.sleep(5)
        driver.get_name("继续").click()
        time.sleep(10)




