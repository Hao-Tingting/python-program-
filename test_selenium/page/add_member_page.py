#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time

import yaml

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 添加成员
    def add_member_list(self,add_name,add_id,add_phone):

        self.driver.find_element_by_id("username").send_keys(add_name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(add_id)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(add_phone)
        self.driver.find_element_by_css_selector(".js_btn_save:nth-child(2)").click()
        time.sleep(3)
        self.driver.find_element_by_id("menu_index").click()
        # return ContactPage(self.driver)
    # 跳转到通讯录页面
    def goto_contact(self):
        pass