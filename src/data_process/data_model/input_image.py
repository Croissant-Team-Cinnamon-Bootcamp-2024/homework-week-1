from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class OcrImages:
    """Class for keeping track of loaded input images."""

    image_list: List[np.ndarray]
