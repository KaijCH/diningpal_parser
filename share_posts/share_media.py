from errors.errors import *

class ShareMedia:

    def __init__(self, media_object: bytes):
        """
            initiate media onject, handle for cloud storage uri or local cache
        
        """
        self.bytes: bytes = media_object
        self.cache: str = ""
        self.uri: str = ""
        self.handles()
        
    def handles(self) -> None:
        """
            handle media object, if fail uploading to cloud storage, reserve to local folder
        
        """
        err = self.uploads()
        if not err:
            return
        # todo: implement local cache ref
        self.cache = ""
        return 

    def finalizes(self) -> Error:
        """
            final-check media online
        
        """
        if self.uri.strip():
            return None
        return self.uploads()
    
    def uploads(self) -> Error:
        """
            upload media to cloud storage

        """
        # todo: implement cloud storage invocation
        self.uri = ""
        return ErrorHttpRequest

    def locates(self) -> str:
        """
            return media storage uri
        
        """
        return self.uri
    