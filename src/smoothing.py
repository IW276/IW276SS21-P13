import matplotlib.pyplot as plt
import analyze_img as ana
import urllib.request as req
import numpy as np
import os
import cv2


os.remove('test.jpg')
req.urlretrieve("https://service.ka-news.de/tools/webcams/?cam=27", "test.jpg")
img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)  # BGR

filter = {"MEAN": 0,
          "GAUSSIAN": 1}


class Filter:

    def __init__(self, image):
        self.img = image
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.height, self.width = self.imgGray.shape

    def average_filter(self):
        blur = cv2.blur(self.imgGray, (5, 5))
        return blur

    def gaussian_filter(self):
        blur = cv2.GaussianBlur(self.imgGray, (5, 5), 0)
        return blur

    def median_filter(self):
        blur = cv2.medianBlur(self.imgGray, 5)
        return blur

    def bilateral_filter(self):
        bil = cv2.bilateralFilter(self.imgGray, 10, 40, 40)
        return bil

    def filter(self):
        kernel = np.array(([1, 4, 1], [4, 16, 4], [1, 4, 1]), np.float32) / 36
        dst = cv2.filter2D(self.imgGray, -1, kernel)
        return dst


def main():
    # setup = ana.evaluate()
    f = Filter(img)
    dst = f.gaussian_filter()
    cv2.imshow("org", f.imgGray)
    cv2.waitKey(0)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    main()
