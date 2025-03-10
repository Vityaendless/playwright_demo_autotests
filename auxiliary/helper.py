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
    def to_be_enabled(el, timeout=TIMEOUT):
        expect(el['locator'], f"Element {el['title']} is disabled").to_be_enabled(timeout=timeout)

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
    def to_have_class(el, cls):
        expect(el['locator'], f"Element {el['title']} don't have class:[{cls}]").to_have_class(cls)

    @staticmethod
    def not_to_have_class(el, cls):
        expect(el['locator'], f"Element {el['title']} have class:[{cls}]").not_to_have_class(cls)

    @staticmethod
    def to_have_attribute(el, attr, value):
        (expect(el['locator'], f"Element {el['title']} don't have attribute:[{attr}] with value:[{value}]").
         to_have_attribute(attr, value))

    @staticmethod
    def to_have_css(el, attr, value, timeout=TIMEOUT):
        (expect(el['locator'], f"Element {el['title']} don't have css:[{attr}] with value:[{value}]").
         to_have_css(attr, value, timeout=timeout))

    @staticmethod
    def to_have_url(page, url, timeout=None):
        expect(page, f"The page doesn't have url: [{url}]").to_have_url(url, timeout=timeout)

    @staticmethod
    def is_present_custom(page, el, css_mod):
        assert page.locator(f"{el['selector']}[{css_mod}]"), f"There's no el:[{el}] in page"

    @staticmethod
    def is_eq(first, second):
        assert first == second, f"[{first}] != [{second}]"

    @staticmethod
    def is_not_eq(first, second):
        assert first != second, f"[{first}] == [{second}]"

    @staticmethod
    def is_less(first, second):
        assert first < second, f"[{first}] >= [{second}]"

    @staticmethod
    def is_in(first, second):
        assert first in second, f"[{first}] not in [{second}]"

    @staticmethod
    def is_not_in(first, second):
        assert first not in second, f"[{first}] in [{second}]"

    @staticmethod
    def to_str(i):
        return str(i)
