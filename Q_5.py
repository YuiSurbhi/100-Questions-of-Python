# Program to swap two numbers.

'''Program using a third variable'''
x = 12  # Initialize variable x with a value of 12
y = 13  # Initialize variable y with a value of 13

temp = x  # Assign the value of x to a temporary variable 'temp'
print("The value of temp variable is:", temp)  # Print the value of the temporary variable

x = y  # Assign the value of y to x
print("The value of x variable is:", x)  # Print the new value of x

y = temp  # Assign the value of the temporary variable back to y
print("The value of y variable is:", y)  # Print the new value of y

'''Program without using a third variable'''
x = 12  # Initialize variable x with a value of 12
y = 13  # Initialize variable y with a value of 13

x, y = y, x  # Swap the values of x and y without using a third variable

print("The value of x variable is:", x)  # Print the new value of x
print("The value of y variable is:", y)  # Print the new value of y
