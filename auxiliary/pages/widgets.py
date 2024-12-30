from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.helper import Helper
from auxiliary.locators import TabsPageLocator as TabsPL, AccordianPageLocator as AccordianPL


class AccordianPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().accordian
        self.section1_heading = {
            'title': 'section1_heading',
            'locator': self.page.locator(AccordianPL.SECTION1_HEADING),
            'selector': AccordianPL.SECTION1_HEADING
        }
        self.section2_heading = {
            'title': 'section2_heading',
            'locator': self.page.locator(AccordianPL.SECTION2_HEADING),
            'selector': AccordianPL.SECTION2_HEADING
        }
        self.section3_heading = {
            'title': 'section3_heading',
            'locator': self.page.locator(AccordianPL.SECTION3_HEADING),
            'selector': AccordianPL.SECTION3_HEADING
        }
        self.section1_content = {
            'title': 'section1_content',
            'locator': self.page.locator(AccordianPL.SECTION1_CONTENT),
            'selector': AccordianPL.SECTION1_CONTENT
        }
        self.section2_content = {
            'title': 'section2_content',
            'locator': self.page.locator(AccordianPL.SECTION2_CONTENT),
            'selector': AccordianPL.SECTION2_CONTENT
        }
        self.section3_content = {
            'title': 'section3_content',
            'locator': self.page.locator(AccordianPL.SECTION3_CONTENT),
            'selector': AccordianPL.SECTION3_CONTENT
        }


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
