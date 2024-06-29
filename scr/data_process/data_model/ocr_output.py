from typing import List, Dict
from dataclasses import dataclass

import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from io import BytesIO

FILE_PATH = 'output'

@dataclass
class OcrResults:
    images: List[np.ndarray]
    ocr_outputs: List[List[Dict[str, Dict[str, int]]]]
    
class JsonProcessor():
    def process(input:OcrResults)->None:
        import json
        with open(FILE_PATH+'/'+'detect_result'+'.json','w') as f:
            json.dump(OcrResults.ocr_outputs,f, indent=4)

class ImageProcessor():
    def create_pdf_from_numpy_images(input:OcrResults, output_filename = 'detect_images.pdf', img_width=6*inch):
        image_list = input.images
        c = canvas.Canvas(output_filename)
        
        for i, img_array in enumerate(image_list):
            # Convert numpy array to PIL Image
            img = Image.fromarray(img_array)
            
            # Calculate aspect ratio and height
            aspect_ratio = img.width / img.height
            img_height = img_width / aspect_ratio
            
            # Convert PIL Image to bytes
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            # Add image to the PDF
            c.drawImage(BytesIO(img_byte_arr), x=inch, y=c._pagesize[1]-img_height-inch, width=img_width, height=img_height)
            
            # Add a new page for the next image (except for the last one)
            if i < len(image_list) - 1:
                c.showPage()
        
        c.save()

    # Example usage:
    # Assuming you have a list of numpy arrays called 'image_list'
    # image_list = [np.array(...), np.array(...), ...]

# create_pdf_from_numpy_images(image_list, 'output.pdf')