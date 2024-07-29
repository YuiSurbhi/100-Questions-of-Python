# Program to add two matrices 

# Define the matrices A & B
A = [[1,5,6],
     [4,2,3],
     [6,9,1]]

B = [[2,6,4],
     [1,7,3],
     [5,8,9]]

# Initialize the result matrix with 0
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):      # Iterate over the rows 
    for j in range(len(A[0])):      # Iterate over the columns 
        result[i][j] = A[i][j] + B[i][j]       # Add corresponding elements 

# Print the result matrix 
for r in result:
    print(r)