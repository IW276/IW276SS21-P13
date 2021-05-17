import argparse
import os

import cv2
import numpy as np

from pipeline import Pipeline

parser = argparse.ArgumentParser(description='Automatic white balancing and exposure compensation.')
parser.add_argument('--datasets-path', type=str)
args = parser.parse_args()

datasets_path = args.datasets_path

image_names_file = os.path.join(datasets_path, "RTTS light", "ImageSets", "test.txt")
image_results_directory = os.path.join(datasets_path, "pipeline-results")

pipeline = Pipeline(datasets_path, image_names_file, image_results_directory)
pipeline.run()

datei = open(image_names_file, 'r')
print("Datei opened")

for zeile in datei:
    picture_name = os.path.join(datasets_path, "RTTS light", "JPEGImages", zeile[:-1] + ".png")
    picture_name_result = os.path.join(datasets_path, "pipeline-results", zeile[:-1] + ".png")

    dim = (600, 400)

    img = cv2.imread(picture_name)
    img = cv2.resize(img, dim)
    img_result = cv2.imread(picture_name_result)
    img_result = cv2.resize(img_result, dim)
    resultImage = np.concatenate((img, img_result), axis=1)
    height, width = img.shape[:2]
    cv2.imshow('image', resultImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
datei.close()
print("datei closed!")
