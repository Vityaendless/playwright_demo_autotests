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
