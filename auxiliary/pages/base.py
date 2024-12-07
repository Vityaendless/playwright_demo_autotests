# from playwright.sync_api import Page


class BasePage:
    def __init__(self, page):
        self.page = page
        self.url = None

    def navigate(self):
        self.page.goto(self.url)

    def click(self, el):
        self.__dict__[el['title']]['locator'].click()

    def fill(self, el, text="Default text"):
        self.__dict__[el['title']]['locator'].fill(text)

    def get_element_text(self, el):
        return self.__dict__[el['title']]['locator'].text_content()
