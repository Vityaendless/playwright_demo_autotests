import allure
import pytest

from auxiliary.constants import TAB_CLASSES


@allure.epic("Тесты виджетов")
class TestWidgets:

    @pytest.mark.skip
    @allure.feature("Раздел аккордеона")
    @allure.story("Разбиение информации по разделам аккордеона")
    @allure.title("Проверка доступности разделов аккордеона")
    @allure.description("Проверка переключения между разделами аккордеона")
    @allure.severity(allure.severity_level.MINOR)
    def test_accordian(self, controller):
        with allure.step('Открыть страницу аккордеона'):
            controller.accordian_page.navigate()
        with allure.step('Проверить доступность заголовков аккордеона'):
            controller.helper.to_be_visible(controller.accordian_page.section1_heading)
            controller.helper.to_be_enabled(controller.accordian_page.section1_heading)
            controller.helper.to_be_visible(controller.accordian_page.section2_heading)
            controller.helper.to_be_enabled(controller.accordian_page.section2_heading)
            controller.helper.to_be_visible(controller.accordian_page.section3_heading)
            controller.helper.to_be_enabled(controller.accordian_page.section3_heading)
        with allure.step('Проверить доступность содержимого первой вкладки аккордеона'):
            controller.helper.to_be_visible(controller.accordian_page.section1_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section2_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section3_content)
        with allure.step('Сделать клик по первой вкладке аккордеона'):
            controller.accordian_page.click(controller.accordian_page.section1_heading)
        with allure.step('Проверить недоступность всего контента'):
            controller.helper.not_to_be_visible(controller.accordian_page.section1_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section2_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section3_content)
        with allure.step('Сделать клик по второй вкладке аккордеона'):
            controller.accordian_page.click(controller.accordian_page.section2_heading)
        with allure.step('Проверить доступность второй вкладки контента'):
            controller.helper.not_to_be_visible(controller.accordian_page.section1_content)
            controller.helper.to_be_visible(controller.accordian_page.section2_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section3_content)
        with allure.step('Сделать клик по третьей вкладке аккордеона'):
            controller.accordian_page.click(controller.accordian_page.section3_heading)
        with allure.step('Проверить доступность третьей вкладки контента'):
            controller.helper.not_to_be_visible(controller.accordian_page.section1_content)
            controller.helper.not_to_be_visible(controller.accordian_page.section2_content)
            controller.helper.to_be_visible(controller.accordian_page.section3_content)


    @pytest.mark.skip
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
