from .data_model.input_image import OcrImages
from .input_handler.image_handler import HeicHandler, PngHandler, TiffHandler
from .input_handler.pdf_handler import DocumentHandler, PdfHandler


class Handler(object):
    def __init__(self) -> None:
        self.list_handlers = [
            PngHandler(),
            HeicHandler(),
            TiffHandler(),
            PdfHandler(),
            DocumentHandler(),
        ]

    def read(self, filepath: str) -> OcrImages:
        image = None
        for handler in self.list_handlers:
            if handler.can_handle(filepath):
                image = handler.process(filepath)
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: not supported!")
        return image
