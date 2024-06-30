import random
import string
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
FILE_PATH = os.path.join(project_root, 'results')

print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    print("jhdfbhjsdafgjkkkkjhasfdggfjdshgjhsfghjsfgdhjgfsdhjgsfdjhgshjfdgsfd")
    os.makedirs(FILE_PATH)

import numpy as np
from ocr_app.data_process.data_model.ocr_output import JsonProcessor, OcrResults, OutputImageProcessor


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
    # print(f"FILE_PATH: {FILE_PATH}")
    imgs, data = genImg_text()
    JsonProcessor.process(OcrResults(imgs, data))
    expected_file_path = os.path.join(FILE_PATH, 'detect_result.json')
    print(f"Expected file path: {expected_file_path}")
    # assert os.path.exists(expected_file_path), f"JSON file {expected_file_path} was not created"
    # os.remove(expected_file_path)  # Clean up
# test_JsonProcessor_process()
imgs, data = genImg_text()
print(JsonProcessor.process(OcrResults(imgs, data)))

def test_OutputImageProcessor_create_pdf_from_numpy_images():
    OutputImageProcessor.create_pdf_from_numpy_images(OcrResults(imgs, data))
    expected_file_path = os.path.join(FILE_PATH, 'detect_images.pdf')
    # assert os.path.exists(expected_file_path), f"PDF file {expected_file_path} was not created"
    # os.remove(expected_file_path)  # Clean up
test_OutputImageProcessor_create_pdf_from_numpy_images()
