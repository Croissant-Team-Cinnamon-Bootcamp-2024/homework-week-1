from typing import Dict, List

import numpy as np
import pytesseract


class TextRecognizer:
    def __init__(self):
        pass

    def extract_text_lines(
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
