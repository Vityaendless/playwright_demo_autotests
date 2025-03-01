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
    PREVENT_PROPOGATION_TAB = "#droppableExample-tab-preventPropogation"
    PR_PR_DRAGGABLE = "#dragBox"
    NOT_GREEDY_OUT_DROP = "#notGreedyDropBox"
    NOT_GREEDY_INNER_DROP = "#notGreedyInnerDropBox"
    GREEDY_OUT_DROP = "#greedyDropBox"
    GREEDY_INNER_DROP = "#greedyDropBoxInner"
    REVERT_TAB = "#droppableExample-tab-revertable"
    REVERTABLE = "#revertable"
    NOT_REVERTABLE = "#notRevertable"
    REVERT_DROPPABLE = "#droppableExample-tabpane-revertable #droppable"


class DraggablePageLocator:
    SIMPLE_DRAG_BOX = "#dragBox"
    AXIS_TAB = "#draggableExample-tab-axisRestriction"
    ONLY_X_DRAG = "#restrictedX"
    ONLY_Y_DRAG = "#restrictedY"
    CONTAINER_TAB = "#draggableExample-tab-containerRestriction"
    CONTAINER = "#containmentWrapper"
    DRAG_IN_CONTAINER = "#containmentWrapper .draggable"
    DRAGGABLE_CONTAINER = "#draggableExample-tabpane-containerRestriction > .draggable"
    DRAG_SPAN = "#draggableExample-tabpane-containerRestriction > .draggable span"
    CURSOR_STYLE_TAB = "#draggableExample-tab-cursorStyle"
    CURSOR_CENTER = "#cursorCenter"
    CURSOR_TOP_LEFT = "#cursorTopLeft"
    CURSOR_BOTTOM = "#cursorBottom"
