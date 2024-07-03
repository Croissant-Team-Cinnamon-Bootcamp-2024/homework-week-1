import argparse
import os

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
    help='input image path (support format .png, .heic, .tiff, .pdf, .doc, .docx)',
)
parser.add_argument(
    '-sd',
    '--secrets-dir',
    type=str,
    required=True,
    help='Path to the secrets directory containing client_secrets.json',
)
parser.add_argument(
    '-rd',
    '--results-dir',
    type=str,
    required=True,
    help='Path to the results directory where OCR output will be saved in local machine',
)
args = parser.parse_args()

# Input data handler
data = InputHandler().read(filepath=args.file)

# OCR model detect
ocr = OCR()
output = ocr.read_text(data)

# Output data handler
OutputHandler.process_output(output, output_dir=args.results_dir)

if GGDRIVE_FOLDER_ID:
    upload_file(GGDRIVE_FOLDER_ID, args.secrets_dir, args.results_dir)
else:
    print(
        "GGDRIVE_FOLDER_ID environment variable not set. Skipping Google Drive upload."
    )
