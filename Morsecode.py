# SHEBANG GOES HERE

"""
This program decrypts and can encrypt Morse Code
It can be imported as a module.
started on 19/08/2015
finished on 19/08/2015
If you have any suggestions or want to help
contact me at`
https://www.facebook.com/AiiYourBaseRBel0ngToUs
This program abides by the rules of presentation for
PEP-8
shown here on
https://www.python.org/dev/peps/pep-0008/
This program also abides by the Unix Philosophy
The MIT License (MIT)
Copyright (c) 2015 Brandon Skerritt
Github: https://github.com/brandonskerritt51
Twitter: @Ofmiceandhelp
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR I
"""

# enable DEVMODE to get accurcate error reports and other
# cool nifty things, only use if you are debugging
DEVMODE = True

# Defines the morse code dictionary using phonetics
# This is a dictionary which contains the english alphabet and their
# morse code equivilants
# it doesn't contain  much puncuation
# if the code errors, it may be because it can't find the dictionary item, try
# adding puncuation
CODE = {'A': 'Di dah', 'B': 'dah di di di', 'C': 'dah di dah di',
		'D': 'dah di di', 'E': 'di', 'F': 'di di dah di',
		'G': 'dah dah di', 'H': 'di di di di', 'I': 'di di',
		'J': 'di dah dah dah', 'K': 'dah di dah', 'L': 'di dah di di',
		'M': 'dah dah', 'N': 'dah di', 'O': 'dah dah dah',
		'P': 'di dah dah di', 'Q': 'dah dah di  dah', 'R': 'di dah di',
		'S': 'di di di', 'T': 'dah', 'U': 'di di dah',
		'V': 'di di di dah', 'W': 'di dah dah', 'X': 'dah di di dah',
		'Y': 'DAH DI DAH DAH', 'Z': 'dah dah di di',

		'0': '-----', '1': '.----', '2': '..---',
		'3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..',
		'9': '----.', '.': '.-.-.-', ',': '--..--',
		'Ä': '.-.-', 'Á': '.--.-', 'É': '..-..',
		'Ü': '..--', ' ' : 'SPACE'
		}

# creates the code dictionary, but in reverse, morse code is equal to english letters
CODE_REVERSED = {value: key for key, value in CODE.items()}


def main():
	# asks the user if they want to decrypt or encrypt
	print("Do you want to encrypt or decrypt Morse?")
	choice = input("E for encrypt, D for decrypt ").upper()
	# gets the user to enter the message they want to encrypt / decrypt
	message = str(input("Enter the string you want to play with: "))
	# checks message to make sure it's morse code
	check = Is_Morse(message)
	if check == False:
		message = ("ERROR, Code is not Morse Code!")
		# code is not morse code
		return message

	if choice.upper().startswith("E"):
		# user wants to encrypt message
		message_processed = to_morse(message)
		# gets morse code encryption and prints it
		print(message_processed)
	else:
		message_processed = from_morse(message)
		# gets more code decryption and prints it
		print(message_processed)


def to_morse(message):
	return ' '.join(CODE.get(i.upper()) for i in message)


# for every space in the message, get the morse code equivilant for the letter
# in the message and print it

def from_morse(message):
	try:
		return ''.join(CODE_REVERSED.get(i) for i in message.split())
	# try decrypting morse code

	except TypeError as e:
		print("\nERROR. This code passed the morse code inspection test\n"
			  "but didn't pass the conversion from Morse Code to English\n"
			  "Now closing the program to avoid further errors....")
		close()


def close():
	# this is the close function.
	import time
	import sys
	# imports time and sys for the 2 below calls
	# waits 5 seconds before going to the next step in the program
	time.sleep(5)
	# close the program
	sys.exit()

def Is_Morse(message):
	# this entire block of a function is all for making sure
	# that the message is actually morse code, if its not morse code
	# and it runs through the program, this program will crash
	# try / except clauses are in place for this too.
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# defines message varaible for use later
	# checks to make sure message is morse
	if LETTERS in message.upper():
		# if the message contains any english letters, it's not Morse Code.
		return False

	allowed = {".", "-", " "}
	# creates a weird type of list which stores all charecters used in morse code

	check = allowed.issuperset(message)
	# checks to see if the message only contains the charecters in the "allowed"
	# variable, if it contains a charecter which isn't in this set then return
	# false, if only the above charecters are in the message variable return True
	# into the check Variable
	if check == True:
		# if check is equal to true then import the detectEnglish module
		import detectEnglish

		try:
			# puts this into a try statement as this can often break the code
			# if a code passes the allowed.issuperset test it can still not be
			# morse code, examples of things that can get through are
			# "---------" "   .. - -- .. . .. " and " ".
			# takes the message and tries to convert it from morse code to english
			# if it fails then
			message = from_morse(message)
		except:
			# print an error message and return False.
			print("Could not convert message from Morse Code.")
			return False
		try:
			# if it was sucessful, then try to find out if the converted message
			# from morse code to english, is actually an english word or sentence
			# by putting it through the detectEnglish module.
			# If the word didn't convert properly, like if it was "--------"
			# this can also make this module error, so it's in a try statement.
			if detectEnglish.isEnglish(message) == True:
				# if the converted word is English, then return True
				return True
		except AttributeError as e:
			# if its not english, print an error and close the program.
			# i close the program as if it isn't closed it'll error so much
			print("Could not convert to English.")
			close()
	else:
		# if it doesnt contain the issuperset then return False
		return False


# required in all programs, if the name "main" is called, run main()
# i do this instead of main() at the bottom so this can
# still be imported as a module
if __name__ == '__main__':
	main()
