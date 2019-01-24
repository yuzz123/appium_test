#! /usr/bin/env python
# coding=utf-8
import time
import unittest
from testcase.public import element
from testcase import pingcang


class chedan(unittest.TestCase):
    def test_chedan(self):#平多仓
        driver = element.Element()  # 实例化类
        driver.get_name("交易").click()
        driver.get_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar$Tab[2]").click()
        items = driver.get_ids("com.yingkuan.futures1:id/recyclerView")
        print(items)
        if items is not None:  # 判断列表是否为空
            # 操作快平
            driver.get_xpath( "//android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
            handnum = driver.get_id("com.yingkuan.futures1:id/etHandNum").text
            time.sleep(2)
            if int(handnum) == 1:
                driver.get_id("com.yingkuan.futures1:id/tvSure").click()
                time.sleep(5)



if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    #suite.addTest(login.Loginmobile("test_zjzh_login"))
    suite.addTest(pingcang.pingcang("test_kuaiping"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)