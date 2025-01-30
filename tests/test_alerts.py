import allure
import pytest
import asyncio


@allure.epic("Тесты уведомлений")
class TestAlerts:

    #@pytest.mark.skip
    @allure.feature("Работа с всплывающими уведомлениями")
    @allure.story("Взаимодействие с элементами всплывающих уведомлений")
    @allure.title("Проверка открытия алерта")
    @allure.description("Проверка открытия алерта")
    @allure.severity(allure.severity_level.MINOR)
    def test_alert(self, controller):
        def handle_alert(dialog):
            controller.helper.is_eq(dialog.type, "alert")
            controller.helper.is_eq(dialog.message, "You clicked a button")
            print(dialog.message)
            dialog.accept()

        with allure.step('Открыть страницу всплывающих уведомлений'):
            controller.alerts_page.navigate()
        with allure.step('Нажать на кнопку и проверить содержимое алерта'):
            controller.alerts_page.page.on("dialog", handle_alert)
            controller.alerts_page.click(controller.alerts_page.alert_btn)
            controller.alerts_page.page.remove_listener("dialog", handle_alert)


    #@pytest.mark.skip
    @allure.feature("Работа с всплывающими уведомлениями")
    @allure.story("Взаимодействие с элементами всплывающих уведомлений")
    @allure.title("Проверка открытия алерта с задержкой")
    @allure.description("Проверка открытия алерта с временной задеркой отклика")
    @allure.severity(allure.severity_level.MINOR)
    def test_time_alert(self, controller):
        def handle_alert(dialog):
            controller.helper.is_eq(dialog.type, "alert")
            controller.helper.is_eq(dialog.message, "This alert appeared after  seconds")
            print(dialog.message + "rtrv")
            dialog.accept()

        with allure.step('Открыть страницу всплывающих уведомлений'):
            controller.alerts_page.navigate()
        with allure.step('Нажать на кнопку и проверить содержимое алерта'):
            controller.alerts_page.page.on("dialog", handle_alert)
            controller.alerts_page.click(controller.alerts_page.time_alert_btn)
            controller.alerts_page.page.remove_listener("dialog", handle_alert)
