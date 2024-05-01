# Program to swap two numbers.

'''program using third variable'''
x = 12;
y = 13;

temp = x;
print("The value of temp variable is : ",temp);

x = y;
print("The value of x variable is : ",x);

y = temp;
print("The value of y variable is : ",y);

'''program without using third variable'''
x = 12;
y = 13;

x,y = y,x;

print("The value of x variable is : ",x);
print("The value of y variable is : ",y);