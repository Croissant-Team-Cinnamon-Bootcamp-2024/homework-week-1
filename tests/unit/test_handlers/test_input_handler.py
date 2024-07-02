# this is a whole intergration
from ocr_app.model.data_preprocess import DataPreprocess
from ocr_app.model.ocr import OCR
from ocr_app.handlers.input_handler.input_handler import InputHandler
from ocr_app.handlers.output_handler.output_handler import OutputHandler, OcrResults

data = InputHandler().read(filepath="../assets/ocr-test.doc")
print(data)

# This is a input -> model part
ocr = OCR()
output = ocr.read_text(data)

# this is a model -> output part

OutputHandler.process_output(output)



