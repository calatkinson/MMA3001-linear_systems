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

# Example Linear Systems

## Example 1 - Hilbert Matrix
The Hilbert Matrix is a square matrix with entries being the unit fractions

{\displaystyle H_{ij}={\frac {1}{i+j-1}}.}
