# Program to Check if a List is Empty

# SOLUTION 1 (using boolean operation)
my_list = []  # Initialize an empty list

# Check if the list is empty using a boolean operation
if not my_list:  
    # `not my_list` will evaluate to True if `my_list` is empty
    print("The list is empty.")

# SOLUTION 2 (using len() function)
my_list = []  # Initialize an empty list
print(len(my_list))  # Print the length of the list, which will be 0 for an empty list

# Check if the list is empty using the len() function
if len(my_list) == 0:  
    # `len(my_list)` returns 0, and the condition checks if the length is 0
    print("The list is empty.")

# SOLUTION 3 (using comparison with [])
my_list = []  # Initialize an empty list

# Check if the list is empty by comparing it with an empty list
if my_list == []:  
    # The condition will be True if `my_list` is equal to an empty list
    print("The list is empty.")
