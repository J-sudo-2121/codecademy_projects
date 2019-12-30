# Looping Through A Dictionary.
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

# To see all information stored in dictionary use a for loop.
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")
# items() method following the name of the dictionary returns a list of key- \
# value pairs.

# Many users. Dictionary inside a dictionary.
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")