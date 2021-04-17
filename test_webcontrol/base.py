#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import os
from selenium import webdriver

class Base:
    def setup(self):
        if self.browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_experimental_option("w3c",False)
            self.driver = webdriver.Chrome(options=option)
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            print("暂时没有其他浏览器")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()