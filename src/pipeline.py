from __future__ import print_function
from datetime import datetime

import cv2

from src.analyze_img import evaluate
from src.gamma_correction import adjust_gamma


def read_image(zeile):
    picture_name = "../datasets/RTTS light/JPEGImages/" + zeile[:-1] + ".png"
    # print(picture_name)
    return cv2.imread(picture_name)


def write_result_image(self, zeile, result_img):
    cv2.imwrite(self.pipeline_result_directory + "/" + zeile[:-1] + ".png", result_img)


class Pipeline:
    def __init__(self, image_names_file, image_results_directory):
        self.start_time = None
        self.end_time = None
        self.fps = None
        self.img_count = 0
        self.image_names_file = open(image_names_file, "r")
        self.pipeline_result_directory = image_results_directory

    def run(self):
        self.start_time = datetime.now().timestamp()
        print("Current Time =", self.start_time)
        for zeile in self.image_names_file:
            self.img_count += 1
            img = read_image(zeile)
            image_setup = evaluate(img)
            result_img = adjust_gamma(img, image_setup.brightness)
            write_result_image(self, zeile, result_img)

        self.end_time = datetime.now().timestamp()
        self.fps = self.img_count / (self.end_time - self.start_time)
        print("Frames per Second = ", self.fps)
