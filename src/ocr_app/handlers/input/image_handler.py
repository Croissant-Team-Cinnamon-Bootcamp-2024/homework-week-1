import mimetypes

import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener

from .base_handler import BaseHandler
from .ocr_images import OcrImages


class PngHandler(BaseHandler):
    def process(self, filepath: str) -> OcrImages:
        image = Image.open(filepath)
        image = image.convert("RGB")
        return OcrImages(image_list=[np.array(image)])

    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/png"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class HeicHandler(PngHandler):
    def process(self, filepath: str) -> OcrImages:
        register_heif_opener()
        return super().process(filepath)

    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/heic"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class TiffHandler(PngHandler):
    def can_handle(self, filepath: str) -> bool:
        mime_text = "image/tiff"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type
