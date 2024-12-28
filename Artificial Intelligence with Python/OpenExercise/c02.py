# 01 Draw the lines
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.plot(x, y1, 'r-', label='y=2x+1')
plt.plot(x, y2, 'b--', label='y=2x+2')
plt.plot(x, y3, 'g+', label='y=2x+3')

plt.title('Graphs of y=2x+1, y=2x+2, y=2x+3')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()

# -------------------
# Task 6: Draw a dot pattern
# -------------------
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])
plt.scatter(x, y, marker='+')
plt.show()

# -------------------
# Task 7: Populating table from a file
# -------------------
data = np.genfromtxt('weight-height.csv', delimiter=',', skip_header=1)

lengths_in = data[:, 1]
weights_lb = data[:, 2]

lengths_cm = lengths_in * 2.54 # 1 inch = 2.54 cm
weights_kg = weights_lb * 0.453592 # 1 pound = 0.453592 kg

print("Mean of lengths: ",np.mean(lengths_cm))
print("Mean of weights: ",np.mean(weights_kg))
print("Median of lengths: ",np.median(lengths_cm))
print("Median of weights: ",np.median(weights_kg))
print("Standard deviation of lengths: ",np.std(lengths_cm))
print("Standard deviation of weights: ",np.std(weights_kg))
print("Variance of lengths:",np.var(lengths_cm))
print("Variance of weights: ",np.var(weights_kg))

plt.hist(lengths_cm, bins=20)
plt.title("Histogram of Lengths (in cm)")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.show()

# -------------------
# Task 8: Determinant
# -------------------
A = np.array([[1, 2],[3, 4]])
B = np.array([[-1, 1],[5, 7]])
AB = np.dot(A, B)

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_AB = np.linalg.det(AB)

print(f"det(A) = {det_A}")
print(f"det(B) = {det_B}")
print(f"det(AB) = {det_AB}")

print(f"det(AB) == det(A) * det(B): {np.isclose(det_AB, det_A * det_B)}")

# -------------------
# Task 9: Inverse matrix
# -------------------
A = np.array([[1, 2, 3],[0, 1, 4], [5, 6, 0]]) 
A_inv = np.linalg.inv(A)

A_A_inv = np.dot(A, A_inv)
A_inv_A = np.dot(A_inv, A)

print("A_inv:", A_inv)
print("A * A_inv:", A_A_inv)
print("A_inv * A:", A_inv_A)