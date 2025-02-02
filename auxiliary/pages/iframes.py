from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import IframePageLocator, NestedIframePageLocator


class IframesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().iframes
        self.first_iframe = {
            'title': 'first_iframe',
            'locator': self.page.locator(IframePageLocator.FIRST_IFRAME),
            'selector': IframePageLocator.FIRST_IFRAME
        }
        self.second_iframe = {
            'title': 'second_iframe',
            'locator': self.page.locator(IframePageLocator.SECOND_IFRAME),
            'selector': IframePageLocator.SECOND_IFRAME
        }


class NestedIframesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().nested_iframes
        self.parent_iframe = {
            'title': 'parent_iframe',
            'locator': self.page.locator(NestedIframePageLocator.PARENT_IFRAME),
            'selector': NestedIframePageLocator.PARENT_IFRAME
        }