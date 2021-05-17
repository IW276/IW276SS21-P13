from __future__ import print_function

import os
from datetime import datetime

import cv2

from analyze_img import evaluate
from binarization import bina_adapt_mean_threshold
from gamma_correction import adjust_gamma
from smoothing import Filter


class Pipeline:
    def __init__(self, datasets_path, image_names_file, image_results_directory):
        self.start_time = None
        self.end_time = None
        self.fps = None
        self.img_count = 0
        self.datasets_path = datasets_path
        self.image_names_file = open(image_names_file, "r")
        self.pipeline_result_directory = image_results_directory

    def read_image(self, zeile):
        picture_name = os.path.join(self.datasets_path, "RTTS_light", "JPEGImages", zeile[:-1] + ".png")
        return cv2.imread(str(picture_name))

    def write_result_image(self, zeile, result_img):
        picture_name = os.path.join(self.pipeline_result_directory, zeile[:-1] + ".png")
        cv2.imwrite(picture_name, result_img)

    def run(self):
        self.start_time = datetime.now().timestamp()
        print("Current Time =", self.start_time)
        for zeile in self.image_names_file:
            if zeile[:-1] == "":
                break
            self.img_count += 1
            img = self.read_image(zeile)
            image_setup = evaluate(img)
            result_img = adjust_gamma(img, image_setup.average)
            result_img = Filter(result_img).gaussian_filter()
            result_img = bina_adapt_mean_threshold(cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY))
            self.write_result_image(zeile, result_img)

        self.end_time = datetime.now().timestamp()
        self.fps = self.img_count / (self.end_time - self.start_time)
        print("Frames per Second = ", self.fps)
