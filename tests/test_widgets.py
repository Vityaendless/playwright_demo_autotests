import time

import allure
import pytest

from auxiliary.constants import TAB_CLASSES, HTMLAttr


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

    @pytest.mark.skip
    @allure.feature("Раздел полей авто подбора информации")
    @allure.story("Ввод информации в поля автоподбора")
    @allure.title("Проверить ввод информации в поля автоподбора")
    @allure.description("Проверить ввод информации в поля автоподбора")
    @allure.severity(allure.severity_level.NORMAL)
    def test_auto_complete(self, controller, colors_data):
        with allure.step('Открыть страницу полей автоподбора'):
            controller.auto_complete_page.navigate()
        with allure.step('Ввод информации в поля множественного ввода данных'):
            for color in colors_data:
                controller.auto_complete_page.type(controller.auto_complete_page.multiple_input, color)
                controller.auto_complete_page.press(controller.auto_complete_page.multiple_input)
        with allure.step('Сравнить кол-во введенных элементов'):
            controller.helper.is_eq(
                controller.auto_complete_page.count(controller.auto_complete_page.colors), len(colors_data)
            )
        with allure.step('Удалить последний выбранный элемент'):
            last_color = controller.auto_complete_page.last(controller.auto_complete_page.remove_color_btn)
            last_color.click()
        with allure.step('Сравнить кол-во введенных элементов'):
            controller.helper.is_eq(
                controller.auto_complete_page.count(controller.auto_complete_page.colors), len(colors_data) - 1
            )
        with allure.step('Очистить поле'):
            controller.auto_complete_page.click(controller.auto_complete_page.clear_btn)
        with allure.step('Сравнить кол-во введенных элементов'):
            controller.helper.is_eq(controller.auto_complete_page.count(controller.auto_complete_page.colors), 0)
        with allure.step('Ввод информации в поле одиночного ввода данных'):
            black = "Black"
            controller.auto_complete_page.type(controller.auto_complete_page.single_input, black)
            controller.auto_complete_page.press(controller.auto_complete_page.single_input)
        with allure.step('Проверить эквивалентность введенного значения'):
            controller.helper.to_contain_text(controller.auto_complete_page.single_input_value, black)

    @pytest.mark.skip
    @allure.feature("Раздел полей выбора дат, времени")
    @allure.story("Ввод информации в поля дат, времени")
    @allure.title("Проверить ввод информации в поля дат, времени")
    @allure.description("Проверить ввод информации в поля дат, времени")
    @allure.severity(allure.severity_level.NORMAL)
    def test_date_picker(self, controller):
        with allure.step('Открыть страницу полей дат, времени'):
            controller.date_picker_page.navigate()
        with allure.step('Ввод информации в поле выбора даты'):
            controller.date_picker_page.click(controller.date_picker_page.select_date)
            controller.date_picker_page.select_option(controller.date_picker_page.select_month, "4")
            controller.date_picker_page.select_option(controller.date_picker_page.select_year, "2027")
            controller.date_picker_page.click(controller.date_picker_page.day_14)
        with allure.step('Сравнить выбранную дату с требуемой'):
            controller.helper.to_have_attribute(controller.date_picker_page.select_date, HTMLAttr.VALUE, "05/14/2027")
        with allure.step('Ввод информации в поле выбора даты и времени'):
            controller.date_picker_page.click(controller.date_picker_page.select_time_date)
            controller.date_picker_page.click(controller.date_picker_page.select_month_dt)
            controller.date_picker_page.page.get_by_text("May").click()
            controller.date_picker_page.click(controller.date_picker_page.select_year_dt)
            controller.date_picker_page.page.get_by_text("2027").click()
            controller.date_picker_page.click(controller.date_picker_page.day_14)
            controller.date_picker_page.page.get_by_text("16:45").click()
        with allure.step('Сравнить выбранную дату с требуемой'):
            controller.helper.to_have_attribute(
                controller.date_picker_page.select_time_date, HTMLAttr.VALUE, "May 14, 2027 4:45 PM"
            )

    @pytest.mark.skip
    @allure.feature("Раздел слайдера")
    @allure.story("Взаимодействие со слайдером")
    @allure.title("Проверить отображение изменения значения при взаимодействии со слайдером")
    @allure.description("Проверить отображение изменения значения при взаимодействии со слайдером")
    @allure.severity(allure.severity_level.NORMAL)
    def test_slider(self, controller):
        slider_amount = "58"
        with allure.step('Открыть страницу слайдера'):
            controller.slider_page.navigate()
        with allure.step('Проверка значения слайдера по умолчанию'):
            controller.helper.to_have_attribute(controller.slider_page.slider_value, HTMLAttr.VALUE, "25")
        with allure.step('Изменить значение слайдера'):
            controller.slider_page.click(controller.slider_page.slider, position={"x": 250, "y": 0})
        with allure.step('Проверка изменение значения после взаимодействия со слайдером'):
            controller.helper.to_have_attribute(controller.slider_page.slider_value, HTMLAttr.VALUE, slider_amount)

    @pytest.mark.skip
    @allure.feature("Раздел прогресс-бара")
    @allure.story("Взаимодействие с элементами прогресс-бара")
    @allure.title("Проверить взаимодействие с прогресс-баром")
    @allure.description("Проверить отображение изменения значения при взаимодействием с прогресс-баром")
    @allure.severity(allure.severity_level.NORMAL)
    def test_progress_bar(self, controller):
        with allure.step('Открыть страницу прогресс-бара'):
            controller.progress_bar.navigate()
        with allure.step('Проверка начальных значений элементов'):
            controller.progress_bar.check_default_state()
        with allure.step('Нажать кнопку Start и ожидаем заполнение прогресс-бара'):
            controller.progress_bar.click(controller.progress_bar.start_btn)
            controller.helper.to_contain_text(controller.progress_bar.progress_bar, "100%", timeout=10000)
            controller.helper.to_contain_text(controller.progress_bar.reset_btn, "Reset", timeout=10000)
            controller.helper.not_to_be_visible(controller.progress_bar.start_btn, timeout=10000)
        with allure.step('Нажать кнопку Reset и проверить сброс прогресс-бара'):
            controller.progress_bar.click(controller.progress_bar.reset_btn)
            controller.progress_bar.check_default_state()

    #@pytest.mark.skip
    @allure.feature("Раздел тул-типов")
    @allure.story("Взаимодействие с элементами тул-типов")
    @allure.title("Проверить взаимодействие с туд-типами")
    @allure.description(
        "Проверить отображение изменения значения при взаимодействием с элементами связанными с тул-типом"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_tool_tip(self, controller, tool_tips_data):
        with allure.step('Открыть страницу тул-типов'):
            controller.tool_tip_page.navigate()
        with allure.step('Проверка, что изначально тул-тип не отображается'):
            controller.helper.not_to_be_visible(controller.tool_tip_page.btn_tt)
            controller.helper.not_to_be_visible(controller.tool_tip_page.field_tt)
            controller.helper.not_to_be_visible(controller.tool_tip_page.first_link_tt)
            controller.helper.not_to_be_visible(controller.tool_tip_page.second_link_tt)
        with allure.step('Навести курсор на кнопку и проверить наличие тул-типа и информации в нем'):
            controller.tool_tip_page.check_tool_tip(
                controller.tool_tip_page.btn, controller.tool_tip_page.btn_tt, tool_tips_data[0]
            )
        with allure.step('Навести курсор на поле ввода и проверить наличие тул-типа и информации в нем'):
            controller.tool_tip_page.check_tool_tip(
                controller.tool_tip_page.field, controller.tool_tip_page.field_tt, tool_tips_data[1]
            )
        with allure.step('Навести курсор на ссылку и проверить наличие тул-типа и информации в нем'):
            controller.tool_tip_page.check_tool_tip(
                controller.tool_tip_page.first_link, controller.tool_tip_page.first_link_tt, tool_tips_data[2]
            )
        with allure.step('Навести курсор на кнопку и проверить наличие тул-типа и информации в нем'):
            controller.tool_tip_page.check_tool_tip(
                controller.tool_tip_page.second_link, controller.tool_tip_page.second_link_tt, tool_tips_data[3]
            )
