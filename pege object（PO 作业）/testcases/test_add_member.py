from page.mainpage import MainPage


class TestAddMember:
    def setup_class(self):
        self.mainpage = MainPage()
    def teardown_class(self):
        self.mainpage.driver.quit()

    def test_add_member(self):
        # 通过首页添加成员
        res = self.mainpage.goto_add_member().add_member().get_member()
        assert "DD老板2" in res
    def test_add_member_fail(self):
        res = self.mainpage.goto_add_member().add_member_fail()
        assert res == "该帐号已被“DD老板2”占有"
    def test_contact_add_meber(self):
        # 通过通讯录添加成员
        self.mainpage.goto_contact().add_member()