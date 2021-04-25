import urllib.request
import cv2
import os

os.remove("test.jpg")
urllib.request.urlretrieve("https://service.ka-news.de/tools/webcams/?cam=27", "test.jpg")
img = cv2.imread('test.jpg', 0)
img2 = cv2.imread('test.jpg', 1)
img = cv2.imread('test.jpg', 2)
cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
