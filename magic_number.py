answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again.")

# Numerical Comparisons
age = 18
age < 21

age <= 21

age > 21

age >= 21
# Can be used as part of an if statement to help detect conditions of interest.

# Using an and statement.
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# Will return False.

age_1 = 22
age_0 >= 21 and age_1 >= 21
# Will return True

# To improve readability you can use parentheses of individual tests, though /
# not required.
(age_0 >= 21) and (age_1 >= 21)

# Using an or statement.
age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21)
# Will return True

age_0 = 18
(age_0 >= 21) or (age_1 >= 21)
# Will return False


