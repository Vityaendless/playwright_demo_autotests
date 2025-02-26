class SortablePageLocator:
    FIRST_EL = "#demo-tabpane-list .list-group-item:first-child"
    SECOND_EL = "#demo-tabpane-list .list-group-item:last-child"
    TO_GRID = "#demo-tab-grid"
    FIRST_EL_GRID = "#demo-tabpane-grid .list-group-item:first-child"
    SECOND_EL_GRID = "#demo-tabpane-grid .list-group-item:last-child"


class SelectablePageLocator:
    LIST_ELS = "#verticalListContainer .list-group-item"
    TO_GRID = SortablePageLocator.TO_GRID
    GRID_ELS = "#gridContainer .list-group-item"


class ResizablePageLocator:
    RESIZABLE_BOX = "#resizableBoxWithRestriction"
    CONTAINER = ".constraint-area"
    RESIZABLE = "#resizable"


class DropPageLocator:
    SIMPLE_DRAGGABLE = "#droppableExample-tabpane-simple #draggable"
    SIMPLE_DROPPABLE = "#droppableExample-tabpane-simple #droppable"
    ACCEPT_TAB = "#droppableExample-tab-accept"
    ACCEPTABLE = "#acceptable"
    NOT_ACCEPTABLE = "#notAcceptable"
    ACCEPT_DROPPABLE = "#droppableExample-tabpane-accept #droppable"
