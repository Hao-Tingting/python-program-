# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver is None:
            desired_cap = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": "com.xueqiu.android.common.MainActivity",
                "noReset": True,
                "automationName": "uiautomator2",
                "skipServerInstallation": True,
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"
                # "dontStopAppOnReset": True
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity("com.xueqiu.android","com.xueqiu.android.common.MainActivity")
        return self
    def main(self):
        return Main(self._driver)