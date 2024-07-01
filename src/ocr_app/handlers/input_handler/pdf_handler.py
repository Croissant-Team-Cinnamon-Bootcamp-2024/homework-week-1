import mimetypes

import fitz
import numpy as np
from PIL import Image

from .base_handler import BaseHandler
from .ocr_images import OcrImages


class PdfHandler(BaseHandler):
    def process(self, filepath: str) -> OcrImages:
        images = []
        document = fitz.open(filepath)
        for page in document:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(np.array(img))
        document.close()
        return OcrImages(image_list=images)

    def can_handle(self, filepath: str) -> bool:
        mime_type = "application/pdf"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_type == guess_mime_type
