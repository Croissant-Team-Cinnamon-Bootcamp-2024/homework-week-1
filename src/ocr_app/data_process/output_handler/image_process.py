import os
from io import BytesIO

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from ..data_model.ocr_output import OcrResults

DEFAULT_SAVE_DIR = "results"


class OutputImageProcessor:
    @staticmethod
    def create_pdf_from_numpy_images(
        input: OcrResults,
        output_dir: str = DEFAULT_SAVE_DIR,
        output_filename: str = 'detect_images.pdf',
    ):
        image_list = input.images

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, output_filename)

        # Create a PDF with the first page
        first_img = Image.fromarray(image_list[0])
        c = canvas.Canvas(output_file, pagesize=(first_img.width, first_img.height))

        for img_array in image_list:
            # Convert numpy array to PIL Image
            img = Image.fromarray(img_array)

            # Set the page size to match the image dimensions
            c.setPageSize((img.width, img.height))

            # Convert PIL Image to bytes
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)  # Reset the buffer position

            # Use ImageReader to handle BytesIO
            img_reader = ImageReader(img_byte_arr)

            # Draw the image on the entire page
            c.drawImage(
                img_reader,
                x=0,
                y=0,
                width=img.width,
                height=img.height,
            )

            # Move to the next page
            c.showPage()

        # Save the PDF
        c.save()
