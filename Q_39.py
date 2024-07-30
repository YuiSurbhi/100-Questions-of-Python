# Program to Sort Words in Alphabetic Order (A B C)

# Get input from the user 
a = input("Enter something here : ")

# Split the input string into a list of words 
w = a.split()

# Convert each word in the list to lowercase 
for i in range (len(w)):
    w[i] = w[i].lower()

# Sort the list of words alphabetically
w.sort()

# Print each word in the sorted list 
for word in w:
    print(word)