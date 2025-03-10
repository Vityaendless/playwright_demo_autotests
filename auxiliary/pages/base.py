# from playwright.sync_api import Page
import time


class BasePage:
    def __init__(self, page):
        self.page = page
        self.url = None
        self.to_login_page = {
            'title': 'to_login_page',
            'locator': self.page.locator("//li[@id='item-0']//*[text()='Login']"),
            'selector': "//li[@id='item-0']//*[text()='Login']"
        }


    def navigate(self):
        self.page.goto(self.url, timeout=120000)

    def click(self, el, button='left', position=None):
        if position:
            print(position)
            self.__dict__[el['title']]['locator'].click(button=button, position=position)
        else:
            self.__dict__[el['title']]['locator'].click(button=button)

    def focus(self, el):
        self.__dict__[el['title']]['locator'].focus()

    def hover(self, el, position=None):
        if position:
            print(position)
            self.__dict__[el['title']]['locator'].hover(position=position)
        else:
            self.__dict__[el['title']]['locator'].hover()

    def is_not_clickable(self, el):
        try:
            self.click(el)
        except Exception:
            return True
        return False

    def dblclick(self, el):
        self.__dict__[el['title']]['locator'].dblclick()

    def check(self, el):
        self.__dict__[el['title']]['locator'].check()

    def fill(self, el, text="Default text"):
        self.__dict__[el['title']]['locator'].fill(text)

    def type(self, el, text="Default text"):
        self.__dict__[el['title']]['locator'].type(text)

    def press(self, el, key="Enter"):
        self.__dict__[el['title']]['locator'].press(key)

    def select_option(self, el, value):
        self.page.select_option(el["selector"], value=value)

    def drag_drop(self, first_el, second_el):
        self.page.locator(first_el['selector']).drag_to(second_el['locator'])

    def get_element_text(self, el):
        return self.__dict__[el['title']]['locator'].text_content()

    def get_attr(self, el, attr):
        return self.__dict__[el['title']]['locator'].get_attribute(attr)

    def all_els(self, els):
        return self.__dict__[els['title']]['locator'].all()

    def count(self, els):
        return self.__dict__[els['title']]['locator'].count()

    def last(self, els):
        return self.__dict__[els['title']]['locator'].last

    def bounding_box(self, el):
        return self.__dict__[el['title']]['locator'].bounding_box()

    def move(self, x, y):
        self.page.mouse.move(x, y)

    def down(self):
        self.page.mouse.down()

    def up(self):
        self.page.mouse.up()

    def drag(self, el, x, y, mode="relative"):
        self.hover(el)
        if mode == "relative":
            el_params = self.bounding_box(el)
            print(el_params)
            x = x + el_params['x']
            y = y + el_params['y']
        time.sleep(1)
        self.down()
        self.move(x, y)
        self.up()

    def drag_n_drop(self, drag, drop, target_position=None):
        self.page.drag_and_drop(drag['selector'], drop['selector'], target_position=target_position)

    @staticmethod
    def get_el_width(el):
        return el['locator'].evaluate('(event) => parseFloat(event.style.width)')

    @staticmethod
    def get_el_height(el):
        return el['locator'].evaluate('(event) => parseFloat(event.style.height)')
