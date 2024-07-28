# Program to Find Factorial of Number Using Recursion

def fact(n):
    # factorial of 1 is 1
    if n == 1:
        return 1
    # factorial of n is n multiplied by factorial of (n-1)
    else:
        return(n*fact(n-1))
    
# Taking input from user     
n = int(input("Enter a number : "))

# Check if the number is less than or equal to 0
if n <= 0:
    print("Factorial of a number less than 1 does not exist.")
else:
    # Print the factorial of the given number 
    print("Factorial of given number is : ",fact(n))