from loggers.runtime_locater import locate_execution
from loggers.runtime_logger import logger
from exqt_errors.error_enums import * 
from configs import default_media


class ShareMedia:

    def __init__(self):
        """
            initiate media object, handle for cloud storage uri or local cache
        
        """
        # media object bytes
        self.content: bytes = None
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
        
    def ingests(self, content: bytes) -> ExqtError:
        """
            ingest picture media from user upload action
        
        """
        # todo: implementing verification of picture requirement
        if not content:
            logger.fails(context=locate_execution(), message="void media content")
            return FailureMissingMedia
        self.content = content
        # fetch media info
        err = self.analyzes()
        if err is not None:
            logger.fails(context=locate_execution(), message="malform media content")
            return err
        # upload to cloud or cache to local
        err = self.uploads()
        if err is not None:
            logger.warns(context=locate_execution(), message="media content upload")
            # todo: implement local cache addr
            self.cache = ""
        return None
    
    def analyzes(self) -> ExqtError:
        """
            fetch media info: name, resolution, size, extension, format

        """
        # todo: fetch media, restrict media format
        
        return FailureMalformMedia
        
    def wraps(self) -> ExqtError:
        """
            final-check media existence in cloud storage
        
        """
        # legit cloud existence
        if self.uri.strip():
            return None
        # re-attempt uploads
        return self.uploads()
    
    def uploads(self) -> ExqtError:
        """
            upload media to cloud storage

        """
        # todo: implement cloud storage invocation
        return FailureHttpRequest

    def locates(self) -> str:
        """
            return media storage uri
        
        """
        return self.cache if not self.uri else self.uri
    