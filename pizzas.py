#Practicing for Loops
pizzas = ['cheese', 'mushroom', 'meat']
for pizza in pizzas:
	print(f"I like {pizza} pizza.\n")
print("I could eat pizza every day!")

animals = ['dog', 'cat', 'fish']
for animal in animals:
	print(f"Have you ever thought of owning a {animal}?\n")
print("Any of these animals would make a great pet!")

# Practicing my knowledge
friends_pizzas = pizzas[:]
pizzas.append('pepperoni')
friends_pizzas.append('veggie')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friends favorite pizzas are:")
for friends_pizza in friends_pizzas:
	print(friends_pizza.title())

