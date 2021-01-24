from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetcookie:
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222" #设置debug地址
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        sleep(15) #手动扫码登陆
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = driver.get_cookies()
        with open("cookie_data.yml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
    # def test_login(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = "127.0.0.1:9222" #设置debug地址
    #     driver = webdriver.Chrome(options=opt)
    #     driver.implicitly_wait(5)
    #     # driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    #     # sleep(15) #手动扫码登陆
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     # cookie = driver.get_cookies()
    #     # with open("cookie_data.yml", "w", encoding="UTF-8") as f:
    #     #     yaml.dump(cookie, f)
    #     driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
    #
    #     member_list = driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    #     member_list2 = []
    #     for i in member_list:
    #         member_list2.append(i.text)
    #     return member_list2