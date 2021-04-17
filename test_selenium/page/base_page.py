#！/user/ting/PycharmProjects
# -*- coding: utf-8 -*-
from selenium import webdriver



class BasePage:
    # 复用浏览器
    def __init__(self,base_driver = None):
        if base_driver is not None:
            self.driver = base_driver
        else:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
            self.driver.implicitly_wait(5)
