import pytest
import os
import sys
import time

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ocr_app.handlers.input.input_handler import InputHandler
from ocr_app.handlers.input.ocr_images import OcrImages
from ocr_app.handlers.output.output_handler import OutputHandler
from ocr_app.handlers.output.ocr_output import OcrResults
from ocr_app.model.ocr import OCR

@pytest.fixture
def test_file_path():
    return os.path.join(os.path.dirname(__file__), "../../assets/ocr-test.doc")

def test_ocr_pipeline_integration(test_file_path, tmp_path):
    output_dir = tmp_path / "results"

    # Step 1: Input Handling
    input_handler = InputHandler()
    data = input_handler.read(filepath=test_file_path)
    
    assert isinstance(data, OcrImages), "InputHandler should return OcrImages object"
    assert hasattr(data, 'image_list'), "Returned object should have 'image_list' attribute"

    # Step 2: OCR Processing
    ocr = OCR()
    output = ocr.read_text(data)
    
    assert isinstance(output, OcrResults), "OCR should return OcrResults object"
    assert hasattr(output, 'images') and hasattr(output, 'ocr_outputs'), "OCR output should have 'images' and 'ocr_outputs' attributes"

    # Step 3: Output Handling
    OutputHandler.process_output(output, output_dir=str(output_dir))

    # Add a small delay to ensure file operations are complete
    time.sleep(1)

    # Assertions to verify the output
    assert output_dir.exists(), "Output directory should be created"
    
    # Check if JSON file is created
    json_file = output_dir / "detect_result.json"
    assert json_file.exists(), f"JSON output file {json_file} should be created"

    # Check if PDF file is created
    pdf_file = output_dir / "detect_images.pdf"
    assert pdf_file.exists(), "PDF output file should be created"

# Clean-up is automatic with tmp_path fixture

if __name__ == "__main__":
    pytest.main([__file__])
