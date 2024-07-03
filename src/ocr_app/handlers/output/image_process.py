import os
from io import BytesIO

from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from .ocr_output import OcrResults

DEFAULT_SAVE_DIR = "results"


class OutputImageProcessor:
    """
    Processes OCR output and generates a PDF document with the recognized images.

    This class takes the output from an OCR process, which includes images stored as numpy arrays,
    and compiles them into a single PDF document. Each page of the PDF corresponds to one image.
    """

    @staticmethod
    def create_pdf_from_numpy_images(
        input: OcrResults,
        output_dir: str = DEFAULT_SAVE_DIR,
        output_filename: str = 'detect_images.pdf',
    ):
        """
        Create a PDF file from a list of images represented as numpy arrays.

        The method reads a list of numpy arrays from the OCR results, converts each array to a PIL Image,
        and adds each image as a separate page in a PDF file stored in the specified output directory.

        Args:
            input (OcrResults): The OCR results containing the images as numpy arrays.
            output_dir (str): The directory to save the output PDF file. Defaults to 'results'.
            output_filename (str): The name of the output PDF file. Defaults to 'detect_images.pdf'.

        Raises:
            OSError: If the directory cannot be created.
        """
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
