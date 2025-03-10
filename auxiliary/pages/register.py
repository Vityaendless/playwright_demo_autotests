from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import RegisterPageLocator as RegisterPL


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().register
        self.first_name = {
            'title': 'first_name',
            'locator': self.page.locator(RegisterPL.FIRST_NAME),
            'selector': RegisterPL.FIRST_NAME
        }
        self.last_name = {
            'title': 'last_name',
            'locator': self.page.locator(RegisterPL.LAST_NAME),
            'selector': RegisterPL.LAST_NAME
        }
        self.username = {
            'title': 'username',
            'locator': self.page.locator(RegisterPL.USERNAME),
            'selector': RegisterPL.USERNAME
        }
        self.password = {
            'title': 'password',
            'locator': self.page.locator(RegisterPL.PASSWORD),
            'selector': RegisterPL.PASSWORD
        }
        self.register_btn = {
            'title': 'register_btn',
            'locator': self.page.locator(RegisterPL.REGISTER_BTN),
            'selector': RegisterPL.REGISTER_BTN
        }
        self.login_btn = {
            'title': 'login_btn',
            'locator': self.page.locator(RegisterPL.GO_TO_LOGIN_BTN),
            'selector': RegisterPL.GO_TO_LOGIN_BTN
        }
        self.recaptcha = {
            'title': 'recaptcha',
            'locator': self.page.locator(RegisterPL.RECAPTCHA),
            'selector': RegisterPL.RECAPTCHA
        }
