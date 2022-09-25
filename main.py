import numpy as np
import cv2

width = 200
height = 100

# 创建图像
# 彩色图像用三通道
img = np.ones((height, width, 3), np.uint8)

# 下面颜色可以叠加，比如绿色和红色配出来的就是黄色
# img[:,:,0] = 255 # 蓝色
img[:, :, 1] = 255  # 绿色
img[:, :, 2] = 255  # 红色
# img[:,:,:] = 255 # 白色
# np.zeros() 通常用来创建掩模，也就是模板


cv2.imshow("", img)
cv2.waitKey()
cv2.destroyAllWindows()
