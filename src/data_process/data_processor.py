import numpy as np

from .input_handler.image_handler import (
    HeicFileHandler,
    PngFileHandler,
    TiffFileHandler,
)
from .input_handler.pdf_handler import DocFileHandler, DocxFileHandler, PdfFileHandler


class ImageFileHandler(object):
    def __init__(self) -> None:
        self.list_handlers = [
            PngFileHandler(),
            HeicFileHandler(),
            TiffFileHandler(),
            PdfFileHandler(),
            DocxFileHandler(),
            DocFileHandler(),
        ]

    def process_image(self, filepath: str) -> np.array:
        image = None
        for handler in self.list_handlers:
            if handler.can_handle(filepath):
                image = handler.process(filepath)
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: not supported!")
        return image
