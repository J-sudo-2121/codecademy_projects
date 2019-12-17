# if Statements
age = 15

if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("You are not old enough to vote kid!")
	print("Register as soon as you turn 18 kid!")

# if-elif-else Chain. It runs each conditional test in order until one passes. /
# When a test passes, the code folloing that test is executed and Python skips /
# the rest of th tests.

# Admission to park
age = 12

if age < 4:
	print("\nYour admission cost is $0.")
elif age < 18:
	print("\nYour admission cost is $25.")
else:
	print("\nYour admission cost is $40.")

# A more concise way to write the code above would be:
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"\nYour admission cost is ${price}.")
# This code above is easier to edit if needed in the future thus making it /
# better than the code written before.

# Using Multiple elif Blocks
age = 65

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"\nYour admission cost is ${price}.")	

# Python doesn't require an else block at the end of n if-elif chain.
age = 12

if age < 0:
	price = 'Input Error'
elif age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f"\nYour admission cost is ${price}.")