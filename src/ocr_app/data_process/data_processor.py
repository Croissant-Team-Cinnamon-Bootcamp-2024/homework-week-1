from .data_model.input_image import OcrImages
from .input_handler.image_handler import (
    HeicFileHandler,
    PngFileHandler,
    TiffFileHandler,https://github.com/Croissant-Team-Cinnamon-Bootcamp-2024/homework-week-1/tree/feat/pdf-read/src/ocr_app/data_process
)
from .input_handler.pdf_handler import DocumentFileHandler, PdfFileHandler


class ImageFileHandler(object):
    def __init__(self) -> None:
        self.list_handlers = [
            PngFileHandler(),
            HeicFileHandler(),
            TiffFileHandler(),
            PdfFileHandler(),
            DocumentFileHandler(),
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
