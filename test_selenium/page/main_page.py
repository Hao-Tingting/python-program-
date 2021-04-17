#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
from selenium import webdriver

from test_selenium.page.add_contact_page import AddContactPage
from test_selenium.page.add_member_page import AddMemberPage
from test_selenium.page.base_page import BasePage
from test_selenium.page.contact_page import ContactPage


class Main_Page(BasePage):
    # 跳转到添加成员页面
    def goto_addmember_page(self):
        self.driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
    # 跳转到通讯录页面
    def goto_contact_page(self):
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactPage(self.driver)
    # 跳转到导入通讯录页面
    def goto_add_contact_page(self):
        self.driver.find_element_by_css_selector(".ww_indexImg_Import").click()
        return AddContactPage(self.driver)