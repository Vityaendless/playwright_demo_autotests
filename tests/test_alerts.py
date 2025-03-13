import allure


@allure.epic("Тесты уведомлений")
class TestAlerts:

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

    @allure.feature("Работа с всплывающими уведомлениями")
    @allure.story("Взаимодействие с элементами всплывающих уведомлений")
    @allure.title("Проверка открытия алерта с задержкой")
    @allure.description("Проверка открытия алерта с временной задеркой отклика")
    @allure.severity(allure.severity_level.MINOR)
    def test_time_alert(self, controller):
        def handle_alert(dialog):
            controller.helper.is_eq(dialog.type, "alert")
            controller.helper.is_eq(dialog.message, "This alert appeared after 5 seconds")
            dialog.accept()

        wait_for_alert = ("var is_alert = false;(function() { var _old_alert = window.alert; window.alert = "
                          "function() {_old_alert.apply(window,arguments); is_alert = true; };})();")

        with allure.step('Открыть страницу всплывающих уведомлений'):
            controller.alerts_page.navigate()
        with allure.step('Нажать на кнопку и проверить содержимое алерта'):
            controller.alerts_page.page.on("dialog", handle_alert)
            controller.alerts_page.click(controller.alerts_page.time_alert_btn)
            controller.alerts_page.page.evaluate(wait_for_alert)
            controller.alerts_page.page.wait_for_function("() => window.is_alert")
            controller.alerts_page.page.remove_listener("dialog", handle_alert)

    @allure.feature("Работа с всплывающими уведомлениями")
    @allure.story("Взаимодействие с элементами всплывающих уведомлений")
    @allure.title("Проверка открытия окна подтверждения")
    @allure.description("Проверка открытия окна подтверждения")
    @allure.severity(allure.severity_level.MINOR)
    def test_confirm(self, controller):
        def check_confirm(dialog):
            controller.helper.is_eq(dialog.type, "confirm")
            controller.helper.is_eq(dialog.message, "Do you confirm action?")
            print(dialog.message)

        def handle_confirm_accept(dialog):
            check_confirm(dialog)
            dialog.accept()

        def handle_confirm_dismiss(dialog):
            check_confirm(dialog)
            dialog.dismiss()

        with allure.step('Открыть страницу всплывающих уведомлений'):
            controller.alerts_page.navigate()
        with allure.step('Нажать на кнопку и проверить содержимое окна подтверждения'):
            controller.alerts_page.page.on("dialog", handle_confirm_accept)
            controller.alerts_page.click(controller.alerts_page.confirm_btn)
            controller.alerts_page.page.remove_listener("dialog", handle_confirm_accept)
        with allure.step('Проверить содержимое строки результата в зависимости от выбранного действия'):
            controller.helper.to_contain_text(controller.alerts_page.confirm_result, "Ok")
        with allure.step('Нажать на кнопку и проверить содержимое окна подтверждения'):
            controller.alerts_page.page.on("dialog", handle_confirm_dismiss)
            controller.alerts_page.click(controller.alerts_page.confirm_btn)
            controller.alerts_page.page.remove_listener("dialog", handle_confirm_dismiss)
        with allure.step('Проверить содержимое строки результата в зависимости от выбранного действия'):
            controller.helper.to_contain_text(controller.alerts_page.confirm_result, "Cancel")

    @allure.feature("Работа с всплывающими уведомлениями")
    @allure.story("Взаимодействие с элементами всплывающих уведомлений")
    @allure.title("Проверка открытия окна ввода результата")
    @allure.description("Проверка открытия окна ввода результата")
    @allure.severity(allure.severity_level.MINOR)
    def test_prompt(self, controller):
        test_name = "test name"

        def handle_prompt(dialog):
            controller.helper.is_eq(dialog.type, "prompt")
            controller.helper.is_eq(dialog.message, "Please enter your name")
            print(dialog.message)
            dialog.accept(test_name)

        with allure.step('Открыть страницу всплывающих уведомлений'):
            controller.alerts_page.navigate()
        with allure.step('Нажать на кнопку и проверить содержимое окна подтверждения'):
            controller.alerts_page.page.on("dialog", handle_prompt)
            controller.alerts_page.click(controller.alerts_page.prompt_btn)
            controller.alerts_page.page.remove_listener("dialog", handle_prompt)
        with allure.step('Проверить содержимое строки результата в зависимости от введенного результата'):
            controller.helper.to_contain_text(controller.alerts_page.prompt_result, test_name)
