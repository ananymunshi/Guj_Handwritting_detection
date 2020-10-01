import cv2 as cv
import numpy as np
import csv
import os


def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Output")
one = [0]
one.clear()
i = 0
j = 0
print(image_dir)


with open("trainer.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png"):
                print("Hello World")
                img = cv.imread(file,0)
                img_not = cv.bitwise_not(img)
                temp = img_not.tolist()
                while i < 28:
                    j = 0
                    while  j < 28:
                        one.append(temp[i][j])
                        j += 1
                    i += 1
                i = 0
                wr.writerow(one)
                temp.clear()
                one.clear()

print("dataset Stored")