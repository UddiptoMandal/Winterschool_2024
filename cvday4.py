import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
import pandas as pd
#canny
def mag(a,b):
    return np.sqrt(a**2 + b**2)

Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
Gy = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
t = 187

img = cv2.imread('chill guy.jpg')
img = cv2.resize(img, (500,500) )
img1 = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
# cv2.imshow("img3", img1)
# cv2.waitKey(0)
#img1 = img
# plt.subplot(121), plt.imshow(img)
# plt.subplot(122), plt.imshow(img1)
# plt.show()
imgx = np.full((500,500), 0, dtype = np.uint8)
imgy = np.full((500,500), 0, dtype = np.uint8)
imgfinal = np.full((500,500), 0, dtype = np.uint8)
for i in range(500):  # greyscale
    for j in range(500):
        b,g,r =img1[i][j]
        g = 0.299 *r + 0.587 *g + 0.114 *b
        img1[i][j] =(g,g,g)
# cv2.imshow("Image", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
sobel_x = np.zeros([500,500])
sobel_y = np.zeros([500,500])

print(type(int(img1[100, 400, 0])))
for i in range(2,498):
    for j in range(2,498):
        arr = np.zeros([3,3])
        for k in range(3):
            for l in range(3):
                arr[k,l] = int(img1[i+k-1,j+l-1, 0])

        sobel_x[i][j] = np.sum(arr * Gx)+128
        sobel_y[i][j] = np.sum(arr * Gy)+128
        imgx[i][j] = sobel_x[i][j]
        imgy[i][j] = sobel_y[i][j]
        grad1 = 0
        grad2 = 0
        
        theta = math.atan(imgy[i][j]/imgx[i][j])

        if theta<math.pi/8 and theta>-math.pi/8:
            if mag(sobel_x[i][j], sobel_y[i][j]) == max(mag(sobel_x[i+1][j], sobel_y[i+1][j]), mag(sobel_x[i][j], sobel_y[i][j]), mag(sobel_x[i-1][j], sobel_y[i-1][j])) and mag(sobel_x[i][j], sobel_y[i][j])>t:
                imgfinal[i][j] = 255
            else:
                imgfinal[i][j] = 0
        elif theta <3*math.pi/8 and theta > math.pi/8:
            if mag(sobel_x[i][j], sobel_y[i][j]) == max(mag(sobel_x[i+1][j+1], sobel_y[i+1][j+1]), mag(sobel_x[i][j], sobel_y[i][j]), mag(sobel_x[i-1][j-1], sobel_y[i-1][j-1])) and mag(sobel_x[i][j], sobel_y[i][j])>t:
                imgfinal[i][j] = 255
            else:
                imgfinal[i][j] = 0
        elif theta > 3*math.pi/8 and theta < -3*math.pi/8:
            if mag(sobel_x[i][j], sobel_y[i][j]) == max(mag(sobel_x[i][j+1], sobel_y[i][j+1]), mag(sobel_x[i][j], sobel_y[i][j]), mag(sobel_x[i][j-1], sobel_y[i][j-1])) and mag(sobel_x[i][j], sobel_y[i][j])>t:
                imgfinal[i][j] = 255
            else:
                imgfinal[i][j] = 0
        else:
            if mag(sobel_x[i][j], sobel_y[i][j]) == max(mag(sobel_x[i+1][j-1], sobel_y[i+1][j-1]), mag(sobel_x[i][j], sobel_y[i][j]), mag(sobel_x[i-1][j+1], sobel_y[i-1][j+1])) and mag(sobel_x[i][j], sobel_y[i][j])>t:
                imgfinal[i][j] = 255
            else:
                imgfinal[i][j] = 0

cv2.imshow("img3", imgfinal)
cv2.waitKey(0)
cv2.destroyAllWindows()




        







