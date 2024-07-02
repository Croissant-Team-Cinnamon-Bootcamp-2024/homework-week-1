import os
import argparse

from ocr_app.handlers.input.input_handler import InputHandler
from ocr_app.handlers.output.drive_upload import upload_file
from ocr_app.handlers.output.output_handler import OutputHandler
from ocr_app.model.ocr import OCR

GGDRIVE_FOLDER_ID = os.environ.get('GGDRIVE_FOLDER_ID')

parser = argparse.ArgumentParser(description='Run OCR app.')

parser.add_argument(
    '-f',
    '--file',
    type=str,
    required=True,
    help='input image path (support format .png, .heic, .tiff, .pdf, .doc, .docx)'
)

args = parser.parse_args()


## Input data handler
data = InputHandler().read(filepath=args.file)

## OCR model detect
ocr = OCR()
output = ocr.read_text(data)

## Output data handler
OutputHandler.process_output(output)

if GGDRIVE_FOLDER_ID:
    upload_file(GGDRIVE_FOLDER_ID)
