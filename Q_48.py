# Program to Sort a Dictionary by Value

marks = {"John": 36, "Lisa": 56, "Sid": 48}
print(marks)  # Print the original dictionary of marks

# SOLUTION 1: Sort the dictionary based on values
sv = sorted(marks.items(), key=lambda x: x[1])  
# `sorted()` function sorts the dictionary items (key-value pairs) based on the second item (value) of each pair
print(sv)  # Print the sorted list of key-value pairs

# SOLUTION 2: Sort only the values
v = sorted(marks.values())  
# `sorted()` function sorts the values of the dictionary in ascending order
print(v)  # Print the sorted list of values
