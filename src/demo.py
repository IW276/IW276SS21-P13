import argparse

import cv2
import numpy as np

from pipeline import Pipeline

parser = argparse.ArgumentParser(description='Automatic white and confession balancing')
parser.add_argument('--datasets_path', type=str)
args = parser.parse_args()

image_names_file = args.datasets_path + "RTTS light/ImageSets/test.txt"
image_results_directory = args.datasets_path + "pipeline-results"

pipeline = Pipeline(image_names_file, image_results_directory)
pipeline.run()

datei = open('../datasets/RTTS light/ImageSets/test.txt', 'r')
print("Datei opened")

for zeile in datei:
    picture_name = "../datasets/RTTS light/JPEGImages/" + zeile[:-1] + ".png"
    picture_name_result = "../datasets/pipeline-results/" + zeile[:-1] + ".png"
    # TODO: Remove or comment print calls after testing
    # print(picture_name)

    width = 600
    height = 400
    dim = (width, height)

    img = cv2.imread(picture_name)
    img = cv2.resize(img, dim)
    img_result = cv2.imread(picture_name_result)
    # img_result = cv2.resize(img_result, dim)
    resultImage = np.concatenate((img, img_result), axis=1)
    height, width = img.shape[:2]
    # TODO: Remove or comment print calls after testing
    # print("width: ", width, "height: ", height)
    cv2.imshow('image', resultImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
datei.close()
print("datei closed!")
