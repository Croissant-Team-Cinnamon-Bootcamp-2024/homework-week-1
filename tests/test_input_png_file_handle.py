from ocr_app.data_process.data_model.input_image import OcrImages
from ocr_app.data_process.input_handler.image_handler import (PngFileHandler,
                                                    HeicFileHandler,
                                                    TiffFileHandler)

IMAGE_SHAPE = 3
NUM_CHANNELS = 3

def test_png_handler_process():
    png_file = "./assets/ocr-test.png"
    file_handler = PngFileHandler()
    can_handle = file_handler.can_handle(png_file)
    assert can_handle
    
    images = file_handler.process(png_file)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS
    

def test_heic_handler_process():
    heic_file = "./assets/ocr-test.heic"
    file_handler = HeicFileHandler()
    can_handle = file_handler.can_handle(heic_file)
    assert can_handle
    
    images = file_handler.process(heic_file)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS
 
def test_tiff_handler_process():
    tiff_file = "./assets/ocr-test.tiff"
    file_handler = TiffFileHandler()
    can_handle = file_handler.can_handle(tiff_file)
    assert can_handle
    
    images = file_handler.process(tiff_file)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS
 
    