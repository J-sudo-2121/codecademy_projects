# Use keyword not
banned_users = ['andrew','carolina', 'david']
user = 'ping'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

else:
	print(f"{user.title()}, you can not post. You are BANNED!")