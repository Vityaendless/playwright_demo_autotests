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


    #@pytest.mark.skip
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
