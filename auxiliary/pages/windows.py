from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import WindowsPageLocator, SamplePageLocator


class WindowsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().browser_windows
        self.new_tab_btn = {
            'title': 'new_tab_btn',
            'locator': self.page.locator(WindowsPageLocator.NEW_TAB_BTN),
            'selector': WindowsPageLocator.NEW_TAB_BTN
        }
        self.new_window_btn = {
            'title': 'new_window_btn',
            'locator': self.page.locator(WindowsPageLocator.NEW_WINDOW_BTN),
            'selector': WindowsPageLocator.NEW_WINDOW_BTN
        }
        self.msg_new_window_btn = {
            'title': 'msg_new_window_btn',
            'locator': self.page.locator(WindowsPageLocator.MESSAGE_NEW_WINDOW_BTN),
            'selector': WindowsPageLocator.MESSAGE_NEW_WINDOW_BTN
        }


class SamplePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().sample
        self.heading = {
            'title': 'heading',
            'locator': self.page.locator(SamplePageLocator.HEADING),
            'selector': SamplePageLocator.HEADING
        }
        self.body = {
            'title': 'heading',
            'locator': self.page.locator(SamplePageLocator.BODY),
            'selector': SamplePageLocator.BODY
        }
