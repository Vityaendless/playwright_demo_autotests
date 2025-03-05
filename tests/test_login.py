import time

import allure
import pytest


@allure.epic("Тесты авторизации")
class TestLogin:

    #@pytest.mark.skip
    @allure.feature("Авторизация")
    @allure.story("Пользователь может авторизоваться на сайте")
    @allure.title("Авторизация")
    @allure.description("Валидная авторизация пользователя на сайте")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, controller, test_user):
        with allure.step('Открыть страницу авторизации'):
            controller.login_page.navigate()
        with allure.step('Авторизоваться на сайте'):
            controller.login_page.fill(controller.login_page.username, test_user['username'])
            controller.login_page.fill(controller.login_page.password, test_user['password'])
            controller.login_page.click(controller.login_page.login_btn)
        with allure.step('Проверка, что авторизация произошла'):
            controller.helper.to_have_url(controller.login_page.page, "https://demoqa.com/profile", timeout=10000)
            controller.helper.to_contain_text(controller.login_page.username_value, test_user['username'])
