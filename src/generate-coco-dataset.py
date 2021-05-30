import glob
import os
import shutil

import copy_and_rename_dataset
import split_train_val
import voc2coco

dataset_parent = os.getcwd() + "/../datasets/pedestrian_dataset"
dataset_train_parent = dataset_parent + "/train"
dataset_val_parent = dataset_parent + "/val"

img_src_parent_train = os.getcwd() + "/../datasets/train/Images"
img_src_parent_val = os.getcwd() + "/../datasets/val/Images"

shutil.rmtree(dataset_parent, ignore_errors=True)
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
    annotation_directory = os.getcwd() + "/../datasets/train/Annotations"
    json_file = os.getcwd() + "/../datasets/pedestrian_dataset/train/output.json"
    xml_files = glob.glob(os.path.join(annotation_directory, "*.xml"))

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    voc2coco.convert(xml_files, json_file)


def create_and_copy_json_val():
    annotation_directory = os.getcwd() + "/../datasets/val/Annotations"
    json_file = os.getcwd() + "/../datasets/pedestrian_dataset/val/output.json"
    xml_files = glob.glob(os.path.join(annotation_directory, "*.xml"))

    # If you want to do train/test split, you can pass a subset of xml files to convert function.
    voc2coco.convert(xml_files, json_file)


def generate():
    copy_images()
    create_and_copy_json_train()
    create_and_copy_json_val()

    shutil.make_archive(dataset_parent, 'zip', dataset_parent)


copy_and_rename_dataset.copy_and_rename()
split_train_val.split_train_val()
generate()
