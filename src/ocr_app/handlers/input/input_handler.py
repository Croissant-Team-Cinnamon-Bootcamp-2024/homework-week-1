from .document_handler import DocumentHandler
from .image_handler import HeicHandler, PngHandler, TiffHandler
from .ocr_images import OcrImages
from .pdf_handler import PdfHandler


class InputHandler(object):
    """
    Handles the input of various file types and directs them to appropriate handlers
    for reading and preparing for OCR.

    This class maintains a list of different file handlers. It checks the file type
    of the input, determines which handler can process the file, and then delegates
    the file processing to that handler.

    Attributes:
        list_handlers (list): A list of initialized handler objects that can
        process different file types.
    """

    def __init__(self) -> None:
        """
        Initialize the InputHandler with a list of specific file type handlers.
        """

        self.list_handlers = [
            PngHandler(),
            HeicHandler(),
            TiffHandler(),
            PdfHandler(),
            DocumentHandler(),
        ]

    def read(self, filepath: str) -> OcrImages:
        """
        Reads a file and processes it using the appropriate handler based on the file type.

        Args:
            filepath (str): The path to the file to be processed.

        Returns:
            OcrImages: An object containing the processed image data ready for OCR.

        Raises:
            NotImplementedError: If no handler is available for the given file type.
            Exception: If an error occurs during the file processing.
        """
        image = None
        for handler in self.list_handlers:
            if handler.can_handle(filepath):
                try:
                    image = handler.process(filepath)
                except Exception as e:
                    raise Exception(f"Cannot extract this image due to {e}")
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: not supported!")
        return image
