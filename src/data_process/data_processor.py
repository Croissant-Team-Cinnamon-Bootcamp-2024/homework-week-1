from .image_handler import (
    PngFileHandler, 
    HeicFileHandler, 
    TiffFileHandler
)
import numpy as np


class ImageFileHandler(object):
    def __init__(self) -> None:
        self.list_handlers = [
            PngFileHandler(),
            HeicFileHandler(),
            TiffFileHandler()
        ]
    
    def process_image(self, filepath: str) -> np.array:
        image = None
        for handler in self.list_handlers: 
            if handler.can_handle(filepath):
                image = handler.process(filepath)
                break
        if image is None:
            raise NotImplementedError(f"File {filepath}: format is not supported!")
        return image