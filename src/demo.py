import urllib.request
import cv2
import os

urllib.request.urlretrieve("https://service.ka-news.de/tools/webcams/?cam=27", "test.jpg")
img = cv2.imread('test.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
try:
    os.remove("test.jpg")
except FileNotFoundError:
    print("Test.jpg does not exist")
