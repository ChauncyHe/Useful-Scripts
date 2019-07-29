#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:16:36 2019
输入数据集路径为多类别根目录，自动将每一个类别文件下的图像进行尺寸重定义，
并保存到一个新的文件下各个对应类别文件夹下。
@author: hcx
"""
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os 
import numpy as np
import skimage

image_size=(224,224,3)
work_path=os.getcwd()
datasets_path=work_path+'/datasets'
resize_datasets_path=work_path+'/resize_datasets'

def image_resize(datasets_path):
    class_folder_name_list=os.listdir(datasets_path)
    for class_folder_name in class_folder_name_list:#在类别文件夹维度上循环
        images_list=os.listdir(os.path.join(datasets_path,class_folder_name))
        for img_name in images_list:#在类别文件夹中的图像维度上循环
            img=skimage.io.imread(os.path.join(datasets_path,class_folder_name,img_name))
            resize_img=skimage.transform.resize(img,image_size)
            skimage.io.imsave(os.path.join(resize_datasets_path,class_folder_name,img_name),resize_img)
    return 0

image_resize(datasets_path)