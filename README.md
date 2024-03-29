[Chinese](./README_zh.md)

## Fine-Grained Image Classification
The problem of fine-grained image classification involves recognizing subclasses within a major category. The distinction and challenge of fine-grained image analysis tasks compared to general image tasks lie in the more detailed granularity of the image categories.

The demand of general image classification is to differentiate major object categories, such as separating "kangaroos" from "dogs." On the other hand, fine-grained image classification tasks require distinguishing between subcategories within a category, for example, identifying images of "Husky" and "Eskimo Dog," which are both subcategories of "dogs." The difficulty and challenges of fine-grained image tasks are undoubtedly greater, not only for computers but also for ordinary people.

## CUB-200 Dataset
https://paperswithcode.com/dataset/cub-200-2011

This dataset contains 11,788 bird images, spanning across 200 bird subclasses. It is divided into a training set with 5,994 images and a test set with 5,794 images. Each image comes with annotations, including image class labels, bounding boxes for the birds, key part information of the birds, and attribute information of the bird species. For this code, only the images are used without any additional information.

## Improvement
Calculate the mean and variance of images in the training dataset, and use these as estimates for the test dataset. Use these values to normalize the images.

Try using different data augmentation techniques and change the batch size accordingly.

Employ a two-stage training process: initially, add a fully connected layer to a pre-trained ImageNet model and fine-tune the layer; subsequently, fine-tune all the parameters with a smaller learning rate.

## How to use GUI
<!-- Because of the huge size of datesete and model, use google drive to get access to them.
All links contain the same content.
https://disk.pku.edu.cn:443/link/99E6F9F69F864E595877741FFC2211FE -->
1. Clone the repository
2. cd to the directory /CUB200fine_tune
3. pip install -r ./requirement.txt
4. cd Classify_GUI-main
5. python GUI.py
6. open any image that you want to classify, for example, the Groove_Billed_Ani_0005_1750.jpg in Classify_GUI-main

For more images, please download the dataset from the link above.


## Google Colab Link: 
[res152-2.ipynb](https://drive.google.com/file/d/14tuEH0OonGIIiV3ITUx8BkkbgaTa90Kh/view?usp=sharing) The test set accuracy reached 82%.
