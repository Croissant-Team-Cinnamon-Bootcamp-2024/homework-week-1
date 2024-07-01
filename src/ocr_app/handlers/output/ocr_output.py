from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class OcrResults:
    """Class for keeping track of OCR model output."""

    images: List[np.ndarray]
    ocr_outputs: List[List[Dict[str, Dict[str, int]]]]
