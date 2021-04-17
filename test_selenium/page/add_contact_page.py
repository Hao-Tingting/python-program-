#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact_page import ContactPage


class AddContactPage(BasePage):
    # 上传文件导入通讯录
    def add_contactlist(self):
        time.sleep(3)
        self.driver.find_element_by_css_selector(".ww_fileImporter_fileContainer_uploadInputMask").send_keys(r"C:\Users\Ykane\Desktop\contactfile.xlsx")
        self.driver.find_element_by_css_selector(".qui_btn.ww_btn.ww_btn_Large.ww_btn_Blue.ww_fileImporter_submit").click()
        self.driver.find_element_by_css_selector(".qui_btn.ww_btn.ww_btn_Big.ww_btn_Blue").click()
        return ContactPage(self.driver)
    # 跳转到通讯录页面
    def goto_contact(self):
        pass