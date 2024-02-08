import cv2
import numpy as np

# แปลงค่าสีจาก RGB เป็น HSV
rgb_color = np.uint8([[[0, 0, 0]]])
hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_RGB2HSV)
print(hsv_color)