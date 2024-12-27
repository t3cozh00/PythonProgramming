# Cutting Matrices (indexing)

import numpy as np

A1 = np.array([[1,2,3], [4,5,6]])
print(A1[0,0]) # 1
print(A1[1,2]) # 6
print(A1[1,1]) # 5
print(A1[0,:]) # [1 2 3]
print(A1[:,1]) # [2 5]

A2 = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 10], [11, 12]],
    [[13, 14], [15, 16], [17, 18]]
])
print(A2[0,1,1]) # 4
print(A2[2,2,1]) # 18

A3 = np.array([1,2,3,4,5,6,7,8,9])
print(A3[0:6:1]) # [1 2 3 4 5 6]
print(A3[0:6:2]) # [1 3 5]

A4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(A4[0:2, 1:3]) # [[2 3] [6 7]]
print(A2[0:4, 0:4:2]) # [[1 3] [5 7] [9 11] [13 15]]

A5 = np.array([[1,2,3],[4,5,6]])
A5[0,0] = 17
A5[1,:] = [11,12,13]
print(A5) # [[17  2  3] [11 12 13]]

A6 = np.array([1, 2, 3])
new = np.vstack((A6, A6))
print(new) # [[1 2 3] [1 2 3]]
new2 = np.hstack((A6, A6))
print(new2) # [1 2 3 1 2 3]

A7 = np.array([[1, 2, 3], [4, 5, 6]])
new3 = np.vstack((A7, A7))
print(new3) # [[1 2 3] [4 5 6] [1 2 3] [4 5 6]]
new4 = np.hstack((A7, A7))
print(new4) # [[1 2 3 1 2 3] [4 5 6 4 5 6]]

A8 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
new5 = np.vstack((A8, A8))
print(new5) # [[[ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12]] [[ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12]]]
new6 = np.hstack((A8, A8))
print(new6) # [[[ 1  2  3] [ 4  5  6] [ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12] [ 7  8  9] [10 11 12]]]
print(new6.shape)

A9 = np.array([1,2,3,4,5,6])
A10 = A9.reshape(2,3)
n,m = np.shape(A10) 
for i in range(n):
    print("Row",i,"is",A10[i,:])

for j in range(m): 
    print("Column",j,"is",A10[:,j])

for i in range(n):
    for j in range(m):
        print("Element",i,j,"is",A10[i,j])

for a in np.nditer(A10):
    print(a)