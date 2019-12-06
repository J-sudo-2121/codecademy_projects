# Modifying Elements in a List

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[1] = 'harley'
print(motorcycles)

# Adding Elements to a List: Python provides several ways to add new data to existing lists.
## Appending Elements to the End of a List
motorcycles = ['honda', ' yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# The append() method adds 'ducati' to the end of the list without affecting any of the other elements in the list:
## The append() method makes it easy to build lists dynamically.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# Building lists this way is very common, because you often wont know the data your users want to store in a program until after
## program is running.

#Inserting Element into a List: You can add a new element at any position in your list by using the insert() method.
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list by using the del Statement. If you know the position of the item you wnt to remove you can use the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[2]
print(motorcycles)
#Once an item is removed using del statement it can no longer be accessed.

#Removing an item using the pop() method. The pop() method removes the last item in a list, but lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

# You can use pop() to remove n item from any position in a list by including the index of the item you want to remove in parentheses.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# Remember that each time you use pop(), the item you ork with is no longer stored in the list. If unsure whether to use the del statement
## or the pop() method, a simple way to decide: when you want to delete an item from a list and not use that item in any way, use del statement;
### if you want to use an item as you remove it, use the pop() method.

# Removing an Item by Value. Sometimes you wont know the position of the value you want to remove from  list. If you only know the value of the item
## you want to remove, you can use the remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# The code tells Python to figure out where 'ducati' is in the list and remove tht element.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
# Note that the remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list,
## you'll need to use  loop to mke sure all occurrences of the value are removed. 