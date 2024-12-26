import requests

from auxiliary.pages import BasePage
from auxiliary.url_path import UrlPaths, BASE_URL
from auxiliary.helper import Helper
from auxiliary.constants import RCode
from auxiliary.locators import (TextboxPageLocator as TextboxPL, CheckboxPageLocator as CheckboxPL,
                                RadioBtnPageLocator as RadioPL, ButtonsPageLocator as ButtonsPL,
                                LinksPageLocator as LinksPL, BrokenLinksImagesPageLocator as BrImgLinksPL,
                                UploadDownloadPageLocator as UploadDownloadPL,
                                DynamicPropertiesPageLocator as DynPropertiesPL, WebTablesPageLocator as WebTablesPL)


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


class LinksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().links
        self.home = {
            'title': 'home',
            'locator': self.page.locator(LinksPL.HOME),
            'selector': LinksPL.HOME
        }
        self.dyn_home = {
            'title': 'dyn_home',
            'locator': self.page.locator(LinksPL.DYN_HOME),
            'selector': LinksPL.DYN_HOME
        }
        self.created = {
            'title': 'created',
            'locator': self.page.locator(LinksPL.CREATED),
            'selector': LinksPL.CREATED
        }
        self.no_content = {
            'title': 'no_content',
            'locator': self.page.locator(LinksPL.NO_CONTENT),
            'selector': LinksPL.NO_CONTENT
        }
        self.moved = {
            'title': 'moved',
            'locator': self.page.locator(LinksPL.MOVED),
            'selector': LinksPL.MOVED
        }
        self.bad_request = {
            'title': 'bad_request',
            'locator': self.page.locator(LinksPL.BAD_REQUEST),
            'selector': LinksPL.BAD_REQUEST
        }
        self.unauthorized = {
            'title': 'unauthorized',
            'locator': self.page.locator(LinksPL.UNAUTHORIZED),
            'selector': LinksPL.UNAUTHORIZED
        }
        self.forbidden = {
            'title': 'forbidden',
            'locator': self.page.locator(LinksPL.FORBIDDEN),
            'selector': LinksPL.FORBIDDEN
        }
        self.invalid_url = {
            'title': 'invalid_url',
            'locator': self.page.locator(LinksPL.INVALID),
            'selector': LinksPL.INVALID
        }
        self.result = {
            'title': 'result',
            'locator': self.page.locator(LinksPL.RESULT),
            'selector': LinksPL.RESULT
        }

    def get_new_tab(self, el):
        with self.page.context.expect_page() as tab:
            self.click(el)
        return tab.value

    def resp_check(self, el):
        response = requests.get(url=BASE_URL + el['selector'][1:])
        code = response.status_code
        Helper.to_contain_text(self.result, Helper.to_str(code))
        name = RCode.get_name(code)
        Helper.to_contain_text(self.result, name)


class BrokenImagesLinksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().broken_img_links
        self.valid_img = {
            'title': 'valid_img',
            'locator': self.page.locator(BrImgLinksPL.VALID_IMG),
            'selector': BrImgLinksPL.VALID_IMG
        }
        self.broken_img = {
            'title': 'broken_img',
            'locator': self.page.locator(BrImgLinksPL.BROKEN_IMG),
            'selector': BrImgLinksPL.BROKEN_IMG
        }
        self.valid_link = {
            'title': 'valid_link',
            'locator': self.page.locator(BrImgLinksPL.VALID_LINK),
            'selector': BrImgLinksPL.VALID_LINK
        }
        self.broken_link = {
            'title': 'broken_link',
            'locator': self.page.locator(BrImgLinksPL.BROKEN_LINK),
            'selector': BrImgLinksPL.BROKEN_LINK
        }

    @staticmethod
    def check_resp_code(url, code):
        response = requests.get(url=url)
        r_code = response.status_code
        Helper.is_eq(Helper.to_str(r_code), Helper.to_str(code))


class UploadDownloadPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().upload_download
        self.download = {
            'title': 'download',
            'locator': self.page.locator(UploadDownloadPL.DOWNLOAD),
            'selector': UploadDownloadPL.DOWNLOAD
        }
        self.upload = {
            'title': 'upload',
            'locator': self.page.locator(UploadDownloadPL.UPLOAD),
            'selector': UploadDownloadPL.UPLOAD
        }
        self.upload_result = {
            'title': 'upload_result',
            'locator': self.page.locator(UploadDownloadPL.UPLOAD_RESULT),
            'selector': UploadDownloadPL.UPLOAD_RESULT
        }
        self.upload_path = {
            'title': 'upload_path',
            'locator': self.page.locator(UploadDownloadPL.UPLOAD_PATH),
            'selector': UploadDownloadPL.UPLOAD_PATH
        }


class DynPropertiesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().dynamic_properties
        self.random_id = {
            'title': 'random_id',
            'locator': self.page.locator(DynPropertiesPL.RANDOM_ID),
            'selector': DynPropertiesPL.RANDOM_ID
        }
        self.enable_after = {
            'title': 'enable_after',
            'locator': self.page.locator(DynPropertiesPL.ENABLE_AFTER),
            'selector': DynPropertiesPL.ENABLE_AFTER
        }
        self.color_change = {
            'title': 'color_change',
            'locator': self.page.locator(DynPropertiesPL.COLOR_CHANGE),
            'selector': DynPropertiesPL.COLOR_CHANGE
        }
        self.visible_after = {
            'title': 'visible_after',
            'locator': self.page.locator(DynPropertiesPL.VISIBLE_AFTER),
            'selector': DynPropertiesPL.VISIBLE_AFTER
        }


class WebTablesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().web_tables
        self.delete_btn = {
            'title': 'delete_btn',
            'locator': self.page.locator(WebTablesPL.DELETE_RECORD),
            'selector': WebTablesPL.DELETE_RECORD
        }
        self.rows = {
            'title': 'rows',
            'locator': self.page.locator(WebTablesPL.ROWS),
            'selector': WebTablesPL.ROWS
        }
        self.search_input = {
            'title': 'search_input',
            'locator': self.page.locator(WebTablesPL.SEARCH_INPUT),
            'selector': WebTablesPL.SEARCH_INPUT
        }
        self.no_rows = {
            'title': 'no_rows',
            'locator': self.page.locator(WebTablesPL.NO_ROWS),
            'selector': WebTablesPL.NO_ROWS
        }
