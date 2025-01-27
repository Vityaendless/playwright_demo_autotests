import time

import allure
import pytest

from auxiliary.constants import HTMLEl, PseudoClsEl


@allure.epic("Тесты работоспособности формы")
class TestForm:

    @pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Форма для заполнения данных пользователя")
    @allure.title("Тест обязательности заполнения полей")
    @allure.description("Проверка обязательности заполнения полей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_required(self, controller):
        with allure.step('Открыть страницу формы'):
            controller.practice_form_page.navigate()
        with allure.step('Задать переменные для проверки'):
            input = HTMLEl.input
            invalid = PseudoClsEl.invalid
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.first_name["selector"]}'):
            el = f"{controller.practice_form_page.first_name['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.last_name["selector"]}'):
            el = f"{controller.practice_form_page.last_name['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.gender_male["selector"]}'):
            el = f"{controller.practice_form_page.gender_male['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.gender_female["selector"]}'):
            el = f"{controller.practice_form_page.gender_female['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.gender_other["selector"]}'):
            el = f"{controller.practice_form_page.gender_other['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.phone_number["selector"]}'):
            el = f"{controller.practice_form_page.phone_number['selector']}"
            data = (input, el, invalid)
            controller.practice_form_page.is_required(*data)


    @pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Форма для заполнения данных пользователя")
    @allure.title("Тест НЕ обязательности заполнения полей")
    @allure.description("Проверка НЕ обязательности заполнения полей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_not_required(self, controller):
        with allure.step('Открыть страницу формы'):
            controller.practice_form_page.navigate()
        with allure.step('Задать переменные для проверки'):
            input = HTMLEl.input
            textarea = HTMLEl.textarea
            valid = PseudoClsEl.valid
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.email["selector"]}'):
            el = f"{controller.practice_form_page.email['selector']}"
            data = (input, el, valid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.birth_date["selector"]}'):
            el = f"{controller.practice_form_page.birth_date['selector']}"
            data = (input, el, valid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.hobby_sports["selector"]}'):
            el = f"{controller.practice_form_page.hobby_sports['selector']}"
            data = (input, el, valid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.hobby_music["selector"]}'):
            el = f"{controller.practice_form_page.hobby_music['selector']}"
            data = (input, el, valid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.hobby_reading["selector"]}'):
            el = f"{controller.practice_form_page.hobby_reading['selector']}"
            data = (input, el, valid)
            controller.practice_form_page.is_required(*data)
        with allure.step(f'Проверка обязательности параметра {controller.practice_form_page.current_address["selector"]}'):
            el = f"{controller.practice_form_page.current_address['selector']}"
            data = (textarea, el, valid)
            controller.practice_form_page.is_required(*data)


    @pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Форма для заполнения данных пользователя")
    @allure.title("Тест отправки формы 1")
    @allure.description("Тест отправки формы с заполнением только обязательных полей")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_required_submit(self, controller, practice_form_user_data):
        with allure.step('Открыть страницу формы'):
            controller.practice_form_page.navigate()
        with allure.step('Заполнение данных формы'):
            controller.practice_form_page.fill(
                controller.practice_form_page.first_name, practice_form_user_data['first_name']
            )
            controller.practice_form_page.fill(
                controller.practice_form_page.last_name, practice_form_user_data['last_name']
            )
            controller.practice_form_page.click(controller.practice_form_page.gender_male)
            choised_gender = controller.practice_form_page.get_element_text(controller.practice_form_page.gender_male)
            controller.practice_form_page.fill(
                controller.practice_form_page.phone_number, practice_form_user_data['phone']
            )
        with allure.step('Нажать кнопку отправки формы'):
            controller.practice_form_page.click(controller.practice_form_page.submit)
        with allure.step('Проверка результата введенных данных'):
            controller.helper.to_contain_text(
                controller.practice_form_page.name_result,
                practice_form_user_data['first_name'] + " " + practice_form_user_data['last_name']
            )
            table_gender = controller.practice_form_page.get_element_text(controller.practice_form_page.gender_result)
            controller.helper.is_eq(choised_gender, table_gender)
            controller.helper.to_contain_text(
                controller.practice_form_page.phone_result,
                practice_form_user_data['phone']
            )

    #@pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Форма для заполнения данных пользователя")
    @allure.title("Тест отправки формы 2")
    @allure.description("Тест отправки формы с заполнением всех полей")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_full_submit(self, controller, practice_form_user_data):
        with allure.step('Открыть страницу формы'):
            controller.practice_form_page.navigate()
        with allure.step('Заполнение данных формы'):
            controller.practice_form_page.fill(
                controller.practice_form_page.first_name, practice_form_user_data['first_name']
            )
            controller.practice_form_page.fill(
                controller.practice_form_page.last_name, practice_form_user_data['last_name']
            )
            controller.practice_form_page.fill(controller.practice_form_page.email, practice_form_user_data['email'])
            controller.practice_form_page.click(controller.practice_form_page.gender_female)
            choised_gender = controller.practice_form_page.get_element_text(controller.practice_form_page.gender_female)
            controller.practice_form_page.fill(
                controller.practice_form_page.phone_number, practice_form_user_data['phone']
            )
            controller.practice_form_page.fill(
                controller.practice_form_page.birth_date, practice_form_user_data['birth_date']
            )
            controller.practice_form_page.press(controller.practice_form_page.birth_date)
            for subject in practice_form_user_data['subjects']:
                controller.practice_form_page.type(controller.practice_form_page.subjects, subject)
                controller.practice_form_page.press(controller.practice_form_page.subjects)
        # with allure.step('Нажать кнопку отправки формы'):
        #     controller.practice_form_page.click(controller.practice_form_page.submit)
        # with allure.step('Проверка результата введенных данных'):
        #     controller.helper.to_contain_text(
        #         controller.practice_form_page.name_result,
        #         practice_form_user_data['first_name'] + " " + practice_form_user_data['last_name']
        #     )
        #     table_gender = controller.practice_form_page.get_element_text(controller.practice_form_page.gender_result)
        #     controller.helper.is_eq(choised_gender, table_gender)
        #     controller.helper.to_contain_text(
        #         controller.practice_form_page.phone_result,
        #         practice_form_user_data['phone']
        #     )
