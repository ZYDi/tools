import csv
import os
import cv2
import numpy as np
# 掩模
path_csv = 'F:\\SAMMA'
path_img = 'F:\\SAMM'
path_write = 'F:\\SAMMB'


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
                        eyeLT = rows
                    if i == 41:
                        eyeLB = rows
                    if i == 17:
                        eyeLL = rows
                    if i == 21:
                        eyeLR = rows
                    if i == 24:
                        eyeRT = rows
                    if i == 47:
                        eyeRB = rows
                    if i == 22:
                        eyeRL = rows
                    if i == 26:
                        eyeRR = rows
                    if i == 29:
                        noseT = rows
                    if i == 33:
                        noseB = rows
                    if i == 31:
                        noseL = rows
                    if i == 35:
                        noseR = rows
                    if i == 52:
                        mouseT = rows
                    if i == 57:
                        mouseB = rows
                    if i == 48:
                        mouseL = rows
                    if i == 54:
                        mouseR = rows
            # 加载图像
            fn = os.path.splitext(filename)[0]
            image = cv2.imread(path_img + '\\' + mid_path + '\\' + fn + '.jpg')
            print(path_img + '\\' + mid_path + '\\' + fn + '.jpg')

            # 左眼区域，填充白色255
            rectangle_eyeL = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(rectangle_eyeL, (int(eyeLL[0]) - 10, int(eyeLT[1]) - 10), (int(eyeLR[0]) + 10, int(eyeLB[1]) + 10), 255, -1)

            # 右眼区域
            rectangle_eyeR = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(rectangle_eyeR, (int(eyeRL[0]) - 10, int(eyeRT[1]) - 10), (int(eyeRR[0]) + 10, int(eyeRB[1]) + 10), 255, -1)

            # 鼻子区域
            rectangle_nose = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(rectangle_nose, (int(noseL[0]) - 10, int(noseT[1]) - 10), (int(noseR[0]) + 10, int(noseB[1]) + 10), 255, -1)

            # 嘴区域
            rectangle_mouse = np.zeros(image.shape[:2], dtype="uint8")
            cv2.rectangle(rectangle_mouse, (int(mouseL[0]) - 10, int(mouseT[1]) - 10), (int(mouseR[0]) + 10, int(mouseB[1]) + 10), 255, -1)

            # 异或运算，不同为1, 相同为0
            bitwiseXor_eye = cv2.bitwise_or(rectangle_eyeL, rectangle_eyeR)
            bitwiseXor_nose = cv2.bitwise_or(bitwiseXor_eye, rectangle_nose)
            bitwiseXor_mouse = cv2.bitwise_or(bitwiseXor_nose, rectangle_mouse)

            # 掩模
            mask = bitwiseXor_mouse
            masked = cv2.bitwise_and(image, image, mask=mask)

            path_creat = path_write + '\\' + mid_path
            if not os.path.exists(path_write + '\\' + sub):
                os.mkdir(path_write + '\\' + sub)
            if not os.path.exists(path_creat):
                os.mkdir(path_creat)

            cv2.imwrite(path_creat + '\\' + fn + '.jpg', masked)
