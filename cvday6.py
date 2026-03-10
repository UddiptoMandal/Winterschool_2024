import numpy as np
import cv2
import random
import math
from collections import deque  


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


img = cv2.imread('maze.jpg')
img = cv2.resize(img, (500, 500))
img = cv2.GaussianBlur(img, (5, 5), 0)
imgfinal = cv2.imread('maze.jpg')
imgfinal = cv2.resize(imgfinal, (500, 500))
imgfinal = cv2.GaussianBlur(imgfinal, (5, 5), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img1 = np.full((500, 500), 0, dtype=np.uint8)
for i in range(500):  # Path detection
    for j in range(500):
        if img[i][j] < 150:
            img1[i][j] = 0
        else:
            img1[i][j] = 255

cv2.imshow("Path", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


def linecollision(img1, x1, y1, x2, y2):
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if img1[y, x1] == 255:
                return False
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if img1[y1, x] == 255:
                return False
    else:  # Diagonal line (Bresenham's algorithm)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        stepx = 1 if x2 > x1 else -1
        stepy = 1 if y2 > y1 else -1
        err = dx - dy
        while x1 != x2 or y1 != y2:
            if img1[y1, x1] != 0:
                return False
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += stepx
            if e2 < dx:
                err += dx
                y1 += stepy
    return True


path = {}
A = []
for _ in range(1000):
    x, y = random.randint(0, 499), random.randint(0, 499)
    if img1[y, x] == 0:  
        A.append((x, y))
        path[(x, y)] = []
        imgfinal[y, x] = (0, 255, 0)

cv2.imshow("Nodes", imgfinal)
cv2.waitKey(0)


for i in range(len(A)):
    node = A[i]
    distnodes = []
    for j in range(len(A)):
        if j != i:
            dist = distance(node[0], node[1], A[j][0], A[j][1])
            distnodes.append((dist, j))
    distnodes.sort()  
    for j in range(5):  # Connect to 5 nearest neighbors
        neighbor = A[distnodes[j][1]]
        if linecollision(img1, node[0], node[1], neighbor[0], neighbor[1]):
            path[node].append(neighbor)
            path[neighbor].append(node)
            cv2.line(imgfinal, node, neighbor, (255, 0, 0))

#starting from (25, 250) till (475 to 250)
min1 = min2 = float(50000)
k1 = k2 = None
for i in path:
    dist_start = distance(25, 250, i[0], i[1])
    dist_end = distance(475, 250, i[0], i[1])
    if dist_start < min1:
        k1 = i
        min1 = dist_start
    if dist_end < min2:
        k2 = i
        min2 = dist_end
start, end = k1, k2
# print(start)
# print(end)

# BFS 

lis = {i: 0 for i in path} 
que = deque([start]) 
que1 = []  
que1label = {start: (-1, -1)} 

while que:
    c = que.popleft()
    if c == end:
        break
    lis[c] = 1
    for t in path[c]:
        if lis[t] == 0:
            que.append(t)
            que1label[t] = c
            lis[t] = 1
    que1.append(c)

# Reconstruct the path
quefinal = []
c = end
while c!= (-1, -1):
    quefinal.append(c)
    c = que1label[c]
quefinal.reverse()


print("Final Path:", quefinal)
for i in range(len(quefinal) - 1):
    cv2.line(imgfinal, quefinal[i], quefinal[i + 1], (0, 0, 255), 2)

cv2.imshow("Final Path", imgfinal)
cv2.waitKey(0)
cv2.destroyAllWindows()
