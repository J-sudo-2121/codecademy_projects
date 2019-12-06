#Integers
print(2 + 3)
print(2 - 1)
print(65 * 3)
print(54 / 3)
print(3 ** 10)

#Order Of Operations
Order = 2 + 3*4 
print(Order)
Order2 = (2 + 3) * 4
print(Order2)

#Floats: Python calls ny number with a decimal point a float.
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
#Sometimes you get an arbitrary number of decimal places in your answer.
print(0.2 + 0.1)
print(3 * 0.1)

#Integers and Floats
#When you divide any two numbers, even if whole number, you always get a float
print(4/2)
#If you mix an integer and a float you will get  float as well.
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

#Underscores in Numbers
#When you're writing long numbers, you can group digits using underscores to make large numbers more readable.
universe_age = 14_000_000_000
print(universe_age)
#To Python, 1000 is the same as 1_000 and 10_00. Works for floats and integers in Python 3.6 and after.

#Mulltiple Assignment
#You can assign values to more than one variable using just a single line. You need to separate the variable names with commas and the same with the values.
x, y, z = 0, 0, 0
print(x, y, z)

#Constants
#A constant is like a variable whose value stays the same throughout the life of a program. Python programmers use all captial letters to indicate a vriable should be treated as a constant nd never be changed.
MAX_CONNECTIONS = 5000

#-----------------------
#Try Myself in Book
print(5 + 3)
print(12 - 4)
print(2 * 4)
print(24 / 3)

favorite_number = 17
quote1 = "My favorite number is " + str(favorite_number) + "."
print(quote1)
#Remember when combining an integer to a string use the str() on the integer so not to get an error.






