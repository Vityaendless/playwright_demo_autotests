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

    @pytest.mark.skip
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


    @pytest.mark.skip
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

    @pytest.mark.skip
    @pytest.mark.parametrize("coord", [(-55, -55), (310, 110), (100, 50)])
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Изменение размера элементов")
    @allure.description("Изменение размера элементов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_resizable(self, controller, coord):
        with allure.step('Открыть страницу изменения размера элементов'):
            controller.resizable_page.navigate()
        with allure.step('Изменить размер элемента'):
            height = controller.resizable_page.get_el_height(controller.resizable_page.resizable_box)
            width = controller.resizable_page.get_el_height(controller.resizable_page.resizable_box)
            print(height, width)
            controller.resizable_page.hover(
                controller.resizable_page.container, position={"x": width+50, "y": height+50}
            )
            time.sleep(2)
            el_params = controller.resizable_page.bounding_box(controller.resizable_page.resizable_box)
            print(el_params)
            bottom_right_x = el_params['x'] + el_params['width']
            bottom_right_y = el_params['y'] + el_params['height']
            print(bottom_right_x, bottom_right_y)
            controller.resizable_page.move(bottom_right_x-4, bottom_right_y-4)
            time.sleep(2)
            controller.resizable_page.down()
            time.sleep(2)
            print(coord[0], coord[1])
            controller.resizable_page.move(bottom_right_x+coord[0], bottom_right_y+coord[1])
            time.sleep(2)
            controller.resizable_page.up()
            style = controller.resizable_page.get_attr(controller.resizable_page.resizable_box, "style")
            print(style)

    @pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Простой Drag'n'drop")
    @allure.description("Простой Drag'n'drop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_simple_drag_n_drop(self, controller, drag_n_drop_info):
        with allure.step('Открыть страницу Drag\'n\'drop'):
            controller.droppable_page.navigate()
        with allure.step('Сделать drag n drop и проверить что он произошел'):
            controller.helper.to_contain_text(controller.droppable_page.simple_droppable, drag_n_drop_info[0])
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.simple_draggable, controller.droppable_page.simple_droppable
            )
            controller.helper.to_contain_text(controller.droppable_page.simple_droppable, drag_n_drop_info[1])

    #@pytest.mark.skip
    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Drag'n'drop с подтверждением")
    @allure.description("Drag'n'drop с подтверждением")
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_drag_n_drop(self, controller, drag_n_drop_info):
        with allure.step('Открыть страницу Drag\'n\'drop'):
            controller.droppable_page.navigate()
        with allure.step('Перейти на вкладку Accept Drag\'n\'drop'):
            controller.droppable_page.click(controller.droppable_page.accept_tab)
        with allure.step('Сделать not acceptable drag n drop и проверить что он НЕ произошел'):
            controller.helper.to_contain_text(controller.droppable_page.accept_droppable, drag_n_drop_info[0])
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.not_acceptable,
                controller.droppable_page.accept_droppable,
                target_position={"x": 30, "y": 30}
            )
            controller.helper.to_contain_text(controller.droppable_page.accept_droppable, drag_n_drop_info[0])
        with allure.step('Получить размеры droppable элемента'):
            el_params = controller.droppable_page.bounding_box(controller.droppable_page.accept_droppable)
            print(el_params)
        with allure.step('Сделать acceptable drag n drop и проверить что он произошел'):
            controller.helper.to_contain_text(controller.droppable_page.accept_droppable, drag_n_drop_info[0])
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.acceptable,
                controller.droppable_page.accept_droppable,
                target_position={"x": int(el_params['width']) - 30, "y": int(el_params['height']) - 30}
            )
            controller.helper.to_contain_text(controller.droppable_page.accept_droppable, drag_n_drop_info[1])
