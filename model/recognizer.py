import pytesseract
import numpy as np
from typing import List, Dict

class TextRecognizer:
    def __init__(self):
        pass

    def extract_text_lines(self, image: np.ndarray, scaling_factor: float) -> List[Dict[str, Dict[str, int]]]:
        d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        n_boxes = len(d['level'])
        text_lines = []
        for i in range(n_boxes):
            if int(d['conf'][i]) > 0:  # Filter out low confidence detections
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                # Adjust the coordinates according to the scaling factor
                text_lines.append({
                    "text": d['text'][i],
                    "location": {"x": int(x / scaling_factor), "y": int(y / scaling_factor),
                                 "width": int(w / scaling_factor), "height": int(h / scaling_factor)}
                })
        return text_lines
