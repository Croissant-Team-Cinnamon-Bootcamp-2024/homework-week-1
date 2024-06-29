from abc import ABC, abstractmethod
import mimetypes

from PIL import Image
from pillow_heif import register_heif_opener
import numpy as np

from .data_model.input_image import OcrImages


class BaseFileHandler(ABC):
    """Prepare image data and process as numpy array format
    """
    @abstractmethod
    def process(self, filepath: str) -> np.array:
        pass
    
    """Check file mime type
    https://mimetype.io/all-types
    """
    @abstractmethod
    def can_handle(self, filepath: str) -> bool:
        pass


class PngFileHandler(BaseFileHandler):
    def process(self, filepath: str) -> np.array:
        image = Image.open(filepath)
        image = image.convert('RGB')
        print(image)
        return OcrImages(image_list=[np.array(image)])
    
    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/png"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type
    
    
class HeicFileHandler(PngFileHandler):
    def process(self, filepath: str) -> np.array:
        register_heif_opener()
        return super().process(filepath)
    
    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/heic"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type
    
    
class TiffFileHandler(PngFileHandler):
    
    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/tiff"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type
    

# pdf2image
class PdfFileHandler(BaseFileHandler):
    def process(self, filepath: str) -> np.array:
        pass
    
    def can_handle(self, filepath: str) -> bool:
        pass
    
    
class DocFileHandler(PdfFileHandler):
    def process(self, filepath: str) -> np.array:
        pass
    
    def can_handle(self, filepath: str) -> bool:
        pass
    