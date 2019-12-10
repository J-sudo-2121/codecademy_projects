# Learning for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title())
# Looping is important because it's one of the most common ways a computer automtes repetitive tasks.

# You can choose any name you want for temporary varible that will be associated with each value in the list. It's helpful to choose
## a meaningful name that represents a single item from the list, such as cat for list of cats.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you, everyone. That was a great show!")
# Note that since the 3rd print was not inside the indent it is not part of the loop and prints only once. If it was unintential, this would be
## a logical error. The syntax is valid, but the code does not produce the desired result because a problem occurs in its logic.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}\n")

	print("Thank you, everyone. That was a great show!")
# Note that the third print was indented. This caused it to be a part of the loop, thus printing it 3 times. This is another example of a logical error.




