from sectional_description import SectionalDescription
from share_media import PushMedia
from enum import Enum
import datetime
import uuid
from errors.failure_enums import ExqtError

class SharePost:

    def __init__(self) -> None:
        """
            initiate share post
        
        """
        self.share_id: str = uuid.uuid4().hex
        self.status: PostStatus = PostStatus.Draft
        self.title: str = ""
        self.descriptions: list[SectionalDescription] = list()
    
    def entitles(self, title: str) -> ExqtError:
        """
            entitle share post, check post existence
        
        """
        self.title = title
        return None

    def describes(self, text: str, score: int, media: bytes, title) -> ExqtError:
        """
            enrich description section, handle media & text

        """
        media = PushMedia(media_object=media)
        description = SectionalDescription(text=text, score=score, media=media, title=title)
        self.descriptions.append(description)
        return None

    def wraps(self) -> ExqtError:
        for description in self.descriptions:
            err = description.wraps()
            if not err:
                continue
            return err
        self.create_time = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        self.status = PostStatus.Public
        return None
    
    def composes(self) -> ExqtError:
        
        return None
    
    
class PostStatus(Enum):
    Draft = 0
    Private = 1
    Public = 2
    Suspend = 3
