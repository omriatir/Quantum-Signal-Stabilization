import numpy as np
import matplotlib.pyplot as plt
from Fresnel_Coefficients import reflectivity,transmissivity
from n_calculation import n

# Define the range of x and y values
x_values = np.linspace(-1, 1, 100)  # Example: 5 points from -1 to 1
y_values = np.linspace(-1, 1, 100)  # Example: 5 points from -1 to 1

# Create the meshgrid
x_mesh, y_mesh = np.meshgrid(x_values, y_values)

# Define parameters for the Gaussian distribution
mu_x = 0  # Mean along x-axis
mu_y = 0  # Mean along y-axis
sigma_x = 0.8  # Standard deviation along x-axis
sigma_y = 0.8  # Standard deviation along y-axis

def two_dim_gaussian(x_mesh,y_mesh):
    gaussian = np.exp(-2*((x_mesh - mu_x) ** 2 / (sigma_x ** 2) + (y_mesh - mu_y) ** 2 / (sigma_y ** 2)))
    return gaussian

starting_beam = two_dim_gaussian(x_mesh,y_mesh)

plt.figure(figsize=(8, 6))
plt.contourf(x_mesh, y_mesh, starting_beam, cmap='viridis')
plt.colorbar(label='Intensity')
plt.title('2D Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)


# the noise model

def random_2d_grid(rows, cols, density=0.5):
    # Generate a random grid of floats between 0 and 1
    random_grid = np.random.rand(rows, cols)

    # Convert the random floats to ones and zeros based on the density
    binary_grid = (random_grid < density).astype(int)

    return binary_grid

# Random Grid Parameters:
rows = 100
cols = 100
density = 0.5

# laser beam properties
wavelength = 0.8 #micrometer
w0 = 0.8 #gaussian beam waist (Standard deviation)

# propagation of beam under changing turbulent conditions:
steps = 200
step_size = 0.001
n1 = 1
z = 0

def w(z,n):
    zr = np.pi*(w0**2)*n/wavelength
    return w0*(1+(z/zr)**2)**0.5

for i in range(steps):
    random_grid = random_2d_grid(rows,cols,density)
    n2 = n(0.8, 15, 101325, 0, 450)
    wz = w(z,1.1)
    advanced_gaussian = ((w0/wz)**2)*np.exp(-2*((x_mesh - mu_x) ** 2 / (wz ** 2) + (y_mesh - mu_y) ** 2 / (wz ** 2)))
    mid_grid = advanced_gaussian*random_grid*(transmissivity(n1,1.1)**2)
    advanced_beam = advanced_gaussian*(random_grid-1)**2 + mid_grid
    z = z + i*step_size

#2D plot

plt.figure(figsize=(8, 6))
plt.contourf(x_mesh, y_mesh, advanced_beam, cmap='viridis')
plt.colorbar(label='Intensity')
plt.title('2D Power Distribution of The Final Beam')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#3D plot

fig=plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(x_mesh, y_mesh,advanced_beam,
                rstride=1,
                cstride=1,
                cmap='rainbow',
                linewidth=0.0,
                )
ax.set_zlabel('Intensity [a.u.]')
plt.show()

fig=plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(x_mesh, y_mesh,starting_beam,
                rstride=1,
                cstride=1,
                cmap='rainbow',
                linewidth=0.0,
                )
ax.set_zlabel('Intensity [a.u.]')
plt.show()
