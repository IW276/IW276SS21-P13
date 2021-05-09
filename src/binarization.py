import urllib.request
import os
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

#method calculates a binary image, with a given, fixed threshold value
def bina_fixed_threshold(image, threshold):
    ret, thresh1 = cv2.threshold(image, threshold , 255, cv2.THRESH_BINARY)
    return thresh1

#adaptive calculation; threshold value is the mean of neighbourhood area
#blocksize: decides the size of the neighbourhood area
def bina_adapt_mean_threshold(image):
    blocksize = 11
    thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blocksize,2)
    return thresh2

#flag TRESH_OTSU is set, so the algorithm finds the optimal threshold value, which is given in ret
def bina_otsu(image):
    ret,tresh3 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return tresh3





