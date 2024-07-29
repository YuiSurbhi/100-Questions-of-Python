# Program Convert Decimal to Binary Using Recursion

def ConvertBinary(n):
    # If the number is greater then 1, continue the recursion
    if n > 1:
        # Divide the number by 2 and process the quotient
        ConvertBinary(n//2)

        # Print the remainder when divided by 2
        # print end="" to avoid adding a new line after each new bit 
    print(n % 2,end="")

# Print a description message before displaying the binary 
print("The binary of the given number is : ")

# Call the ConvertBinary function with 32 to convert it to binary 
ConvertBinary(32)