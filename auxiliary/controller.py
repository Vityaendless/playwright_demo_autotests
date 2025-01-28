from playwright.sync_api import Page

from auxiliary.helper import Helper
from auxiliary.pages import (TextboxPage, CheckboxPage, RadioBtnPage, BtnPage, LinksPage, BrokenImagesLinksPage,
                             UploadDownloadPage, DynPropertiesPage, WebTablesPage, TabsPage, AccordianPage,
                             PracticeFormPage, WindowsPage, SamplePage)


class Controller:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.helper = Helper()
        self.textbox_page = TextboxPage(self.page)
        self.checkbox_page = CheckboxPage(self.page)
        self.radio_btn_page = RadioBtnPage(self.page)
        self.btn_page = BtnPage(self.page)
        self.links_page = LinksPage(self.page)
        self.broken_obj_page = BrokenImagesLinksPage(self.page)
        self.upload_download_page = UploadDownloadPage(self.page)
        self.dyn_properties_page = DynPropertiesPage(self.page)
        self.web_table_page = WebTablesPage(self.page)
        self.tabs_page = TabsPage(self.page)
        self.accordian_page = AccordianPage(self.page)
        self.practice_form_page = PracticeFormPage(self.page)
        self.windows_page = WindowsPage(self.page)
        self.sample_page = SamplePage(self.page)
