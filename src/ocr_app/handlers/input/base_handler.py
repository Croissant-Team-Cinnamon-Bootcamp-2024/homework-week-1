from abc import ABC, abstractmethod

from .ocr_images import OcrImages


class BaseHandler(ABC):
    """Prepare image data and process as numpy array format
    Check file mime type to pass to specific handler
    https://mimetype.io/all-types
    """

    @abstractmethod
    def process(self, filepath: str) -> OcrImages:
        """Process the given file path and return OCR image data."""

    @abstractmethod
    def can_handle(self, filepath: str) -> bool:
        """Check if the handler can process the given file path."""
