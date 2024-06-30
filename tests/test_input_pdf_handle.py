from ocr_app.data_process.data_model.input_image import OcrImages
from ocr_app.data_process.input_handler.pdf_handler import (DocFileHandler,
                                                    DocxFileHandler,
                                                    PdfFileHandler)

IMAGE_SHAPE = 3
NUM_CHANNELS = 3


def test_pdf_handler_process():
    pdf_file = "./assets/ocr-test.pdf"
    file_handler = PdfFileHandler()
    can_handle = file_handler.can_handle(pdf_file)
    assert can_handle

    images = file_handler.process(pdf_file)
    assert isinstance(images, OcrImages)
    # each image should be in shape [w, h, c]
    assert len(images.image_list[0].shape) == IMAGE_SHAPE
    # num channels should be 3 for RGB image
    assert images.image_list[0].shape[-1] == NUM_CHANNELS


# def test_doc_handler_process():
#     doc_file = "./assets/ocr-test.doc"
#     file_handler = DocFileHandler()
#     can_handle = file_handler.can_handle(doc_file)
#     assert can_handle

#     images = file_handler.process(doc_file)
#     assert isinstance(images, OcrImages)
#     # each image should be in shape [w, h, c]
#     assert len(images.image_list[0].shape) == IMAGE_SHAPE
#     # num channels should be 3 for RGB image
#     assert images.image_list[0].shape[-1] == NUM_CHANNELS


# def test_docx_handler_process():
#     docx_file = "./assets/ocr-test.docx"
#     file_handler = DocxFileHandler()
#     can_handle = file_handler.can_handle(docx_file)
#     assert can_handle

#     images = file_handler.process(docx_file)
#     assert isinstance(images, OcrImages)
#     # each image should be in shape [w, h, c]
#     assert len(images.image_list[0].shape) == IMAGE_SHAPE
#     # num channels should be 3 for RGB image
#     assert images.image_list[0].shape[-1] == NUM_CHANNELS
