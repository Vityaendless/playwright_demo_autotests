from playwright.sync_api import Page

from auxiliary.helper import Helper
from auxiliary.pages import (TextboxPage, CheckboxPage, RadioBtnPage, BtnPage, LinksPage, BrokenImagesLinksPage,
                             UploadDownloadPage, DynPropertiesPage, WebTablesPage, TabsPage, AccordianPage,
                             PracticeFormPage, WindowsPage, SamplePage, AlertsPage, IframesPage, NestedIframesPage,
                             ModalDialogsPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage,
                             ToolTipPage, MenuPage, SelectMenuPage, SortablePage, SelectablePage, ResizablePage,
                             DroppablePage, DraggablePage, LoginPage)


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
        self.alerts_page = AlertsPage(self.page)
        self.iframes_page = IframesPage(self.page)
        self.nested_iframes_page = NestedIframesPage(self.page)
        self.modal_dialogs_page = ModalDialogsPage(self.page)
        self.auto_complete_page = AutoCompletePage(self.page)
        self.date_picker_page = DatePickerPage(self.page)
        self.slider_page = SliderPage(self.page)
        self.progress_bar = ProgressBarPage(self.page)
        self.tool_tip_page = ToolTipPage(self.page)
        self.menu_page = MenuPage(self.page)
        self.select_menu = SelectMenuPage(self.page)
        self.sortable_page = SortablePage(self.page)
        self.selectable_page = SelectablePage(self.page)
        self.resizable_page = ResizablePage(self.page)
        self.droppable_page = DroppablePage(self.page)
        self.draggable_page = DraggablePage(self.page)
        self.login_page = LoginPage(self.page)
