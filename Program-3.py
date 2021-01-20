#Write an Image- the image which is read from the system(sunflower.jpg) will saved in the existing folder with name 'output.jpg'
#It saves the image 
import cv2
img=cv2.imread('sunflower.jpg')
cv2.imwrite('output.jpg',img)