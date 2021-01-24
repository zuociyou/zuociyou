from selenium import webdriver

from page.base_page import BasePage
from page.contact_page import ContactPage


class AddMember(BasePage):
    #下表横杠为将变量设置为私有变量，实现PO不要暴露页面内部的元素给外部
    _location_username = "username"
    _location_english_name = "memberAdd_english_name"
    _location_acctid = "memberAdd_acctid"
    _location_mail = "memberAdd_mail"
    _location_phone = "memberAdd_phone"
    def add_member(self):
    #     # 添加成员
        self.driver.find_element_by_id(self._location_username).send_keys("DD老板2")
        self.driver.find_element_by_id(self._location_english_name).send_keys("DD2")
        self.driver.find_element_by_id(self._location_acctid).send_keys("13022222201")
        self.driver.find_element_by_id(self._location_mail).send_keys("12345601@qq.com")
        self.driver.execute_script("return document.getElementsByClassName('qui_btn ww_btn js_btn_save')[1]").click()
        return ContactPage(self.driver)
    def add_member_fail(self):
        self.driver.find_element_by_id(self._location_username).send_keys("DD老板2")
        self.driver.find_element_by_id(self._location_english_name).send_keys("DD2")
        self.driver.find_element_by_id(self._location_acctid).send_keys("13022222201")
        # self.driver.find_element_by_id(self._location_mail).send_keys("12345601@qq.com")
        self.driver.find_element_by_id(self._location_phone).send_keys("13022222201")
        self.driver.execute_script("return document.getElementsByClassName('qui_btn ww_btn js_btn_save')[1]").click()
        error_message = self.driver.find_element_by_css_selector(".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        return error_message