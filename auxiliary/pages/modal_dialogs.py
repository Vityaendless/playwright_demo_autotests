from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.locators import ModalDialogsPageLocator as ModalDialogsPL


class ModalDialogsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().modal_dialogs
        self.small_modal_btn = {
            'title': 'small_modal_btn',
            'locator': self.page.locator(ModalDialogsPL.SMALL_MODAL_BTN),
            'selector': ModalDialogsPL.SMALL_MODAL_BTN
        }
        self.small_modal_heading = {
            'title': 'small_modal_heading',
            'locator': self.page.locator(ModalDialogsPL.SMALL_MODAL_HEADING),
            'selector': ModalDialogsPL.SMALL_MODAL_HEADING
        }
        self.close_small_modal_btn = {
            'title': 'close_small_modal_btn',
            'locator': self.page.locator(ModalDialogsPL.CLOSE_SMALL_MODAL_BTN),
            'selector': ModalDialogsPL.CLOSE_SMALL_MODAL_BTN
        }
        self.large_modal_btn = {
            'title': 'large_modal_btn',
            'locator': self.page.locator(ModalDialogsPL.LARGE_MODAL_BTN),
            'selector': ModalDialogsPL.LARGE_MODAL_BTN
        }
        self.large_modal_heading = {
            'title': 'large_modal_heading',
            'locator': self.page.locator(ModalDialogsPL.LARGE_MODAL_HEADING),
            'selector': ModalDialogsPL.LARGE_MODAL_HEADING
        }
        self.close_large_modal_btn = {
            'title': 'close_large_modal_btn',
            'locator': self.page.locator(ModalDialogsPL.CLOSE_LARGE_MODAL_BTN),
            'selector': ModalDialogsPL.CLOSE_LARGE_MODAL_BTN
        }
        self.modal_body = {
            'title': 'modal_body',
            'locator': self.page.locator(ModalDialogsPL.MODAL_BODY),
            'selector': ModalDialogsPL.MODAL_BODY
        }
        self.close_modal_btn = {
            'title': 'close_modal_btn',
            'locator': self.page.locator(ModalDialogsPL.CLOSE_MODAL_BTN),
            'selector': ModalDialogsPL.CLOSE_MODAL_BTN
        }
