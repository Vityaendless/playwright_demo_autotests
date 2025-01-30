import allure
import pytest


@allure.epic("Тесты окон браузера")
class TestWindows:

    @pytest.mark.skip
    @allure.feature("Работа с окнами браузера")
    @allure.story("Взаимодействие с элементами окон и вкладок блаузера")
    @allure.title("Проверка открытия новой вкладки")
    @allure.description("Проверка открытия новой вкладки браузера")
    @allure.severity(allure.severity_level.MINOR)
    def test_new_tab(self, controller):
        with allure.step('Открыть страницу окон браузера'):
            controller.windows_page.navigate()
        with allure.step('Нажать на кнопку открытия новой вкладки'):
            with controller.page.context.expect_page() as tab:
                controller.windows_page.click(controller.windows_page.new_tab_btn)
        with allure.step('Перейти на новую вкладку и проверить наличия заголовка на ней'):
            new_tab = tab.value
            sample_page_text = new_tab.locator(
                controller.sample_page.heading['selector'], has_text='This is a sample page'
            )
            assert sample_page_text.is_visible()


    @pytest.mark.skip
    @allure.feature("Работа с окнами браузера")
    @allure.story("Взаимодействие с элементами окон и вкладок блаузера")
    @allure.title("Проверка открытия нового окна")
    @allure.description("Проверка открытия нового окна браузера")
    @allure.severity(allure.severity_level.MINOR)
    def test_new_window(self, controller):
        with allure.step('Открыть страницу окон браузера'):
            controller.windows_page.navigate()
        with allure.step('Нажать на кнопку открытия нового окна'):
            with controller.page.context.expect_page() as wnd:
                controller.windows_page.click(controller.windows_page.new_window_btn)
        with allure.step('Перейти к новому окну и проверить наличия заголовка на нем'):
            new_wnd = wnd.value
            sample_page_text = new_wnd.locator(
                controller.sample_page.heading['selector'], has_text='This is a sample page'
            )
            assert sample_page_text.is_visible()

    @pytest.mark.skip
    @allure.feature("Работа с окнами браузера")
    @allure.story("Взаимодействие с элементами окон и вкладок блаузера")
    @allure.title("Проверка открытия нового окна с сообщением")
    @allure.description("Проверка открытия нового окна браузера с сообщением")
    @allure.severity(allure.severity_level.MINOR)
    def test_new_window_message(self, controller):
        with allure.step('Открыть страницу окон браузера'):
            controller.windows_page.navigate()
        with allure.step('Нажать на кнопку открытия нового окна'):
            with controller.page.context.expect_page() as wnd:
                controller.windows_page.click(controller.windows_page.msg_new_window_btn)
        with allure.step('Перейти к новому окну и проверить наличия заголовка на нем'):
            new_wnd = wnd.value
            wnd_text = "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."
            sample_page_text = new_wnd.locator(controller.sample_page.body['selector'], has_text=wnd_text)
            assert sample_page_text.is_visible()
