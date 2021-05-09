import cv2
from src.pipeline import Pipeline



# Funktion öffnet eine Textdatei, welche dateinamen von Bildern enthält. Diese
# Bilder werden mittels cv geöffnet und angezeigt


def open_pics():
    image_names_file = "../datasets/RTTS light/ImageSets/test.txt"
    datei = open('../datasets/RTTS light/ImageSets/test.txt', 'r')
    pipeline = Pipeline(image_names_file)
    print("Datei opened")
    for zeile in datei:
        picture_name = "../datasets/RTTS light/JPEGImages/" + zeile[:-1] + ".png"
        print(picture_name)
        img = cv2.imread(picture_name)

        height, width = img.shape[:2]
        print("width: ", width, "height: ", height)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    datei.close()
    print("datei closed!")


#open_pics()
