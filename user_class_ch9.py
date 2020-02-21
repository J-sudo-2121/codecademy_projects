class User:
	"""Store attributes that are typically stored in a user profile"""

	def __init__(self, first_name, last_name, user_email, user_department, 
				user_extension):
		self.name = first_name + " " + last_name
		self.email = user_email
		self.department = user_department
		self.extension = user_extension
		self.login_attempts = 0

	def describe_user(self):
		"""Print out a summary of the user's profile"""
		print(f"\n{self.name.title()}'s profile is as follows:")
		print(f"- {self.email}")
		print(f"- {self.department.title()} Department")
		print(f"- Ex. {self.extension}")

	def greet_user(self):
		"""Greeting for the user"""
		print(f"Welcome back {self.name.title()}.")

	def read_login_attempts(self):
		"""Print a statement to user with the number of failed logins."""
		print(f"You have {self.login_attempts} failed login attempts.")

	def login_results(self, results):
		"""Results of login attempts"""
		if results == False:
			return self.increment_login_attempts(1)
		elif results == True:
			return self.reset_login_attempts()
		else:
			print("Error Try Again.")

	def increment_login_attempts(self, login):
		"""Add the given amount to failed login attempts."""
		self.login_attempts += login

	def reset_login_attempts(self):
		self.login_attempts = 0