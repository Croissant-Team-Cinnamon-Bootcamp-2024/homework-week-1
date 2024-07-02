from .document_handler import DocumentHandler
from .image_handler import HeicHandler, PngHandler, TiffHandler
from .ocr_images import OcrImages
from .pdf_handler import PdfHandler


class InputHandler(object):
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
                try:
                    image = handler.process(filepath)
                except Exception as e:
                    raise Exception(f"Cannot extract this image due to {e}")
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: not supported!")
        return image