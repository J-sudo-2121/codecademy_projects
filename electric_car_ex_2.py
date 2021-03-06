# Importing a Module into a Module
"""A set of classes tht can be used to represent electric cars."""

from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

# 9-9 Battery Upgrade:	
	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100
			print("Your battery has been upgraded to 100-kWh.")
		else:
			print("Your battery doesn't need an upgrade.")

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statemnt about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
			print(f"This car can go about {range} miles on a full change.")
		elif self.battery_size == 100:
			range = 315
			print(f"This car can go about {range} miles on a full change.")
		else:
			print("This cars battery range is unknown.")
					
class ElectricCar(Car):
	"""Represents spects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()