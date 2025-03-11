import time

import allure
import pytest

from auxiliary.constants import HTMLAttr


@allure.epic("Тесты авторизации")
class TestLogin:
    LOGIN_ERROR_MESSAGE = "Invalid username or password!"

    @pytest.mark.skip
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
            controller.helper.to_have_url(controller.login_page.page, controller.profile_page.page.url, timeout=10000)
            controller.helper.to_contain_text(controller.login_page.username_value, test_user['username'])

    @pytest.mark.skip
    @allure.feature("Авторизация")
    @allure.story("Пользователь может авторизоваться на сайте")
    @allure.title("Авторизация несуществующего пользователя")
    @allure.description("Авторизация несуществующего пользователя на сайте")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_username(self, controller, test_user):
        with allure.step('Открыть страницу авторизации'):
            controller.login_page.navigate()
        with allure.step('Авторизоваться на сайте'):
            controller.login_page.fill(controller.login_page.username, test_user['invalid_username'])
            controller.login_page.fill(controller.login_page.password, test_user['password'])
            controller.login_page.click(controller.login_page.login_btn)
        with allure.step('Проверка, что авторизация НЕ произошла'):
            controller.helper.to_contain_text(controller.login_page.message, TestLogin.LOGIN_ERROR_MESSAGE)

    @pytest.mark.skip
    @allure.feature("Авторизация")
    @allure.story("Пользователь может авторизоваться на сайте")
    @allure.title("Авторизация с некорректным паролем")
    @allure.description("Авторизация пользователя с паролем, не подходящим под условия")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_password(self, controller, test_user):
        with allure.step('Открыть страницу авторизации'):
            controller.login_page.navigate()
        with allure.step('Авторизоваться на сайте'):
            controller.login_page.fill(controller.login_page.username, test_user['username'])
            controller.login_page.fill(controller.login_page.password, test_user['invalid_password'])
            controller.login_page.click(controller.login_page.login_btn)
        with allure.step('Проверка, что авторизация НЕ произошла'):
            controller.helper.to_contain_text(controller.login_page.message, TestLogin.LOGIN_ERROR_MESSAGE)

    @pytest.mark.skip
    @allure.feature("Авторизация")
    @allure.story("Пользователь может авторизоваться на сайте")
    @allure.title("Переход к странице регистрации")
    @allure.description("Проверка перехода к странице регистрации")
    @allure.severity(allure.severity_level.MINOR)
    def test_to_register(self, controller):
        with allure.step('Открыть страницу авторизации'):
            controller.login_page.navigate()
        with allure.step('Проверка перехода к странице регистрации'):
            controller.login_page.click(controller.login_page.reg_btn)
            controller.helper.to_have_url(controller.login_page.page, controller.register_page.page.url, timeout=10000)

    @pytest.mark.skip
    @allure.feature("Авторизация")
    @allure.story("Пользователь может авторизоваться на сайте")
    @allure.title("Страница авторизации после авторизации")
    @allure.description("Проверка содержимого страницы авторизации после авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_after_login(self, auth):
        with allure.step('Авторизоваться'):
            auth_controller = auth
            auth_controller.helper.to_be_visible(auth_controller.profile_page.logout)
        with allure.step('Открыть страницу авторизации'):
            auth_controller.profile_page.click(auth_controller.profile_page.to_login_page)
        with allure.step('Проверить содержимое страницы авторизации'):
            auth_controller.helper.is_present(auth_controller.login_page.page, auth_controller.login_page.loading_label)
            auth_controller.helper.is_present(
                auth_controller.login_page.page, auth_controller.login_page.to_profile_link
            )
            auth_controller.helper.to_contain_text(
                auth_controller.login_page.loading_label, "You are already logged in. View your profile."
            )
            auth_controller.helper.to_have_attribute(
                auth_controller.login_page.to_profile_link, HTMLAttr.HREF, "/profile"
            )
