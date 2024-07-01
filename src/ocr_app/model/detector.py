from typing import Tuple

import cv2
import numpy as np


class TextDetector:
    def _resize_image(self, img: np.ndarray, max_size: Tuple[int, int] = (2000, 2000)) -> Tuple[np.ndarray, float]:
        """
        Resize the input image while maintaining aspect ratio
        and ensuring it fits within `max_size`.

        Args:
            img (np.ndarray): Input image as a numpy array to be resized.
            max_size (Tuple[int, int]): Maximum allowed size (height, width)
            for the resized image. Defaults to (2000, 2000).

        Returns:
            Tuple[np.ndarray, float]: Resized image as a numpy array and the scaling factor applied.
        """
        height, width = img.shape[:2]

        if height > max_size[0] or width > max_size[1]:
            scaling_factor = min(max_size[0] / height, max_size[1] / width)
            img = cv2.resize(
                img,
                None,
                fx=scaling_factor,
                fy=scaling_factor,
                interpolation=cv2.INTER_AREA,
            )
        elif height < 800 or width < 800:
            scaling_factor = max(800 / height, 800 / width)
            img = cv2.resize(
                img,
                None,
                fx=scaling_factor,
                fy=scaling_factor,
                interpolation=cv2.INTER_LINEAR,
            )
        else:
            scaling_factor = 1.0

        return img, float(scaling_factor)

    def preprocess_image(self, img: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Preprocess the input image by resizing and applying adaptive thresholding.

        Args:
            img (np.ndarray): Input image as a numpy array to be preprocessed.

        Returns:
            Tuple[np.ndarray, float]: Preprocessed image as a numpy array and
            the scaling factor applied.
        """
        resized_image, scaling_factor = self._resize_image(img)

        # Check if the image is already in grayscale
        if len(resized_image.shape) == 2:
            gray = resized_image
        else:
            gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        return adaptive_threshold, float(scaling_factor)
