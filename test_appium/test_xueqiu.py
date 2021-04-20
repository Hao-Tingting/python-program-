# ！G:\pyworksp\PycharmProjects
# -*- coding: utf-8 -*-
import time

import pytest
from hamcrest import *

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,
            "automationName":"uiautomator2",
            "skipServerInstallation":True,
            "unicodeKeyBoard":"true",
            "resetKeyBoard":"true"
            # "dontStopAppOnReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_xueqiu(self):

        """
        雪球测试用例：
        1.打开雪球app
        2。点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索结果里面选择“阿里巴巴”，然后进行点击
        5.获取阿里巴巴的股价，判断价格>200
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        cur_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert cur_price > 200

    def test_xueqiuattr(self):
        """
        雪球测试用例：
        1.打开雪球app首页
        2。定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性
        4.打印搜索框这个元素的左上角坐标和他的宽高
        5.向搜索框输入“alibaba”
        6.判断【阿里巴巴】是否可见
        7.如果可见，打印搜索成功，并点击，如果不可见，打印搜索失败
        :return:
        """
        search_name = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").text
        search_loc = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").location
        search_size = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").size
        print(search_name)
        print(search_loc)
        print(search_size)
        ele_search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 显示等待
        locator = (MobileBy.ID,"com.xueqiu.android:id/tv_search")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # 使用lambda表达式也可以作为条件
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        flg = ele_search.is_enabled()
        if True == flg:
            ele_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            # display_attr = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").is_displayed()
            # print(f'{display_attr}')
            # if True == display_attr:
            # 或者以下写法获取displayed属性
            ele_dp = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            dp_flg = ele_dp.get_attribute("displayed")
            print(ele_dp.get_attribute("resource-id"))
            print(ele_dp.get_attribute("text"))
            if "true" == dp_flg:
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):

        touchact = TouchAction(self.driver)
        touchact.press(x=270,y=770).move_to(x=270,y=150).release().perform()
        time.sleep(3)

    def test_get_price(self):
        """
        雪球测试用例：
        1.打开雪球app
        2。点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索结果里面选择“阿里巴巴”，然后进行点击
        5.获取香港阿里的的股价，判断价格>200
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        cur_price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(f"{cur_price}")
        # assert cur_price > 200
        # hamcrest断言
        # assert_that(cur_price,equal_to(200),"股价不为200")
        assert_that(cur_price, close_to(200,40), "股价在指定区间范围内")

    def test_uiseletor(self):
        """
        雪球测试用例：
        1.打开雪球app
        2。点击我的，进入个人信息页面
        3.点击登录，进入登录页面
        4.输入用户名，输入密码
        5.点击登录
        使用uiselector
        toast的定位
        :return:
        """
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().text("我的")').click()
        # 定位"我的"也可以用下面的方法
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().text("帐号密码登录")').click()
        # 定位"帐号密码登录"也可以用下面的方法
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/rl_login").childSelector(text("帐号密码登录"))').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12345678")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        self.driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/weixin_login").click()
        # print(self.driver.page_source)
        # toast_test = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        # 也可使用contains
        toast_test = self.driver.find_element_by_xpath("//*[contains(@text,'安装微信')]").text
        print(toast_test)
        time.sleep(3)

    def test_scroll(self):
        """
        雪球测试用例：
        1.滚动查找
        :return:
        """
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("疯投哥").'
            'instance(0));').click()

        time.sleep(3)

    @pytest.mark.parametrize("name,id,expect_price",[("阿里巴巴","BABA",300),("小米","01810",25)])
    def test_search(self,name,id,expect_price):
        """
        1.打开雪球app
        2.点击搜索框输入搜索词“阿里巴巴”，“小米”，“。。。”
        3.点击第一个搜索结果
        4.判断股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(name)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name']").click()
        current_price = float(self.driver.find_element_by_xpath(
            f"//*[@text='{id}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(expect_price)
        print(close_to(expect_price,expect_price*0.5))
        assert_that(current_price,close_to(expect_price,expect_price*0.5),f"这是{name}的断言")

    def test_datadrive(self,name,id,expect_price):
        """
        1.打开雪球app
        2.点击搜索框输入搜索词“阿里巴巴”，“小米”，“。。。”
        3.点击第一个搜索结果
        4.判断股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(name)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name']").click()
        current_price = float(self.driver.find_element_by_xpath(
            f"//*[@text='{id}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(expect_price)
        print(close_to(expect_price,expect_price*0.5))
        assert_that(current_price,close_to(expect_price,expect_price*0.5),f"这是{name}的断言")