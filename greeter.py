# Learning to write clear prompts.
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Builing prompt over several lines to write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}! Thank you for that information.")

# Using int() to accept numerical input.
age = input("How old are you? ")

age = int(age)
age >= 18