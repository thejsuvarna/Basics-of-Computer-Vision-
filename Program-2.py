#Reading info of an image
import cv2
img=cv2.imread('sunflower.jpg')
print(img.shape)
print('Height of an image:',int(img.shape[0]),"pixels")
print('Width of an image:',int(img.shape[1]),"pixels")

