# Organizing a List. Sorting a List Permanently with the sort() Method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# The cars are now in alphbetical order and we can never revert back to the original order.

# You can also sort the list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
# Again the list is permanently changed.

# Sorting a List Temporarily with the sorted() Function. The sorted() function lets you display your list in a particular
## order but doesn't affect the actual order of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.
## Use print(sorted(name, reverse=True)) to print in reverse using the sorted() Function.

# Printing a List in Reverse Order. You can use the reverse() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# Note that reverse() doesnt sort backward alphabetically. It just reverses the order of the list. The reverse() method changes
## the order of a list permanently, but you can revert to the original order by applying reverse() a second time to the same list.

# Finding the length of a List can be found quickly using the len() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

####################################

places_to_visit = ['Antarctica', 'Brazil', 'Arctic Circle', 'Peru', 'Moon']
print(places_to_visit)

print(sorted(places_to_visit))

print(sorted(places_to_visit, reverse=True))

print(places_to_visit)

places_to_visit.reverse()
places_to_visit.reverse()

places_to_visit.sort()
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(places_to_visit)
