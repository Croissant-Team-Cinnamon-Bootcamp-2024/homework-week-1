import os
from io import BytesIO

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from ocr_app.data_process.data_model.ocr_output import OcrResults

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
    'results',
)
print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


class OutputImageProcessor:
    @staticmethod
    def create_pdf_from_numpy_images(input: OcrResults, output_filename='detect_images.pdf'):
        image_list = input.images
        output_file = os.path.join(FILE_PATH, output_filename)

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
