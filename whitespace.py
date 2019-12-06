#Tab with \t
print("\tPython")

#Add new line with \n
print("Languages:\nPython\nC\nJavaScript")

#Combine Tabs and Newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#To ensure no whitespce exists at the right end of a string use the rstrip()method
favorite_language = 'python '
favorite_language.rstrip()
favorite_language = favorite_language.rstrip() #Have to do this line to make permanent
print(favorite_language)

#To ensure no whitespce exists at the left end of a string use the lstrip()method
favorite_language = ' python'
favorite_language.lstrip()
favorite_language = favorite_language.lstrip()
print(favorite_language)

#Can remove from both sides by using .strip()
favorite_language = ' python '
favorite_language.strip()
favorite_language = favorite_language.strip()
print(favorite_language)