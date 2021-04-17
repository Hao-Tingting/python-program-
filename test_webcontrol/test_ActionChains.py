#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from test_webcontrol.base import Base


class TestActionChains(Base):
    browser = "chrome"
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_dbcli = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        ele_cli = self.driver.find_element_by_css_selector("body > form > input[type=button]:nth-child(10)")
        ele_rcli = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(ele_cli)
        action.double_click(ele_dbcli)
        action.context_click(ele_rcli)
        action.perform()
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele_move = self.driver.find_element_by_id("s-usersetting-top")

        action = ActionChains(self.driver)
        action.move_to_element(ele_move)
        action.perform()

    def test_intput(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_username = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele_username.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1).perform()
        time.sleep(3)

# if __name__ == '__main__':
#     pytest.main(['-v','-s','test_ActionChains.py'])