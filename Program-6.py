#Code to print white and black background separately

import cv2
import numpy as np
img=np.ones((512,512,3))
img1=np.zeros((512,512,3))
cv2.imshow('White Background',img)
cv2.imshow('Black Background',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()