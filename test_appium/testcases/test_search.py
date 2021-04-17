# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
from test_appium.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")