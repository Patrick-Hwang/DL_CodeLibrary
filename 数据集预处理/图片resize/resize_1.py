# coding = utf-8
from PIL import Image
import os


"""
param:
    dir: 数据集所在目录，如 "./train/"
    out_dir: resized数据集输出目录, 如 "./resized_train/"
    width: resize图片的输出宽度, 如 256
    height: resize图片输出高度, 如 256
"""
def pic_resize(dir,out_dir,width,height):
    file_list = os.listdir(dir)
    # print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        out_path = out_dir+filename
        im = Image.open(path)
        out = im.resize((width,height),Image.ANTIALIAS)
        print("%s has been resized!"%filename)
        out.save(out_path)
     
if __name__ == '__main__':
    pic_resize("./o_data/train/", "./o_data/resized_train/", 256, 256)
