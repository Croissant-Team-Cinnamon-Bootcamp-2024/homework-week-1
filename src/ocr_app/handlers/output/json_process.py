import json
import os

from .ocr_output import OcrResults


class JsonProcessor:
    """Converts OCR results to a JSON file for storage or further processing."""

    @staticmethod
    def process(
        input: OcrResults,
        output_dir: str,
        output_filename: str = 'detect_result.json',
    ) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, output_filename)

        with open(output_file, 'w') as f:
            json.dump(input.ocr_outputs, f, indent=4)
