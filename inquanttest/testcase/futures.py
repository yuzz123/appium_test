#! /usr/bin/env python
# coding=utf-8
import time
import unittest
from testcase.public import element


class future(unittest.TestCase):
    def test_getfuture(self):  # 获取期货账号
        driver = element.Element()  # 实例化类
        driver.get_name("交易").click()
        '''data=userread.read_file("F:\\Python 3.7\\userstest.txt")
        print(data)'''
        futures = driver.get_classes("android.support.v7.app.ActionBar$Tab")
        print(futures)
        for name, val in enumerate(futures):
            print("序号：%s   值：%s" % (name + 1, val))
        #print(name)
        for future in futures:
            if future=="创元期货":
                driver.get_id("com.yingkuan.futures1:id/et_trades_pwd").send_keys('023414')
                driver.get_id("com.yingkuan.futures1:id/btn_trades_login").click()
                time.sleep(10)
                print("zjzh_login ok")




if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(("test_getfuture"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)