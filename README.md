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

To load the A matrix and b vector for each case,
```
from load_systems import case

A1,b1 = case(1) # for example 1
A2,b2 = case(2) # for example 2
```


# Example Linear Systems $\mathbf{A}\cdot\mathbf{x}=\mathbf{b}$

## Example 1
Is a square matrix (5x5) matrix

$$\mathbf{A} = \begin{bmatrix} 4 & 1 & 0 & 0 & 0\\
1 & 4 & 1 & 0 & 0\\
0 & 1 & 4 & 1 & 0\\
0 & 0 & 1 & 4 & 1\\
0 & 0 & 0 & 1 & 4
\end{bmatrix}$$

and 

$$\mathbf{b} = \begin{bmatrix} 1\\ 
2 \\ 
3 \\ 
4 \\ 
5 \end{bmatrix}$$

## Example 2 - Hilbert Matrix
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

## Example 3

$$\mathbf{A} = \begin{bmatrix} 3.271428391e8 & 1.552948112e9 & 9.114228551e7 & 4.771992331e6 & 8.221551992e5\\
9.814285173e8 & 4.657844336e9 & 2.735268565e8 & 1.431597699e7 & 2.466465597e6\\
1 & 1 & 1 & 1 & 1\\
0 & 1 & 2 & 3 & 4\\
1 & 3 & 5 & 7 & 9
\end{bmatrix}$$

and 

$$\mathbf{b} = \begin{bmatrix} 1\\ 
2 \\ 
3 \\ 
4 \\ 
5 \end{bmatrix}$$

