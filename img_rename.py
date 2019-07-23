# 修改图片名称

import os

path ='F:\\SAMMD'
path_img = 'F:\\SAMME'

for sub in  sorted([infile for infile in os.listdir(path)]):
    for vid in sorted([inrfile for inrfile in os.listdir(path + '\\' + sub)]):
        mid_path = sub + '\\' + vid
        current_path = path + '\\' + mid_path + '\\'
        filenames = os.listdir(current_path)
        for file in filenames:
            name = file.split('img')[1].split('.')[0]
            if not os.path.exists(path_img + '\\' + sub):
                os.mkdir(path_img + '\\' + sub)
            if not os.path.exists(path_img + '\\' + mid_path):
                os.mkdir(path_img + '\\' + mid_path)
            os.rename(os.path.join(path + '\\' + mid_path, file), os.path.join(path_img + '\\' + mid_path, 'img' + '%03d' % int(name) + ".jpg"))   #‘%05d’表示一共5位数
            print(current_path + name)
