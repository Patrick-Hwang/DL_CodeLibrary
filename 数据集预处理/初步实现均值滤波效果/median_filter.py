from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 均值滤波函数
def median_filter02(image, win=3):
    H, W = image.shape
    result = image.copy() 
    for h in range(1, H):
        for w in range(1, W):
            result[h, w] = np.median(result[h:h+win, w:w+win])
    return result


if __name__ == "__main__":
    img = Image.open("wafer_1.png")     # 使用 Image 打开图片
    img = np.asarray(img)               # 将 Image 打开的图片转为 numpy.ndarray 类型
    medianFilter_wafer = median_filter02(img, win=3)    # 调用均值滤波
    plt.figure("wafer")
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(medianFilter_wafer)
    plt.show()
