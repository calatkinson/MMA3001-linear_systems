# MMA3001-linear_systems
A series of sample linear systems.

Matrices for each system are stored as NumPy binary *.npy files 
using the NumPY save and load functions below.

```
import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Export to binary
np.save('my_matrix.npy', matrix)

# Reload it later
loaded_matrix = np.load('my_matrix.npy')
```

# Example Linear Systems $\mathbf{A}\cdot\mathbf{x}=\mathbf{b}$

## Example 1 - Hilbert Matrix
The Hilbert Matrix is a square matrix with entries being the unit fractions

$$H_{ij}=\frac{1}{i+j-1}$$

Consider a system where 

$$\mathbf{A} = H_{ij} = \begin{bmatrix} 1 & \frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \frac{1}{5}\\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \frac{1}{5} & \frac{1}{6}\\
\frac{1}{3} & \frac{1}{4} & \frac{1}{5} & \frac{1}{6} & \frac{1}{7}\\
\frac{1}{4} & \frac{1}{5} & \frac{1}{6} & \frac{1}{7} & \frac{1}{8}\\
\frac{1}{5} & \frac{1}{6} & \frac{1}{7} & \frac{1}{8} & \frac{1}{9}
\end{bmatrix}$$

and

$$b_i = \sum^5_{j=0}H_{ij}$$

or

$$\mathbf{b} = \begin{bmatrix} 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5}\\
\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\\
\frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7}\\
\frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}\\
\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9}
\end{bmatrix}$$
