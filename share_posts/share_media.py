from configs import default_media
from errors.failure_enums import * 
from loggers import runtime_logger

class PushMedia:

    def __init__(self):
        """
            initiate media object, handle for cloud storage uri or local cache
        
        """
        # media object bytes
        self.object: bytes = default_media.DefaultPictureDish
        # resolution height
        self.height: int = 0
        # resolution width
        self.width: int= 0
        # media file name
        self.name: str = ""
        # media local cache addr
        self.cache: str = ""
        # media cloud storge addr
        self.uri: str = ""
        
    def ingests(self, object: bytes) -> ExqtError:
        """
            ingest picture media from user upload atempt
        
        """
        # todo: implementing verification of picture requirement
        if not object:
            runtime_logger.logs()
            return FailureMissingMedia
        self.object = object
        # fetch media info
        err = self.analyzes()
        if err is not None:
            return err
        # upload to cloud storage ot cache to local
        err = self.uploads()
        if err is not None:
            self.cache = ""
            return err
        return None
    
    def analyzes(self) -> None:
        """
            fetch media info: name, resolution, size, extension, format

        """
        # todo: fetch media, restrict media format
        
        return FailureMalformMedia
        
    def wraps(self) -> ExqtError:
        """
            final-check media online
        
        """
        if self.uri.strip():
            return None
        return self.uploads()
    
    def uploads(self) -> ExqtError:
        """
            upload media to cloud storage

        """
        # todo: implement cloud storage invocation
        self.uri = ""
        return FailureHttpRequest

    def locates(self) -> str:
        """
            return media storage uri
        
        """
        return self.cache if not self.uri else self.uri
    