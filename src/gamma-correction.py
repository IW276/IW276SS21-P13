# import the necessary packages
from __future__ import print_function
import numpy as np
import cv2


def adjust_gamma(image, gamma=1):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


img = cv2.imread('../datasets/test-1.jpeg', 0)
img = cv2.imread('../datasets/test.jpg', 0)
# img2 = cv2.imread('../datasets/test-1.jpeg', 0)
img2 = cv2.imread('../datasets/test.jpg', 0)
# img2 = cv2.imread('../datasets/test-1.jpeg', 0)
result = adjust_gamma(img2)
resultImage = np.concatenate((img, result), axis=1)
cv2.imshow('images', resultImage)

cv2.waitKey(0)
