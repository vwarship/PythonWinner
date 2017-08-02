import cv2

from tutorial.opencv import fapiao

img = cv2.imread(fapiao, 0)
gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imwrite('test.jpg', dst)
