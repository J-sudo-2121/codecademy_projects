import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific Functions
from pizza import make_pizza

make_pizza(12, 'veggie')
make_pizza(16, 'pepperoni', 'mushrooms')

# Giving a Function an Alias with as
from pizza import make_pizza as mp

mp(16, 'sausage')
mp(12, 'pepperoni', 'ham')

# Using as to Give a Module an Alias
import pizza as p 

p.make_pizza(12, 'cheese')
p.make_pizza(12, 'pineapple', 'bacon')

# Importing All Functions in a Module
from pizza import *

make_pizza(12, 'onion')
make_pizza(16, 'bacon', 'sausage', 'pepperoni')