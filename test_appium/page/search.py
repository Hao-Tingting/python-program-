# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"]=value
        self.steps("../file/search.yaml")