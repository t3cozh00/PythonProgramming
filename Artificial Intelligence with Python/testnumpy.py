import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Numpy array:",arr)

arr_sum = np.sum(arr)
print("Sum of array elements:", arr_sum)
arr_mean = np.mean(arr)
print("Mean of array elements:", arr_mean)

arr_2nd = np.array([[1, 2], [3, 4]])
print("2D Numpy array:\n", arr_2nd)

arr_2nd_transpose = np.transpose(arr_2nd)
print("Transpose of 2D Numpy array:\n", arr_2nd_transpose)