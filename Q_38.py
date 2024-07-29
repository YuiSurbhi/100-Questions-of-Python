# Program: How to Multiply Two Matrices?

# Define the matrices A and B
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1,2,1,1],
     [4,2,1,2],
     [6,3,4,1]]

# Initializing the result matrix with 0
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# Perform matrices multiplication 
for i in range(len(A)):       # Iterate over rows of A
    for j in range(len(B[0])):       # Iterate over columns of B
        for k in range(len(B)):        # Iterate over rows of B
            result[i][j] += A[i][k] * B[k][j]

# Print the result matrix 
for r in result:
    print(r)