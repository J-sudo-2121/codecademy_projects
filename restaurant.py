class Restaurant:
	"""A class to store restaurant attributes"""

	def __init__(self, restaurant_name, cuisine_type,):
		self.name = restaurant_name
		self.cuisine = cuisine_type
		#Setting a default value for an attribute.
		self.number_served = 0

	def describe_restaurant(self):
		"""A method that describes the restaurant in a statement."""
		print(f"{self.name.title()} is a restaurant that serves" \
			f" {self.cuisine.title()} style food.")

	def open_restaurant(self):
		"""Simulate the restaurant open for business."""
		print(f"{self.name.title()} is now open for business.")

	def read_number_served(self):
		"""Print a statement showing the car's mileage."""
		print(f"The restaurant has served {self.number_served} customers.")

	"""Add a method that prints the number of customers served."""
	def set_number_served(self, served):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if served >= self.number_served:
			self.number_served = served
		else:
			print("You can't take customers away!")

	def increment_number_served(self, customer):
		"""Adding customers to total so far."""
		self.number_served += customer