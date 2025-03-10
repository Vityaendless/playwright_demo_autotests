import time
import random

import allure
import pytest

from auxiliary.constants import HTMLAttr


@allure.epic("Тесты регистрации")
class TestRegister:

    @pytest.mark.skip
    @allure.feature("Регистрация")
    @allure.story("Пользователь может зарегистрироваться на сайте на сайте")
    @allure.title("Регистрация")
    @allure.description("Валидная регистрация пользователя на сайте")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_register(self, controller, fake_user):
        with allure.step('Открыть страницу регистрации'):
            controller.register_page.navigate()
        with allure.step('Зарегистрироваться на сайте'):
            controller.helper.is_present(
                controller.register_page.page, controller.register_page.first_name, HTMLAttr.REQUIRED
            )
            controller.helper.is_present(
                controller.register_page.page, controller.register_page.last_name, HTMLAttr.REQUIRED
            )
            controller.helper.is_present(
                controller.register_page.page, controller.register_page.username, HTMLAttr.REQUIRED
            )
            controller.helper.is_present(
                controller.register_page.page, controller.register_page.password, HTMLAttr.REQUIRED
            )
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.type(controller.register_page.first_name, fake_user['first_name'])
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.type(controller.register_page.last_name, fake_user['last_name'])
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.type(controller.register_page.username, fake_user['username'])
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.type(controller.register_page.password, fake_user['password'])
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.hover(controller.register_page.recaptcha)
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            controller.register_page.down()
            controller.register_page.up()
            controller.register_page.page.wait_for_timeout(random.randint(1, 5) * 2000 + 500)
            # controller.register_page.click(controller.register_page.register_btn)
            # time.sleep(5)
        # with allure.step('Проверка, что авторизация произошла'):
        #     controller.helper.to_have_url(controller.login_page.page, "https://demoqa.com/profile", timeout=10000)
        #     controller.helper.to_contain_text(controller.login_page.username_value, test_user['username'])

    @pytest.mark.skip
    @allure.feature("Регистрация")
    @allure.story("Пользователь может зарегистрироваться на сайте на сайте")
    @allure.title("Переход к странице авторизации")
    @allure.description("Проверка перехода к странице авторизации")
    @allure.severity(allure.severity_level.MINOR)
    def test_to_login(self, controller):
        with allure.step('Открыть страницу регистрации'):
            controller.register_page.navigate()
        with allure.step('Проверка перехода к странице регистрации'):
            controller.register_page.click(controller.register_page.login_btn)
            controller.helper.to_have_url(controller.register_page.page, controller.login_page.page.url, timeout=10000)
