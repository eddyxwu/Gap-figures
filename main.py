import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the number of distributions
num_distributions = 5

# Define the mean and covariance of each distribution
means = np.random.rand(num_distributions, 3)
covs = np.random.rand(num_distributions, 3, 3)

# Create the data for each distribution
data = [np.random.multivariate_normal(means[i], covs[i], 500) for i in range(num_distributions)]

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each distribution
for i in range(num_distributions):
    ax.scatter(data[i][:,0], data[i][:,1], data[i][:,2], alpha=0.5)

# Set the axis labels and title
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("3D Gaussian Distributions")

# Show plot
plt.show()
