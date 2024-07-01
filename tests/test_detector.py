import numpy as np
import pytest
from PIL import Image

from ocr_app.model.detector import TextDetector


@pytest.fixture
def sample_image():
    # Provide a sample image for testing
    img = Image.new('RGB', (1000, 1000), color=(73, 109, 137))
    return np.array(img)


def test_resize_image(sample_image):
    detector = TextDetector()
    resized_img, scaling_factor = detector._resize_image(sample_image)
    assert isinstance(resized_img, np.ndarray)
    assert isinstance(scaling_factor, float)


def test_preprocess_image(sample_image):
    detector = TextDetector()
    preprocessed_image, scaling_factor = detector.preprocess_image(sample_image)
    assert isinstance(preprocessed_image, np.ndarray)
    assert isinstance(scaling_factor, float)
    
if __name__ == "__main__":
    pytest.main()