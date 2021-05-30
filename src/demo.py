import argparse
import os

import cv2
import numpy as np

from pipeline import Pipeline


def extract_command_line_arguments():
    parser = argparse.ArgumentParser(description='Automatic white balancing and exposure compensation.')
    parser.add_argument('--datasets_path', type=str)
    parser.add_argument('--pipeline_results', type=str)
    args = parser.parse_args()
    return args.datasets_path, args.pipeline_results


def show_results():
    for image_file_name in os.listdir(datasets_path):
        img_path = os.path.join(datasets_path, image_file_name)
        img_result_path = os.path.join(result_directory, image_file_name.replace(".png", "_result.png"))
        dim = (500, 350)
        img = cv2.imread(img_path)
        img = cv2.resize(img, dim)
        img_result = cv2.imread(img_result_path)
        img_result = cv2.resize(img_result, dim)
        result_image = np.concatenate((img, img_result), axis=1)

        cv2.imshow(os.path.basename(img_path) + " => " + os.path.basename(img_result_path), result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


datasets_path, result_directory = extract_command_line_arguments()

pipeline = Pipeline(datasets_path, result_directory)
pipeline.run()

show_results()
