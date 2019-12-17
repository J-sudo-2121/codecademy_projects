# When you want to determine whether two values are not equal use (!=). !
# represents not.
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")
# Most of the conditional expressions you write will test for equality. /
# Sometimes you'll find it more efficient to test for inequlity.

# To find out wheter a particular value is already in a list, use keyword in.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
# Will return True

'pepperoni' in requested_toppings
# Will return False

# This is helpful by allowing you to create a list of esential values and then /
# easily check whether the value you're testing matches one of the values on /
# the list.

# Sometimes it's important to check all of the conditions of interest. If so, /
# use a series of simple if statments without elif or else blocks.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")
# This code wouldn't work properly if an if-elif-else chain was used. If you /
# want only one block of code to run, use an if-elif-else chain. If more than /
# one block of code needs to run, use a series of independent if statements.

# Searching for special values that need to be treated differently than other /
# values in the list.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("\nSorry, we are out of green peppers right now.")
	else:
		print(f"\nAdding {requested_topping}.")

print("\nFinished making your pizza!")

#Checking that a list is not empty.
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"\nAdding {requested_topping}")
	print("\nFinished making your pizza!")
else:
	print("\nAre you sure you want a plain pizza?")

# Using Multple Lists.
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
					  'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

print("\nCan I take your order?")
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")