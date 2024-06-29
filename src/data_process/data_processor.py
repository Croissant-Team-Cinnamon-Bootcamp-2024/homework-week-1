import numpy as np

from .input_handler.image_handler import (
    HeicFileHandler,
    PngFileHandler,
    TiffFileHandler,
)


class ImageFileHandler(object):
    def __init__(self) -> None:
        self.list_handlers = [
            PngFileHandler(),
            HeicFileHandler(),
            TiffFileHandler(),
        ]

    def process_image(self, filepath: str) -> np.array:
        image = None
        try:
            for handler in self.list_handlers:
                if handler.can_handle(filepath):
                    image = handler.process(filepath)
                    break
            if image is None:
                raise NotImplementedError(f"File {filepath}: not supported!")
        except Exception as e:
            print(f"Error input file handler: {e}")
        return image
