# Program to print multiplication table.

'''program using for loop'''
num = int(input("Enter the number : "));

for i in range(1,11):
    print(num,"X",i,"=",num*i);

'''program using while loop'''
num = int(input("Enter the number : "));

i = 1;
while i<=10:
    print(num,"X",i,"=",num*i);
    
    i = i + 1;