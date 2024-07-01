from abc import ABC, abstractmethod

from ..data_model.input_image import OcrImages


class BaseHandler(ABC):
    """Prepare image data and process as numpy array format
    Check file mime type to pass to specific handler
    https://mimetype.io/all-types
    """

    @abstractmethod
    def process(self, filepath: str) -> OcrImages:
        pass

    @abstractmethod
    def can_handle(self, filepath: str) -> bool:
        pass
