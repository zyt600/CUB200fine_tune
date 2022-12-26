from tkinter import *
from tkinter import filedialog
import torch
from torchvision import transforms
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as tkFont
# from predict_bird import trained_model
from predict_bird_class import predict_bire_class
import webbrowser

# 类别表
df = pd.read_excel('cate.xlsx')


def predict():
    global img_file
    path = filedialog.askopenfilename()
    if path == '':
        return
    img_file = Image.open(path)

    # 图片大小处理
    w, h = img_file.size
    if w/h > root.winfo_width()/(root.winfo_height()*11/12):
        img_file = img_file.resize(
            (root.winfo_width(), int(root.winfo_width() / w * h)))
    else:
        img_file = img_file.resize(
            (int(11/12*root.winfo_height() / h * w), int(11/12*root.winfo_height())))
    img_file = ImageTk.PhotoImage(img_file)
    show_img.create_image(int(root.winfo_width()*0.5),
                          0, anchor='n', image=img_file)

    number = predict_bire_class(path)   # 调用模型
    var.set(df.iloc[number, 1])
    var1.set(df.iloc[number, 3])
    global url
    url = df.iloc[number, 2]


def click(event):   # 打开wiki链接
    webbrowser.open(url)


root = Tk()
root.title('pridict_bird')
root.geometry("800x600")
var = StringVar()
var1 = StringVar()
open_Style = tkFont.Font(family="Lucida Grande", size=12)
pre_Style = tkFont.Font(family="Bahnschrift SemiBold", size=16)

# 展示图片
show_img = Canvas(root, bg='snow')
show_img.place(relx=0, rely=1/6, anchor='nw', relwidth=1, relheight=5/6)

# 打开图片按钮
open_img = Button(root, text='打开图片', font=open_Style, command=predict)
open_img.place(relx=0, rely=0, anchor='nw', relwidth=1/8, relheight=1/12)

# 百科链接
wiki = Button(root, text='Wiki', font=open_Style)
wiki.pack
wiki.bind("<Button-1>", click)
wiki.place(relx=700/800, y=0, anchor='nw', relwidth=1/8, relheight=1/12)

# 简要介绍
intro = Label(root, textvariable=var1, bg='Lemonchiffon', font=pre_Style)
intro.place(relx=0, rely=1/12, anchor='nw', relwidth=1, relheight=1/12)

# 分类结果
predictive_probability = Label(
    root, textvariable=var, bg='SkyBlue', font=pre_Style)
predictive_probability.place(
    relx=100/800, y=0, anchor='nw', relwidth=6/8, relheight=1/12)

root.mainloop()
