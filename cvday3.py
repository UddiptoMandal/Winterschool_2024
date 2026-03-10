import numpy as np
import cv2
from matplotlib import pyplot as plt
#sobel
# img = cv2.imread('img1.jpg')
# img1 = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
# plt.subplot(121), plt.imshow(img)
# plt.subplot(122), plt.imshow(img1)
# plt.show()


#apply edge detection on maps
# image = cv2.imread('img1.jpg')
# sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 3)
# sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 3)

# magnitude = cv2.magnitude(sobel_x, sobel_y)

Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
Gy = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
t = 12

img = cv2.imread('chill guy.jpg')
img = cv2.resize(img, (500,500) )
img1 = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
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
# img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
sobel_x = np.zeros([500,500])
sobel_y = np.zeros([500,500])

# print(type(int(img1[100, 400, 0])))
for i in range(1,499):
    for j in range(1,499):
        arr = np.zeros([3,3])
        for k in range(3):
            for l in range(3):
                arr[k,l] = int(img1[i+k-1,j+l-1, 0])
        # sobel_x[i][j] = np.sum(arr * Gx)+128
        # if abs(sobel_x[i][j])>t:
        #     imgx[i][j] = sobel_x[i][j]
        # else:
        #     imgx[i][j] = (0)
        # sobel_y[i][j] = np.sum(arr * Gy)+128
        # if abs(sobel_y[i][j])>t:
        #     imgy[i][j] = sobel_y[i][j]
        # else:
        #     imgy[i][j] = (0)
        sobel_x[i][j] = np.sum(arr * Gx)+128
        sobel_y[i][j] = np.sum(arr * Gy)+128
        imgx[i][j] = sobel_x[i][j]
        imgy[i][j] = sobel_y[i][j]


# cv2.imshow("img", imgx)
# cv2.imshow("img1",imgy)

for i in range (500):
    for j in range (500):
        mag = ((imgx[i][j]**2) + (imgy[i][j]**2))**0.5
        if mag>t:
            imgfinal[i][j] = 255
        else:
            imgfinal[i][j] = 0

# cv2.imshow("img", imgx)
# cv2.imshow("img1",imgy)
# cv2.imshow("img3", imgfinal)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.subplot(2, 2, 2)
plt.imshow(imgx)
plt.title("Sobelx")
plt.subplot(2, 2, 3)
plt.imshow(imgy)
plt.title("Sobely")
plt.subplot(2, 2, 4)
plt.imshow(imgfinal)
plt.title("Final img")

plt.tight_layout()
plt.show()






