from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    def add_member(self):
        # 添加成员操作
        pass
    def get_member(self):
        # 获取成员列表,用来做断言
        member_list = self.driver.find_elements(*self._location_member_list)
        member_list2 = []
        for i in member_list:
            member_list2.append(i.text)
        return member_list2