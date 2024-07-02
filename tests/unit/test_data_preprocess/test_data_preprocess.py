import numpy as np
import pytest
from PIL import Image

from ocr_app.model.data_preprocess import DataPreprocess


@pytest.fixture
def sample_image():
    # Provide a sample image for testing
    img = Image.new('RGB', (1000, 1000), color=(73, 109, 137))
    return np.array(img)


def test_resize_image(sample_image):
    processor = DataPreprocess()
    resized_img, scaling_factor = processor._resize_image(sample_image)
    assert isinstance(resized_img, np.ndarray)
    assert isinstance(scaling_factor, float)


def test_preprocess_image(sample_image):
    processor = DataPreprocess()
    preprocessed_image, scaling_factor = processor.preprocess(sample_image)
    assert isinstance(preprocessed_image, np.ndarray)
    assert isinstance(scaling_factor, float)
    
if __name__ == "__main__":
    pytest.main()
