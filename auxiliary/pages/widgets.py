from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.helper import Helper
from auxiliary.locators import (TabsPageLocator as TabsPL, AccordianPageLocator as AccordianPL,
                                AutoCompletePageLocator as AutoCompletePL, DatePickerPageLocator as DatePickerPL,
                                SliderPageLocator as SliderPL, ProgressBarPageLocator as ProgressBarPL,
                                ToolTipsPageLocator as ToolTipPL)


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


class SliderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().slider
        self.slider = {
            'title': 'slider',
            'locator': self.page.locator(SliderPL.SLIDER),
            'selector': SliderPL.SLIDER
        }
        self.slider_value = {
            'title': 'slider_value',
            'locator': self.page.locator(SliderPL.SLIDER_VALUE),
            'selector': SliderPL.SLIDER_VALUE
        }


class ProgressBarPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().progress_bar
        self.start_btn = {
            'title': 'start_btn',
            'locator': self.page.locator(ProgressBarPL.BTN),
            'selector': ProgressBarPL.BTN
        }
        self.reset_btn = {
            'title': 'reset_btn',
            'locator': self.page.locator(ProgressBarPL.RESET_BTN),
            'selector': ProgressBarPL.RESET_BTN
        }
        self.progress_bar = {
            'title': 'progress_bar',
            'locator': self.page.locator(ProgressBarPL.PROGRESS_BAR),
            'selector': ProgressBarPL.PROGRESS_BAR
        }

    def check_default_state(self):
        Helper.to_contain_text(self.start_btn, "Start")
        Helper.to_contain_text(self.progress_bar, "0%")
        Helper.not_to_be_visible(self.reset_btn)


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


class ToolTipPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().tool_tips
        self.btn = {
            'title': 'btn',
            'locator': self.page.locator(ToolTipPL.BTN),
            'selector': ToolTipPL.BTN
        }
        self.btn_tt = {
            'title': 'btn_tt',
            'locator': self.page.locator(ToolTipPL.BTN_TOOL_TIP),
            'selector': ToolTipPL.BTN_TOOL_TIP
        }
        self.field = {
            'title': 'field',
            'locator': self.page.locator(ToolTipPL.FIELD),
            'selector': ToolTipPL.FIELD
        }
        self.field_tt = {
            'title': 'field_tt',
            'locator': self.page.locator(ToolTipPL.FIELD_TOOL_TIP),
            'selector': ToolTipPL.FIELD_TOOL_TIP
        }
        self.first_link = {
            'title': 'first_link',
            'locator': self.page.locator(ToolTipPL.FIRST_LINK),
            'selector': ToolTipPL.FIRST_LINK
        }
        self.first_link_tt = {
            'title': 'first_link_tt',
            'locator': self.page.locator(ToolTipPL.FIRST_LINK_TOOL_TIP),
            'selector': ToolTipPL.FIRST_LINK_TOOL_TIP
        }
        self.second_link = {
            'title': 'second_link',
            'locator': self.page.locator(ToolTipPL.SECOND_LINK),
            'selector': ToolTipPL.SECOND_LINK
        }
        self.second_link_tt = {
            'title': 'second_link_tt',
            'locator': self.page.locator(ToolTipPL.SECOND_LINK_TOOL_TIP),
            'selector': ToolTipPL.SECOND_LINK_TOOL_TIP
        }

    def check_tool_tip(self, hover_on_el, hover_el, text):
        self.hover(hover_on_el)
        Helper.to_be_visible(hover_el)
        Helper.to_contain_text(hover_el, text)
