# Guests for a party
guests = ['Mommy', 'Lila', 'Ava']
guest1 = guests[0]
guest2 = guests[1]
guest3 = guests[2]
print(f"{guest1.title()}, you are invited to the party!")
print(f"\n{guest2.title()}, you are invited to the party!")
print(f"\n{guest3.title()}, you are invited to the party!")

# Ava is unable to make it to the party so we are inviting Ruby.
ava_cant_go = 'Ava'
guests.remove(ava_cant_go)
print(guests)
print(f"\n{ava_cant_go.title()} will not be making it to the party.")
guests.insert(2, 'Ruby')
guest1 = guests[0]
guest2 = guests[1]
guest3 = guests[2]
print(f"\n{guest1.title()}, you are invited to the party!")
print(f"\n{guest2.title()}, you are invited to the party!")
print(f"\n{guest3.title()}, you are invited to the party!")

# We now are able to get a bigger table so we will be inviting more people.
print(f"\nI have found a larger table, so more people will be joining us.")
guests.insert(0, 'Nana')
guests.insert(2, 'Meme')
guests.append('Katie')
print(guests)

guest1 = guests[0]
guest2 = guests[1]
guest3 = guests[2]
guest4 = guests[3]
guest5 = guests[4]
guest6 = guests[5]

print(f"\n{guest1.title()}, you are invited to the party!")
print(f"\n{guest2.title()}, you are invited to the party!")
print(f"\n{guest3.title()}, you are invited to the party!")
print(f"\n{guest4.title()}, you are invited to the party!")
print(f"\n{guest5.title()}, you are invited to the party!")
print(f"\n{guest6.title()}, you are invited to the party!")

# Plans for the table fell through so we no only have room for 2.
print(f"\nSorry everyone but I only have room for two now.")

katie_popped = guests.pop()
print(f"\n{katie_popped.title()}, you are uninvited to the party!")

ruby_popped = guests.pop()
print(f"\n{ruby_popped.title()}, you are uninvited to the party!")

lila_popped = guests.pop()
print(f"\n{lila_popped.title()}, you are uninvited to the party!")

meme_popped = guests.pop()
print(f"\n{meme_popped.title()}, you are uninvited to the party!")

print(guests)

guests_left = 'Nana and Mommy'
print(f"\n{guests_left.title()} the party is still on!")

# Finishing out the project. Party canceled all together.
del guests[0]
print(guests)
del guests[0]
print(guests)
print(len(guests))
