# Program to find factorial of a number.

num = int(input("Enter the number : "));

fact = 1;

if num < 0:
    print("Factorial of 0 does not exist.");

if num == 0:
    print("Factorial of 0 is : ",1);

if num > 0:
    for i in range (1,num + 1):
        fact = fact*i;
print("The factorial of a given number is : ",fact);

'''program using recursion'''
def fact(a):
    if a == 0:
        return 1;
    else:
        return((a)*fact(a - 1));
num = int(input("Enter the number : "));

result = fact(num);
print("The factorial of given number is : ",result);
