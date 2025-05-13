class ExqtError:

    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code

    def details(self) -> str:
        return self.message
