# 此文件用于遍历图像尺寸，经验证，尺寸小于（C，H，W）=（3，224，224）的，在过一遍vgg16的fature后，输出小于（512，7，7），
# 在AdaptiveAvgPool2d的时候会有问题，遍历后发现，

import os
import torch
from PIL import Image

pathh = "."+os.sep+r"CUB_200_2011/CUB_200_2011/images"
files = os.listdir(pathh)
min1 = 9999999
min2 = 9999999
max1 = 0
max2 = 0
for file in files:
    print("now check",file)
    subfiles = os.listdir(pathh + os.sep + file)
    for f in subfiles:
        # with Image.open(pathh+os.sep+file+os.sep+f) as op:
        if True:
            op = Image.open(pathh + os.sep + file + os.sep + f)
            # pp=0
            if max1 < op.size[0]:
                # pp=1
                max1 = op.size[0]
            if max2 < op.size[1]:
                # pp=1
                max2 = op.size[1]
            # if pp==1:
            #     print(op.size)
            if min1 > op.size[0]:
                min1 = op.size[0]
            if min2 > op.size[1]:
                min2 = op.size[1]

print("max1", max1, "max2", max2)   # max1 500 max2 500
print("min1", min1, "min2", min2)   # min1 121 min2 120
# torch.cuda.empty_cache()
