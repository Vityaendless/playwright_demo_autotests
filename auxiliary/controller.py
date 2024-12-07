from playwright.sync_api import Page

from auxiliary.helper import Helper
from auxiliary.pages import TextboxPage


class Controller:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.helper = Helper()
        self.textbox_page = TextboxPage(self.page)
