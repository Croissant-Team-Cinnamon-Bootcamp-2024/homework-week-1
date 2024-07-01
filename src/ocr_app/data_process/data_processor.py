from .data_model.input_image import OcrImages
from .data_model.ocr_output import OcrResults
from .input_handler.image_handler import (
    HeicFileHandler,
    PngFileHandler,
    TiffFileHandler,
)
from .input_handler.pdf_handler import DocumentFileHandler, PdfFileHandler
from .output_handler.image_process import OutputImageProcessor
from .output_handler.json_process import JsonProcessor

DEFAULT_SAVE_DIR = "results"


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


class ModelOutputHandler(object):
    @staticmethod
    def process_output(
        ocr_results: OcrResults,
        output_dir: str = DEFAULT_SAVE_DIR,
    ) -> None:
        JsonProcessor.process(
            input=ocr_results,
            output_dir=output_dir,
        )

        OutputImageProcessor.create_pdf_from_numpy_images(
            input=ocr_results,
            output_dir=output_dir,
        )
