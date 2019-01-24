#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from testcase import buysale
import HTMLTestRunner
from testcase import tiaojiandan


#条件单
if __name__ == '__main__':
    # 构造测试集
    # unittest.TextTestRunner(verbosity=1).run(suite)
    suite = unittest.TestSuite()
    # 添加测试用例
    suite.addTest(tiaojiandan.TiaoJianDan("test_buyopen"))
    suite.addTest(tiaojiandan.TiaoJianDan("test_sellopen"))
    suite.addTest(tiaojiandan.TiaoJianDan("test_buyclose"))
    suite.addTest(tiaojiandan.TiaoJianDan("test_sellclose"))
    now_time = time.strftime("%Y%m%d_%H-%M-%S") # 本地日期时间作为测试报告的名字
    print(now_time)
    filename = 'F://Pycharm/html_result/'+ now_time + '_TestResult.html' # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()

