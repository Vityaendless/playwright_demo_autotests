from .base import BasePage
from auxiliary.url_path import UrlPaths
# from auxiliary.locators import ProfilePageLocator as ProfilePL


class BooksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().books_store
