import time
import pytest
import allure

@allure.epic("Тесты элементов")
class TestElements:

    @allure.feature("Форма отправки данных юзера")
    @allure.story("Авторизация")
    @allure.title("Тест заполнения текстовой формы")
    @allure.description("Ввод данных в форму и проверка сохранения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_textbox(self, controller, user_data):
        username = user_data['username']
        email = user_data['email']
        curr_address = user_data['curr_address']
        per_address = user_data['per_address']
        with allure.step('Открыть страницу формы'):
            controller.textbox_page.navigate()
        with allure.step('Проверить отсуствие элемента вывода данных'):
            controller.helper.not_to_be_visible(controller.textbox_page.output)
        with allure.step('Ввести данные в форму'):
            controller.textbox_page.fill(controller.textbox_page.username, username)
            controller.textbox_page.fill(controller.textbox_page.email, email)
            controller.textbox_page.fill(controller.textbox_page.c_address, curr_address)
            controller.textbox_page.fill(controller.textbox_page.p_address, per_address)
        with allure.step('Нажать кнопку "Submit"'):
            controller.textbox_page.click(controller.textbox_page.submit)
        with allure.step('Проверить наличие элемента вывода данных'):
            controller.helper.to_be_visible(controller.textbox_page.output)
        with allure.step('Проверить, что элемент вывода данных содержит информацию, введенную в форму'):
            controller.helper.to_contain_text(controller.textbox_page.output_name, username)
            controller.helper.to_contain_text(controller.textbox_page.output_email, email)
            controller.helper.to_contain_text(controller.textbox_page.output_c_address, curr_address)
            controller.helper.to_contain_text(controller.textbox_page.output_p_address, per_address)
