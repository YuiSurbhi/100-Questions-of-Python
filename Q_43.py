# Program to Merge Two Dictionaries

# 1) USING | (BAR) OPERATOR

# Define the two dictionaries 
dict1 = {"John" : 89, "Lisa" : 99}
dict2 = {"Lisa" : 94, "Peter" : 78}

# Print the merged dictionary; dict2 overwrite dict1
print(dict1 | dict2)

# 2) USING ** OPERATOR 

# Define the two dictionaries 
dict1 = {"John" : 89, "Lisa" : 99}
dict2 = {"Lisa" : 94, "Peter" : 78}

# Print merged dictionary using dictionary unpacking 
print({**dict1,**dict2})

# 3) USING COPY() AND UPDATE() METHOD 

# Define the two dictionaries
dict1 = {"John" : 89, "Lisa" : 99}
dict2 = {"Lisa" : 94, "Peter" : 78}

# Create a copy of dict2
dict3 = dict2.copy()
# Update dict3 with the content of dict1
dict3.update(dict1)

# Print the resulted dictionary 
print(dict3)