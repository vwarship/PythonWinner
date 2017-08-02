import cv2


(major, minor, _) = cv2.__version__.split(".")
print('version: ', cv2.__version__)
print('major: %s minor: %s' % (major, minor))

img = cv2.imread('images/fapiao1.jpg')
cv2.imshow('Itisatitle', img)
cv2.waitKey()
cv2.destroyAllWindows()
