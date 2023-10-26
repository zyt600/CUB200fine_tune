from torchvision.transforms import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import os
from torch import nn
import torchvision.models as models
import torch


def predict_bird_class(imgPath="bird.jpg"):
    """预测鸟类类别函数，调用方法：输入图片的路径，返回鸟类分类的类号（0～199）"""
    # print("start")
    md = torch.load("./almighty4+3.pth",map_location="cpu").eval()
    op = Image.open(imgPath)
    op = op.resize((224, 224))
    trans = transforms.ToTensor()
    op = trans(op)

    op = op.view(1, 3, 224, 224)
    with torch.no_grad():
        out = md(op)
    out = out[0]
    return int(out.argmax())
    # print(op.size())
    # print(out)


predict_bird_class()
