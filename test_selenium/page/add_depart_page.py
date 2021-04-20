#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
import time

from test_selenium.page.base_page import BasePage


class AddDepartPage(BasePage):

    # 添加部门
    def add_departlist(self):
        self.driver.find_element_by_css_selector(".js_create_party").click()
        self.driver.find_element_by_name("name").send_keys("开发部")
        self.driver.find_element_by_css_selector(".js_parent_party_name").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(".qui_dialog_body.ww_dialog_body [id='1688852036030423_anchor']").click()
        self.driver.find_element_by_css_selector("[d_ck=submit]").click()
        ele_list = self.driver.find_elements_by_css_selector(".jstree-anchor")
        depart_list = [i.text for i in ele_list]
        return depart_list