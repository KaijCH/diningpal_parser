from loggers.runtime_locater import locate_execution
from loggers.runtime_logger import logger
from share_media.share_media import ShareMedia
from exqt_errors.error_enums import *


class ShareDetail:

    def __init__(self) -> None:
        """
            initiate detail section
        
        """
        self.title: str = ""
        self.description: str = ""
        self.score: int = 0
        self.media: ShareMedia = None
        self.media_uri: str = ""

    def scores(self, score: int) -> ExqtError:
        """
            rate score of subject of detail section
        
        """
        if not 0 <= score <= 5:
            return FailureInvalidInput
        self.score = score
        return None

    def entitles(self, title: str) -> ExqtError:
        """
            set title for detail section
        
        """
        title = title.strip()
        if not title:
            return FailureEmptyInput
        self.title = title
        return None
    
    def describes(self, text: str) -> ExqtError:
        """
            set description for detail section
        
        """
        text = text.strip()
        if not text:
            return FailureEmptyInput
        self.description = text
        return None
    
    def wraps(self) -> ExqtError:
        """
            check current detail section for info completeness
        
        """
        if not self.title or not self.description:
            logger.fails(locate_execution(), "empty liternal content")
            return FailureEmptyInput
        
        err = self.media.wraps()
        if err is not None:
            logger.warns(locate_execution(), "failure in media cloud storage rediness")
            return FailureMissingMedia
        self.media_uri = self.media.locates()
        return None
        