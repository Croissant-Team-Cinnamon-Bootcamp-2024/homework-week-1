import random
import string
import sys
sys.path.append('../src')

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
    JsonProcessor.process(OcrResults(imgs, data))


def test_OutputImageProcessor_create_pdf_from_numpy_images():
    OutputImageProcessor.create_pdf_from_numpy_images(OcrResults(imgs, data))


test_JsonProcessor_process()
test_OutputImageProcessor_create_pdf_from_numpy_images()
