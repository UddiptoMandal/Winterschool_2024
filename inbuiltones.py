import cv2 
import numpy as np 
  
#Capture livestream video content from camera 0 
img = cv2.imread("chill guy.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img = cv2.GaussianBlur(img, (5, 5), 5)
img1 = img
cv2.imshow('blur',img1) 
# Calculation of Sobelx 
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3) 

# Calculation of Sobely 
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3) 

# Calculation of Laplacian 
laplacian = cv2.Laplacian(img,cv2.CV_64F) 

cv2.imshow('sobelx',sobelx) 
cv2.imshow('sobely',sobely) 
cv2.imshow('laplacian',laplacian) 
cv2.waitKey(0)

cv2.destroyAllWindows() 
  
