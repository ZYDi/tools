from PIL import Image
import os

# 调整图像大小

path_yuan = 'F:\\SAMMC'
path = 'F:\\SAMMD'

for sub in sorted([infile for infile in os.listdir(path_yuan)]):
    for vid in sorted([inrfile for inrfile in os.listdir(path_yuan + '\\' + sub)]):
        mid_path = sub + '\\' + vid
        current_path = path_yuan + '\\' + mid_path + '\\'
        filenames = os.listdir(current_path)
        for filename in filenames:
            infile = current_path + filename
            outfile = path + '\\' + mid_path + '\\' + filename
            img = Image.open(infile)
            out = img.resize((224, 224), Image.ANTIALIAS)
            if not os.path.exists(path + '\\' + sub):
                os.mkdir(path + '\\' + sub)
            if not os.path.exists(path + '\\' + mid_path):
                os.mkdir(path + '\\' + mid_path)
            out.save(outfile)
            print(outfile)
