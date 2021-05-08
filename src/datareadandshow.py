import cv2
import numpy
# Funktion öffnet eine Textdatei, welche dateinamen von Bildern enthält. Diese
# Bilder werden mittels cv geöffnet und angezeigt


def open_pics():
    datei = open('../datasets/RTTS light/ImageSets/test.txt', 'r')
    print("Datei opened")
    for zeile in datei:
        picture_name = "../datasets/RTTS light/JPEGImages/" + zeile[:-1] + ".png"
        print(picture_name)
        img = cv2.imread(picture_name)
        height, width = img.shape[:2]
        heights = str(height)
        widths = str(width)
        print("width: ", width, "height: ", height)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    datei.close()
    print("datei closed!")

open_pics()

