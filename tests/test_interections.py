import random
import time
import allure
import pytest


@allure.epic("Тесты взаимодейстий между элементами")
class TestInteractions:

    @pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Перемещение элементов в списке")
    @allure.description("Перемещение одного элемента к другому")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sortable_list(self, controller):
        with allure.step('Открыть страницу перемещения элементов'):
            controller.sortable_page.navigate()
        with allure.step('Перенести первый элемент к последнему и проверить, что элемент перенесен'):
            first_el_text = controller.sortable_page.get_element_text(controller.sortable_page.first_el)
            controller.sortable_page.drag_drop(controller.sortable_page.first_el, controller.sortable_page.second_el)
            last_el_new_text = controller.sortable_page.get_element_text(controller.sortable_page.second_el)
            controller.helper.is_eq(first_el_text, last_el_new_text)

    @pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Перемещение элементов в гриде")
    @allure.description("Перемещение одного элемента к другому")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sortable_grid(self, controller):
        with allure.step('Открыть страницу перемещения элементов'):
            controller.sortable_page.navigate()
        with allure.step('Открыть вкладку грида'):
            controller.sortable_page.click(controller.sortable_page.to_grid)
        with allure.step('Перенести первый элемент к последнему и проверить, что элемент перенесен'):
            first_el_text = controller.sortable_page.get_element_text(controller.sortable_page.first_el_grid)
            controller.sortable_page.drag_drop(
                controller.sortable_page.first_el_grid, controller.sortable_page.second_el_grid
            )
            last_el_new_text = controller.sortable_page.get_element_text(controller.sortable_page.second_el_grid)
            controller.helper.is_eq(first_el_text, last_el_new_text)

    #@pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Выбор элементов в списке")
    @allure.description("Выбор элементов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_selectable_list(self, controller):
        with allure.step('Открыть страницу выбора элементов'):
            controller.selectable_page.navigate()
        with allure.step('Выбрать рандомный элемент'):
            els_count = controller.selectable_page.count(controller.selectable_page.list_els)
            random_number = random.randint(0, els_count - 1)
        with allure.step('Получить все элементы'):
            list_els = controller.selectable_page.all_els(controller.selectable_page.list_els)
        with allure.step('Проверить, что элементы не выбраны и сделать клик по рандомному элементу'):
            controller.selectable_page.check_not_active(list_els, random_number)
        with allure.step('Проверить, что рандомный элемент выбран'):
            controller.selectable_page.check_active(list_els, random_number)


    #@pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Выбор элементов в гриде")
    @allure.description("Выбор элементов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_selectable_grid(self, controller):
        with allure.step('Открыть страницу выбора элементов'):
            controller.selectable_page.navigate()
        with allure.step('Открыть вкладку грида'):
            controller.selectable_page.click(controller.selectable_page.to_grid)
        with allure.step('Выбрать рандомный элемент'):
            els_count = controller.selectable_page.count(controller.selectable_page.grid_els)
            random_number = random.randint(0, els_count - 1)
        with allure.step('Получить все элементы'):
            grid_els = controller.selectable_page.all_els(controller.selectable_page.grid_els)
        with allure.step('Проверить, что элементы не выбраны и сделать клик по рандомному элементу'):
            controller.selectable_page.check_not_active(grid_els, random_number)
        with allure.step('Проверить, что рандомный элемент выбран'):
            controller.selectable_page.check_active(grid_els, random_number)
