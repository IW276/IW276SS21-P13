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


def extract_image_names():
    image_names_file_name = os.path.join(datasets_path, "RTTS_light", "ImageSets", "test.txt")
    print("Using pictures defined in file ", image_names_file_name)

    image_names_file = open(image_names_file_name, 'r')
    result = [name for name in image_names_file if not name[:-1] == ""]
    image_names_file.close()
    return result


def show_results():
    for image_name in image_names:
        picture_name = os.path.join(datasets_path, "RTTS_light", "JPEGImages", image_name[:-1] + ".png")
        picture_name_result = os.path.join(result_directory, image_name[:-1] + ".png")
        dim = (500, 350)
        img = cv2.imread(picture_name)
        img = cv2.resize(img, dim)
        img_result = cv2.imread(picture_name_result)
        img_result = cv2.resize(img_result, dim)
        result_image = np.concatenate((img, img_result), axis=1)

        cv2.imshow('image', result_image)
        result_path = os.path.join("..", "gif", image_name.replace("\n", "") + ".png")
        cv2.imwrite(result_path, result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


datasets_path, result_directory = extract_command_line_arguments()

image_names = extract_image_names()

pipeline = Pipeline(datasets_path, image_names, result_directory)
pipeline.run()

show_results()
