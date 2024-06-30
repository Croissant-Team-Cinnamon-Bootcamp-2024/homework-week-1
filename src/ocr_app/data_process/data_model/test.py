import random
import string

import numpy as np


def generate_arbitrary_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(8, 12)
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def generate_random_int(L, r):
    return random.randint(L, r)


def genImg_text():
    img_size = [generate_random_int(512, 1024), generate_random_int(512, 1024)]
    h, w = img_size
    img = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)
    num_text = generate_random_int(1, 2)
    texts = []
    for _ in range(num_text):
        texts.append(
            {
                "text": generate_arbitrary_string(),
                "location": {
                    "x": generate_random_int(0, w),
                    "y": generate_random_int(0, h),
                    "width": generate_random_int(0, w),
                    "height": generate_random_int(0, h),
                },
            }
        )
    return img, texts
