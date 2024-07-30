# Program to Count the Number of Each Vowel 

# 1) USING DICTIONARY 
# Initializing the string and vowels 
a = "Harry Potter And The Goblet Of Fire"
vowel = "aeiou"

# Convert string into lowercase for case insensitive processing 
a = a.casefold()
print(a)

# Initializing dictionary to hold vowel count as keys
count = {}.fromkeys(vowel,0)
print(count)

# Iterate over each character in the lower case
for char in a:
    # Check if the character is one of the vowels we are counting
    if char in count:
        count[char] += 1

# Print the result 
print(count)

# 2) USING LIST AND DICTIONARY COMPREHENSIVE 
# Initializing the string and vowels 
a = "Harry Potter And The Goblet Of Fire"
vowel = "aeiou"