from user_class_ch9 import User

class Privileges:
	"""A class to define Admin user privilges."""
	def __init__(self):
		self.privileges = ('Can add post' + ", " + 'Can delete post' + ", "  
		 				+ 'Can ban user')

	def show_privileges(self):
		print(f"\nYou have the following privileges: {self.privileges}." )

class Admin(User):
	"""A child class to represent an Admin User."""
	def __init__(self, first_name, last_name, user_email, user_department,
		user_extension):
		"""Initialize attributes of the parent class."""
		super().__init__(first_name, last_name, user_email, user_department, 
				user_extension)
		self.privileges = Privileges()
