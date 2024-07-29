# Program to Transpose a Matrix 

# 1) USING FOR LOOP 
# Original matrix A
A = [[1,2,3],
     [4,5,6]]

# Initialize the transposed matrix T with 0
# The dimension of T should be reverse of A
T = [[0,0],       
     [0,0],
     [0,0]]

# Iterate over each element in the original matrix A
for i in range(len(A)):      # Loop through rows of matrix A
    for j in range(len(A[0])):       # Loop through columns of matrix A
        T[j][i] = A[i][j]

# Print the transpose matrix T
for i in T:
    print(i)

# 2) USING LIST COMPREHENSION 
# Original matrix A
A = [[1,2,3],
     [4,5,6]]

# Transpose matrix A using list comprehension 
# 'i' iterate over columns of A, 'j' iterate over rows of A
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Print transposed matrix T
for i in T:
    print(i)