# Dining Pal Parser

## breif intro

Implementation of DiningPal client, handling post content ingestion, preparing for upsertion

## class impl guideline

Some common member func for class implementation

```Python
class SomeClass

    def __init__(self) -> None:
        """
            class definition, member attr initiation

        """
    
    def ingests(self, object: bytes) -> ExqtError:
        """
            media file (bytes) upsertion

        """

    def entitles(self, title: str) -> ExqtError:
        """
            title (string) upsertion

        """

    def describes(self, text: str) -> ExqtError:
        """
            text (string) upsertion

        """
    
    def wraps(self) -> ExqtError:
        """
            full class member attr validation

        """

```
