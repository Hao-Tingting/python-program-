#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time
from test_webcontrol.base import Base

class TestForm(Base):
    browser = "chrome"
    def test_form(self):
        self.driver.get("http://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("zhangsan")
        self.driver.find_element_by_id("user_password").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[3]/div/label").click()
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input")
        time.sleep(3)