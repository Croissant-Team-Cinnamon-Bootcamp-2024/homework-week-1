from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="ocr_app",
    version="0.0.1",
    description="A simple OCR app read image and pdf file",
    author="Croissant Team",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=required,
)
