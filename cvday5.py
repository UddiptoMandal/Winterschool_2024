import numpy as np
import cv2

A = [[3, 2], [1,3,4], [1,2,4,5], [2,3,5,6], [3,4], [4]]
lis = [0,0,0,0,0,0]

def DFS(c):
    print(c)
    if c==6:
        return
    lis[c-1] = 1
    for i in range(len(A[c-1])):
        t = A[c-1][i]
        if lis[t-1] == 0:
            DFS(t)
    return
DFS(1) 
print("DFS")


lis = [0,0,0,0,0,0]
A = [[3, 2], [1,3,4], [1,2,4,5], [2,3,5,6], [3,4], [4]]
que = [1]
c = 1
#BFS
while(len(que)):
    c= que[0]
    if(c==6):
        print(6)
        break
    
    lis[c-1] = 1
    for i in range (len(A[c-1])):
        t = A[c-1][i]
        if lis[t-1] == 0:
            que.append(t)
            lis[t-1] = 1
    print(c)
    que.pop(0)
    
# img = cv2.imread('MAP for BFS.jpg')
# cv2.imshow("Image", img)
# cv2.waitKey(0)


# def dist(a,b):
#     return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
# def check1(a): #if obstacle
#     if img1[a] != 0:
#         return False
#     else:
#         return True
# def check2(a, b):
#     theta = math.atan(b[1]-a[i]/b[0] - a[0])
#     if theta<math.pi/8 and theta>-math.pi/8:
#         if b[0] > a[0]:
#             img2[a[0], a[1]] = 255
#             return check2([a[0]+1, a[1]], b)
#         else
#             img2[a[0], a[1] ]=255
#             return check2([a[0]-1, a[1], b])
        
#     elif theta <3*math.pi/8 and theta > math.pi/8:


           
#     elif theta > 3*math.pi/8 and theta < -3*math.pi/8:
            
#     else:



# img = cv2.imread('MAP for BFS.jpg')
# img = cv2.resize(img, (500,500) )
# #img = cv2.GaussianBlur(img, (5, 5), 0) 
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img1 = np.full((500,500), 0, dtype = np.uint8)
# img2 = np.full((500,500), 0, dtype = np.uint8)
# for i in range(500):#path  possible
#     for j in range(500):
#         if img[i][j] <80:
#             img1[i][j] = 0
#         else:
#             img1[i][j] = 255
# cv2.imshow("Image", img)
# cv2.imshow("path", img1)
# cv2.waitKey(0)


# A = {}
# end = (420, 471)
# lis = {}

# for i in range (1,499):
#     for j in range (1,499):
        
#         if img1[i][j] ==0:
#             lis.update({(i,j):0})
#             if img1[i+1][j] == 0 and img1[i][j+1]==0 and img1[i-1][j]==0 and img1[i][j-1]==0:
#                 A.update({(i,j):[[i+1,j], [i,j+1], [i-1,j], [i,j-1]]})
#             elif img1[i][j+1]==0 and img1[i-1][j]==0 and img1[i][j-1]==0:
#                 A.update({(i,j):[[i,j+1], [i-1,j], [i,j-1]]})
#             elif img1[i-1][j]==0 and img1[i][j-1]==0:
#                 A.update({(i,j):[[i-1,j],[i,j-1]]})
#             elif img1[i][j-1]==0:
#                 A.update({(i,j):[i,j-1]})

# print(A)
# print(lis)
# print(len(A))

# c = (15,15)
# que = [c]
# while(len(que)):
#     c = que[0]
    
#     if c==end:
#         img2[c[0], c[1]] = 255
#         break
#     lis[c[0], c[1]] = 1
#     for i in range (len(A[c[0], c[1]])):
#         t = A[c[0], c[1]]
#         if t[0] == 0 or t[1] == 0 or t[0] == 499 or t[1] == 499:
#             continue
#         if lis[t[0],t[1]]==0:
#             que.append(t)
#             lis[t[0],t[1]] =1
#     img2[c[0], c[1]] = 255
#     que.remove(c)

# cv2.imshow("pah", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

        


A = [[3, 2], [1,3,4], [1,2,4,5], [2,3,5,6], [3,4], [4]]
vis = [0 for _ in range(len(A))]
st = []
def DFS(st):
    t = st[-1]
    if vis[t-1] == 0:
        print(t)
        vis[t-1] = 1
        for i in A[t-1]:
            st.append(i)
            DFS(st)
    else:
        return
print("DFS")
st.append(1)
DFS(st)

# Kruskal's algorithm
