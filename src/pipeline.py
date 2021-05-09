from __future__ import print_function

import cv2

from src.analyze_img import evaluate
from src.gamma_correction import adjust_gamma


class Pipeline:
    def __init__(self, image_names_file, image_results_directory):
        self.image_names_file = open(image_names_file, "r")
        self.pipeline_result_directory = image_results_directory

    def run(self):
        for zeile in self.image_names_file:
            picture_name = "../datasets/RTTS light/JPEGImages/" + zeile[:-1] + ".png"
            print(picture_name)
            img = cv2.imread(picture_name)
            image_setup = evaluate(img)
            result_img = adjust_gamma(img, image_setup.brightness)
            cv2.imwrite(self.pipeline_result_directory + "/" + zeile[:-1] + ".png", result_img)
