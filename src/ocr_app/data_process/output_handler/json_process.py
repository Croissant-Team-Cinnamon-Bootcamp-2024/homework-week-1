import os

from ocr_app.data_process.data_model.ocr_output import OcrResults

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
    'results',
)
print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


class JsonProcessor:
    @staticmethod
    def process(input: OcrResults) -> int:
        print("in process")
        import json

        print(f"FILE_PATH: {FILE_PATH}")

        print("ok")
        output_file = os.path.join(FILE_PATH, 'detect_result.json')
        print(f"output_file: {output_file}")
        with open(output_file, 'w') as f:
            json.dump(input.ocr_outputs, f, indent=4)
        return 1234


# print(JsonProcessor.process(tmp))
# JsonProcessor.process(tmp)
