import numpy as np

# Define two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Perform matrix multiplication
result = np.dot(A, B)

# Display the result
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix Multiplication Result (A x B):")
print(result)
