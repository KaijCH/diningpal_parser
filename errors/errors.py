from enum import Enum

class Error(Enum):

    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code

    def info(self) -> str:
        return self.message

# enumeration of errs

ErrorHttpRequest = Error("", 4)

ErrorMediaMiss = Error("", 5)

ErrorEmptyInput = Error("", 6)

ErrorInputInvalid = Error("", 8)
