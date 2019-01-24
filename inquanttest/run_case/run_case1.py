#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase import login
import HTMLTestRunner

if __name__ == '__main__':
    # unittest.TextTestRunner(verbosity=1).run(suite)

    # 构造测试集
    suite = unittest.TestSuite()
    # 添加测试用例，登录手机号，登录资金账号
    suite.addTest(login.Login("test_login_mb"))
    suite.addTest(login.Login("test_login_zjzh"))
    now_time = time.strftime("%Y%m%d_%H-%M-%S")  # 本地日期时间作为测试报告的名字
    print(now_time)
    filename = 'F://Pycharm/html_result/' + now_time + '_TestResult.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner= HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()
