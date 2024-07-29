from typing import Dict, List

import numpy as np
import pytesseract

from ..handlers.input.ocr_images import OcrImages
from ..handlers.output.ocr_output import OcrResults
from .data_preprocess import DataPreprocess


class OCR:
    """
    OCR class to process images and extract text using Tesseract OCR.
    """

    def __init__(self):
        pass

    def _extract_text_lines(
        self, image: np.ndarray, scaling_factor: float
    ) -> List[Dict[str, Dict[str, int]]]:
        """
        Extracts text lines from the input image using Tesseract OCR.

        Args:
            image (np.ndarray): Input image as a numpy array.
            scaling_factor (float): Scaling factor applied during preprocessing.

        Returns:
            List[Dict[str, Dict[str, int]]]: List of dictionaries,
            where each dictionary represents a text line with 'text' and 'location' information.
                'text' (str): Extracted text from the line.
                'location' (Dict[str, int]): Bounding box coordinates of
                the text line adjusted according to the scaling factor.
        """
        d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        n_boxes = len(d["level"])
        text_lines = []
        for i in range(n_boxes):
            if int(d["conf"][i]) > 0:  # Filter out low confidence detections
                (x, y, w, h) = (
                    d["left"][i],
                    d["top"][i],
                    d["width"][i],
                    d["height"][i],
                )
                # Adjust the coordinates according to the scaling factor
                text_lines.append(
                    {
                        "text": d["text"][i],
                        "location": {
                            "x": int(x / scaling_factor),
                            "y": int(y / scaling_factor),
                            "width": int(w / scaling_factor),
                            "height": int(h / scaling_factor),
                        },
                    }
                )
        return text_lines

    def read_text(self, data: OcrImages) -> OcrResults:
        """
        Reads text from a list of images using OCR and returns structured results.

        Args:
            data (OcrImages): An OcrImages object containing a list of images to process with OCR.

        Returns:
            OcrResults: An object containing the original images and the corresponding OCR results.
        """
        list_ocr_output = []
        for datum in data.image_list:
            processor = DataPreprocess()
            try:
                threshold, scaling_factor = processor.preprocess(datum)
                output = self._extract_text_lines(threshold, scaling_factor)
                list_ocr_output.append(output)
            except Exception as e:
                raise Exception(f"Failed to process image for OCR: {e}")
        return OcrResults(data.image_list, list_ocr_output)
