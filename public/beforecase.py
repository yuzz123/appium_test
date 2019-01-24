#! /usr/bin/env python
# coding=utf-8
import time
import unittest
from appium import webdriver
import HTMLTestRunner

class AppiumTest:
    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.yingkuan.futures1',
                        'appActivity': 'com.yingkuan.futures.model.SplashActivity',
                        'noReset': "True"
                       }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)


    def get_driver(self):
        return self.driver


    def tearDown(self):
        self.driver.quit()
        print
        "close app!"
        time.sleep(5)




