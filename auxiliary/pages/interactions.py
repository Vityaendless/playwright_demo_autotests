from .base import BasePage
from auxiliary.url_path import UrlPaths
from auxiliary.constants import HTMLAttr, HTMLValue
from auxiliary.helper import Helper
from auxiliary.locators import (SortablePageLocator as SortablePL, SelectablePageLocator as SelectPL,
                                ResizablePageLocator as ResizablePL, DropPageLocator as DropPL,
                                DraggablePageLocator as DragPL)


class SortablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().sortable
        self.first_el = {
            'title': 'first_el',
            'locator': self.page.locator(SortablePL.FIRST_EL),
            'selector': SortablePL.FIRST_EL
        }
        self.second_el = {
            'title': 'second_el',
            'locator': self.page.locator(SortablePL.SECOND_EL),
            'selector': SortablePL.SECOND_EL
        }
        self.to_grid = {
            'title': 'to_grid',
            'locator': self.page.locator(SortablePL.TO_GRID),
            'selector': SortablePL.TO_GRID
        }
        self.first_el_grid = {
            'title': 'first_el_grid',
            'locator': self.page.locator(SortablePL.FIRST_EL_GRID),
            'selector': SortablePL.FIRST_EL_GRID
        }
        self.second_el_grid = {
            'title': 'second_el_grid',
            'locator': self.page.locator(SortablePL.SECOND_EL_GRID),
            'selector': SortablePL.SECOND_EL_GRID
        }


class SelectablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().selectable
        self.list_els = {
            'title': 'list_els',
            'locator': self.page.locator(SelectPL.LIST_ELS),
            'selector': SelectPL.LIST_ELS
        }
        self.grid_els = {
            'title': 'grid_els',
            'locator': self.page.locator(SelectPL.GRID_ELS),
            'selector': SelectPL.GRID_ELS
        }
        self.to_grid = {
            'title': 'to_grid',
            'locator': self.page.locator(SelectPL.TO_GRID),
            'selector': SelectPL.TO_GRID
        }

    @staticmethod
    def check_not_active(els, el_amount):
        for i, el in enumerate(els):
            cls = el.get_attribute(HTMLAttr.CLASS)
            Helper.is_not_in(HTMLValue.ACTIVE, cls)
            if el_amount == i:
                el.click()

    @staticmethod
    def check_active(els, el_amount):
        for i, el in enumerate(els):
            if el_amount == i:
                cls = el.get_attribute(HTMLAttr.CLASS)
                Helper.is_in(HTMLValue.ACTIVE, cls)


class ResizablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().resizable
        self.resizable_box = {
            'title': 'resizable_box',
            'locator': self.page.locator(ResizablePL.RESIZABLE_BOX),
            'selector': ResizablePL.RESIZABLE_BOX
        }
        self.container = {
            'title': 'container',
            'locator': self.page.locator(ResizablePL.CONTAINER),
            'selector': ResizablePL.CONTAINER
        }
        self.resizable = {
            'title': 'resizable',
            'locator': self.page.locator(ResizablePL.RESIZABLE),
            'selector': ResizablePL.RESIZABLE
        }


class DroppablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().droppable
        self.simple_draggable = {
            'title': 'simple_draggable',
            'locator': self.page.locator(DropPL.SIMPLE_DRAGGABLE),
            'selector': DropPL.SIMPLE_DRAGGABLE
        }
        self.simple_droppable = {
            'title': 'simple_droppable',
            'locator': self.page.locator(DropPL.SIMPLE_DROPPABLE),
            'selector': DropPL.SIMPLE_DROPPABLE
        }
        self.accept_tab = {
            'title': 'accept_tab',
            'locator': self.page.locator(DropPL.ACCEPT_TAB),
            'selector': DropPL.ACCEPT_TAB
        }
        self.acceptable = {
            'title': 'acceptable',
            'locator': self.page.locator(DropPL.ACCEPTABLE),
            'selector': DropPL.ACCEPTABLE
        }
        self.not_acceptable = {
            'title': 'not_acceptable',
            'locator': self.page.locator(DropPL.NOT_ACCEPTABLE),
            'selector': DropPL.NOT_ACCEPTABLE
        }
        self.accept_droppable = {
            'title': 'accept_droppable',
            'locator': self.page.locator(DropPL.ACCEPT_DROPPABLE),
            'selector': DropPL.ACCEPT_DROPPABLE
        }
        self.pr_pr_tab = {
            'title': 'pr_pr_tab',
            'locator': self.page.locator(DropPL.PREVENT_PROPOGATION_TAB),
            'selector': DropPL.PREVENT_PROPOGATION_TAB
        }
        self.pr_pr_draggable = {
            'title': 'pr_pr_draggable',
            'locator': self.page.locator(DropPL.PR_PR_DRAGGABLE),
            'selector': DropPL.PR_PR_DRAGGABLE
        }
        self.not_greedy_out_drop = {
            'title': 'not_greedy_out_drop',
            'locator': self.page.locator(DropPL.NOT_GREEDY_OUT_DROP),
            'selector': DropPL.NOT_GREEDY_OUT_DROP
        }
        self.not_greedy_inner_drop = {
            'title': 'not_greedy_inner_drop',
            'locator': self.page.locator(DropPL.NOT_GREEDY_INNER_DROP),
            'selector': DropPL.NOT_GREEDY_INNER_DROP
        }
        self.greedy_out_drop = {
            'title': 'greedy_out_drop',
            'locator': self.page.locator(DropPL.GREEDY_OUT_DROP),
            'selector': DropPL.GREEDY_OUT_DROP
        }
        self.greedy_inner_drop = {
            'title': 'greedy_inner_drop',
            'locator': self.page.locator(DropPL.GREEDY_INNER_DROP),
            'selector': DropPL.GREEDY_INNER_DROP
        }
        self.revert_tab = {
            'title': 'revert_tab',
            'locator': self.page.locator(DropPL.REVERT_TAB),
            'selector': DropPL.REVERT_TAB
        }
        self.revertable = {
            'title': 'revertable',
            'locator': self.page.locator(DropPL.REVERTABLE),
            'selector': DropPL.REVERTABLE
        }
        self.not_revertable = {
            'title': 'not_revertable',
            'locator': self.page.locator(DropPL.NOT_REVERTABLE),
            'selector': DropPL.NOT_REVERTABLE
        }
        self.revert_droppable = {
            'title': 'revert_droppable',
            'locator': self.page.locator(DropPL.REVERT_DROPPABLE),
            'selector': DropPL.REVERT_DROPPABLE
        }


class DraggablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = UrlPaths().dragabble
        self.simple_drag_box = {
            'title': 'simple_drag_box',
            'locator': self.page.locator(DragPL.SIMPLE_DRAG_BOX),
            'selector': DragPL.SIMPLE_DRAG_BOX
        }
        self.axis_tab = {
            'title': 'axis_tab',
            'locator': self.page.locator(DragPL.AXIS_TAB),
            'selector': DragPL.AXIS_TAB
        }
        self.only_x_drag = {
            'title': 'only_x_drag',
            'locator': self.page.locator(DragPL.ONLY_X_DRAG),
            'selector': DragPL.ONLY_X_DRAG
        }
        self.only_y_drag = {
            'title': 'only_y_drag',
            'locator': self.page.locator(DragPL.ONLY_Y_DRAG),
            'selector': DragPL.ONLY_Y_DRAG
        }
        self.container_tab = {
            'title': 'container_tab',
            'locator': self.page.locator(DragPL.CONTAINER_TAB),
            'selector': DragPL.CONTAINER_TAB
        }
        self.container = {
            'title': 'container',
            'locator': self.page.locator(DragPL.CONTAINER),
            'selector': DragPL.CONTAINER
        }
        self.drag_in_container = {
            'title': 'drag_in_container',
            'locator': self.page.locator(DragPL.DRAG_IN_CONTAINER),
            'selector': DragPL.DRAG_IN_CONTAINER
        }
        self.draggable_container = {
            'title': 'draggable_container',
            'locator': self.page.locator(DragPL.DRAGGABLE_CONTAINER),
            'selector': DragPL.DRAGGABLE_CONTAINER
        }
        self.drag_span = {
            'title': 'drag_span',
            'locator': self.page.locator(DragPL.DRAG_SPAN),
            'selector': DragPL.DRAG_SPAN
        }
        self.cursor_style_tab = {
            'title': 'cursor_style_tab',
            'locator': self.page.locator(DragPL.CURSOR_STYLE_TAB),
            'selector': DragPL.CURSOR_STYLE_TAB
        }
        self.cursor_center = {
            'title': 'cursor_center',
            'locator': self.page.locator(DragPL.CURSOR_CENTER),
            'selector': DragPL.CURSOR_CENTER
        }
        self.cursor_top_left = {
            'title': 'cursor_top_left',
            'locator': self.page.locator(DragPL.CURSOR_TOP_LEFT),
            'selector': DragPL.CURSOR_TOP_LEFT
        }
        self.cursor_bottom = {
            'title': 'cursor_bottom',
            'locator': self.page.locator(DragPL.CURSOR_BOTTOM),
            'selector': DragPL.CURSOR_BOTTOM
        }

    def get_cursor_position_while_moving(self, el, x, y):
        self.hover(el)
        down_params = self.bounding_box(el)
        print(down_params)
        self.down()
        self.move(down_params['x'] + x, down_params['y'] + y)
        self.up()
        up_params = self.bounding_box(el)
        x = self.page.evaluate('() => x')
        y = self.page.evaluate('() => y')
        print(el["title"], up_params, x, y)
