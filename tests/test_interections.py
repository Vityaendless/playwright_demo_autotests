import random
import time
import allure
import pytest

from auxiliary.constants import HTMLAttr


@allure.epic("Тесты взаимодейстий между элементами")
class TestInteractions:
    DEFAULT_POSITION = "position: relative;"

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

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Drag'n'drop с вложенностью элементов")
    @allure.description("Drag'n'drop с вложенностью элементов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_prevent_propogation_drag_n_drop(self, controller, drag_n_drop_info):
        with allure.step('Открыть страницу Drag\'n\'drop'):
            controller.droppable_page.navigate()
        with allure.step('Перейти на вкладку Prevent Propogation Drag\'n\'drop'):
            controller.droppable_page.click(controller.droppable_page.pr_pr_tab)
        with allure.step('Сделать not greedy drag n drop и проверить что он отработал для родителя'):
            controller.helper.to_contain_text(controller.droppable_page.not_greedy_out_drop, drag_n_drop_info[2])
            controller.helper.to_contain_text(
                controller.droppable_page.not_greedy_inner_drop, "Inner droppable (not greedy)"
            )
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.pr_pr_draggable,
                controller.droppable_page.not_greedy_inner_drop
            )
            controller.helper.to_contain_text(controller.droppable_page.not_greedy_out_drop, drag_n_drop_info[1])
            controller.helper.to_contain_text(controller.droppable_page.not_greedy_inner_drop, drag_n_drop_info[1])
        with allure.step('Сделать greedy drag n drop и проверить что он НЕ отработал для родителя'):
            controller.helper.to_contain_text(controller.droppable_page.greedy_out_drop, drag_n_drop_info[2])
            controller.helper.to_contain_text(
                controller.droppable_page.greedy_inner_drop, "Inner droppable (greedy)"
            )
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.pr_pr_draggable,
                controller.droppable_page.greedy_inner_drop
            )
            controller.helper.to_contain_text(controller.droppable_page.greedy_out_drop, drag_n_drop_info[2])
            controller.helper.to_contain_text(controller.droppable_page.greedy_inner_drop, drag_n_drop_info[1])

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Drag'n'drop с отменой действия")
    @allure.description("Drag'n'drop с отменой действия")
    @allure.severity(allure.severity_level.NORMAL)
    def test_revert_drag_n_drop(self, controller, drag_n_drop_info):
        DEFAULT_POSITION = "position: relative; left: 0px; top: 0px;"
        with allure.step('Открыть страницу Drag\'n\'drop'):
            controller.droppable_page.navigate()
        with allure.step('Перейти на вкладку Revert Drag\'n\'drop'):
            controller.droppable_page.click(controller.droppable_page.revert_tab)
        with allure.step('Сделать drag n drop и проверить что он отработал с отменой'):
            controller.helper.to_contain_text(controller.droppable_page.revert_droppable, drag_n_drop_info[0])
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.revertable,
                controller.droppable_page.revert_droppable
            )
            controller.helper.to_contain_text(controller.droppable_page.revert_droppable, drag_n_drop_info[1])
            time.sleep(1)
            style = controller.droppable_page.get_attr(controller.droppable_page.revertable, HTMLAttr.STYLE)
            controller.helper.is_eq(style, DEFAULT_POSITION)
        with allure.step('Перезагрузить страницу и перейти на вкладку Revert Drag\'n\'drop'):
            controller.droppable_page.page.reload()
            controller.droppable_page.click(controller.droppable_page.revert_tab)
            time.sleep(1)
        with allure.step('Сделать drag n drop и проверить что он отработал без отменой'):
            controller.helper.to_contain_text(controller.droppable_page.revert_droppable, drag_n_drop_info[0])
            controller.droppable_page.drag_n_drop(
                controller.droppable_page.not_revertable,
                controller.droppable_page.revert_droppable
            )
            controller.helper.to_contain_text(controller.droppable_page.revert_droppable, drag_n_drop_info[1])
            time.sleep(1)
            style = controller.droppable_page.get_attr(controller.droppable_page.not_revertable, HTMLAttr.STYLE)
            controller.helper.is_not_eq(style, DEFAULT_POSITION)

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Перемещение элемента")
    @allure.description("Перемещение элемента относительно текущего положения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_simple_drag(self, controller):
        with allure.step('Открыть страницу Draggable'):
            controller.draggable_page.navigate()
        with allure.step('Сделать drag и проверить что он отработал'):
            controller.helper.to_have_css(controller.draggable_page.simple_drag_box, "position", "relative")
            default_style = controller.draggable_page.get_attr(
                controller.draggable_page.simple_drag_box, HTMLAttr.STYLE
            )
            controller.helper.is_eq(default_style, TestInteractions.DEFAULT_POSITION)
            controller.draggable_page.drag(controller.draggable_page.simple_drag_box, 150, 120)
            style = controller.draggable_page.get_attr(controller.draggable_page.simple_drag_box, "style")
            print(style)
            controller.helper.to_have_css(controller.draggable_page.simple_drag_box, "left", "100px")
            controller.helper.to_have_css(controller.draggable_page.simple_drag_box, "top", "100px")

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Перемещение элемента")
    @allure.description("Перемещение элементов по какой-то отдельной оси")
    @allure.severity(allure.severity_level.NORMAL)
    def test_asix_drag(self, controller):
        with allure.step('Открыть страницу Draggable'):
            controller.draggable_page.navigate()
        with allure.step('Перейти на вкладку Axis Drag'):
            controller.draggable_page.click(controller.draggable_page.axis_tab)
        with allure.step('Сделать drag и проверить что он отработал только по определенной оси'):
            controller.helper.to_have_css(controller.draggable_page.only_x_drag, "position", "relative")
            controller.helper.to_have_css(controller.draggable_page.only_y_drag, "position", "relative")
            default_style_only_x = controller.draggable_page.get_attr(
                controller.draggable_page.only_x_drag, HTMLAttr.STYLE
            )
            controller.helper.is_eq(default_style_only_x, TestInteractions.DEFAULT_POSITION)
            default_style_only_y = controller.draggable_page.get_attr(
                controller.draggable_page.only_y_drag, HTMLAttr.STYLE
            )
            controller.helper.is_eq(default_style_only_y, TestInteractions.DEFAULT_POSITION)
            controller.draggable_page.drag(controller.draggable_page.only_x_drag, 150, 120)
            only_x_style = controller.draggable_page.get_attr(controller.draggable_page.only_x_drag, "style")
            print(only_x_style)
            controller.draggable_page.drag(controller.draggable_page.only_y_drag, 150, 120)
            only_y_style = controller.draggable_page.get_attr(controller.draggable_page.only_y_drag, "style")
            print(only_y_style)
            controller.helper.to_have_css(controller.draggable_page.only_x_drag, "left", "100px")
            controller.helper.to_have_css(controller.draggable_page.only_x_drag, "top", "0px")
            controller.helper.to_have_css(controller.draggable_page.only_y_drag, "left", "0px")
            controller.helper.to_have_css(controller.draggable_page.only_y_drag, "top", "100px")

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Перемещение элемента")
    @allure.description("Перемещение элементов внутри контейнера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_container_drag(self, controller):
        with allure.step('Открыть страницу Draggable'):
            controller.draggable_page.navigate()
        with allure.step('Перейти на вкладку Contsiner Drag'):
            controller.draggable_page.click(controller.draggable_page.container_tab)
        with allure.step('Сделать drag и проверить что он отработал только внутри контейнера'):
            controller.helper.to_have_css(controller.draggable_page.drag_in_container, "position", "relative")
            controller.helper.to_have_css(controller.draggable_page.drag_span, "position", "relative")
            default_style_in_container = controller.draggable_page.get_attr(
                controller.draggable_page.drag_in_container, HTMLAttr.STYLE
            )
            controller.helper.is_eq(default_style_in_container, TestInteractions.DEFAULT_POSITION)
            default_span_style = controller.draggable_page.get_attr(
                controller.draggable_page.drag_span, HTMLAttr.STYLE
            )
            controller.helper.is_eq(default_span_style, TestInteractions.DEFAULT_POSITION)
            el_params_container = controller.draggable_page.bounding_box(controller.draggable_page.container)
            el_params_draggable_container = controller.draggable_page.bounding_box(
                controller.draggable_page.draggable_container
            )
            print(el_params_container)
            print(el_params_draggable_container)
            controller.draggable_page.drag(
                controller.draggable_page.drag_in_container, el_params_container['width'], el_params_container['height']
            )
            drag_in_container_style = controller.draggable_page.get_attr(
                controller.draggable_page.drag_in_container, "style"
            )
            print(drag_in_container_style)
            controller.draggable_page.hover(controller.draggable_page.draggable_container)
            controller.draggable_page.drag(
                controller.draggable_page.drag_span,
                el_params_draggable_container['width'],
                el_params_draggable_container['height']
            )
            drag_span_style = controller.draggable_page.get_attr(controller.draggable_page.drag_span, "style")
            print(drag_span_style)

    @allure.feature("Взаимодействие элементов")
    @allure.story("Взаимодействие между различными элементами")
    @allure.title("Положение курсора")
    @allure.description("Положение курсора относительно перемещаемого элемента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cursor_position(self, controller):
        with allure.step('Открыть страницу Draggable'):
            controller.draggable_page.navigate()
        with allure.step('Перейти на вкладку Cursor Position'):
            controller.draggable_page.click(controller.draggable_page.cursor_style_tab)
        with allure.step('Сделать drag и проверить что он отработал только внутри контейнера'):
            controller.draggable_page.page.evaluate("var x; var y;"
                                                    "document.addEventListener('mousemove', mousePosition);"
                                                    "function mousePosition(e) {"
                                                    "x = e.clientX;"
                                                    "y = e.clientY;"
                                                    "console.log(x);"
                                                    "console.log(y);"
                                                    "}")
            controller.draggable_page.get_cursor_position_while_moving(
                controller.draggable_page.cursor_center, 350, 150
            )
            controller.draggable_page.get_cursor_position_while_moving(
                controller.draggable_page.cursor_top_left, 50, 150
            )
            controller.draggable_page.get_cursor_position_while_moving(
                controller.draggable_page.cursor_bottom, 150, 150
            )
