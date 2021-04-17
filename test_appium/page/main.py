# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.page.base_page import BasePage
from test_appium.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../file/main.yaml")
        return Market(self._driver)
