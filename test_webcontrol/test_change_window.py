#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time
from test_webcontrol.base import Base

class TestChangeWindow(Base):
    browser = "chrome"
    def test_ChangeWindow(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("zhangsan")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13899991111")
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        time.sleep(3)
