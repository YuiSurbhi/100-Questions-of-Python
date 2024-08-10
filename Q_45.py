# Program to Accessing Index of List using for Loop.

# USING ENUMERATE METHOD

# Define a list of numbers
l = [22,56,11,41,19]

# Iterate over the list with enumerate to get index ad value
for index,value in enumerate(l):
    # Print the index and corresponding value
    print(index,"-",value)

# WITHOUT USING ENUMERATE METHOD

# Define list of numbers
l = [22,56,11,41,19]

# Iterate over the range of indices for the list 
for index in range(len(l)):
    # Access the element at the current index
    value = l[index]
    # Print the index and corresponding value
    print(index,"-",value)