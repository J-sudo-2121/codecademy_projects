#A List is a collection of items in a prticular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of 
# all the people in your family. In Python, square brackets ([]) indicte a list, the individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# print() will print everything in the list including the brackets unless otherwise told not to.

#Accessing elements in a list.
#Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
print(bicycles[0])

#You can also use the string methods from Ch2 on any element in this list.
print(bicycles[0].title())

#Remember index numbers start at 0, not 1.
print(bicycles[1])
print(bicycles[3])

#Python has special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list.
print(bicycles[-1])

#Using Individual Values from a List.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#Remember f-string is for format string.

#--------------------
#Try It Yourself
names = ["Eve", "Aaron", "Will", "Billy"]
print(names[0])
print(names[-1])
print(names[-2])
print(names[1])
print(names[0:4])

greeting = "Hello " + names[0] + ", it's so nice to see you!"
print(greeting)
greeting = "Hello " + names[1] + ", it's so nice to see you!" 
print(greeting)
greeting = "Hello " + names[-2] + ", it's so nice to see you!"
print(greeting)
greeting = "Hello " + names[-1] + ", it's so nice to see you!" 
print(greeting)

favorite_motor_vehicle = ["Tesla", "Motorbike", "Boat"]
statement = "I would like to own a "
print(statement + favorite_motor_vehicle[0])
print(statement + favorite_motor_vehicle[1])
print(statement + favorite_motor_vehicle[-1])
#----------------------------------------------------------------







