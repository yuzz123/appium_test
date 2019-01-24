#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase import login
from testcase import xiadan
from testcase import kuaiping
from testcase import buysale
from testcase import fanshou
import HTMLTestRunner

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(login.Login("test_login_mb"))#登录手机号
    suite.addTest(login.Login("test_login_zjzh"))#登录资金账号
    suite.addTest(xiadan.Xiadan("test_buy"))#买多，锁仓
    suite.addTest(kuaiping.kuaiping("test_kuaiping"))#操作快平，全平
    suite.addTest(buysale.buysale("test_buy"))  # 买多
    suite.addTest(fanshou.Fanshou("test_fanshou"))  # 反多，反空-锁仓
    now_time = time.strftime("%Y%m%d_%H-%M-%S")  # 本地日期时间作为测试报告的名字
    print(now_time)
    filename = 'F://Pycharm/html_result/' + now_time + '_TestResult.html'  # 目录路径
    fp = open(filename, 'wb')
    runner= HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()
