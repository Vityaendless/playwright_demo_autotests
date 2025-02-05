import allure
import pytest


@allure.epic("Тесты модальных окон")
class TestModalDialogs:

    @pytest.mark.skip
    @allure.feature("Работа с модальными окнами")
    @allure.story("Взаимодействие с элементами модальных окон")
    @allure.title("Проверка доступа к элементам модального окна")
    @allure.description("Проверка доступа к элементам модального окна и взаимодействия с такими окнами")
    @allure.severity(allure.severity_level.MINOR)
    def test_modal_dialogs(self, controller, modal_dialogs_information):
        small_modal, large_modal = modal_dialogs_information
        with allure.step('Открыть страницу модальных окон'):
            controller.modal_dialogs_page.navigate()
        with allure.step('Открыть маленькое модальное окно'):
            controller.modal_dialogs_page.click(controller.modal_dialogs_page.small_modal_btn)
        with allure.step('Проверить содержание маленького модального окна'):
            controller.helper.to_contain_text(controller.modal_dialogs_page.small_modal_heading, small_modal['heading'])
            controller.helper.to_contain_text(controller.modal_dialogs_page.modal_body, small_modal['text'])
        with allure.step('Закрыть маленькое модальное окно'):
            controller.modal_dialogs_page.click(controller.modal_dialogs_page.close_small_modal_btn)
        with allure.step('Открыть большое модальное окно'):
            controller.modal_dialogs_page.click(controller.modal_dialogs_page.large_modal_btn)
        with allure.step('Проверить содержание большого модального окна'):
            controller.helper.to_contain_text(controller.modal_dialogs_page.large_modal_heading, large_modal['heading'])
            controller.helper.to_contain_text(controller.modal_dialogs_page.modal_body, large_modal['text'])
        with allure.step('Закрыть большое модальное окно'):
            controller.modal_dialogs_page.click(controller.modal_dialogs_page.close_large_modal_btn)
