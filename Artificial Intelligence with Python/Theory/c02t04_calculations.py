# Calculations with Matrices
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[3,9],[4,-1]])
print(A+B) # [[ 4 11] [ 7  3]]
print(A-B) # [[-2 -7] [-1  5]]
print(A**2) # [[ 1  4] [ 9 16]]
np.matmul(A,B) # [[11  7] [25 27]]
print(np.sqrt(A))
# np.sin(A)
# np.cos(A)
# np.tan(A)
# np.log(A)
# np.exp(A)
# np.log10(A)
# np.log2(A)

T = 5*np.ones((4,4))
print(T) # [[5. 5. 5. 5.] [5. 5. 5. 5.] [5. 5. 5. 5.] [5. 5. 5. 5.]]

B2 = np.array([[5],[7]])
print(np.matmul(A,B2)) # [[19] [43]]

# A = np.array([[1,2],[3,4]])
print(np.all(A>1))
print(np.any(A>3))

A1 = np.array([1,2,3,4,5,6,7])
B1 = A1[A1>3]
print(B1) # [4 5 6 7]

A2 = np.array([[2,1],[-4,3]])
b = np.array([11,3])
X = np.linalg.solve(A2,b)
print(X) # [3. 5.]

# Ainv = np.linalg.inv(A2)
# print(Ainv) 
# print(np.matmul(Ainv,b))