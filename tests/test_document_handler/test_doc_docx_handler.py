import os
import pytest
from ocr_app.data_process.data_model.input_image import OcrImages
from ocr_app.data_process.input_handler.pdf_handler import DocumentHandler

IMAGE_SHAPE = 3
NUM_CHANNELS = 3

@pytest.mark.parametrize("doc_file", [
    "ocr-test.doc",
    "ocr-test.docx"
])
def test_document_handler_process(assets_dir, doc_file):
    doc_file_path = os.path.join(assets_dir, doc_file)
    file_handler = DocumentHandler()
    can_handle = file_handler.can_handle(doc_file_path)
    assert can_handle

    images = file_handler.process(doc_file_path)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS

if __name__ == "__main__":
    pytest.main([__file__])
