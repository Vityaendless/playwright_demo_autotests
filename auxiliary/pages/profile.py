from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import ProfilePageLocator as ProfilePL


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().profile
        self.logout = {
            'title': 'logout',
            'locator': self.page.locator(ProfilePL.LOGOUT_BTN),
            'selector': ProfilePL.LOGOUT_BTN
        }
