# Program to Illustrate Different Set Operations

# Defining the sets 
A = {1,2,3,6,8,9}
B = {3,4,5,6,7,8}

# Calculate the union of sets A and B
print("The Union is : ",A | B)

# Calculate the intersection of sets A and B
print("The Intersection is : ",A & B)

# Calculate the difference of sets A and B (elements in A but not in B)
print("The Difference is : ",A - B)

# Calculate the symmetric difference of sets A and B (elements in either A or B but not in both)
print("The Symmetric Difference is : ",A ^ B)