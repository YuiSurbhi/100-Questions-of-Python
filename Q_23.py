#program to convert decimal into binary, octal, and hexadecimal

decimal = int(input("Enter a number : "))

print("The conversion of decimal number", decimal,"is : ")
print(bin(decimal),"in binary")
print(oct(decimal),"in octal")
print(hex(decimal),"in hexadecimal")