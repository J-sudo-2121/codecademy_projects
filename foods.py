# You can copy a list by making a slice that has the entire list [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

# To show that we have two different lists, add new item to each. Also practicing for loops.

my_foods.append('cannoli')
friends_foods.append('ice cream')
print("\nMy favorite foods are:")
for my_food in my_foods:
	print(my_food.title())

print("\nMy friend's favorite foods are:")
for friends_food in friends_foods:
	print(friends_food.title())
# Had a slice not been used it would not have produced two separate lists.