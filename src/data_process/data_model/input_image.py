from typing import List
from dataclasses import dataclass

import numpy as np

@dataclass
class OcrImages:
    """Class for keeping track of input images."""
    image_list: List[np.ndarray]