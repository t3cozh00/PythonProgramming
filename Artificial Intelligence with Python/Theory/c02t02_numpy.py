import numpy as np

Z = np.zeros(5)
print(".zeros(): ", Z)
Zs = np.shape(Z)
print(".shape(): ", Zs)

Z2 = np.zeros((4,5)) # notice doulbe pracets
# print(Z2)
Z2s = np.shape(Z2)
# print(Z2s)

Y = np.ones((2,3))
# print(Y)

# np.full() creates a 2D array with 7 rows and 8 columns, where every element is filled with the value 11
F=np.full((7,8),11) 
# print(F)
E=np.full((2,4),4.8)
# print(E)

# np.linspace(0, 5, 10) creates an array of 10 evenly spaced numbers between the start value 0 and the end value 5 (inclusive).
x1 = np.linspace(0,5,10)
print(x1)

x2 = np.linspace(0,5,11)
print(x2)

# arange () in turn takes the step length as the third parameter, does not reach a final value
x3 = np.arange(0,5,0.2)
print(x3)
x4 = np.arange(0,5,1)
print(x4)

# randint() return random integers from low (inclusive) to high (exclusive).
a = 1
b = 6
amount = 50
nopat = np.random.randint(a,b+1,amount)
print(nopat)
print(np.shape(nopat))

# .randn() generates an array of random numbers with the specified shape, where the numbers are drawn from a standard normal distribution(正态分布).
x5 = np.random.randn(4)
print(x5)

# .random() generates an array of random numbers with the specified shape, where the numbers are drawn from a uniform distribution between 0 and 1 (exclusive of 1).
x6 = np.random.random(10)
print(x6)