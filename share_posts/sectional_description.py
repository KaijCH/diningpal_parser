from share_media import ShareMedia
from errors.errors import *

class SectionalDescription:

    def __init__(self, text: str, score: int = None, media: ShareMedia = None, title: str = None) -> None:
        self.title: str = title
        self.text: str = text
        self.score: int = -1
        self.media: ShareMedia = media
        self.media_uri: str = ""

    def scores(self, score: int) -> Error:
        if not 0 <= score <= 5:
            return ErrorInputInvalid
        self.score = score
        return None

    def entitles(self, title: str) -> Error:
        self.title = title.strip()
        if not self.title:
            return ErrorEmptyInput
        return None
    
    def describes(self, text: str) -> Error:
        self.text = text.strip()
        if not self.text:
            return ErrorEmptyInput
        return None
    
    def wraps(self) -> Error:
        if not self.title or not self.text:
            return ErrorEmptyInput
        
        err = self.media.finalizes()
        if err is not None:
            return ErrorMediaMiss
        self.media_uri = self.media.locates()
        return None
        