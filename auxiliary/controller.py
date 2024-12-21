from playwright.sync_api import Page

from auxiliary.helper import Helper
from auxiliary.pages import TextboxPage, CheckboxPage, RadioBtnPage, BtnPage, LinksPage, BrokenImagesLinksPage


class Controller:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.helper = Helper()
        self.textbox_page = TextboxPage(self.page)
        self.checkbox_page = CheckboxPage(self.page)
        self.radio_btn_page = RadioBtnPage(self.page)
        self.btn_page = BtnPage(self.page)
        self.links_page = LinksPage(self.page)
        self.broken_obj_page = BrokenImagesLinksPage(self.page)
