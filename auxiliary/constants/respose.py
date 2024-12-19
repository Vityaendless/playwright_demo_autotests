from enum import Enum


class ResCode(Enum):
    CREATED = (201, "Created")

    def __init__(self, code, title) -> None:
        self.code = code
        self.title = title

    @classmethod
    def get_els(cls):
        return list(cls)

    @staticmethod
    def get_name(param):
        name = None
        for code in ResCode.get_els():
            if code.code == param:
                name = code.title
        return name
