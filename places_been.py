places_been = ['Thailand', 'UAE', 'USA', 'Japan', 'Cambodia', 'Spain','Mexico']

print("\nHere are some places I have been:")
print(places_been)

print("\nHere is the sorted list of places I have been:")
print(sorted(places_been))

print('\nHere is the orignal list again:')
print(places_been)

print('\nI have been to more than ' + str(len(places_been)) + ' different places.')

favorite_place = places_been[0]

print("\nMy favorite place so far has been " + str(favorite_place) + ".")

# Adding New Places to List.
places_been[-1] = "Greece"
print(places_been)

places_been.append("Bahrain")
print(places_been)
places_been.append("Qatar")
print(places_been)

places_been.insert(0, 'Ireland')
print(places_been)

# Taking some off the list.
del places_been[0]
print(places_been)
popped_place = places_been.pop()
print(places_been)
print(popped_place)

print(f'\nOne of my leaset favorite places I have been is {popped_place.title()}.')

# Sorting List
places_been.sort(reverse=True)
print(places_been)
places_been.reverse()
print(places_been)


# Indexing Error. Remember to start counting at 0 when working with lists.






