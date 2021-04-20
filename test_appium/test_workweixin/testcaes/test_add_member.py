# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.test_workweixin.page.message_page import MessagePage


class TestAddMember:

    def setup(self):
        self.main = MessagePage()

    def testaddmember(self):
        path = "../file/memberlist.yaml"
        self.main.goto_contact().add_member(path)
