from .image_process import OutputImageProcessor
from .json_process import JsonProcessor
from .ocr_output import OcrResults

DEFAULT_SAVE_DIR = "results"


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
