import random
import string
import os

import numpy as np
from ocr_app.data_process.data_model.ocr_output import OcrResults
from ocr_app.data_process.output_handler.json_process import JsonProcessor
from ocr_app.data_process.output_handler.image_process import OutputImageProcessor


def generate_arbitrary_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(8, 12)
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_random_int(l, r):
    return random.randint(l, r)

def genImg_text():
    img_size = [generate_random_int(512, 1024), generate_random_int(512, 1024)]
    h, w = img_size
    img = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)
    num_text = generate_random_int(1, 2)
    texts = []
    for _ in range(num_text):
        texts.append(
            {
                "text": generate_arbitrary_string(),
                "location": {
                    "x": generate_random_int(0, w),
                    "y": generate_random_int(0, h),
                    "width": generate_random_int(0, w),
                    "height": generate_random_int(0, h),
                },
            }
        )
    return img, texts


def test_JsonProcessor_process():
    imgs, data = genImg_text()
    dummy_model_output = OcrResults(imgs, data)
    
    save_dir = "./results"
    expected_file_path = os.path.join(save_dir, 'detect_result.json')
    
    JsonProcessor.process(
        input=dummy_model_output, 
        output_dir=save_dir,
    )
    assert os.path.exists(expected_file_path), f"JSON file {expected_file_path} was not created"
    os.remove(expected_file_path)  # Clean up


def test_OutputImageProcessor_create_pdf_from_numpy_images():
    imgs, data = genImg_text()
    dummy_model_output = OcrResults(imgs, data)
    
    save_dir = "./results"
    expected_file_path = os.path.join(save_dir, 'detect_images.pdf')
    
    OutputImageProcessor.create_pdf_from_numpy_images(
        input=dummy_model_output,
        output_dir=save_dir,
    )
    
    assert os.path.exists(expected_file_path), f"Image pdf file {expected_file_path} was not created"
