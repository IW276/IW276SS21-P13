import cv2
import numpy as np


def adjust_gamma(image, brightness=127):
    if not 127 - 2 <= brightness <= 127 + 2:
        gamma = 2 - (brightness / 255)
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)
    else:
        return image
