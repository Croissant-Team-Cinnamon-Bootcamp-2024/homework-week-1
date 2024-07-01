import os
import pytest
from ocr_app.data_process.input_handler.image_handler import HeicHandler
from ocr_app.data_process.data_model.input_image import OcrImages

IMAGE_SHAPE = 3
NUM_CHANNELS = 3

def test_heic_handler_process(assets_dir):
    heic_file = os.path.join(assets_dir, 'ocr-test.heic')
    file_handler = HeicHandler()
    can_handle = file_handler.can_handle(heic_file)
    assert can_handle

    images = file_handler.process(heic_file)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS

if __name__ == "__main__":
    pytest.main([__file__])
