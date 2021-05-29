import glob
import os
import shutil

import voc2coco

dataset_parent = "C:/Users/Lukassause/Downloads/pedestrian_dataset"
dataset_train_parent = dataset_parent + "/train"
dataset_val_parent = dataset_parent + "/val"

img_src_parent_train = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/train/Images"
img_src_parent_val = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/val/Images"

shutil.rmtree(dataset_parent)
os.makedirs(dataset_train_parent, exist_ok=True)
os.makedirs(dataset_val_parent, exist_ok=True)


def copy_images():
    for filename in os.listdir(img_src_parent_train):
        src = img_src_parent_train + "/" + filename
        dest = dataset_train_parent + "/" + filename
        shutil.copyfile(src, dest)

    for filename in os.listdir(img_src_parent_val):
        src = img_src_parent_val + "/" + filename
        dest = dataset_val_parent + "/" + filename
        shutil.copyfile(src, dest)


def create_and_copy_json_train():
    annotation_directory = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/train/Annotations"
    json_file = "C:/Users/Lukassause/Downloads/pedestrian_dataset/train/output.json"
    xml_files = glob.glob(os.path.join(annotation_directory, "*.xml"))

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    voc2coco.convert(xml_files, json_file)


def create_and_copy_json_val():
    annotation_directory = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/val/Annotations"
    json_file = "C:/Users/Lukassause/Downloads/pedestrian_dataset/val/output.json"
    xml_files = glob.glob(os.path.join(annotation_directory, "*.xml"))

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    voc2coco.convert(xml_files, json_file)


copy_images()
create_and_copy_json_train()
create_and_copy_json_val()
