import os

from ocr_app.handlers.input.input_handler import InputHandler
from ocr_app.handlers.output.drive_upload import upload_file
from ocr_app.handlers.output.output_handler import OutputHandler
from ocr_app.model.ocr import OCR

GGDRIVE_FOLDER_ID = os.getenv('GGDRIVE_FOLDER')

data = InputHandler().read(filepath="assets/ocr-test.docx")
print(data)
ocr = OCR()
output = ocr.read_text(data)
OutputHandler.process_output(output)

upload_file(GGDRIVE_FOLDER_ID)
