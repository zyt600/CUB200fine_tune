# 本文件用于随机从训练集中抽取少量图片，在超小的一个训练集上测试是否能过拟合，以确认代码无bug

smallBatchSize = 10  # 从每一个类中抽取多少张图片

import os
from PIL import Image

smallBatchSize = 10  # 从每一个类中抽取多少张图片


imgPath = "." + os.sep + "CUB_200_2011" + os.sep + "CUB_200_2011" + os.sep + "images"
which = 0

imgDirs = os.listdir(imgPath)
for imgDir in imgDirs:
    imgDirPath = imgPath + os.sep + imgDir
    imgFiles = os.listdir(imgDirPath)
    num = 0
    which += 1
    for img in imgFiles:
        op = Image.open(imgDirPath + os.sep + img)
        num += 1
        op.save("." + os.sep + "smallBatch" + os.sep + str(which) + "(" + str(num) + ").jpg")
        # print("." + os.sep + "smallBatch" + os.sep + str(which))

        if num >= smallBatchSize:
            break
print("finish saving")


