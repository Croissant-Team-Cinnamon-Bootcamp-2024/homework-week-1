from .data_model.input_image import OcrImages
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

    def process_image(self, filepath: str) -> OcrImages:
        image = None
        for handler in self.list_handlers:
            if handler.can_handle(filepath):
                image = handler.process(filepath)
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: not supported!")
        return image
