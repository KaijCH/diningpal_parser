from share_media import PushMedia
from errors.failure_enums import *

class SectionalDescription:

    def __init__(self, text: str, score: int = None, media: PushMedia = None, title: str = None) -> None:
        self.title: str = title
        self.text: str = text
        self.score: int = -1
        self.media: PushMedia = media
        self.media_uri: str = ""

    def scores(self, score: int) -> ExqtError:
        if not 0 <= score <= 5:
            return FailureInvalidInput
        self.score = score
        return None

    def entitles(self, title: str) -> ExqtError:
        self.title = title.strip()
        if not self.title:
            return FailureEmptyInput
        return None
    
    def describes(self, text: str) -> ExqtError:
        self.text = text.strip()
        if not self.text:
            return FailureEmptyInput
        return None
    
    def wraps(self) -> ExqtError:
        if not self.title or not self.text:
            return FailureEmptyInput
        
        err = self.media.wraps()
        if err is not None:
            return FailureMissingMedia
        self.media_uri = self.media.locates()
        return None
        