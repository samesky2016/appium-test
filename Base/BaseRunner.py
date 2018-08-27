# -*- coding: utf-8 -*-
from Base.BaseAppiumServer import AppiumServer
from Base.BaseLog import myLog
import unittest
from appium import webdriver
import os
from Base.BaseElementEnmu import Element
import platform
import time
from Base.BaseYaml import getYam

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(devices):
    desired_caps = {}

    if str(devices["platformName"]).lower() == "android":
        desired_caps['appPackage'] = devices["appPackage"]
        desired_caps['appActivity'] = devices["appActivity"]
        desired_caps['udid'] = devices["deviceName"]
        desired_caps['app'] = devices["app"]
        # desired_caps["recreateChromeDriverSessions"] = "True"
        # 解决多次切换到webview报错问题，每次切换到非chrome-Driver时kill掉session 注意这个设置在appium 1.5版本上才做了处理
    else:
        # desired_caps['automationName'] = devices["automationName"] # Xcode8.2以上无UIAutomation,需使用XCUITest
        desired_caps['bundleId'] = devices["bundleId"]
        desired_caps['udid'] = devices["udid"]
        # desired_caps['newCommandTimeout'] = 3600  # 1 hour

    desired_caps['platformVersion'] = devices["platformVersion"]
    desired_caps['platformName'] = devices["platformName"]
    #uiautomation2 支持
    desired_caps["automationName"] = devices['automationName']
    desired_caps['deviceName'] = devices["deviceName"]
    desired_caps["noReset"] = "False"
    desired_caps['noSign'] = "True"
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    desired_caps["systemPort"] = int(devices["systemPort"])

    # desired_caps['app'] = devices["app"]
    remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
    # remote = "http://127.0.0.1:" + "4723" + "/wd/hub"

    try:
        driver = webdriver.Remote(remote, desired_caps)

        return driver,"0"
    except:

        return driver,"1"



class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devicess

        devicess = param


    @classmethod
    def setUpClass(cls):
        pass
        # 注释掉通过unittest方式初始化基础数据，造成外部调用拿不到driver等数据
        cls.driver, cls.launch_app = appium_testcase(devicess)
        cls.devicesName = devicess["deviceName"]
        cls.logTest = myLog().getLog(cls.devicesName)  # 每个设备实例化一个日志记录器

    def setUp(self):
        # 注释掉通过unittest方式初始化基础数据，造成外部调用拿不到driver等数据
        # self.driver, self.launch_app = appium_testcase(devicess)
        # 每次用例执行完成重启一次app，而不断开会话，提升用例执行效率
        self.driver.launch_app()
    @classmethod
    def tearDownClass(cls):
        pass
        cls.driver.close_app()
        cls.driver.quit()

    def tearDown(self):

        pass
        # self.driver.close_app()
        # self.driver.quit()

    @staticmethod
    def parametrize(testcase_klass, param=None):
        # print("---parametrize-----")
        # print(param)
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
