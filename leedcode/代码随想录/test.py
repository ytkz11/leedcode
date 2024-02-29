#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2024/2/21 10:14 
# @File : test.py 
from typing import List

import os
from PIL import Image
import numpy as np


def save_bmp():
    # 文件夹路径
    folder_path = r'/home/storage/test/road_voc/road/SegmentationClass'

    # 获取文件夹中所有的文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为.bmp文件
        if filename.endswith('.bmp'):
            # 完整的文件路径
            file_path = os.path.join(folder_path, filename)

            # 打开图像
            img = Image.open(file_path)

            # 转换为灰度
            img_gray = img.convert('L')

            # 保存灰度图像（覆盖原文件）
            img_gray.save(file_path)


def convert_value():
    folder_path = r'C:\Users\OBT-SJCP-B-A08\Desktop'

    # 获取文件夹中所有的文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为.bmp文件
        if filename.endswith('.bmp'):
            # 完整的文件路径
            file_path = os.path.join(folder_path, filename)

            # 打开图像
            img = Image.open(file_path)
            img_np = np.array(img)
            img_np[img_np==255] = 1

            img_new = Image.fromarray(img_np)
            img_new.save(file_path)




if __name__ == '__main__':
    convert_value()
