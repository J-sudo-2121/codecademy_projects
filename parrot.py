# How the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Letting the user choose when to quit using a while loop.
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)

# Added an if condition to clean up the display .
	if message != 'quit':
		print(message)

# Using a flag.
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False

	else:
		print(message)