#! /usr/bin/env python3
# coding=utf-8


import time
import unittest
from testcase.public import element


class YinQiZhuanZhang(unittest.TestCase):
     def test_rujin(self):
        driver = element.Element()
        driver.get_id("com.yingkuan.futures1:id/action_main_trade").click()
        time.sleep(5)
        driver.get_name("银期转账").click()
        driver.get_name("查询余额").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/et_bank_password").send_keys("023414")
        driver.get_id("com.yingkuan.futures1:id/et_fund_password").send_keys("023414")
        driver.get_name("确定").click()
        time.sleep(5)
        driver.get_id("com.yingkuan.futures1:id/et_price").send_keys("0.01")
        driver.get_id("com.yingkuan.futures1:id/et_bank_pwd").send_keys("023414")
        driver.get_id("com.yingkuan.futures1:id/et_fund_pwd").send_keys("023414")
        driver.get_name("确认转账").click()
        time.sleep(10)

     def test_chujin(self):
         driver = element.Element()
         driver.get_id("com.yingkuan.futures1:id/action_main_trade").click()
         time.sleep(5)
         driver.get_name("银期转账").click()
         driver.get_name("期货转银行").click()
         driver.get_id("com.yingkuan.futures1:id/et_price").send_keys("0.01")
         driver.get_id("com.yingkuan.futures1:id/et_fund_pwd").send_keys("023414")
         driver.get_name("确认转账").click()
         time.sleep(10)

