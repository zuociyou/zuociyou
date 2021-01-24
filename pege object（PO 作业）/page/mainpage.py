from selenium import webdriver

from page.base_page import BasePage
from page.contact_page import ContactPage
from page.index_add_member_page import AddMember



class MainPage(BasePage):
    _location_goto_member = '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div'
    def goto_add_member(self):
        # 跳转到添加成员页面
        self.driver.find_element_by_xpath(self._location_goto_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        # 跳转到通讯录页面
        return ContactPage(self.driver)
