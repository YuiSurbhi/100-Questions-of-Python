#program to display power of 2 using anonymous function 

nterms = int(input("Enter the number of terms : "))

result = list(map(lambda x: 2**x,range(nterms +1)))

print(result)

#displaying nterms line by line
for i in range (nterms +1):
    print("The value of 2 raised to the power", i,"is", result[i])
