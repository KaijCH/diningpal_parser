from exqt_errors.error_enums import *


class ShareAuthor:

    def __init__(self) -> None:
        self.sign: str = ""
        self.mail: str = ""

    def signs(self, sign: str) -> ExqtError:
        self.sign = sign

    def endorses(self) -> str:
        return self.sign

    def checks(self) -> ExqtError:
        """
            check author status
        
        """
        if not self.sign:
            return FailureSubmiterExpire
        return None


submiter = ShareAuthor()
