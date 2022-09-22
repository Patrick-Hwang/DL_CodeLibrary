# coding = utf-8
from PIL import Image
import os
import shutil

def pic_move(dir,out_dir):
    file_list = os.listdir(dir)
    # print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        out_path = out_dir+filename
        if filename[-8:-4] == 'mask':   # 判断文件是否移动的条件，本代码中，如果 [-8:-4]为‘mask’，则移动文件
            shutil.move(path, out_dir)


'''
实现图片的重命名功能
下面代码实现功能为：
    原图片名称为 “000.png”、“001.png”......“020.png”
    重名名为 “400.png”、“401.png”......“420.png”
'''
def rename_1(dir):
    file_list = os.listdir(dir)
    i = 0
    j = 400
    for filename in file_list:
        path = ''
        filename_path = dir + filename
        if filename[:3] == ("%03d" % i):    # 判断前三个字符
            new_filename = filename.replace(filename[:3], str(j))
            new_filename_path = dir + new_filename
            os.rename(filename_path, new_filename_path) # 主要实现函数为 os.rename(原始图片路径，新图片路径)
            i += 1
            j += 1

def rename(dir):
    file_list = os.listdir(dir)
    for filename in file_list:
        filename_path = dir + filename
        filename_1 = filename[:-8]
        filename_2 = filename[-4:]
        new_filename = filename_1 + filename_2
        new_filename_path = dir + new_filename
        os.rename(filename_path, new_filename_path) 

     
if __name__ == '__main__':
    pic_move("./train/", "./mask/")
    rename_1('./val/')