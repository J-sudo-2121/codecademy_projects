# A list in a dictionary.
#Store info about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

#Summrize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the "
	"following toppings:")
# When you need to break up a long line in a print() call, choose a point \
# at which to break the line being printed, and end the line with a quotation \
# mark. Indent the next line, add an opening quotation mark, and continue \
# string.

for topping in pizza['toppings']:
	print("\t" + topping.title())

