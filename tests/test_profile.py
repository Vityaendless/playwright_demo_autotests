import allure
import pytest


@allure.epic("Тесты профиля")
class TestProfile:
    NOT_LOGIN_LABEL = ("Currently you are not logged into the Book Store application, please visit the login page to "
                       "enter or register page to register yourself.")

    @pytest.mark.skip
    @allure.feature("Профиль")
    @allure.story("Пользователь может зайти в свой профиль")
    @allure.title("Переход в раздел профиля до авторизации")
    @allure.description("Проверка содержимого профиля до авторизации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_profile_before_login(self, controller):
        with allure.step('Открыть страницу профиля'):
            controller.profile_page.navigate()
        with allure.step('Проверка содержимого профиля до авторизации'):
            controller.helper.to_contain_text(controller.profile_page.not_login_label, TestProfile.NOT_LOGIN_LABEL)
            controller.helper.is_present(controller.profile_page.page, controller.profile_page.to_login_link)
            controller.helper.is_present(controller.profile_page.page, controller.profile_page.to_reg_link)


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
