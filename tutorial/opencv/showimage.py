import cv2

from tutorial.opencv import fapiao

(major, minor, _) = cv2.__version__.split(".")
print('version: ', cv2.__version__)
print('major: %s minor: %s' % (major, minor))

img = cv2.imread(fapiao)
cv2.imshow('Itisatitle', img)
cv2.waitKey()
cv2.destroyAllWindows()
