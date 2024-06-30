import mimetypes

import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener

from ..data_model.input_image import OcrImages
from .base_handler import BaseFileHandler


class PngFileHandler(BaseFileHandler):
    def process(self, filepath: str) -> OcrImages:
        image = Image.open(filepath)
        image = image.convert("RGB")
        return OcrImages(image_list=[np.array(image)])

    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/png"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class HeicFileHandler(PngFileHandler):
    def process(self, filepath: str) -> OcrImages:
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
