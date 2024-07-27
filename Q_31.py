# Program to Find the Sum of Natural Numbers Using Recursion

# NNS is natural number sum
def NNS  (n):       
    # When n is 1 or less, just return n
    if n <= 1:
        return n
    # Sum of current number n plus sum of numbers up to (n-1)
    else:
        return (n)+NNS(n-1)    

# Input from the user     
n = int(input("Enter an number : "))

# Check if number is positive 
if n <= 0:
    print("Enter a positive number.")
else:
    # Call the NNS function and print the result 
    print("The sum of natural number upto given number is : ",NNS(n))


