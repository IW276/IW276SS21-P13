import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_multiotsu
from skimage.restoration import estimate_sigma

brightness = {"DARK": 0,
              "NORMAL": 1,
              "LIGHT": 2}

contrast = {"HIGH": 2,
            "NORMAL": 1,
            "LOW": 0}

noise = {"NOISY": 1,
         "DEFAULT": 0}


class ImageSetup:
    def __init__(self):
        self.brightness = None
        self.contrast = None
        self.gamma = 1
        # grayscale values
        self.average = -1
        self.std_deviation = -1
        self.threshold = -1
        # saturation values
        self.sat_average = -1
        self.sat_std_deviation = -1
        self.sat_threshold = -1
        # noise
        self.noise = noise["DEFAULT"]
        self.val_noise = -1


def average(img2d):
    rows, cols = img2d.shape
    m = np.mean(img2d[0:rows, 0:cols])
    return m


def variance_std_deviation(img2d):
    # variance
    v = np.var(img2d)
    # standard deviation
    s = np.sqrt(v)
    return v, s


def histogram(img2d, name=None, plot=False):
    hist = cv2.calcHist([img2d], [0], None, [256], [0, 256])
    if plot:
        plt.hist(img2d.ravel(), 256, [0, 256])
        plt.xlabel(name)
        plt.show()
    hist_norm = hist.ravel() / hist.sum()
    return hist, hist_norm


def threshold(img2d):
    # return is the threshold value followed by the result image
    thr, o1 = cv2.threshold(img2d, 0, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C + cv2.THRESH_OTSU)
    return thr


def multi_thresholding(img2d):
    thresholds = threshold_multiotsu(img2d)
    # thresholds is an array with two elements
    return thresholds


def estimate_noise(img2d):
    sigma = estimate_sigma(img2d)
    # sigma is a value that describes the noise
    return sigma


class Configuration:
    def __init__(self, image):
        self.img = image
        self.imgGray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.imgHSV = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.rows, self.cols, self.cha = self.img.shape
        self.pixels = self.cols * self.rows
        self.imgSetup = ImageSetup()
        self.th = None

    def get_brightness(self):
        m = average(self.imgGray)
        if m < 100:
            self.imgSetup.brightness = brightness["DARK"]
        elif 100 < m < 150:
            self.imgSetup.brightness = brightness["NORMAL"]
        else:
            self.imgSetup.brightness = brightness["LIGHT"]
        self.imgSetup.average = m

    def get_saturation(self):
        m_sat = average(self.imgHSV[:, :, 1])
        s2, s = variance_std_deviation(self.imgHSV[:, :, 1])
        self.imgSetup.sat_average = m_sat
        self.imgSetup.sat_std_deviation = s

    def get_contrast(self):
        s2, s = variance_std_deviation(self.imgGray)
        if s >= 70:
            self.imgSetup.contrast = contrast["HIGH"]
        elif s >= 40:
            self.imgSetup.contrast = contrast["NORMAL"]
        else:
            self.imgSetup.contrast = contrast["LOW"]
        self.imgSetup.std_deviation = s

    def get_thresholds(self, do_print=False):
        gray_thresh = threshold(self.imgGray)
        sat_thresh = threshold(self.imgHSV[:, :, 1])
        self.imgSetup.threshold = gray_thresh
        self.imgSetup.sat_threshold = sat_thresh
        self.th = multi_thresholding(self.imgGray)
        if do_print:
            print("thresholds multi otsu: ", self.th)

    def get_noise(self):
        n = estimate_noise(self.imgGray)
        # n > 10 noisy image otherwise not
        if n < 10.0:
            self.imgSetup.noise = noise["NOISY"]
        self.imgSetup.val_noise = n

    def print_values(self, do_print=True):
        if do_print:
            print("Average brightness: " + str(self.imgSetup.average))
            print("Standard deviation: " + str(self.imgSetup.std_deviation))
            print("Average saturation: " + str(self.imgSetup.sat_average))
            print("Std. deviation sat: " + str(self.imgSetup.sat_std_deviation))
            print("Threshold gray: " + str(self.imgSetup.threshold))
            print("Threshold sat: " + str(self.imgSetup.sat_threshold))
            print("Brightness: " + str(self.imgSetup.brightness))
            print("Contrast: " + str(self.imgSetup.contrast))

    def show(self, show=True):
        if show:
            cv2.imshow("Color", self.img)
            cv2.waitKey(0)
            cv2.imshow("Gray", self.imgGray)
            cv2.waitKey(0)
            cv2.imshow("Saturation", self.imgHSV[:, :, 1])
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def evaluate(img):
    c = Configuration(img)
    c.get_brightness()
    c.get_contrast()
    histogram(c.imgGray, "gray")
    histogram(c.imgHSV[:, :, 1], "saturation")
    c.get_saturation()
    c.get_thresholds()
    c.get_noise()
    c.print_values(False)
    c.show(False)
    return c.imgSetup
