#Binary Image-Black and white

import cv2
img=cv2.imread('sunflower.jpg',0)
cv2.imshow('GrayScale',img)
cv2.waitKey(1000)
ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()