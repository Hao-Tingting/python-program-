#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time

from test_selenium.page.add_depart_page import AddDepartPage
from test_selenium.page.base_page import BasePage


class ContactPage(BasePage):
    # 检查是否成功添加成员
    def check_memberlist(self):
        ele_list = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = [i.text for i in ele_list]
        return name_list

    # 跳转到添加部门页面
    def goto_add_depart(self):
        time.sleep(3)
        self.driver.find_element_by_css_selector(".member_colLeft_top_addBtn").click()
        return AddDepartPage(self.driver)
    # 跳转到导入通讯录页面
    def goto_add_contact(self):
        pass