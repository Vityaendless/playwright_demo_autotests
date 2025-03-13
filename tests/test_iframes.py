import allure


@allure.epic("Тесты встроенных окон")
class TestIframes:

    @allure.feature("Работа со встроенными окнами")
    @allure.story("Взаимодействие с элементами встроенных окон")
    @allure.title("Проверка доступа к элементам встроенного окна")
    @allure.description("Проверка доступа к элементам встроенного окна")
    @allure.severity(allure.severity_level.MINOR)
    def test_iframes(self, controller):
        with allure.step('Открыть страницу встроенных окон'):
            controller.iframes_page.navigate()
        with allure.step('Проверить содержимое встроенных окон'):
            iframe1 = controller.iframes_page.page.frame_locator(controller.iframes_page.first_iframe['selector'])
            iframe1_heading = iframe1.locator(controller.sample_page.heading["selector"])
            iframe2 = controller.iframes_page.page.frame_locator(controller.iframes_page.second_iframe['selector'])
            iframe2_heading = iframe2.locator(controller.sample_page.heading["selector"])
            controller.helper.is_eq(iframe1_heading.text_content(), iframe2_heading.text_content())

    @allure.feature("Работа со встроенными окнами")
    @allure.story("Взаимодействие с элементами встроенных окон")
    @allure.title("Проверка доступа к дочернему встроенному окну")
    @allure.description("Проверка доступа к дочернему встроенному окну")
    @allure.severity(allure.severity_level.MINOR)
    def test_nested_iframes(self, controller):
        BODY_TAG = "body"
        with allure.step('Открыть страницу родительского и дочернего встроенных окон'):
            controller.nested_iframes_page.navigate()
        with allure.step('Проверить содержимое родительского и дочернего встроенных окон'):
            parent_iframe = controller.nested_iframes_page.page.frame_locator(
                controller.nested_iframes_page.parent_iframe['selector']
            )
            parent_iframe_text = parent_iframe.locator(BODY_TAG).text_content()
            print(parent_iframe_text)
            controller.helper.is_eq("Parent frame", parent_iframe_text)
            child_iframe = parent_iframe.frame_locator("iframe")
            child_iframe_text = child_iframe.locator(BODY_TAG).text_content()
            print(child_iframe_text)
            controller.helper.is_eq("Child Iframe", child_iframe_text)
