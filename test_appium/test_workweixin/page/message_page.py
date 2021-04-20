# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.test_workweixin.page.base_page import BasePage
from test_appium.test_workweixin.page.contact_page import ContactPage


class MessagePage(BasePage):
    def goto_contact(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        return ContactPage(self.driver)

    def goto_search(self):
        pass

    def sendmessage(self):
        pass
