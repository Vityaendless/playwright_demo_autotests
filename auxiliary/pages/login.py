from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import LoginPageLocator as LoginPL


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().login
        self.username = {
            'title': 'username',
            'locator': self.page.locator(LoginPL.USERNAME),
            'selector': LoginPL.USERNAME
        }
        self.password = {
            'title': 'password',
            'locator': self.page.locator(LoginPL.PASS),
            'selector': LoginPL.PASS
        }
        self.login_btn = {
            'title': 'login_btn',
            'locator': self.page.locator(LoginPL.LOGIN_BTN),
            'selector': LoginPL.LOGIN_BTN
        }
        self.reg_btn = {
            'title': 'reg_btn',
            'locator': self.page.locator(LoginPL.REG_BTN),
            'selector': LoginPL.REG_BTN
        }
        self.username_value = {
            'title': 'username_value',
            'locator': self.page.locator(LoginPL.USERNAME_VALUE),
            'selector': LoginPL.USERNAME_VALUE
        }
        self.message = {
            'title': 'message',
            'locator': self.page.locator(LoginPL.MESSAGE),
            'selector': LoginPL.MESSAGE
        }
