import csv
import os
import cv2
import dlib
import numpy as np
# 68特征点

path = 'F:\\SAMM'
path2 = 'F:\\SAMMA'

# 导入人脸检测模型
detector = dlib.get_frontal_face_detector()
# 导入检测人脸特征点的模型
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

for sub in  sorted([infile for infile in os.listdir(path)]):
    for vid in sorted([inrfile for inrfile in os.listdir(path + '\\' + sub)]):
        mid_path = sub + '\\' + vid
        current_path = path + '\\' + mid_path + '\\'
        filenames = os.listdir(current_path)
        for filename in filenames:
            img_path = current_path + filename
            # print(img_path)
            # 读取图像
            img = cv2.imread(img_path)
            # 取灰度
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            fn = os.path.splitext(filename)[0]
            file_path = path2 + '\\' + mid_path
            file_path_name = file_path + '\\' + fn + '.csv'
            # print(file_path)
            if not os.path.exists(path2 + '\\' + sub):
                os.mkdir(path2 + '\\' + sub)
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            f = open(file_path_name, 'a+', newline='')
            o = csv.writer(f, dialect='excel')
            # 人脸数rects
            rects = detector(img_gray, 0)
            for i in range(len(rects)):
                landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[i]).parts()])
                for idx, point in enumerate(landmarks):
                    # 68点的坐标
                    pos1 = str(point[0, 0])
                    pos2 = str(point[0, 1])
                    pos = [pos1, pos2]
                    # print(pos)
                    o.writerow(pos)
            print(img_path)
            f.close()
