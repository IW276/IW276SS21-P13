import cv2
import numpy as np


class Filter:

    def __init__(self, image):
        self.img = image
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.height, self.width = self.imgGray.shape

    def average_filter(self):
        blur = cv2.blur(self.imgGray, (5, 5))
        return cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

    def gaussian_filter(self):
        blur = cv2.GaussianBlur(self.imgGray, (5, 5), 0)
        return cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

    def median_filter(self):
        blur = cv2.medianBlur(self.imgGray, 5)
        return cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)

    def bilateral_filter(self):
        bil = cv2.bilateralFilter(self.imgGray, 10, 40, 40)
        return cv2.cvtColor(bil, cv2.COLOR_GRAY2BGR)

    def filter(self):
        kernel = np.array(([1, 4, 1], [4, 16, 4], [1, 4, 1]), np.float32) / 36
        dst = cv2.filter2D(self.imgGray, -1, kernel)
        return cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
