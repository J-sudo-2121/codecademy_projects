# Write a program that asks the user what kind of rental car they want.
car = input("What type of car would you like rent? ")
print(f"\nLet me check our database to see if we have any {car.title()}s " 
	"available.")

# Write a program that asks the user how many people are in their dinner group.
dinner_group = input("How many people are in your dinner party? ")
dinner_group = int(dinner_group)

if dinner_group >= 8:
	print(f"\nYour group of {dinner_group} will have to wait for more tables "
		"to open before we can seat you.")
else:
	print(f"\nYour group of {dinner_group} can be seated right away.")

# Ask the user for a number. Report if the number is a multiple of 10 or not.
number = input("Enter a number and I will determine if it is a multiple "
	"of ten. ")
number = int(number)

if number % 10 == 0:
	print(f"\nThe number {number} is a multiple of ten!")
else:
	print(f"\nThe number {number} is not a multiple of ten!") 

# 7-4 Pizza Toppings. Write a loop tht prompts the user to enter a series of \
# pizza toppings until they enter a 'quit' value.
toppings_prompt = "\nPlease enter the type of topping(s) you would like:"
toppings_prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	toppings = input(toppings_prompt)

	if toppings == 'quit':
		break
	else:
		print(f"\n{toppings.title()} have been added to your pizza.")

# 7-5 Movie Tickets. Write a loop in which you ask users their age, and then \
# tell them the cost of their movie ticket.
age = input("\nHow old are you? ")
age = int(age)

if age < 0:
	ticket_price = "\n!!!Input Error!!!"
elif age < 4:
	ticket_price = "\nYour Ticket Is Free."
elif age < 13:
	ticket_price = "\nYour Ticket is $10."
else:
	ticket_price = "\nYour Ticket is $15."
print(ticket_price)

# 7-7 Infinite Loop.
# x = 1
# while x <= 5:
#	print(x)

# 7-8/9 Deli. Make a list and fill it with the name of variou sandwhiches. Then \
# make an empty list. Loop through the list to print a message.
sandwhich_orders = ['turkey', 'tuna', 'pastrami', 'turkey', 'chicken', 
	'pastrami', 'pastrami']
finished_sandwhich = []

# The deli has run out of pastrami.
while 'pastrami' in sandwhich_orders:
	sandwhich_orders.remove('pastrami')

# Moving each sandwhich order to finished sandwhich.
while sandwhich_orders:
	making_sandwhich = sandwhich_orders.pop()

	print(f"\nMaking a {making_sandwhich} sandwhich.")
	finished_sandwhich.append(making_sandwhich)

# Display all finished sandwhiches.
print(f"\nSandwhiches ready for pick up!")
for finished_sandwhiches in finished_sandwhich:
	print(finished_sandwhiches.title())

if sandwhich_orders == []:
	print("\nAll orders have been made.")

# 7-10 Dream Vacation. Poll users about their dream vacation.
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("If you could visit one place in the world, where "
				"would you go? ")

	# Store the response in the dictionary.
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():	
	print(f"{name} would like to visit {response}.")
