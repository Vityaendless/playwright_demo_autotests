class AccordianPageLocator:
    SECTION1_HEADING = "#section1Heading"
    SECTION2_HEADING = "#section2Heading"
    SECTION3_HEADING = "#section3Heading"
    SECTION1_CONTENT = "#section1Content"
    SECTION2_CONTENT = "#section2Content"
    SECTION3_CONTENT = "#section3Content"


class AutoCompletePageLocator:
    MULTIPLE_INPUT = "#autoCompleteMultipleInput"
    SINGLE_INPUT = "#autoCompleteSingleInput"
    COLORS = ".auto-complete__multi-value__label"
    REMOVE_COLOR_BTN = ".auto-complete__multi-value__remove"
    CLEAR_BTN = ".auto-complete__clear-indicator"
    SINGLE_INPUT_VALUE = ".auto-complete__single-value"


class DatePickerPageLocator:
    SELECT_DATE = "#datePickerMonthYearInput"
    SELECT_TIME_DATE = "#dateAndTimePickerInput"
    SELECT_MONTH = ".react-datepicker__month-select"
    SELECT_YEAR = ".react-datepicker__year-select"
    DAY_14 = ".react-datepicker__day--014"
    SELECT_MONTH_DT = ".react-datepicker__month-read-view"
    SELECT_YEAR_DT = ".react-datepicker__year-read-view--selected-year"


class SliderPageLocator:
    SLIDER = ".range-slider"
    SLIDER_VALUE = "#sliderValue"


class ProgressBarPageLocator:
    BTN = "#startStopButton"
    RESET_BTN = "#resetButton"
    PROGRESS_BAR = "#progressBar"


class ToolTipsPageLocator:
    BTN = "#toolTipButton"
    BTN_TOOL_TIP = "#buttonToolTip"
    FIELD = "#texFieldToolTopContainer"
    FIELD_TOOL_TIP = "#textFieldToolTip"
    FIRST_LINK = "#texToolTopContainer a:first-child"
    FIRST_LINK_TOOL_TIP = "#contraryTexToolTip"
    SECOND_LINK = "#texToolTopContainer a:last-child"
    SECOND_LINK_TOOL_TIP = "#sectionToolTip"


class TabsPageLocator:
    WHAT_TAB = "#demo-tab-what"
    ORIGIN_TAB = "#demo-tab-origin"
    USE_TAB = "#demo-tab-use"
    MORE_TAB = "#demo-tab-more"
    WHAT_CONTENT = "#demo-tabpane-what"
    ORIGIN_CONTENT = "#demo-tabpane-origin"
    USE_CONTENT = "#demo-tabpane-use"
    MORE_CONTENT = "#demo-tabpane-more"


class MenuPageLocator:
    MAIN_ITEMS = "#nav > li > a"
    SUB_ITEMS = "#nav > li:nth-child(2) > ul > li > a"
    SUB_SUB_ITEMS = "#nav > li:nth-child(2) > ul > li:last-child > ul a"


class SelectMenuPageLocator:
    OPTION_SELECTOR = "#withOptGroup"
    OPTION_INPUT = "#withOptGroup input"
    SELECT_ONE = "#selectOne"
    SELECT_ONE_INPUT = "#selectOne input"
    OLD_SELECTOR = "#oldSelectMenu"
    MULTI_SELECT = "(//p/b[text()='Multiselect drop down']/following::div)[1]"
    MULTI_SELECT_INPUT = "//p/b[text()='Multiselect drop down']/following::div//input"
    OLD_MULTI_SELECT = "#cars"
