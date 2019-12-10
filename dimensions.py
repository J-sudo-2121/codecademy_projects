# Tuples are immutable lists. Tuple looks just like a lit except you use () inst
# ead of [].

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Tuples are defined by the presence of a comma. If you want to make a tuple 
# with a single element, a comma needs to be included. my_t = (3,)

# Looping through all values in a tuple using a for loop is the same as with a 
# list.
for dimension in dimensions:
	print(dimension)

# You can assign a new value to a variable that represents a tuple thus allowing
# you to make changes to a tuple through the new value.
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)