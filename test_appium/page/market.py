# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../file/market.yaml")
        return Search(self._driver)