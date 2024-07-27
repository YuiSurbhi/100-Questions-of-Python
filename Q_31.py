# Program to Find the Sum of Natural Numbers Using Recursion

def NNS  (n):        # NNS is natural number sum
    if n <= 1:
        return n
    else:
        return (n)+NNS(n-1)    
    
n = int(input("Enter an number : "))

if n <= 0:
    print("Enter a positive number.")
else:
    print("The sum of natural number upto given number is : ",NNS(n))


