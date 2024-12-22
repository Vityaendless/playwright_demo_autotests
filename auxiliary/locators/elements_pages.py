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


class ButtonsPageLocator:
    DBL_CLICK = "#doubleClickBtn"
    DBL_CLICK_RESULT = "#doubleClickMessage"
    RIGHT_CLICK = "#rightClickBtn"
    RIGHT_CLICK_RESULT = "#rightClickMessage"
    CLICK = "//button[text()='Click Me']"
    CLICK_RESULT = "#dynamicClickMessage"


class LinksPageLocator:
    HOME = "#simpleLink"
    DYN_HOME = "#dynamicLink"
    CREATED = "#created"
    NO_CONTENT = "#no-content"
    MOVED = "#moved"
    BAD_REQUEST = "#bad-request"
    UNAUTHORIZED = "#unauthorized"
    FORBIDDEN = "#forbidden"
    INVALID = "#invalid-url"
    RESULT = "#linkResponse"


class BrokenLinksImagesPageLocator:
    VALID_IMG = "//p[text()='Valid image']/following::img[1]"
    BROKEN_IMG = "//p[text()='Broken image']/following::img[1]"
    VALID_LINK = "//p[text()='Valid Link']/following::a[1]"
    BROKEN_LINK = "//p[text()='Broken Link']/following::a[1]"


class UploadDownloadPageLocator:
    DOWNLOAD = "#downloadButton"
    UPLOAD = "#uploadFile"
    UPLOAD_RESULT = "#uploadFile"
    UPLOAD_PATH = "#uploadedFilePath"
