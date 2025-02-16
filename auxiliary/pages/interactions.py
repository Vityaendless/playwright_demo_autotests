from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.constants import HTMLAttr, HTMLValue
from auxiliary.helper import Helper
from auxiliary.locators import (SortablePageLocator as SortablePL, SelectablePageLocator as SelectPL,
                                ResizablePageLocator as ResizablePL)


class SortablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().sortable
        self.first_el = {
            'title': 'first_el',
            'locator': self.page.locator(SortablePL.FIRST_EL),
            'selector': SortablePL.FIRST_EL
        }
        self.second_el = {
            'title': 'second_el',
            'locator': self.page.locator(SortablePL.SECOND_EL),
            'selector': SortablePL.SECOND_EL
        }
        self.to_grid = {
            'title': 'to_grid',
            'locator': self.page.locator(SortablePL.TO_GRID),
            'selector': SortablePL.TO_GRID
        }
        self.first_el_grid = {
            'title': 'first_el_grid',
            'locator': self.page.locator(SortablePL.FIRST_EL_GRID),
            'selector': SortablePL.FIRST_EL_GRID
        }
        self.second_el_grid = {
            'title': 'second_el_grid',
            'locator': self.page.locator(SortablePL.SECOND_EL_GRID),
            'selector': SortablePL.SECOND_EL_GRID
        }


class SelectablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().selectable
        self.list_els = {
            'title': 'list_els',
            'locator': self.page.locator(SelectPL.LIST_ELS),
            'selector': SelectPL.LIST_ELS
        }
        self.grid_els = {
            'title': 'grid_els',
            'locator': self.page.locator(SelectPL.GRID_ELS),
            'selector': SelectPL.GRID_ELS
        }
        self.to_grid = {
            'title': 'to_grid',
            'locator': self.page.locator(SelectPL.TO_GRID),
            'selector': SelectPL.TO_GRID
        }

    @staticmethod
    def check_not_active(els, el_amount):
        for i, el in enumerate(els):
            cls = el.get_attribute(HTMLAttr.CLASS)
            Helper.is_not_in(HTMLValue.ACTIVE, cls)
            if el_amount == i:
                el.click()

    @staticmethod
    def check_active(els, el_amount):
        for i, el in enumerate(els):
            if el_amount == i:
                cls = el.get_attribute(HTMLAttr.CLASS)
                Helper.is_in(HTMLValue.ACTIVE, cls)


class ResizablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().resizable
        self.resizable_box = {
            'title': 'resizable_box',
            'locator': self.page.locator(ResizablePL.RESIZABLE_BOX),
            'selector': ResizablePL.RESIZABLE_BOX
        }
