import mimetypes
import os
import platform
import subprocess
from pathlib import Path

import fitz
import numpy as np
from PIL import Image

from ..data_model.input_image import OcrImages
from .image_handler import BaseFileHandler


class PdfFileHandler(BaseFileHandler):
    def process(self, filepath: str) -> OcrImages:
        images = []
        document = fitz.open(filepath)
        for page in document:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(np.array(img))
        document.close()
        return OcrImages(image_list=images)

    def can_handle(self, filepath: str) -> bool:
        mime_text = "application/pdf"
        guess_mime_type, _ = mimetypes.guess_type(filepath)
        return mime_text == guess_mime_type


class DocumentFileHandler(PdfFileHandler):
    def process(self, filepath: str) -> OcrImages:
        pdf_filepath = self.convert_to_pdf(filepath)
        if pdf_filepath:
            return super().process(pdf_filepath)
        else:
            print(f"Conversion failed for {filepath}")
            return OcrImages(image_list=[])

    def can_handle(self, filepath: str) -> bool:
        ext = Path(filepath).suffix.lower()
        return ext in ('.doc', '.docx')

    def convert_to_pdf(self, input_filepath: str) -> str:
        """Converts a document file to PDF."""
        if platform.system() == 'Windows':
            return self.convert_using_word(input_filepath)
        elif platform.system() == 'Linux':
            return self.convert_using_libreoffice(input_filepath)
        else:
            print(f"Unsupported operating system: {platform.system()}")
            return None

    def convert_using_word(self, doc_filepath: str) -> str:
        """Converts a DOC file to PDF using Microsoft Word."""
        try:
            import comtypes.client

            word = comtypes.client.CreateObject('Word.Application')
            doc_path = os.path.abspath(doc_filepath)
            temp_dir = os.environ['TEMP']
            pdf_path = os.path.join(
                temp_dir, f"{os.path.splitext(os.path.basename(doc_path))[0]}.pdf"
            )

            doc = word.Documents.Open(doc_path)
            doc.SaveAs(pdf_path, FileFormat=17)  # 17 corresponds to PDF format
            doc.Close()
            word.Quit()
            print(f"Converted {doc_filepath} to {pdf_path} successfully.")
            return pdf_path
        except Exception as e:
            print(f"Error converting {doc_filepath} to PDF: {str(e)}")
            return None

    def convert_using_libreoffice(self, docx_filepath: str) -> str:
        """Converts a document file to PDF using LibreOffice."""
        try:
            doc_path = os.path.abspath(docx_filepath)
            temp_dir = '/tmp'
            pdf_path = os.path.join(
                temp_dir, f"{os.path.splitext(os.path.basename(doc_path))[0]}.pdf"
            )

            # Construct the command for LibreOffice
            command = [
                'libreoffice',
                '--headless',
                '--convert-to',
                'pdf',
                doc_path,
                '--outdir',
                temp_dir,
            ]
            subprocess.run(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
            )

            print(f"Converted {docx_filepath} to {pdf_path} successfully.")
            return pdf_path
        except subprocess.CalledProcessError as e:
            print(f"Error converting {docx_filepath} to PDF: {e.stderr.decode()}")
            return None
