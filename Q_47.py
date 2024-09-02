# Program to Iterate Over Dictionaries Using For Loop

friends = {"Richeal":"Ross","Monica":"Chandler","Phoebe":"Joe"}
print(friends)
print(friends["Monica"])

# SOLUTION 1  WITH (.items)
for key,value in friends.items():
    print(key,"-",value)

# SOLUTION 2 WITH (keys)
for key in friends:
    print(key,":",friends[key])

# SOLUTION 3 WITH (keys and values)
for key in friends.keys():
    print(key)

for i in friends.values():
    print(i)