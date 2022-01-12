#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/22 17:04
@Desc   ：贴纸元素数据
=================================================="""
import PIL
import csv
import cv2
import math
import random
from PIL import Image
import numpy as np
from matplotlib import image
from sklearn.cluster import KMeans
from os import listdir
import png
from function.subject import canvas
import os
class ColorMultiImage(object):
    def __init__(self,k = 30,init_method = 'random',random_state = 88):
        self.k = k
        self.init_method = init_method
        self.random_state = random_state
        self.color_number = 0
    def box_method(self,color_data, group_distance,colors_number):
        color_data_random_box = []
        for i in range(0, colors_number):
            color_data_random_box.append(
                color_data[(len(color_data) - 1) - (i * group_distance + random.randint(0, group_distance - 1))])
        return color_data_random_box

    def rgb_to_hex(self,rgb):
        color = ''
        for i in rgb:
            num = round(float(i))
            color += str(hex(num))[-2:].replace('x', '0').lower()
        return color

    def get_all_colors_list(self,model, k):
        colors = []
        labels_list = np.arange(0, k + 1)
        (proportion, _) = np.histogram(model.labels_, bins=labels_list)
        proportion = proportion.astype("float")
        proportion /= proportion.sum()
        for (_, color) in sorted(zip(proportion, model.cluster_centers_), key=lambda x: x[0], reverse=True):
            colors.append(list(map(int, color)))
        return colors

    def get_main_colors(self,directory):
        colors_all_out = []
        for filename in listdir(directory):
            img = cv2.imread(directory + filename)
            try:
                PIL.Image.fromarray(image.imread(directory + filename))
            except FileNotFoundError:
                continue
            img_data = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            r, g, _ = cv2.split(img_data)
            img = img.reshape((img_data.shape[0] * img_data.shape[1], 3))
            print("加载" + filename + "中......")
            model = KMeans(n_clusters=self.k, init=self.init_method, random_state=self.random_state)
            model.fit(img)
            colors_all_out += self.get_all_colors_list(model, self.k)
            print("完成" + filename + "提取!")
        return colors_all_out

    def get_color_data(self,color_distance_filepath,colors_number):
        f = open(color_distance_filepath, "r+", encoding="utf-8-sig")
        reader = csv.reader(f)
        color_data_sort = list(reader)
        box = self.box_method(color_data_sort, len(color_data_sort) // colors_number,colors_number)
        return [self.rgb_to_hex(i[:3]) for i in box]

    def colour_distance(self,rgb_1, rgb_2):
        R_1, G_1, B_1 = rgb_1
        R_2, G_2, B_2 = rgb_2
        rmean = (R_1 + R_2) / 2
        R = R_1 - R_2
        G = G_1 - G_2
        B = B_1 - B_2
        return math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))

    def random_colors(self):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        color = ""
        for random_value in range(6):
            color += colorArr[random.randint(0, 14)]
        return color

    def merge(self,sticker0, sticker1):
        colors = sticker0['colors']
        index = {}
        for i, color in enumerate(sticker1['colors']):
            if color not in colors:
                colors.append(color)
                index[i] = colors.index(color)
                self.colors_number = colors.index(color)
            else:
                index[i] = colors.index(color)
        for i, row in enumerate(sticker1['data']):
            for j, color in enumerate(row):
                if color > 0:
                    sticker0['data'][i][j] = index[color]
        return sticker0

    def merges(self,stickers):
        if len(stickers) >= 2:
            sticker = self.merge(stickers.pop(0), stickers.pop(0))
            stickers.insert(0, sticker)
        else:
            return stickers[0]
        return self.merges(stickers)

    def generate(self,image_data, name,number,color_distance_filepath,coloring_style,colors_number):
        palette = [(255, 255, 255,0)]
        if coloring_style == 0:
            colors = ['000000'] + [self.random_colors() for i in range(0,colors_number)] #随机颜色
        if coloring_style == 1:
            colors = ['000000'] + self.get_color_data(color_distance_filepath,colors_number)  # 艺术家风格
        for color in colors:
            color = [int(c, 16) for c in (color[:2], color[2:4], color[4:])]
            palette.append(tuple(color))
        image = np.asarray([palette[np.asarray(image_data['data']).flatten()[x]] for x in range(0,len(np.asarray(image_data['data']).flatten()))]).flatten().reshape((24,24,3))
        dirs = os.getcwd() + "\\output\\" + str(name) + "-output\\"
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        image = cv2.resize(image,(2500,2500),interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(dirs + name + number + ".png",image)
