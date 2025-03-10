import allure
import pytest


@allure.epic("Тесты профиля")
class TestProfile:

    @pytest.mark.skip
    @allure.feature("Профиль")
    @allure.story("Пользователь может зайти в свой профиль")
    @allure.title("Выход из профиля")
    @allure.description("Проверка возможности выйти из профиля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, controller, auth):
        login = auth
        with allure.step('Нажать на кнопку логаута'):
            controller.profile_page.click(controller.profile_page.logout)
        with allure.step('Проверка, что логаут произошел'):
            controller.helper.to_have_url(controller.profile_page.page, login.login_page.page.url, timeout=10000)
