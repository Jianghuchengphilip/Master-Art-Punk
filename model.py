#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：蒋虎成
@Date   ：2021/9/24 19:12
@Desc   ：模型训练
=================================================="""
import csv
import os
from settings import DATACENTER_ID,WORKER_ID,SEQUENCE,color_distance
from colors import ColorMultiImage
import numpy as np
from function.snowflake import IdWorker
def training(color_data_path):
    black_rbg = [0, 0, 0]
    color_data_distance = []
    color_distance_filepath = os.getcwd() + "\\output\\csv\\" + str(IdWorker(DATACENTER_ID, WORKER_ID, SEQUENCE).get_id()) + ".csv"
    get_model = ColorMultiImage()
    color_distance_csv = open(color_distance_filepath, "a+", newline="", encoding="utf-8-sig")
    color_data = get_model.get_main_colors(color_data_path)

    writer = csv.writer(color_distance_csv)

    for rbg in color_data:
        color_data_distance.append(rbg + [get_model.colour_distance(rbg, black_rbg)])

    color_data_sort = sorted(color_data_distance, key=lambda x: x[3])
    color_data_sort = np.array(color_data_sort)
    color_data_sort_index = (color_data_sort[:, 3] > color_distance)
    color_data_sort = color_data_sort[color_data_sort_index]
    for rbg in color_data_sort:
        writer.writerow(tuple(rbg))
    return color_distance_filepath