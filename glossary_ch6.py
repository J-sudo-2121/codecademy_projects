# Glossary.
glossary_meanings = {
	'variable': 'A reserved memory location to store values.',
	'tuples': 'A squence of immutable objects in Python.',
	'lists': 'Created by placing all the items inside a square bracket, \
separated by commas.', 
	'the slice method': 'Slice object is used to slice a given squence or \
object which supports squence protocol.',
	'a for loop': 'Traditionally used when you have a block of code which you \
want to repeat a fixed number times.',
	'dictionary values()': 'An inbuilt method in Python that returns a list of \
all the values available in a given dictionary.',
	'set': 'An unordered collection data type that is iterable, mutable, and \
has no duplicate elements.',
	'the sorted() function': 'Sorts any sequence and always returns a list with\
 the elements in sorted manner, without modifying the original sequence.',
	'dictionary keys() method': 'returns a list of all the available keys in \
the dictionary.',
	'the print() function': 'Prints the given object to the standard output \
device or to the text stream file.',
	}

for glossary, meaning in glossary_meanings.items():
	print(f"\n{glossary.title()}:\n{meaning}")

# Make a dictionary containing 3 major rivers and their locations.
rivers_and_locations = {'mississippi': 'USA', 'mekong': 'Laos', 
	'ganges': 'India',
	}
# Use a loop to print a sentence bout each.
for river, location in rivers_and_locations.items():
	print(f"\nThe {river.title()} runs through {location}.")

# Use a loop to print each name of each river.
print("\nThe Rivers Are:")
for river in rivers_and_locations:
	print(f"The {river.title()}")

# Use a loop to print the name of each country.
print("\nThe Countries Are:")
for location in rivers_and_locations.values():
	print(location)