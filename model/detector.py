import cv2
import numpy as np
from PIL import Image

class TextDetector:
    def resize_image(self, image: Image.Image, max_size: tuple = (2000, 2000)) -> tuple:
        img = np.array(image)
        height, width = img.shape[:2]

        if height > max_size[0] or width > max_size[1]:
            scaling_factor = min(max_size[0] / height, max_size[1] / width)
            img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        elif height < 800 or width < 800:
            scaling_factor = max(800 / height, 800 / width)
            img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)
        else:
            scaling_factor = 1.0

        return Image.fromarray(img), float(scaling_factor)

    def preprocess_image(self, image: Image.Image) -> tuple:
        resized_image, scaling_factor = self.resize_image(image)
        img = np.array(resized_image)

        # Check if the image is already in grayscale
        if len(img.shape) == 2:
            gray = img
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        adaptive_threshold = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        return adaptive_threshold, float(scaling_factor)

