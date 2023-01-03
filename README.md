## 细粒度图像分类
细粒度图像分类问题是对大类下的子类进行识别。细粒度图像分析任务相对通用图像任务的区别和难点在于其图像所属类别的粒度更为精细。
通用图像分类其任务诉求是将“袋鼠”和“狗”这两个物体大类分开；而细粒度图像的分类任务则要求对“狗”该类类别下细粒度的子类，即分别为“哈士奇”和“爱斯基摩犬”的图像分辨开来。不止对计算机，对普通人来说，细粒度图像任务的难度和挑战无疑也更为巨大。


## CUB-200数据集
该数据集共有11788张鸟类图像，包含200类鸟类子类，其中训练数据集有5994张图像，测试集有5794张图像，每张图像均提供了图像类标记信息，图像中鸟的bounding box，鸟的关键part信息，以及鸟类的属性信息。本代码仅使用图片，不使用额外信息。


## google Colab链接: 
* [res152-2.ipynb](https://drive.google.com/file/d/14tuEH0OonGIIiV3ITUx8BkkbgaTa90Kh/view?usp=sharing)测试集准确率达82%。