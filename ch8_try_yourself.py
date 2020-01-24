# 8-1 Message
def display_message():
	"""What I am learning this chapter."""
	print("I am learning about functions in Chapter 8!")

# Remember that function do not need print() to print.
display_message()

# 8-2 Favorite Book
def favorite_book(title):
	"""Favorite book to read"""
	print(f"My current favorite book is {title}.")

favorite_book('Python Crash Course')

# 8-3 T-shirt
def make_shirt(shirt_size, shirt_text):
	"""Functions should print a sentence of the size and message on shirt"""
	print(f"\nYou ordered a {shirt_size.lower()} sized shirt with text of " 
		f"'{shirt_text}'.")

# Call the function using positional arguments.
make_shirt('Large', 'i > u')

# Call the function using keyword arguments.
make_shirt(shirt_text='i <3 u', shirt_size='SMALL')

# 8-4 Large Shirts
def make_shirt(shirt_size='large', shirt_text='I love Python'):
	"""Functions should print a sentence of the size and message on shirt"""
	print(f"\nYou ordered a {shirt_size.lower()} sized shirt with text of " 
		f"'{shirt_text}'.")

# Make a large shirt with default message.
make_shirt()

# Make a medium shirt with default message.
make_shirt(shirt_size='medium')

# Make a shirt of any size and new messge.
make_shirt(shirt_size='small', shirt_text='Vote For Pedro!')

# 8-5 Cities
def describe_city(city_name, city_country='china'):
	"""The function should print a simple sentence for name and country."""
	print(f"\n{city_name.title()} is in {city_country.title()}.")

# Call your function for 3 different cities. 1 should not be in the country.
describe_city('shanghai')
describe_city('singapore')
describe_city('shenzhen')

# 8-6 City Names
def city_country(city, country):
	"""Function should return a string formatted City, Country."""
	city_and_country = f"{city}, {country}"
	return city_and_country.title()

first_c_c = city_country('santiago', 'chile')
second_c_c = city_country('bangkok', 'thailand')
third_c_c = city_country('mexico city', 'mexico')
print(f"\n{first_c_c} \n{second_c_c} \n{third_c_c}")

# 8-7 Album
def make_album(album_artist, album_name, number_of_songs=None):
	"""Function should return dictionary of album names and artists"""
	album_info = {'artist': album_artist, 'name': album_name}
	if number_of_songs:
		album_info['songs'] = number_of_songs
	return album_info

first_album = make_album('korn', 'korn', 12)
second_album = make_album('i prevail', 'lifelines')
thrid_album = make_album('logic', 'bobby trantino', 11)
print(first_album)
print(second_album)
print(thrid_album)

# 8-8 User Albums Add a while loop to 8-7
def make_album(album_artist, album_name):
	"""Function should return dictionary of album names and artists"""
	album_info = f"{album_artist} {album_name}"
	return album_info.title()

while True:
	print("\nPlease tell me your favorite musical artist and their album:")
	print("(enter 'q' at any time to quit)")

	artist = input("Artist: ")
	if artist == 'q':
		break

	album = input("Album: ")
	if album == 'q':
		break

	album_answers = make_album(artist, album)
	print(f"\nOh! {album_answers}! That's a good album!")

print("\n")

# 8-9 Messages / 8-10 Sending Messages / 8-11 Archived Messages
def show_messages(unprocessed_messages, processed_messages):
	"""
	Simulate sending messages, until none are left.
	Move each message to processed_messages after sending.
	"""
	while unprocessed_messages:
		pending_message = unprocessed_messages.pop()	
		print(f"The following message is sending: {pending_message.title()}")
		processed_messages.append(pending_message)

print("\n")

def send_messages(processed_messages):
	"""Show all the messages that were sent."""
	print("\nThe following messages have been sent:")
	for processed_message in processed_messages:
		print(processed_message.title())


unprocessed_messages = ['hello', 'good bye', 'lol']
processed_messages = []

show_messages(unprocessed_messages[:], processed_messages)
send_messages(unprocessed_messages)

# Prove your slice worked
print(unprocessed_messages)
print(processed_messages)

print('\n')

# 8-12 Sandwhiches
def sandwhich_order(*items):
	"""Summarize the sandwhich about to be made."""
	print("\nMaking a sandwhich with the following items:")
	for item in items:
		print(f"- {item.title()}")

sandwhich_order('turkey', 'american cheese', 'mayo', 'salt', 'pepper')
sandwhich_order('american cheese', 'mayo')
sandwhich_order('ham', 'turkey', 'bacon', 'lettuce', 'tomato')

print('\n')
# 8-13 User Profile 
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('bob', 'butcher', 
							job='baker',
							location='columbia',
							phone_number='123-345-5678',
							)

print(user_profile)

print('\n')

# 8-14 Cars
def make_car(manufacturer, model, **kwargs):
	"""Build a function that stores information about a car in a dictionary."""
	kwargs['make'] = manufacturer
	kwargs['model_type'] = model
	return kwargs

car_info = make_car('honda', 'civic',
				color='black',
				hatch_back=False
				)

print(car_info)

# For 8-15 refer to printing_models.py / printing_functions.py

# For 8-16 refer to build_profile.py / profile_dicitonary.py
