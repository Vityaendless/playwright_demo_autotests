import allure
import pytest


@allure.epic("Тесты работоспособности формы")
class TestForm:

    #@pytest.mark.skip
    @allure.feature("Форма отправки данных юзера")
    @allure.story("Авторизация")
    @allure.title("Тест заполнения текстовой формы")
    @allure.description("Ввод данных в форму и проверка сохранения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_textbox(self, controller, user_data):
        # username = user_data['username']
        # email = user_data['email']
        # curr_address = user_data['curr_address']
        # per_address = user_data['per_address']
        with allure.step('Открыть страницу формы'):
            controller.practice_form_page.navigate()
        controller.practice_form_page.click(controller.practice_form_page.submit)
        # t = controller.practice_form_page.get_attr(controller.practice_form_page.first_name, "class")
        # k = controller.practice_form_page.get_attr(controller.practice_form_page.email, "class")
        # t = controller.practice_form_page.first_name["locator"].inner_text()
        content = controller.page.evaluate(f"window.getComputedStyle(document.getElementById('#firstName')), ''")
        assert False, f"{content}"
