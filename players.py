# Working with a specific group of items in a list is called a slice (slicing) 
# in Python.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# You can generate any subset of a list.
print(players[1:4])
# If you omit the first index in a slice Python automatically starts your slice 
# at the beginning of the list.
print(players[:4])
# Same goes for the last index.
print(players[1:])
print(players[-3:])
# Adding a third number to the index tells Python how many items to skip between
# items in the specified range.
print(players[::2])

# You can use  slice in a for loop if you want to loop through parts of the 
# elements in a list.
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# Trying my own. Three different slices.

# Print the first 3 from the list.
print("The first three items on the list are:")
for first_three in players[:3]:
	print(first_three.title())

# Print 3 items from the middle of the list
print(len(players))
print("Three items from the middle of the list are:")
for middle_three in players[1:4]:
	print(middle_three.title())

# Print last 3 items on the list.
print("The last three items from the list are:")
for last_three in players[-3:]:
	print(last_three.title())



