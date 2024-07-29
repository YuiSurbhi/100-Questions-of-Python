# Program To Check Whether a String is Palindrome or Not

# Input from the user 
a = input("Enter a word here : ")

# Reverse the string 
rev = a[::-1]

# Check if the original string is equal to the reversed string 
if a == rev:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")