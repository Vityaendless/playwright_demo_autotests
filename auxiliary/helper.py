from playwright.sync_api import expect


class Helper:
    TIMEOUT = None

    @staticmethod
    def to_be_visible(el, timeout=TIMEOUT):
        expect(el['locator'], f"Element {el['title']} isn't visible").to_be_visible(timeout=timeout)

    @staticmethod
    def not_to_be_visible(el, timeout=TIMEOUT):
        expect(el['locator'], f"Element {el['title']} is visible").not_to_be_visible(timeout=timeout)

    @staticmethod
    def to_contain_text(el, text, timeout=TIMEOUT):
        (expect(el['locator'], f"Element {el['title']} doesn't contain text:[{text}]").
         to_contain_text(text, timeout=timeout))
