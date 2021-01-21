#Solid color-RGB Background

import cv2
import numpy as np
img=np.zeros((250,250,3))
img1=np.zeros((250,255,3))
img2=np.zeros((250,250,3))

img[:]=0,0,255
img1[:]=0,255,0
img2[:]=255,0,0
cv2.imshow('Red',img)
cv2.imshow('Green',img1)
cv2.imshow('Blue',img2)
cv2.waitKey(0)