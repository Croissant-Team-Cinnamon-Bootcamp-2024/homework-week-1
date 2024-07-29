import mimetypes

import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener

from .base_handler import BaseHandler
from .ocr_images import OcrImages


class PngHandler(BaseHandler):
    """
    A handler for reading PNG image files to prepare them for OCR.

    This handler is specialized in reading images with PNG format, converting them to
    a format (RGB) suitable for OCR operations.

    Attributes:
        Inherits all attributes from BaseHandler.
    """

    def process(self, filepath: str) -> OcrImages:
        """
        Read a PNG image file and prepare it for OCR by converting it to RGB format.

        Args:
            filepath (str): The path to the PNG image file.

        Returns:
            OcrImages: An OcrImages object containing the image data in a format ready for OCR processing.
        """
        image = Image.open(filepath)
        image = image.convert("RGB")
        return OcrImages(image_list=[np.array(image)])

    def can_handle(self, filepath: str) -> bool:
        """
        Determine if this handler can process the given file based on its MIME type.

        Args:
            filepath (str): The path to the file to be checked.

        Returns:
            bool: True if the file is a PNG image, False otherwise.
        """
        mime_text = "image/png"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class HeicHandler(PngHandler):
    """
    A handler for reading HEIC image files to prepare them for OCR.

    This handler extends the PngHandler by adding support for HEIC images through registering a HEIC opener.

    Attributes:
        Inherits all attributes from PngHandler.
    """

    def process(self, filepath: str) -> OcrImages:
        """
        Read a HEIC image file and prepare it for OCR using the base class method after registering a HEIC opener.

        Args:
            filepath (str): The path to the HEIC image file.

        Returns:
            OcrImages: An OcrImages object containing the image data in a format ready for OCR processing.
        """
        register_heif_opener()
        return super().process(filepath)

    def can_handle(self, filepath: str) -> bool:
        """
        Determine if this handler can process the given file based on its MIME type.

        Args:
            filepath (str): The path to the file to be checked.

        Returns:
            bool: True if the file is a HEIC image, False otherwise.
        """
        mime_text = "image/heic"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class TiffHandler(PngHandler):
    """
    A handler for reading TIFF image files to prepare them for OCR.

    This handler extends the PngHandler to include support for TIFF images.

    Attributes:
        Inherits all attributes from PngHandler.
    """

    def can_handle(self, filepath: str) -> bool:
        """
        Determine if this handler can process the given file based on its MIME type.

        Args:
            filepath (str): The path to the file to be checked.

        Returns:
            bool: True if the file is a TIFF image, False otherwise.
        """
        mime_text = "image/tiff"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type
