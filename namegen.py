#!/usr/bin/env python



# File Docstring
"""Name Generator

This is a script that will roughly and randomly generate strings
that appear to look like names."""



# Import packages.
import random
import string
import time



def newname():
	"""Generate the name."""

	# Random Seed
	random.seed()

	# How many individual words, up to 3.
	countW = random.randint(1, 3)

	# How many vowels.
	countV = 0

	# How many consonants.
	countC = 0

	# The name to build, and its potential length.
	name = ""
	namelen = random.randrange(5,8)

	# The alphabet, separated by vowel and consonant.
	letter = ['aeiouy', 'bcdfghjklmnpqrstvwxz']

	# Randomly pick between the vowels and consonants.
	# And if there is more than enough of each, choose the other.
	for i in xrange(countW):
		for j in xrange(namelen):
			VC = random.choice(letter)

			if VC == letter[0]:
				countV += 1
			elif VC == letter[1]:
				countC += 1

			if countC > 1:
				VC = letter[0]
				countC = 0
			elif countV > 1:
				VC = letter[1]
				countV = 0

			# Add the new letter to name.
			name += random.choice(VC)

		# After the name is done, separate for the next name.
		name += ' '

	# Capitalize the name.
	name = str.title(name)

	return name



# Application
if __name__ == '__main__':

	# Greeting
	greet = """TRICORNE NAME GENERATOR - 2015 Tricorne Games

Making a character for your story or game and you just can't think of a name?
Give this program a try, and maybe it will help you come up with something
unique, fun, or outright silly.

Simply press [ENTER] to keep generating a name. It will display anywhere from
one, two, or three names at once, to appear like a full name. Read through, and
see what rings nicely with you. To quit, type in 'Q' (just capital Q) and press
[ENTER], and you're done.

Enjoy!"""
	print('')
	print(greet)
	print('')

	# App Loop
	while True:
		CMD = raw_input("Press [ENTER] to generate a name. Enter 'Q' to quit. >>> ")
		if CMD == 'Q':
			print('')
			print("Thank you, and goodbye!")
			print('')
			time.sleep(2)
			break
		else:
			print
			print newname()
			print