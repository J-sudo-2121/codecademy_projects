# Python's range() function makes it easy to generate a series of numbers.
for value in range(1, 5):
	print(value)
# range() when printed has the off-by-one behavior. The range() function causes Python to start counting at the first value you give, and stop when it reaches the second value.
## To print the numbers from 1 to 5 you would need to use range(1, 6).
for value in range(1, 6):
	print(value)
# Using only one argument with range() will start the count from 0.
for value in range(5):
	print(value)

# When you wrap list() around a call to the range() function, the output ill be a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# You can use the range() function to tell Python to skip numbers in a given range. The 3rd value is what Python uses for skipping.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# In Python ** represents exponents.
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

# A few Python functions are helpful when working with lists of numbers. Finding the minimum, maximum, and sum of a list of numbers.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension allows you to generate same list as "squares" listed above in just one line of code. A list comprehension combines
## the for loop and the creation of the new elements into one line and automtically appends each new elemnt.
squares = [value**2 for value in range(1, 11)]
print(squares)

# Practicing making for loop to print numbers from 1 to 20.
for value in range(1, 21):
	print(value)

# Practicing making a loop to print from one to one million.
million = list(range(1, 1_000_001))
print(million)

# Practicing summing a million.
print(min(million))
print(max(million))
print(sum(million))

# Practicing Printing Odd Numbers.
for odd_numbers in range(1, 21, 2):
	print(odd_numbers)

# Practicing Making list of multiples of 3's.
for multiples_of_three in range(3, 31, 3):
	print(multiples_of_three)

# Practicing Making Cubes.
cubes = []
for value in range(1, 11):
	cube = value ** 3
	cubes.append(cube)
print(cubes)

# Practicing Making cube comprehenion.
cubes = [value**3 for value in range(1, 11)]
print(cubes)