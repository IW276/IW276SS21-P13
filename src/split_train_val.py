import os
import random
import shutil

img_src_parent = os.path.join(os.getcwd(), "..", "datasets", "train", "Images")
img_parent_val = os.path.join(os.getcwd(), "..", "datasets", "val", "Images")
xml_src_parent = os.path.join(os.getcwd(), "..", "datasets", "train", "Annotations")
xml_parent_val = os.path.join(os.getcwd(), "..", "datasets", "val", "Annotations")

shutil.rmtree(img_parent_val, ignore_errors=True)
shutil.rmtree(xml_parent_val, ignore_errors=True)
os.makedirs(img_parent_val, exist_ok=True)
os.makedirs(xml_parent_val, exist_ok=True)


def copy_images(n):
    src = img_src_parent + "/" + str(n) + ".png"
    dest = img_parent_val + "/" + str(n) + ".png"
    shutil.copyfile(src, dest)
    os.remove(src)


def copy_xmls(n):
    src = xml_src_parent + "/" + str(n) + ".xml"
    dest = xml_parent_val + "/" + str(n) + ".xml"
    shutil.copyfile(src, dest)
    os.remove(src)


def split_train_val():
    val = []
    val_amount = 1

    while val_amount < 1080:
        random_number = random.randint(1, 4321)
        while val.__contains__(random_number):
            random_number = random.randint(1, 4321)
        val.append(random_number)
        val_amount += 1

    for number in val:
        copy_images(number)
        copy_xmls(number)
