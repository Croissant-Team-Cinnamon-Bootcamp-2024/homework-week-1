import mimetypes

import fitz
import numpy as np
from PIL import Image

from .base_handler import BaseHandler
from .ocr_images import OcrImages


class PdfHandler(BaseHandler):
    """
    A handler for processing PDF files to extract images for OCR.

    This handler reads PDF files, extracts each page as an image, and prepares them for OCR processing.
    It uses PyMuPDF (fitz) to handle PDF operations, converting each page to an RGB image format.

    Attributes:
        Inherits all attributes from BaseHandler.
    """

    def process(self, filepath: str) -> OcrImages:
        """
        Process a PDF file by extracting each page as an image ready for OCR.

        This method opens a PDF file, extracts each page as an image, converts it to RGB format, and returns
        a collection of these images wrapped in an OcrImages object.

        Args:
            filepath (str): The path to the PDF file.

        Returns:
            OcrImages: An object containing a list of image arrays, each representing a page from the PDF.
        """
        images = []
        document = fitz.open(filepath)
        for page in document:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(np.array(img))
        document.close()
        return OcrImages(image_list=images)

    def can_handle(self, filepath: str) -> bool:
        """
        Determine if this handler can process the given PDF file based on its MIME type.

        Args:
            filepath (str): The path to the file to be checked.

        Returns:
            bool: True if the file is a PDF, False otherwise.
        """
        mime_type = "application/pdf"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_type == guess_mime_type
