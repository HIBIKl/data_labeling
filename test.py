import cv2
import numpy as np

# 读取图像
image = cv2.imread('./data/5/zn1.jpg', 0)

# 阈值处理
_, threshold = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个空的列表来保存细胞的中心坐标
cell_centers = []

for contour in contours:
    # 计算最小包围圆
    (x, y), radius = cv2.minEnclosingCircle(contour)

    # 计算细胞的中心坐标
    cX = int(x)
    cY = int(y)

    # 将坐标添加到列表中
    cell_centers.append((cX, cY))

# 在图像上绘制细胞的中心坐标和包围细胞的矩形
for center in cell_centers:
    cv2.circle(image, center, 5, (255, 0, 0), -1)
    cv2.rectangle(image, (center[0]-25, center[1]-25), (center[0]+25, center[1]+25), (255, 0, 0), 2)

# 显示图像
cv2.imshow('Image with Cell Centers and Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()