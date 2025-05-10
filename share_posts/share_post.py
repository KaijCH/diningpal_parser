from sectional_description import SectionalDescription
from share_media import ShareMedia
from enum import Enum
import datetime
import uuid
from errors.errors import Error

class SharePost:

    def __init__(self, title: str, ) -> None:
        """
            initiate share post
        
        """
        self.share_id: str = uuid.uuid4().hex
        self.status: PostStatus = PostStatus.Draft
        self.title: str = ""
        self.descriptions: list[SectionalDescription] = list()
    
    def entitles(self, title: str) -> Error:
        """
            entitle share post, check post existence
        
        """
        self.title = title
        return None

    def describes(self, text: str, score: int, media: bytes, title) -> Error:
        """
            enrich description section, handle media & text

        """
        media = ShareMedia(media_object=media)
        description = SectionalDescription(text=text, score=score, media=media, title=title)
        self.descriptions.append(description)
        return None

    def wraps(self) -> Error:
        for description in self.descriptions:
            err = description.wraps()
            if not err:
                continue
            return err
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        self.create_time = int(utc_now.timestamp())
        self.status = PostStatus.Public
        return None

    
class PostStatus(Enum):
    Draft = 0
    Private = 1
    Public = 2
    Suspend = 3
