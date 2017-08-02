import cv2


img = cv2.imread('images/fapiao1.jpg', 0)
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)   # 转回uint8
absY = cv2.convertScaleAbs(y)

# 3 轮廓的清晰度
dst = cv2.addWeighted(absX, 3, absY, 3, 0)

cv2.imwrite('test.jpg', dst)
