from .image_process import OutputImageProcessor
from .json_process import JsonProcessor
from .ocr_output import OcrResults

DEFAULT_SAVE_DIR = "results"


class OutputHandler(object):
    """
    Handles the saving of OCR results in both JSON and PDF formats.
    """

    @staticmethod
    def process_output(
        ocr_results: OcrResults,
        output_dir: str = DEFAULT_SAVE_DIR,
    ) -> None:
        """
        Processes and saves OCR results to specified directory in JSON and PDF formats.
        """
        JsonProcessor.process(
            input=ocr_results,
            output_dir=output_dir,
        )

        OutputImageProcessor.create_pdf_from_numpy_images(
            input=ocr_results,
            output_dir=output_dir,
        )

        print(f"Result files have been saved to /{output_dir}")
