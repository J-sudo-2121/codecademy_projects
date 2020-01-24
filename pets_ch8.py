# Positional Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls
describe_pet('dog', 'willie')

# Mixing up the order on positional arguments
describe_pet('harry', 'hamster')

# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Simplest method to use new function.
describe_pet('willie')

# Override the default value.
describe_pet(pet_name='harry', animal_type='hamster')