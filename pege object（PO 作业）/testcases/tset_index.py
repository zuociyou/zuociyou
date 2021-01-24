from page.index_page import IndexPage


class TestIndex:
    def setup_class(self):
        self.index_page = IndexPage()
    def test_login(self):
        # 跳转到登陆页面-扫码登陆
        self.index_page.goto_login().login_scanf()
        pass

    def test_register(self):
        # 跳转到注册页面-注册
        self.index_page.goto_register().register()
        pass