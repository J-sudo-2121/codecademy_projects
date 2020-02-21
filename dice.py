# Exercise 9-13 Dice
from random import randint

"""A class to represent rolling a die"""
class Die:

	def __init__(self):
		self.sides = 6
		self.ten_sided = 10
		self.twenty_sided = 20

	def roll_die(self):
		print(f"You rolled {randint(1, 6)} with the {self.sides} sided die.")

	def ten_sided_die(self):
		print(f"You rolled {randint(1, 10)} with the {self.ten_sided} "
			f"sided die.")

	def twenty_sided_die(self):
		print(f"You rolled {randint(1, 20)} with the {self.twenty_sided} "
			f"sided die.")

roll = Die()

roll.roll_die()
roll.ten_sided_die()
roll.twenty_sided_die()