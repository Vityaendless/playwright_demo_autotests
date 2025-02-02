from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import AlertsPageLocator


class AlertsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().alerts
        self.alert_btn = {
            'title': 'alert_btn',
            'locator': self.page.locator(AlertsPageLocator.ALERT_BTN),
            'selector': AlertsPageLocator.ALERT_BTN
        }
        self.time_alert_btn = {
            'title': 'time_alert_btn',
            'locator': self.page.locator(AlertsPageLocator.TIME_ALERT_BTN),
            'selector': AlertsPageLocator.TIME_ALERT_BTN
        }
        self.confirm_btn = {
            'title': 'confirm_btn',
            'locator': self.page.locator(AlertsPageLocator.CONFIRM_BTN),
            'selector': AlertsPageLocator.CONFIRM_BTN
        }
        self.confirm_result = {
            'title': 'confirm_result',
            'locator': self.page.locator(AlertsPageLocator.CONFIRM_RESULT),
            'selector': AlertsPageLocator.CONFIRM_RESULT
        }
        self.prompt_btn = {
            'title': 'prompt_btn',
            'locator': self.page.locator(AlertsPageLocator.PROMPT_BTN),
            'selector': AlertsPageLocator.PROMPT_BTN
        }
        self.prompt_result = {
            'title': 'prompt_result',
            'locator': self.page.locator(AlertsPageLocator.PROMPT_RESULT),
            'selector': AlertsPageLocator.PROMPT_RESULT
        }
