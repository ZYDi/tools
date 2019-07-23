# -*- coding=utf-8 -*-
from PIL import Image
import csv    # 加载csv包便于读取csv文件
csv_file = open('/home/d/document/0000.csv')    # 打开csv文件
csv_reader_lines = csv.reader(csv_file)   # 逐行读取csv文件
number = 0
for line in csv_reader_lines:
    path = line[1]
    img = Image.open(path) # 打开当前路径图像
    a = line[2]
    b = line[3]
    c = line[4]
    d = line[5]
    aa = int(c)
    bb = int(b)
    cc = int(a)		
    dd = int(d)
    box = (aa, bb, cc + aa, dd + bb)    # 设置图像裁剪区域
    image = img.crop(box)   # 图像裁剪
    image.save(line[1])  # 存储当前区域
    number = number + 1
    print(number)

