#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time

from selenium.webdriver import ActionChains

from test_webcontrol.base import Base

class TestChangeFrame(Base):
    browser = "chrome"
    def test_ChangeFrame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele_start = self.driver.find_element_by_id("draggable")
        ele_end = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_start,ele_end).perform()
        # 切到alert弹窗，并确认
        self.driver.switch_to.alert.accept()
        # 切回父frame节点
        # self.driver.switch_to.parent_frame()
        # 切回默认frame节点
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/form/button").click()
        time.sleep(3)
