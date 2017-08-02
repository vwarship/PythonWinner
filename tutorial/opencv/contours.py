import cv2

img = cv2.imread('images/fapiao1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imwrite('test.jpg', img)
