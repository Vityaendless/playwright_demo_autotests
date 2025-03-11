class ProfilePageLocator:
    NOT_LOGIN_LABEL = "#notLoggin-label"
    TO_LOGIN_LINK = "//label[@id='notLoggin-label']/a[@href='/login']"
    TO_REG_LINK = "//label[@id='notLoggin-label']/a[@href='/register']"
    LOGOUT_BTN = ".text-right label~#submit"
