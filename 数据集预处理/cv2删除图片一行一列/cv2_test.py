import cv2
import numpy as np

# cv2操作图片，删除图片的一行一列
img = cv2.imread("wafer_1_binary.jpg")
print(type(img))
img_1 = np.delete(img, (0), axis=0) # 删除第一行
img_1 = np.delete(img_1, (0), axis=1)   # 删除第一列
img_1.size
cv2.imwrite("wafer_1_binary_51.jpg", img_1)