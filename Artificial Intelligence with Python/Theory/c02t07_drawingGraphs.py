import numpy as np
import matplotlib.pyplot as plt

# -------------------
# First Plot: Simple Red Line
# -------------------
x1 = [1,2,3,4]
y1 = [1,4,9,16]
plt.plot(x1,y1,'r',label='y = x^2')
plt.title('Title1')
plt.xlabel('x1')
plt.ylabel('y1')
plt.grid(True)
plt.show()


# -------------------
# Second Plot: Multiple Lines with Different Styles
# -------------------
x2 = np.linspace(0,7,100)
y2 = np.sin(x2)
plt.plot(x2,y2, 'go--', linewidth=2,label='y = sin(x)')
plt.plot(x2, 2*y2, 'r^', label='y = 2*sin(x)')
plt.title('Title2')
plt.xlabel('x2')
plt.ylabel('y2')
plt.legend() # distinguish between the two plotted lines
plt.grid(True)
plt.show()


# plt.subplot(1,2,1) # 1x2 grid 1. subpicture
# plt.plot(x1,y1)
# plt.title("first")
# plt.subplot(1,2,2) # 1x2 grid 2. subpicture
# plt.plot(x1,2*y1)
# plt.title("second")
# plt.suptitle("Common Title")
# plt.show()


# -------------------
# Third Plot: Subplots with Common Title
# -------------------
# Using plt.subplots() for better control
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns
# First Subplot
ax1.plot(x1, y1, 'b-o')  # Blue line with circle markers
ax1.set_title("First")
ax1.set_xlabel('x1')
ax1.set_ylabel('y1')
ax1.grid(True)  # Optional
# Second Subplot
ax2.plot(x1, 2 * np.array(y1), 'm-s')  # Magenta line with square markers
ax2.set_title("Second")
ax2.set_xlabel('x1')
ax2.set_ylabel('2*y1')
ax2.grid(True)  # Optional
# Common Title
fig.suptitle("Common Title", fontsize=16)
# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Leave space for suptitle
plt.show()


# -------------------
# Fourth Plot: Bar Chart
# -------------------
plt.barh(['2018','2019','2020'],[120000,125000,130000],color="blue")
plt.title("Title3")
plt.xlabel("years")
plt.ylabel("Sales")
plt.show()


# -------------------
# Fifth Plot: Histogram
# -------------------
x3 = np.random.randn(2000)
plt.hist(x3,10) # creates a histogram of the x3 data with 10 bins; 将数据（x3）分成10个区间（bins）绘制直方图
plt.ylabel('frequencies')
plt.show()


# -------------------
# Sixth Plot: creates two 2D arrays from these 1D arrays; heatmap
# -------------------
points = np.arange(-2,2,0.01)
print(points.size) # 400
x,y = np.meshgrid(points,points)
z = np.sqrt(x**2 + y**2)
plt.imshow(z)
plt.colorbar()
plt.show()


# -------------------
# Seventh Plot: Contour Plot
# -------------------
plt.contour(x, y, z)
plt.colorbar()  # Add colorbar to show levels
plt.title('Contour Plot')
plt.show()


# -------------------
# check the current working directory
# -------------------
import os
print("Current working directory:", os.getcwd())


# -------------------
# Eighth Plot: read and display an image in the current working directory
# -------------------
import matplotlib.image as mpimg
I=mpimg.imread('cameraman.png') # make sure the image is in the current working directory
plt.imshow(I)
plt.show()


# -------------------
# Ninth Plot: 3D Plot
# -------------------
from mpl_toolkits import mplot3d

x, y = np.meshgrid(np.linspace(-2, 2, 30),np.linspace(-2, 2, 30))
z = np.cos(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
ax.set_title('Texture')
plt.savefig('3D-plot.pdf')
plt.show()
