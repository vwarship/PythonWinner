import cv2

from tutorial.opencv import fapiao

img = cv2.imread(fapiao, 0)
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)   # 转回uint8
absY = cv2.convertScaleAbs(y)

# alpha 伸缩系数
# beta  累加到结果上的一个值
# gamma 累加到结果上的一个值
alpha = 3
beta = 3
gamma = 0
dst = cv2.addWeighted(absX, alpha, absY, beta, gamma)

cv2.imwrite('test.jpg', dst)
