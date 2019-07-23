import os
from PIL import Image
import csv

# 抠图

path_csv = 'F:\\SAMMA'  # CSV文件
path_yuan = 'F:\\SAMMB'  # 原图
path = 'F:\\SAMMC'  # 修改后图

for sub in  sorted([infile for infile in os.listdir(path_csv)]):
    for vid in sorted([inrfile for inrfile in os.listdir(path_csv + '\\' + sub)]):
        mid_path = sub + '\\' + vid
        current_path = path_csv + '\\' + mid_path + '\\'
        filenames = os.listdir(current_path)
        for filename in filenames:
            csv_path = current_path + filename
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for i, rows in enumerate(reader):
                    if i == 19:
                        top = rows
                    if i == 57:
                        bottom = rows
                    if i == 17:
                        left = rows
                    if i == 26:
                        right = rows
            fn = os.path.splitext(filename)[0]
            img = Image.open(path_yuan + '\\' + mid_path + '\\' + fn + '.jpg')
            box = (int(left[0]) - 20, int(top[1]) - 20, int(right[0]) + 20, int(bottom[1]) + 20)
            image = img.crop(box)
            if not os.path.exists(path + '\\' + sub):
                os.mkdir(path + '\\' + sub)
            if not os.path.exists(path + '\\' + mid_path):
                os.mkdir(path + '\\' + mid_path)
            image.save(path + '\\' + mid_path + '\\' + fn + '.jpg')
            print(path + '\\' + mid_path + '\\' + fn + '.jpg')

