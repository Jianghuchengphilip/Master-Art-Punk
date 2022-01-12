#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ： 基础配置文件
========================================d=========="""
import function.subject as subject
import function.stickers as stickers
color_data_path = './data/Monet/'  # 这里填入你的训练集文件夹路径例如：\\你的电脑路径\\data\\monet\
DATACENTER_ID = 0
WORKER_ID = 0
SEQUENCE = 0
color_model_path = "./output/csv/1456536544394346496.csv"
module = [subject.canvas, subject.mouse]
n = 1000 #生成数量
color_output_name = 'mouse' #文件夹名字
color_style = 0 #0为随机风格，1为艺术家风格
k = 30  # K-Means算法分成K类
init_method = 'random'
random_state = 88 # 艺术家风格分箱颜色数
color_distance = 300 #艺术家风格颜色差异距离检查
train = False

