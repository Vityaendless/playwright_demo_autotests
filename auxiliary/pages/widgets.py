from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.helper import Helper
from auxiliary.locators import (TabsPageLocator as TabsPL, AccordianPageLocator as AccordianPL,
                                AutoCompletePageLocator as AutoCompletePL, DatePickerPageLocator as DatePickerPL)


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


class AutoCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().auto_complete
        self.single_input = {
            'title': 'single_input',
            'locator': self.page.locator(AutoCompletePL.SINGLE_INPUT),
            'selector': AutoCompletePL.SINGLE_INPUT
        }
        self.multiple_input = {
            'title': 'multiple_input',
            'locator': self.page.locator(AutoCompletePL.MULTIPLE_INPUT),
            'selector': AutoCompletePL.MULTIPLE_INPUT
        }
        self.colors = {
            'title': 'colors',
            'locator': self.page.locator(AutoCompletePL.COLORS),
            'selector': AutoCompletePL.COLORS
        }
        self.remove_color_btn = {
            'title': 'remove_color_btn',
            'locator': self.page.locator(AutoCompletePL.REMOVE_COLOR_BTN),
            'selector': AutoCompletePL.REMOVE_COLOR_BTN
        }
        self.clear_btn = {
            'title': 'clear_btn',
            'locator': self.page.locator(AutoCompletePL.CLEAR_BTN),
            'selector': AutoCompletePL.CLEAR_BTN
        }
        self.single_input_value = {
            'title': 'single_input_value',
            'locator': self.page.locator(AutoCompletePL.SINGLE_INPUT_VALUE),
            'selector': AutoCompletePL.SINGLE_INPUT_VALUE
        }


class DatePickerPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().date_picker
        self.select_date = {
            'title': 'select_date',
            'locator': self.page.locator(DatePickerPL.SELECT_DATE),
            'selector': DatePickerPL.SELECT_DATE
        }
        self.select_time_date = {
            'title': 'select_time_date',
            'locator': self.page.locator(DatePickerPL.SELECT_TIME_DATE),
            'selector': DatePickerPL.SELECT_TIME_DATE
        }
        self.select_month = {
            'title': 'select_month',
            'locator': self.page.locator(DatePickerPL.SELECT_MONTH),
            'selector': DatePickerPL.SELECT_MONTH
        }
        self.select_year = {
            'title': 'select_year',
            'locator': self.page.locator(DatePickerPL.SELECT_YEAR),
            'selector': DatePickerPL.SELECT_YEAR
        }
        self.day_14 = {
            'title': 'day_14',
            'locator': self.page.locator(DatePickerPL.DAY_14),
            'selector': DatePickerPL.DAY_14
        }
        self.select_month_dt = {
            'title': 'select_month_dt',
            'locator': self.page.locator(DatePickerPL.SELECT_MONTH_DT),
            'selector': DatePickerPL.SELECT_MONTH_DT
        }
        self.select_year_dt = {
            'title': 'select_year_dt',
            'locator': self.page.locator(DatePickerPL.SELECT_YEAR_DT),
            'selector': DatePickerPL.SELECT_YEAR_DT
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
