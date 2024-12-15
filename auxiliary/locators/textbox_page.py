class TextboxPageLocator:
    USERNAME = "#userName"
    EMAIL = "#userEmail"
    C_ADDRESS = "#currentAddress"
    P_ADDRESS = "#permanentAddress"
    SUBMIT = "#submit"
    OUTPUT = "#output"
    OUTPUT_NAME = OUTPUT + " p#name"
    OUTPUT_EMAIL = OUTPUT + " p#email"
    OUTPUT_C_ADDRESS = OUTPUT + " p#currentAddress"
    OUTPUT_P_ADDRESS = OUTPUT + " p#permanentAddress"


class CheckboxPageLocator:
    EXPAND_ALL = "//button[@aria-label='Expand all']"
    COLLAPSE_ALL = "//button[@aria-label='Collapse all']"
    HOME = "//label[@for='tree-node-home']"
    ELS = ".rct-title"
    RESULT = "#result"


class RadioBtnPageLocator:
    YES = "//label[@for='yesRadio']"
    YES_RADIO = "#yesRadio"
    IMPRESSIVE = "//label[@for='impressiveRadio']"
    IMPRESSIVE_RADIO = "#impressiveRadio"
    NO_RADIO = "#noRadio"
    RESULT = ".mt-3 .text-success"
