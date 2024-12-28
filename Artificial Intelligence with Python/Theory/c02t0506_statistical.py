# Statistical functions
# sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod
# About Data Types
# https://numpy.org/doc/stable/reference/arrays.dtypes.html
import numpy as np

A1 = np.array([[1,2,3],[4,5,6]])
r101 = np.sum(A1) # sum of all elements
r102 = np.sum(A1,0) # column sums, summed along rows
r103 = np.sum(A1,1) # row sums, summed along columns
print(r101) # 21
print(r102) # [5 7 9]
print(r103) # [ 6 15]

print(A1.dtype)
print(A1.itemsize) # 表示数组中每个元素占用的字节数
print(A1.nbytes) # 表示整个数组占用的内存字节数
A3 = A1.astype("int8") 
print(A3.dtype)
print(A3.itemsize)
print(A3.nbytes)
A2 = np.array([1,2,3,4,5,6],dtype="int64")
print(A2.nbytes)