# Login messages.
usernames = ['admin', 'mike', 'jon', 'mellisa', 'jane']
users = ['Mike']

for user in users:
	if user  == 'admin':
		print('Hello Admin, would you like to see a status report?')
	elif user.lower() in usernames:
		print(f"Welcome back to work {user.title()}. Have a good day!")
	else:
		print("You are not an authorized user. Locking Building Down Now!")
if (usernames == []) and (users == []):
	print("We need some users!")

# Checking user names against current list before they can create.
current_users = ['jon', 'mike', 'mellisa', 'jane', 'neil']
new_users = ['wally', 'Mike', 'frank', 'JANE', 'amber']

print("\nInput a username to see if it is available.")
for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"{new_user.title()} is taken plese create a new name.")
	elif new_user.lower() not in current_users:
		print(f"{new_user.title()} is available.")
		current_users.append(new_user.lower())

if user == 'admin':
	print("\nThe current list of users are:")
	for current_user in current_users:
		print(current_user.title())

# Ordinal Numbers with line spacing between each output.
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numbers in ordinal_numbers:
	if numbers == 1:
		print('\n1st')
	elif numbers == 2:
		print('\n2nd')
	elif numbers == 3:
		print('\n3rd')
	else:
		print(f'\n{numbers}th')
