from share_details.share_detail import ShareDetail
from exqt_errors.exqt_error import ExqtError
from loggers.runtime_locater import locate_execution
from loggers.runtime_logger import logger
from sign_authors.sign_author import submiter
from exqt_errors.error_enums import *

import datetime
import uuid


class SharePost:

    Draft, Public, Private, Suspend = 0, 1, 2, 3

    def __init__(self) -> None:
        """
            initiate share post for site / subject
        
        """
        self.create_time = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        self.share_id: str = uuid.uuid4().hex
        self.author: str = submiter.endorses()
        self.title: str = ""
        self.summa: str = ""
        self.score: int = 0
        self.descriptions: dict[int, ShareDetail] = dict()
        self.status: int = 0
    
    def entitles(self, title: str) -> ExqtError:
        """
            entitle share post, check post existence
        
        """
        title = title.strip() 
        if not title:
            logger.fails(context=locate_execution(), message="empty title for post")
            return FailureEmptyInput
        self.title = title
        return None

    def scores(self, score: int) -> ExqtError:
        """
            rate score of share subject
        
        """
        if not 0 <= score <= 5:
            return FailureInvalidInput
        self.score = score
        return None

    def summarizes(self, summa: str) -> ExqtError:
        """
            take summary for current share post
        
        """
        summa = summa.strip()
        if not summa:
            logger.fails(context=locate_execution(), message="empty summary for post")
            return FailureEmptyInput
        self.summa = summa
        return None

    def enriches(self) -> ExqtError:
        """
            enqueue new description section

        """
        if not self.descriptions:
            self.descriptions: dict[int, ShareDetail] = dict()
        description = ShareDetail()
        self.descriptions[len(self.descriptions)] = description
        return None
    
    def finds(self, idx: int) -> tuple[ShareDetail, ExqtError]:
        """
            retrieve description section by index
        
        """
        if idx not in self.descriptions:
            logger.fails(context=locate_execution(), message="unfound description section")
            return None, FailureInvalidInput
        description = self.descriptions[idx]
        return description, None
        
    def wraps(self) -> ExqtError:
        """
            wrap check all sections in current post
        
        """
        for description in self.descriptions:
            err = description.wraps()
            if not err:
                continue
            return err
        return None
    
    def composes(self) -> ExqtError:
        self.status = self.Public
        return None
