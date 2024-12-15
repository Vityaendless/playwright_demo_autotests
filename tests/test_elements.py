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

    @allure.feature("Раскрывающийся список")
    @allure.story("Иеархия элементов")
    @allure.title("Тест выбора элементов в иеархии")
    @allure.description("Выбор элементов и иеархии и проверка этого выбора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkbox(self, controller):
        els_lst = []
        with allure.step('Открыть страницу элементов иеархии'):
            controller.checkbox_page.navigate()
        with allure.step('Проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.checkbox_page.result)
        with allure.step('Раскрыть иеархию'):
            controller.checkbox_page.click(controller.checkbox_page.expand_all)
        with allure.step('Нажать кнопку "Home"'):
            controller.checkbox_page.click(controller.checkbox_page.home)
        with allure.step('Проверить наличие элемента результата'):
            controller.helper.to_be_visible(controller.checkbox_page.result)
        all_els = controller.checkbox_page.all_els(controller.checkbox_page.els)
        with allure.step('Получить названия всех элементов иеархии'):
            for el in all_els:
                els_lst.append(el.text_content().lower().split(".")[0].replace(' file', 'File'))
        with allure.step('Скрыть иеархию'):
            controller.checkbox_page.click(controller.checkbox_page.collapse_all)
        with allure.step('Проверить, что все элементы отобразились в строке результата'):
            for title in els_lst:
                controller.helper.to_contain_text(controller.checkbox_page.result, title)
        with allure.step('Повторно нажать кнопку "Home"'):
            controller.checkbox_page.click(controller.checkbox_page.home)
        with allure.step('Повторно проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.checkbox_page.result)

    @allure.feature("Выбор ответа через radio btns")
    @allure.story("Выбор ответа")
    @allure.title("Тест выбора ответа")
    @allure.description("Выбор ответа и проверка этого выбора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_radio_btn(self, controller):
        with allure.step('Открыть страницу выбора на основе radio btns'):
            controller.radio_btn_page.navigate()
        with allure.step('Проверить отсуствие элемента результата'):
            controller.helper.not_to_be_visible(controller.radio_btn_page.result)
        with allure.step('Проверить стартовое отображение элементов'):
            controller.helper.to_be_disabled(controller.radio_btn_page.no_radio)
            controller.helper.not_to_be_disabled(controller.radio_btn_page.yes_radio)
            controller.helper.not_to_be_disabled(controller.radio_btn_page.impressive_radio)
        with allure.step('Выбрать первый ответ "YES"'):
            controller.radio_btn_page.check(controller.radio_btn_page.yes)
        with allure.step('Проверить, что в результате ответ "YES"'):
            controller.helper.to_have_text(
                controller.radio_btn_page.result, controller.radio_btn_page.yes['title'].capitalize()
            )
        with allure.step('Выбрать первый ответ "IMPRESSIVE"'):
            controller.radio_btn_page.check(controller.radio_btn_page.impressive)
        with allure.step('Проверить, что в результате ответ "IMPRESSIVE"'):
            controller.helper.to_have_text(
                controller.radio_btn_page.result, controller.radio_btn_page.impressive['title'].capitalize()
            )
