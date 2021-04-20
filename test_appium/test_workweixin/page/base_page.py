# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from appium import webdriver


class BasePage:
    def __init__(self, driver: webdriver = None):
        if driver is None:
            desired_cap = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "automationName": "uiautomator2",
                "skipServerInstallation": True,
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"
                # "dontStopAppOnReset": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        else:
            self.driver = driver
        self.driver.implicitly_wait(10)
