from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        # 注解，不是赋值操作，用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def __cookie_login(self):
        with open("cookie_data.yml", encoding="UTF-8") as f:
            cooke_data = yaml.safe_load(f)
            for cookes in cooke_data:
                self.driver.add_cookie(cookes)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")