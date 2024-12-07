from auxiliary.pages import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import TextboxPageLocator as TextboxPL


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
