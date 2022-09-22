import cv2
from os.path import splitext

def pic2binary(pic_name = ""):
    img = cv2.imread(pic_name)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 首先转为灰度化图片
    ret, thresh = cv2.threshold(gray_img, 150, 255,cv2.THRESH_BINARY)
    binary_name = str(splitext(pic_name)[0] + "_binary" + ".png")
    print(binary_name)
    cv2.imwrite(binary_name, thresh)

if __name__ == "__main__":
    pic2binary("wafer_1.png")