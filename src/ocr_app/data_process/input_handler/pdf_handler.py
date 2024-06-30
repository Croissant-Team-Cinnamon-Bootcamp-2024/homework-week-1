import mimetypes

import fitz
import numpy as np
from doc2docx import convert as doc2docx_convert
from docx2pdf import convert as docx2pdf_convert
from PIL import Image

from ..data_model.input_image import OcrImages
from .image_handler import BaseFileHandler


class PdfFileHandler(BaseFileHandler):
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
        mime_text = "application/pdf"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class DocxFileHandler(PdfFileHandler):
    def process(self, filepath: str) -> OcrImages:
        docx_filepath = filepath.replace(".docx", ".pdf")
        docx2pdf_convert(filepath, docx_filepath)
        return super().process(docx_filepath)

    def can_handle(self, filepath: str) -> bool:
        return filepath.endswith(".docx")


class DocFileHandler(DocxFileHandler):
    def process(self, filepath: str) -> OcrImages:
        docx_filepath = filepath.replace(".doc", ".docx")
        doc2docx_convert(filepath, docx_filepath)
        return super().process(docx_filepath)

    def can_handle(self, filepath: str) -> bool:
        return filepath.endswith(".doc")
