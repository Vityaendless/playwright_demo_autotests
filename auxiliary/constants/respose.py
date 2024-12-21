from enum import Enum


class ResCode(Enum):
    OK = (200, "Ok")
    CREATED = (201, "Created")
    NO_CONTENT = (204, "No Content")
    MOVED = (301, "Moved Permanently")
    NOT_MODIFIED = (304, "Not Modified")
    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORIZED = (401, "Unauthorized")
    FORBIDDEN = (403, "Forbidden")
    NOT_FOUND = (404, "Not Found")
    INTERNAL_SERVER_ERR = (500, "Internal Server Error")

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
