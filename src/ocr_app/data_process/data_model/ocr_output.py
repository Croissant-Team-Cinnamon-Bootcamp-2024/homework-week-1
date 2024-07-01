import os
from dataclasses import dataclass
from typing import Dict, List

import numpy as np

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
    'results',
)
print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


@dataclass
class OcrResults:
    images: List[np.ndarray]
    ocr_outputs: List[List[Dict[str, Dict[str, int]]]]
