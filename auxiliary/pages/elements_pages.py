from auxiliary.pages import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import (TextboxPageLocator as TextboxPL, CheckboxPageLocator as CheckboxPL,
                                RadioBtnPageLocator as RadioPL, ButtonsPageLocator as ButtonsPL)


class TextboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().textbox
        self.username = {
            'title': 'username',
            'locator': self.page.locator(TextboxPL.USERNAME),
            'selector': TextboxPL.USERNAME
        }
        self.email = {
            'title': 'email',
            'locator': self.page.locator(TextboxPL.EMAIL),
            'selector': TextboxPL.EMAIL
        }
        self.c_address = {
            'title': 'c_address',
            'locator': self.page.locator(TextboxPL.C_ADDRESS),
            'selector': TextboxPL.C_ADDRESS
        }
        self.p_address = {
            'title': 'p_address',
            'locator': self.page.locator(TextboxPL.P_ADDRESS),
            'selector': TextboxPL.P_ADDRESS
        }
        self.submit = {
            'title': 'submit',
            'locator': self.page.locator(TextboxPL.SUBMIT),
            'selector': TextboxPL.SUBMIT
        }
        self.output = {
            'title': 'output',
            'locator': self.page.locator(TextboxPL.OUTPUT),
            'selector': TextboxPL.OUTPUT
        }
        self.output_name = {
            'title': 'output_name',
            'locator': self.page.locator(TextboxPL.OUTPUT_NAME),
            'selector': TextboxPL.OUTPUT_NAME
        }
        self.output_email = {
            'title': 'output_email',
            'locator': self.page.locator(TextboxPL.OUTPUT_EMAIL),
            'selector': TextboxPL.OUTPUT_EMAIL
        }
        self.output_c_address = {
            'title': 'output_c_address',
            'locator': self.page.locator(TextboxPL.OUTPUT_C_ADDRESS),
            'selector': TextboxPL.OUTPUT_C_ADDRESS
        }
        self.output_p_address = {
            'title': 'output',
            'locator': self.page.locator(TextboxPL.OUTPUT_P_ADDRESS),
            'selector': TextboxPL.OUTPUT_P_ADDRESS
        }

class CheckboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().checkbox
        self.expand_all = {
            'title': 'expand_all',
            'locator': self.page.locator(CheckboxPL.EXPAND_ALL),
            'selector': CheckboxPL.EXPAND_ALL
        }
        self.collapse_all = {
            'title': 'collapse_all',
            'locator': self.page.locator(CheckboxPL.COLLAPSE_ALL),
            'selector': CheckboxPL.COLLAPSE_ALL
        }
        self.result = {
            'title': 'result',
            'locator': self.page.locator(CheckboxPL.RESULT),
            'selector': CheckboxPL.RESULT
        }
        self.home = {
            'title': 'home',
            'locator': self.page.locator(CheckboxPL.HOME),
            'selector': CheckboxPL.HOME
        }
        self.els = {
            'title': 'els',
            'locator': self.page.locator(CheckboxPL.ELS),
            'selector': CheckboxPL.ELS
        }


class RadioBtnPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().radio_btn
        self.yes = {
            'title': 'yes',
            'locator': self.page.locator(RadioPL.YES),
            'selector': RadioPL.YES
        }
        self.yes_radio = {
            'title': 'yes_radio',
            'locator': self.page.locator(RadioPL.YES_RADIO),
            'selector': RadioPL.YES_RADIO
        }
        self.impressive = {
            'title': 'impressive',
            'locator': self.page.locator(RadioPL.IMPRESSIVE),
            'selector': RadioPL.IMPRESSIVE
        }
        self.impressive_radio = {
            'title': 'impressive_radio',
            'locator': self.page.locator(RadioPL.IMPRESSIVE_RADIO),
            'selector': RadioPL.IMPRESSIVE_RADIO
        }
        self.no_radio = {
            'title': 'no_radio',
            'locator': self.page.locator(RadioPL.NO_RADIO),
            'selector': RadioPL.NO_RADIO
        }
        self.result = {
            'title': 'result',
            'locator': self.page.locator(RadioPL.RESULT),
            'selector': RadioPL.RESULT
        }


class BtnPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().buttons
        self.dbl_click_el = {
            'title': 'dbl_click_el',
            'locator': self.page.locator(ButtonsPL.DBL_CLICK),
            'selector': ButtonsPL.DBL_CLICK
        }
        self.dbl_click_result = {
            'title': 'dbl_click_result',
            'locator': self.page.locator(ButtonsPL.DBL_CLICK_RESULT),
            'selector': ButtonsPL.DBL_CLICK_RESULT
        }
        self.right_click_el = {
            'title': 'right_click_el',
            'locator': self.page.locator(ButtonsPL.RIGHT_CLICK),
            'selector': ButtonsPL.RIGHT_CLICK
        }
        self.right_click_result = {
            'title': 'right_click_result',
            'locator': self.page.locator(ButtonsPL.RIGHT_CLICK_RESULT),
            'selector': ButtonsPL.RIGHT_CLICK_RESULT
        }
        self.click_el = {
            'title': 'click_el',
            'locator': self.page.locator(ButtonsPL.CLICK),
            'selector': ButtonsPL.CLICK
        }
        self.click_result = {
            'title': 'click_result',
            'locator': self.page.locator(ButtonsPL.CLICK_RESULT),
            'selector': ButtonsPL.CLICK_RESULT
        }
