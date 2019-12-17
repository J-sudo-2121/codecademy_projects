# Alien Colors #1 if statement that works.
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print("5 points earned!")

# Alien Colors #1 if statement that fails.
alien_color = ['green', 'yellow', 'red']
if 'blue' in alien_color:
	print("100 points earned!")

# Alien Colors #2 Choose a color for an alien as in Alien #1 and write an if- /
# else chain.
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print("\n5 points earned!")
if alien_color != 'green':
	print("10 points earned!")
else:
	print("\nGame Over! You didn't the green Alien.")

# Alien Colors #2 else version.
alien_color = ['green', 'yellow', 'red']
if 'brown' in alien_color:
	print("\n5 points earned!")
else:
	print("\nGame Over! You didn't get the brown Alien.")

# Alien Colors #3 turn your if-else chain from #2 into an if-elif-else chain.
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print("\n5 points earned!")
elif 'yellow' in alien_color:
	print("\n10 points earned!")
elif 'red' in alien_color:
	print("\n15 points earned!")

# Alien Colors #3 make elif trigger.
alien_color = ['green', 'yellow', 'red']
if 'blue' in alien_color:
	print("\n5 points earned!")
elif 'yellow' in alien_color:
	print("\n10 points earned!")
elif 'red' in alien_color:
	print("\n15 points earned!")

# Alien Color #3 making second elif trigger.
alien_color = ['green', 'yellow', 'red']
if 'blue' in alien_color:
	print("\n5 points earned!")
elif 'brown' in alien_color:
	print("\n10 points earned!")
elif 'red' in alien_color:
	print("\n15 points earned!")

# Stages of Life. Writing if-elif-else to determines a person's stage in life.

age = 44

if age < 0:
	stage_in_life = "\n!!!Input Error!!!"
elif age < 2:
	stage_in_life = "\nThis person is a baby."
elif age < 4:
	stage_in_life = "\nThis person is a toddler."
elif age < 13:
	stage_in_life = "\nThis person is a kid."
elif age < 20:
	stage_in_life = "\nThis person is a teenager."
elif age < 65:
	stage_in_life = "\nThis person is an adult."
else:
	stage_in_life = "\nThis person is an elder."
print(stage_in_life)

# Favorite Fruit. Make a list of fav. fruit w/ a series of independent if /
# statements that check for certain fruits on list.

favorite_fruits = ['durian', 'mangosteen', 'orange', 'papaya', 'pineapple']

if 'bananas' in favorite_fruits:
	print("\nWow you love bananas!")
if 'durian' in favorite_fruits:
	print("\nHow can you eat such smelly fruit?")
if 'orange' in favorite_fruits:
	print("\nI like apples more than oranges.")
if 'apple' in favorite_fruits:
	print("\nI like sour apples.")
if 'mangosteen' in favorite_fruits:
	print("\nMangosteens have a tough skin.")

