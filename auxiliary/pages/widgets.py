from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.helper import Helper
from auxiliary.locators import TabsPageLocator as TabsPL


class TabsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().tabs
        self.what_tab = {
            'title': 'what_tab',
            'locator': self.page.locator(TabsPL.WHAT_TAB),
            'selector': TabsPL.WHAT_TAB
        }
        self.origin_tab = {
            'title': 'origin_tab',
            'locator': self.page.locator(TabsPL.ORIGIN_TAB),
            'selector': TabsPL.ORIGIN_TAB
        }
        self.use_tab = {
            'title': 'use_tab',
            'locator': self.page.locator(TabsPL.USE_TAB),
            'selector': TabsPL.USE_TAB
        }
        self.more_tab = {
            'title': 'more_tab',
            'locator': self.page.locator(TabsPL.MORE_TAB),
            'selector': TabsPL.MORE_TAB
        }
        self.what_content = {
            'title': 'what_content',
            'locator': self.page.locator(TabsPL.WHAT_CONTENT),
            'selector': TabsPL.WHAT_CONTENT
        }
        self.origin_content = {
            'title': 'origin_content',
            'locator': self.page.locator(TabsPL.ORIGIN_CONTENT),
            'selector': TabsPL.ORIGIN_CONTENT
        }
        self.use_content = {
            'title': 'use_content',
            'locator': self.page.locator(TabsPL.USE_CONTENT),
            'selector': TabsPL.USE_CONTENT
        }
        self.more_content = {
            'title': 'more_content',
            'locator': self.page.locator(TabsPL.MORE_CONTENT),
            'selector': TabsPL.MORE_CONTENT
        }

    def is_class_contain(self, el, cls):
        cls_text = self.get_attr(el, "class")
        Helper.is_in(cls, cls_text)

    def is_not_class_contain(self, el, cls):
        cls_text = self.get_attr(el, "class")
        Helper.is_not_in(cls, cls_text)
