import allure

from auxiliary.constants import TAB_CLASSES


@allure.epic("Тесты виджетов")
class TestWidgets:

    @allure.feature("Раздел вкладок с информацией")
    @allure.story("Разбиение информации по вкладкам")
    @allure.title("Проверка доступности вкладок")
    @allure.description("Проверка переключения между вкладками и соотвествия отображемой этим вкладкам информации")
    @allure.severity(allure.severity_level.MINOR)
    def test_tabs(self, controller):
        with allure.step('Открыть страницу вкладок'):
            controller.tabs_page.navigate()
        with allure.step('Проверить активность вкладки WHAT'):
            controller.tabs_page.is_class_contain(controller.tabs_page.what_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.origin_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.use_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_tab, TAB_CLASSES[0])
        with allure.step('Проверить активность контента WHAT'):
            controller.tabs_page.is_class_contain(controller.tabs_page.what_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.origin_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.use_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_content, TAB_CLASSES[1])
            controller.helper.to_be_visible(controller.tabs_page.what_content)
            controller.helper.not_to_be_visible(controller.tabs_page.origin_content)
            controller.helper.not_to_be_visible(controller.tabs_page.use_content)
            controller.helper.not_to_be_visible(controller.tabs_page.more_content)
        with allure.step('Нажать на вкладку ORIGIN'):
            controller.tabs_page.click(controller.tabs_page.origin_tab)
        with allure.step('Проверить активность вкладки ORIGIN'):
            controller.tabs_page.is_class_contain(controller.tabs_page.origin_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.what_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.use_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_tab, TAB_CLASSES[0])
        with allure.step('Проверить активность контента ORIGIN'):
            controller.tabs_page.is_class_contain(controller.tabs_page.origin_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.what_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.use_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_content, TAB_CLASSES[1])
            controller.helper.to_be_visible(controller.tabs_page.origin_content)
            controller.helper.not_to_be_visible(controller.tabs_page.what_content)
            controller.helper.not_to_be_visible(controller.tabs_page.use_content)
            controller.helper.not_to_be_visible(controller.tabs_page.more_content)
        with allure.step('Нажать на вкладку USE'):
            controller.tabs_page.click(controller.tabs_page.use_tab)
        with allure.step('Проверить активность вкладки USE'):
            controller.tabs_page.is_class_contain(controller.tabs_page.use_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.what_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.origin_tab, TAB_CLASSES[0])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_tab, TAB_CLASSES[0])
        with allure.step('Проверить активность контента USE'):
            controller.tabs_page.is_class_contain(controller.tabs_page.use_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.what_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.origin_content, TAB_CLASSES[1])
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_content, TAB_CLASSES[1])
            controller.helper.to_be_visible(controller.tabs_page.use_content)
            controller.helper.not_to_be_visible(controller.tabs_page.what_content)
            controller.helper.not_to_be_visible(controller.tabs_page.origin_content)
            controller.helper.not_to_be_visible(controller.tabs_page.more_content)
        with allure.step('Проверить, что вкладка MORE неактивна и контент не отображается'):
            controller.tabs_page.is_not_class_contain(controller.tabs_page.more_tab, TAB_CLASSES[0])
            controller.tabs_page.is_class_contain(controller.tabs_page.more_tab, TAB_CLASSES[2])
            controller.helper.not_to_be_visible(controller.tabs_page.more_content)
            assert controller.tabs_page.is_not_clickable(controller.tabs_page.more_tab), f"[{controller.tabs_page.more_tab['title']}] is clickable"
