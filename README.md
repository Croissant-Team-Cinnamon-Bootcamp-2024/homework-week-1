# Homework Week 1: OCR App

## Introduction

This is an OCR app that could read all document and images and extract the texts and their corresponding locations in a json file. This app is helpful for information extraction to digital formats, making them easier to store, search, and manage. This app can support different input file types, such as: ``.png``, ``.heic``, ``.tiff``, ``.pdf``, ``.doc``, ``.docx``.

This app utilizes different tech stacks:
- **Read images/docs**: mimetypes, pillow, pillow-heif, PyMuPDF
- **Preprocess images**: numpy
- **Text detection**: opencv-python
- **Text extraction**: pytesseract
- **Save and store outputs**: os, json

## App design


![alt text](docs/code_design.jpg)

### Workflow
1. **Image read and preprocessing**:
- The system accepts various file types (png, heic, tiff, pdf, doc) as input images.
- The ``InputHandler`` reads the file and delegates processing to the appropriate file handler based on the file type. The selected handler processes the file and converts it into an ``OcrImages`` object containing preprocessed image data.
- ``DataPreprocess`` resizes and preprocesses the images to prepare them for OCR.

2. **OCR Model**:
- The ``OCR`` class uses the preprocessed images to extract text lines and generate an ``OcrResults`` object.

3. **Process Output**:
- OutputHandler processes the ``OcrResults`` object from the previous step.
- The ``JsonProcessor`` and ``OutputImageProcessor`` handle converting the OCR results to JSON and PDF formats, respectively.

4. **Uploading**:
The processed output (JSON and/or PDF) is uploaded to a drive using the ``drive_upload`` function.

## Set up

### Clone this repository
```bash
git clone https://github.com/Croissant-Team-Cinnamon-Bootcamp-2024/homework-week-1.git
cd homework-week-1
```

### Install Dependencies

For Linux, run
```
sudo apt-get install tesseract-ocr
pip install .
```

For Windows, follow the below steps
- Download Tesseract installer for Windows: https://github.com/UB-Mannheim/tesseract/wiki
- Add the path to the directory of Tesseract folder (normally is: ```C:\Program Files\Tesseract-OCR```) to the System Environment Variables (edit the Path variable, click on **New** button and paste the path above).
- Run ```pip install .```


## Run OCR script

For Linux, run
```bash
export GGDRIVE_FOLDER_ID=<Google Drive Folder ID>
# Run your own file by changing the path after -f
python scripts/run.py -f assets/ocr-test.pdf
```

For Windows, run
```bash
set GGDRIVE_FOLDER_ID=<Google Drive Folder ID>
# Run your own file by changing the path after -f
python scripts/run.py -f assets/ocr-test.pdf
```
