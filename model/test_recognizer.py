import pytest
from PIL import Image
import numpy as np
from .detector import TextDetector
from .recognizer import TextRecognizer

@pytest.fixture
def sample_image():
    # Provide a sample image for testing
    img = Image.new('RGB', (1000, 1000), color=(73, 109, 137))
    return img

@pytest.fixture
def sample_preprocessed_image(sample_image):
    detector = TextDetector()
    preprocessed_image, scaling_factor = detector.preprocess_image(sample_image)
    return preprocessed_image, scaling_factor

def test_extract_text_lines(sample_preprocessed_image):
    recognizer = TextRecognizer()
    preprocessed_image, scaling_factor = sample_preprocessed_image
    text_lines = recognizer.extract_text_lines(preprocessed_image, scaling_factor)
    assert isinstance(text_lines, list)
    assert len(text_lines) >= 0  # Assuming there might be no text in the sample image
    for line in text_lines:
        assert "text" in line
        assert "location" in line
        assert isinstance(line["location"], dict)

if __name__ == "__main__":
    pytest.main()
