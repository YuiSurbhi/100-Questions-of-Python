# Program Remove Punctuations From a String

# Defining a string containing all punctuation characters 
punc = '''!()[]{},.;:"'!`-_<>/?!@#$%^&*~'''

# Read input from the user 
string = input("Enter anything here : ")

# Initializing an empty string to store character that are not punctuation 
empty_str = ""

# Iterate over each character in the input string 
for i in string:
    # Check if character is not in the punctuation list 
    if i not in punc:
        # Append the character to the result string 
        empty_str += i

# Printing the string with punctuation removed 
print(empty_str)