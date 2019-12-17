# Using an if statement.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# Python uses the values of True and False to decide whether the code in an if /
# statement should be executed.

# Conditional Tests.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

animal = 'dog'
print("\nIs animal == 'fish'? I predict False")
print(animal == 'fish')

print("\nIs animal == 'dog'? I predict True")
print(animal == 'dog')

color = 'brown'
print("\nIs color == 'brown'? I predict True")
print(color == 'brown')

print("\nIs color == 'yellow'? I predict False")
print(color == 'yellow')

computer = 'Asus'
print("\nIs computer == 'asus'? I predict False")
print(computer == 'Dell')

print("\nIs computer == 'asus'? I predict True")
print(computer.lower() == 'asus')

fruit = 'durian'
print("\nIs fruit == 'papaya'? I predict False")
print(fruit == 'papaya')

print("\nIs fruit == 'durian'? I predict True")
print(fruit == 'durian')

shoes = 'nike'
print("\nIs shoes != 'adidas'? I predict True")
print(shoes != 'adidas')

print("\nIs shoes != 'nike'? I predict False")
print(shoes != 'nike')

number = 37
print('\nIs number > 31? I predict True')
print(number > 31)

print("\nIs number <= 17? I predict False")
print(number <= 17)

print("\nIs number < 22 and 39? I predict False")
print((number < 22) and (number <39))

print("\nIs number > 56 or 22? I predict True")
print((number > 56) or (number > 22))

storage_items = ['pens', 'staples', 'paper', 'ink', 'pencils']
requested_items = ['pens', 'pencils', 'erasers', 'markers']
for requested_item in requested_items:
	if requested_item in storage_items:
		print(f"\n{requested_item.title()} can be found on the second shelf in \
the closet")
	else:
		print(f"\nSorry, we are out of {requested_item}.")