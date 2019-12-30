# A Dictionary of Similar Objects. You can use a dictionary to store one kind \
# of information about many objects.
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
# Each key is the name of a person and each value is their language choice. \
# When you know you'll need more than one line to define a dictionary, press \
# Enter after the opening brace. The closing brace should be indented one level.

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Creating a loop for the dictionary.
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

# The keys() method is useful when you dont need to work ith values in a \
# dictionary.
for name in favorite_languages.keys():
	print(name.title())

# Looping through the keys is the default behavior when looping through a \
# dictionary. The following will give the same output as above.
for name in favorite_languages:
	print(name.title())

# You can access the value associated with any key you care about inside the \
# loop by using the current key.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

# Using the keys() method to find out if a particular person was polled.
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# Use the sort() function to get a copy of the key in order.
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

# For finding only the values in a dictionary use the values() method.
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# To see each language without repetition can use set. A set is a collection \
# in which each item must be unique.
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# You can build a set directly using braces and separating the elements with \
# commas.
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
# Sets do not retain items in any specific order.

# Make a list of people who should take the favorite languages poll.
take_the_poll = ['jen', 'mike', 'jon', 'phil']
for name in take_the_poll:
	if name in favorite_languages.keys():
		print(f"\nThank you {name.title()} for taking the poll.")
	else:
		print(f"\n{name.title()}, please remember to take the poll.")

# You can nest a list inside a dictionary any time you want more than one value\
# to be associated with  single key in a dictionary. Inside the dictionary's \
# for loop, we use another for loop to run through the list of languages.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
# If the nested items are much deeper than what is in preceding example, there \
# most likely is a simpler way to solve the problem.