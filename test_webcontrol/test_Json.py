#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time
from selenium.webdriver import ActionChains
from test_webcontrol.base import Base
import pytest

class TestJson(Base):
    browser = "chrome"
    @pytest.mark.skip
    def test_Json(self):
        self.driver.get("http://testerhome.com")
        ele_pho = self.driver.execute_script("return document.querySelector('#main-nav-menu > li:nth-child(1) > a')")
        ele_pho.click()
        self.driver.execute_script("document.documentElement.scrollTop=1500")
        time.sleep(3)

    def test_ReadOnly(self):
        self.driver.get("https://www.12306.cn/index/")
        ele_time = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-04-11'")
        time.sleep(3)
