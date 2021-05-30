import os
import shutil

image_count = 0


def copy_images():
    img_src_parent = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/RTTS/JPEGImages"
    img_parent_train = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/train/Images"

    shutil.rmtree(img_parent_train)
    os.makedirs(img_parent_train, exist_ok=True)

    img_count = 0

    for filename in os.listdir(img_src_parent):
        img_count += 1
        src = img_src_parent + "/" + filename
        dest = img_parent_train + "/" + str(img_count) + ".png"
        shutil.copyfile(src, dest)


def copy_xmls():
    xml_src_parent = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/RTTS/Annotations"
    xml_parent_train = "C:/Users/Lukassause/Studium/07_Semester/Wahlpflichtfächer 3/IW276SS21-P13/datasets/train/Annotations"

    shutil.rmtree(xml_parent_train)
    os.makedirs(xml_parent_train, exist_ok=True)

    img_count = 0

    for filename in os.listdir(xml_src_parent):
        img_count += 1
        src = xml_src_parent + "/" + filename
        dest = xml_parent_train + "/" + str(img_count) + ".xml"
        shutil.copyfile(src, dest)


def copy_and_rename():
    copy_xmls()
    copy_images()
