from torchvision.transforms import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import os
from torch import nn
import torchvision.models as models
import torch

md = torch.load(
    ".\\Classify_GUI-main\\predict_bird\\almighty4+3.pth").to("cuda:0").eval()
trans = transforms.ToTensor()


def predict_bird_class(imgPath=".\\Classify_GUI-main\\predict_bird\\Red_Winged_Blackbird_0020_4050.jpg"):
    """预测鸟类类别函数，调用方法：输入图片的路径，返回鸟类分类的类号（0～199）"""
    # print("start")
    op = Image.open(imgPath)
    op = op.resize((224, 224))
    op = trans(op)
    op = op.view(1, 3, 224, 224)

    # op=torch.randn(1,3,224,224)
    op = op.to("cuda:0")
    with torch.no_grad():
        out = md(op)
    out = out[0]
    # print(op.size())
    # print(out)
    return int(out.argmax())


predict_bird_class()
