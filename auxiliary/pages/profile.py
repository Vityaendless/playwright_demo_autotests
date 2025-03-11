from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import ProfilePageLocator as ProfilePL


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().profile
        self.not_login_label = {
            'title': 'not_login_label',
            'locator': self.page.locator(ProfilePL.NOT_LOGIN_LABEL),
            'selector': ProfilePL.NOT_LOGIN_LABEL
        }
        self.to_login_link = {
            'title': 'to_login_link',
            'locator': self.page.locator(ProfilePL.TO_LOGIN_LINK),
            'selector': ProfilePL.TO_LOGIN_LINK
        }
        self.to_reg_link = {
            'title': 'to_reg_link',
            'locator': self.page.locator(ProfilePL.TO_REG_LINK),
            'selector': ProfilePL.TO_REG_LINK
        }
        self.logout = {
            'title': 'logout',
            'locator': self.page.locator(ProfilePL.LOGOUT_BTN),
            'selector': ProfilePL.LOGOUT_BTN
        }
