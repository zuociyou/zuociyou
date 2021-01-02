# -*- coding: utf-8 -*-
# coding: utf-8
from selenium import webdriver
from time import sleep
import yaml

#获取cookie并存到yaml文件中
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
class TestWework:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
        pass

    def test_work(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("cookie_data.yml", encoding="UTF-8") as f:
            cooke_data = yaml.safe_load(f)
        for cookes in cooke_data:
            self.driver.add_cookie(cookes)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")   #进入企业微信首页
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()
        self.driver.find_element_by_id("username").send_keys("DD老板")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("DD")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("13022222222")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("123456@qq.com")
        self.driver.execute_script("return document.getElementsByClassName('qui_btn ww_btn js_btn_save')[1]").click()
        self.driver.find_element_by_id("menu_contacts").click()

        def test_asser(self):
            try:
                a = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[1]/td[2]/span').text
                if a == "DD老板":
                    return True
            except :
                print("元素没找到")
                return False
        assert test_asser(self)