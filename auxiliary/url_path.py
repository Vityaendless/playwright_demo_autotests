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
