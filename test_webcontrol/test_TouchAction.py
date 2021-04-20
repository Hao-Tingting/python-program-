#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
from selenium.webdriver import TouchActions
import time
from test_webcontrol.base import Base


class TestActionChains(Base):
    browser = "chrome"
    def test_scroll_bottom(self):
        self.driver.get("https://www.baidu.com/")
        ele_input = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele_input.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_input)
        action.tap(ele_search)
        action.scroll_from_element(ele_input,0,10000)
        ele_nextpage = self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]")
        action.tap(ele_nextpage)
        action.perform()
        time.sleep(3)