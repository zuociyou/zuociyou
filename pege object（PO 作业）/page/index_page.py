from page.login_page import LoginPage
from page.register_page import RegisterPage


class IndexPage:
    def goto_login(self):
        """
        跳转到登陆页
        """
        return LoginPage()
        pass

    def goto_register(self):
        """
        跳转到注册页面
        """
        return RegisterPage()
        pass