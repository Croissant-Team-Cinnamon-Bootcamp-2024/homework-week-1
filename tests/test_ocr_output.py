import random
import string
import sys
import os

sys.path.append('../src')
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# import os

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    'results',
)

if not os.path.exists(FILE_PATH):
    print("jhdfbhjsdafgjkkkkjhasfdggfjdshgjhsfghjsfgdhjgfsdhjgsfdjhgshjfdgsfd")
    os.makedirs(FILE_PATH)

import numpy as np
from data_process.data_model.ocr_output import JsonProcessor, OcrResults, OutputImageProcessor


def genInt(l, r):
    return random.randint(l, r)


def generate_arbitrary_string():
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random length between 8 and 12
    length = random.randint(8, 12)

    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


def genImg_text():
    img_size = [genInt(512, 1024), genInt(512, 1024)]
    h, w = img_size
    img = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)
    num_text = genInt(1, 2)
    texts = []
    for _ in range(num_text):
        texts.append(
            {
                "text": generate_arbitrary_string(),
                "location": {
                    "x": genInt(0, w),
                    "y": genInt(0, h),
                    "width": genInt(0, w),
                    "height": genInt(0, h),
                },
            }
        )
    return img, texts


imgs = []
data = []
for page in range(2):
    img, texts = genImg_text()
    imgs.append(img)
    data.append(texts)

def test_JsonProcessor_process():
    print(f"FILE_PATH: {FILE_PATH}")
    JsonProcessor.process(OcrResults(imgs, data))
    expected_file_path = os.path.join(FILE_PATH, 'detect_result.json')
    print(f"Expected file path: {expected_file_path}")
    assert os.path.exists(expected_file_path), f"JSON file {expected_file_path} was not created"
    os.remove(expected_file_path)  # Clean up
test_JsonProcessor_process()

def test_OutputImageProcessor_create_pdf_from_numpy_images():
    OutputImageProcessor.create_pdf_from_numpy_images(OcrResults(imgs, data))
    expected_file_path = os.path.join(FILE_PATH, 'detect_images.pdf')
    assert os.path.exists(expected_file_path), f"PDF file {expected_file_path} was not created"
    os.remove(expected_file_path)  # Clean up
