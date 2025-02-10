BASE_URL = "https://demoqa.com/"


class UrlPaths:
    def __init__(self):
        self.domain = BASE_URL

    def get_path(self, path):
        return self.domain + path

    @property
    def textbox(self):
        return self.get_path("text-box")

    @property
    def checkbox(self):
        return self.get_path("checkbox")

    @property
    def radio_btn(self):
        return self.get_path("radio-button")

    @property
    def buttons(self):
        return self.get_path("buttons")

    @property
    def links(self):
        return self.get_path("links")

    @property
    def broken_img_links(self):
        return self.get_path("broken")

    @property
    def upload_download(self):
        return self.get_path("upload-download")

    @property
    def dynamic_properties(self):
        return self.get_path("dynamic-properties")

    @property
    def web_tables(self):
        return self.get_path("webtables")

    @property
    def accordian(self):
        return self.get_path("accordian")

    @property
    def tabs(self):
        return self.get_path("tabs")

    @property
    def practice_form(self):
        return self.get_path("automation-practice-form")

    @property
    def browser_windows(self):
        return self.get_path("browser-windows")

    @property
    def alerts(self):
        return self.get_path("alerts")

    @property
    def iframes(self):
        return self.get_path("frames")

    @property
    def nested_iframes(self):
        return self.get_path("nestedframes")

    @property
    def modal_dialogs(self):
        return self.get_path("modal-dialogs")

    @property
    def auto_complete(self):
        return self.get_path("auto-complete")

    @property
    def date_picker(self):
        return self.get_path("date-picker")

    @property
    def slider(self):
        return self.get_path("slider")

    @property
    def progress_bar(self):
        return self.get_path("progress-bar")

    @property
    def tool_tips(self):
        return self.get_path("tool-tips")

    @property
    def sample(self):
        return self.get_path("sample")
