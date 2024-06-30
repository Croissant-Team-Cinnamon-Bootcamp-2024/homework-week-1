import os
from dataclasses import dataclass
from io import BytesIO
from typing import Dict, List

import numpy as np
from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

FILE_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    ),
    'results',
)
print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


@dataclass
class OcrResults:
    images: List[np.ndarray]
    ocr_outputs: List[List[Dict[str, Dict[str, int]]]]


class JsonProcessor:
    def process(input: OcrResults) -> None:
        print("in process")
        import json

        print(f"FILE_PATH: {FILE_PATH}")

        print("ok")
        output_file = os.path.join(FILE_PATH, 'detect_result.json')
        print(f"output_file: {output_file}")
        with open(output_file, 'w') as f:
            json.dump(input.ocr_outputs, f, indent=4)


from reportlab.lib.utils import ImageReader


class OutputImageProcessor:
    @staticmethod
    def create_pdf_from_numpy_images(
        input: OcrResults, output_filename='detect_images.pdf', img_width=6 * inch
    ):
        image_list = input.images
        output_file = os.path.join(FILE_PATH, output_filename)
        c = canvas.Canvas(output_file)

        for i, img_array in enumerate(image_list):
            # Convert numpy array to PIL Image
            img = Image.fromarray(img_array)

            # Calculate aspect ratio and height
            aspect_ratio = img.width / img.height
            img_height = img_width / aspect_ratio

            # Convert PIL Image to bytes
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)  # Reset the buffer position

            # Use ImageReader to handle BytesIO
            img_reader = ImageReader(img_byte_arr)

            # Add image to the PDF
            c.drawImage(
                img_reader,
                x=inch,
                y=c._pagesize[1] - img_height - inch,
                width=img_width,
                height=img_height,
            )

            # Add a new page for the next image (except for the last one)
            if i < len(image_list) - 1:
                c.showPage()

        c.save()
