import allure
import pytest


@allure.epic("Тесты профиля")
class TestProfile:
    NOT_LOGIN_LABEL = ("Currently you are not logged into the Book Store application, please visit the login page to "
                       "enter or register page to register yourself.")

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

    @allure.feature("Профиль")
    @allure.story("Пользователь может зайти в свой профиль")
    @allure.title("Выход из профиля")
    @allure.description("Проверка возможности выйти из профиля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, controller, auth):
        login_controller = auth
        with allure.step('Нажать на кнопку логаута'):
            controller.profile_page.click(controller.profile_page.logout)
        with allure.step('Проверка, что логаут произошел'):
            controller.helper.to_have_url(
                controller.profile_page.page, login_controller.login_page.page.url, timeout=10000
            )

    @allure.feature("Профиль")
    @allure.story("Пользователь может зайти в свой профиль")
    @allure.title("Переход к разделу Bookstore")
    @allure.description("Проверка возможности перейти в Bookstore")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_bookstore(self, auth):
        login_controller = auth
        with allure.step('Нажать на кнопку перехода в Bookstore'):
            login_controller.profile_page.click(login_controller.profile_page.go_to_bookstore)
        with allure.step('Проверка, что переход в раздел BooksStore произошел'):
            login_controller.helper.to_have_url(
                login_controller.profile_page.page, login_controller.books_page.page.url, timeout=10000
            )

    @pytest.mark.skip
    @allure.feature("Профиль")
    @allure.story("Пользователь может зайти в свой профиль")
    @allure.title("Удаление пользователя")
    @allure.description("Проверка возможности удалить пользователя в профиле")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_bookstore(self, auth, restore_user_api):
        login_controller = auth
        with allure.step('Нажать на кнопку перехода в Bookstore'):
            login_controller.profile_page.click(login_controller.profile_page.delete_acc_btn)
            login_controller.profile_page.click(login_controller.profile_page.accept_delete_btn)
        with allure.step('Проверка, что пользователь удален и произошел переход к разделу login'):
            login_controller.helper.to_have_url(
                login_controller.profile_page.page, login_controller.login_page.page.url, timeout=10000
            )
        with allure.step('Восстановление удаленного пользователя'):
            restoring = restore_user_api
