import cv2

from tutorial.opencv import *

# load the example image and convert it to grayscale
image = cv2.imread(img_example_01)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# write the grayscale image to disk as a temporary file so we can apply OCR to it
cv2.imwrite('test.jpg', gray)