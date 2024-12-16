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
    def to_be_disabled(el):
        expect(el['locator'], f"Element {el['title']} is enabled").to_be_disabled()

    @staticmethod
    def not_to_be_disabled(el, timeout=TIMEOUT):
        expect(el['locator'], f"Element {el['title']} is disabled").not_to_be_disabled(timeout=timeout)

    @staticmethod
    def to_have_text(el, text):
        expect(el['locator'], f"Element {el['title']} doesn't have text:[{text}]").to_have_text(text)

    @staticmethod
    def to_contain_text(el, text, timeout=TIMEOUT):
        (expect(el['locator'], f"Element {el['title']} doesn't contain text:[{text}]").
         to_contain_text(text, timeout=timeout))

    @staticmethod
    def to_have_attribute(el, attr, value):
        (expect(el['locator'], f"Element {el['title']} don't have attribute:[{attr}] with value:[{value}]").
         to_have_attribute(attr, value))
