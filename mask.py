# 导入库
import numpy as np
import argparse
import cv2

# 构建参数解析器
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())

# 加载猫的图像
image = cv2.imread("G:/190417/001.jpg")
# cv2.imshow("Cat", image)

# 创建矩形区域，填充白色255
rectangle = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(rectangle, (100, 100), (200, 200), 255, -1)
# cv2.imshow("Rectangle", rectangle)

# 创建圆形区域，填充白色255
circle = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(circle, (100, 30), 105, 255, -1)
# cv2.imshow("Circle", circle)

# 异或运算，不同为1, 相同为0
bitwiseXor = cv2.bitwise_or(rectangle, circle)
# cv2.imshow("XOR", bitwiseXor)
# cv2.waitKey(0)

mask = bitwiseXor
# cv2.imshow("Mask", mask)

# Apply out mask -- notice how only the person in the image is cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
