# A Simple Dictionary.
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# A dictionary in Python is a collection of key-value pairs. Each key is \
# connected to a value, and you can use a key to access the value associated \
# with that key. A dictionary is wrapped inside braces {}. Every key is \
# conncected to its value by a colon :.

# Accessing Values in a Dictionary. To get the value associated with a key give\
# the name of the dictionary and then place the key inside a set of square \
# brackets []

print(alien_0['color'])

# If a player shoots down an alien you can now look up how man points they earn.

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs. Dictionaries are dynamic structures.
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary.
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary.
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

# Storing a value that has alien's current speed and then use it to determine \
# how far to the right it should move.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs. You can ue the del statement to completely remove \
# a key-value pair. All del needs is the name of the dictionary and the key to \
# remove.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# Points is now deleted permanently.

# Using get() to Access Values.
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0)
# For dictionaries you can use the get() method to set a default value that \
# will be returned if the requested key doesnt exist.

# The get() method requires a key as a first arguement.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If the key 'points' exists in the dictionary, you'll get the corresponing \
# value. If it doesn't you get the default value

# Nesting. You can nest dictionries inside a list, a list of items inside a \
# dictionary, or a dictionary inside another dictionary.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# A more realistic example:
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# When it's time to change colors, we can use a for loop and an if statement to\
# change colors of aliens.
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")