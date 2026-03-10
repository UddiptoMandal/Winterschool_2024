import numpy as np
import cv2
import random
import matplotlib as mp

img = cv2.imread("kmeansimg.jpg")
img = cv2.resize(img, (500,500) )
height = img.shape[0]
width = img.shape[1]



centroid1 = [random.randint(0,499), random.randint(0,499)]
centroid2 = [random.randint(0,499), random.randint(0,499)]
centroid3 = [random.randint(0,499), random.randint(0,499)]
print (centroid1, centroid2, centroid3)
points = []
k = 0
for i in range (500):
    for j in range (500):
        b,g,r = img[i][j]
        if b!= 0 and g!= 0 and r!= 0:
            points.append([i,j])
            k+= 1

print(points[0])
for c in range (10):
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in range (k):
        dist1 = ((points[i][0]-centroid1[0])**2+ (points[i][1]-centroid1[1])**2)
        dist2 = ((points[i][0]-centroid2[0])**2+ (points[i][1]-centroid2[1])**2)
        dist3 = ((points[i][0]-centroid3[0])**2+ (points[i][1]-centroid3[1])**2)
        if dist1<= dist2 and dist1 <= dist3:
            cluster1.append(points[i])
        elif dist2<= dist1 and dist2 <= dist3:
            cluster2.append(points[i])
        else:
            cluster3.append(points[i])
        sum = [0,0]
    for j in range (len(cluster1)):
        sum+= np.array(cluster1[j])
    centroid1 = [int(sum[0]/(j+1)), int(sum[1]/(j+1))]
    sum = [0,0]
    for j in range (len(cluster2)):
        sum+= np.array(cluster2[j])
    centroid2 = [int(sum[0]/(j+1)), int(sum[1]/(j+1))]
    sum = [0,0]
    for j in range (len(cluster3)):
        sum+= np.array(cluster3[j])
    centroid3 = [int(sum[0]/(j+1)), int(sum[1]/(j+1))]
print(centroid1, centroid2, centroid3)

output_image = np.zeros((height, width, 3), dtype=np.uint8)

for i in range (len(cluster1)):
    output_image[cluster1[i][0], cluster1[i][1]] = (255,0,0)
for i in range (len(cluster2)):
    output_image[cluster2[i][0], cluster2[i][1]] = (0,255,0)
for i in range (len(cluster3)):
    output_image[cluster3[i][0], cluster3[i][1]] = (0,0 ,255)
for i in range (3):
    for j in range (3):
        output_image[centroid1[0]+i, centroid1[0]+j] = (255,0,0)
        output_image[centroid2[0]+i, centroid2[0]+j] = (255,0,0)
        output_image[centroid3[0]+i, centroid3[0]+j] = (255,0,0)
cv2.imshow("out", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

        

