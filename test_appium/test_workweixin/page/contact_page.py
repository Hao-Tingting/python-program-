# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from test_appium.test_workweixin.page.base_page import BasePage


class ContactPage(BasePage):
    def add_member(self, path):
        mem_count = 0
        with open(path, encoding="utf-8") as f:
            member_lists: list[dict] = yaml.safe_load(f)
            len_mem = len(member_lists)
            for member_list in member_lists:
                mem_count += 1
                print(mem_count)
                if mem_count == 1:
                    print(member_list["name"])
                    try:
                        ele_add = self.driver.find_element_by_xpath("//*[@text='添加成员']")
                    except NoSuchElementException as e:
                        self.driver.find_element_by_android_uiautomator(
                            'new UiScrollable(new UiSelector().'
                            'scrollable(true).instance(0)).'
                            'scrollIntoView(new UiSelector().text("添加成员").'
                            'instance(0));').click()
                    else:
                        ele_add.click()
                    self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
                    self.__addm__(member_list, mem_count, len_mem)
                    try:
                        ele_fail = self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']")
                    except Exception as e:
                        continue
                    else:
                        ele_fail.click()
                    self.width = self.driver.get_window_size()["width"]
                    self.height = self.driver.get_window_size()["height"]
                    self.driver.swipe(int(self.width * 0.5), int(self.height * 0.2), int(self.width * 0.5),
                                      int(self.height * 0.8))
                elif mem_count > 1 and mem_count < len(member_lists):
                    self.__addm__(member_list, mem_count, len_mem)
                    try:
                        ele_fail = self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']")
                    except Exception as e:
                        continue
                    else:
                        ele_fail.click()
                    self.width = self.driver.get_window_size()["width"]
                    self.height = self.driver.get_window_size()["height"]
                    self.driver.swipe(int(self.width * 0.5), int(self.height * 0.2), int(self.width * 0.5),
                                      int(self.height * 0.8))
                else:
                    self.__addm__(member_list, mem_count, len_mem)
                    try:
                        ele_fail = self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']")
                    except Exception as e:
                        continue
                    else:
                        ele_fail.click()

    def goto_search(self):
        pass

    def __addm__(self, member_list, mem_count, len_mem):
        self.driver.find_element_by_xpath(
            "//*[@text='姓名　']/..//*[@resource-id='com.tencent.wework:id/ays']").send_keys(member_list["name"])

        if "女" == member_list["sex"]:
            self.driver.find_elements(MobileBy.XPATH, "//*[@text='性别']/..//*[@class='android.widget.TextView']")[
                1].click()
            self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/content']//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机　']/..//*[@class='android.widget.EditText']").send_keys(
            member_list["phone"])
        if mem_count != len_mem:
            self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().'
                'scrollable(true).instance(0)).'
                'scrollIntoView(new UiSelector().text("保存并继续添加").'
                'instance(0));').click()
        else:
            self.driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().'
                'scrollable(true).instance(0)).'
                'scrollIntoView(new UiSelector().text("保存").'
                'instance(0));').click()
            print(self.driver.page_source)
