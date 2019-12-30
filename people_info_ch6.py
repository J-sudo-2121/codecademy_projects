# Store info about a person in a dictionary.
personal_info = {
	'Bob': {
		'first_name': 'bob',
		'last_name': 'smith',
		'age': 56,
		'city_of_residence': 'new york',
		},
	'Lisa': {'first_name': 'lisa',
		'last_name': 'Yandi',
		'age': 43,
		'city_of_residence': 'singapore',
		},
	'Luke':{
		'first_name': 'luke',
		'last_name': 'butter',
		'age': 21,
		'city_of_residence': 'moscow',
		},
	}

for name, info in personal_info.items():
	print(f"\nName: {name.title()}")
	full_name = f"{info['first_name']} {info['last_name']}"
	age = info['age']
	residence = info['city_of_residence']

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tResidence: {residence.title()}")

# Make a dictionary called favorite_places.
favorite_places = {'andrew': 'san francisco', 'leia': 'antarctica', 
	'reggie': 'djbouti', 'peter': 'missouri',
	}
for name, place in favorite_places.items():
	print(f"\n{name.title()}'s favorite place in the whole world "
	f"is {place.title()}.")

# Store people's favorite numbers.
favorite_numbers = {
	'bob': [44, 33, 444],
	'lisa': [23,],
	'meg': [376, 13],
	'mike': [15, 22],
	'luke': [9, 45, 999999999999],
	}
for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	print(f"\t{numbers}")

# Cities information.
cities = {
	'new york': {
		'country': 'united states',
		'population': 1_000_000,
		'nickname': 'the big apple',
		},
	'honolulu': {
		'country': 'united states',
		'population': 1_000_000,
		'nickname': 'the big pineapple',
		},
	'venice': {
		'country': 'italy',
		'population': 1_000_000,
		'nickname': 'city of bridges',
		},
	'rio de janerio': {
		'country': 'brazil',
		'population': 1_000_000,
		'nickname': 'marvellous city',
		},
	}
for city, facts in cities.items():
	print(f"\n{city.title()}:")
	print(f"\tLocation: {facts['country'].title()}")
	print(f"\tPopulation: {facts['population']}")
	print(f"\tNickname: {facts['nickname'].title()}")
