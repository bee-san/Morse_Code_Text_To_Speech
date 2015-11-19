import Morsecode
import os
import sys
import time
# imports the main modules used in this program

def main():
	message = input("Enter message to convert here: ")
	message = morseconvert(message)
	# takes user insput as a string and translate it to morse code
	SpeakMorse(message)
	close()
	# speaks the morse code and then closes

def MorseConvertAndTTS(message):
	# cretes a function so this can be imported
	message = Morsecode.to_morse(message)
	SpeakMorse(message)
	close()


def morseconvert(message):
	message = Morsecode.to_morse(message)
	# converts message to morse code
	message = message.split(" ")
	# splits message up into a list

	return message

def SpeakMorse(message):
	for i in message:
		# for every iteration in list
		Speak = ("say -r 90 \'{}\'".format(i))
		# Use's OSX's say command to speak the morse code out
		# says at a rate of 90 words per minute
		os.system(Speak)

		time.sleep(0.1)
		# sleeps for 0.1 seconds

		#message = ("say -r 90 \"{}\"".format(message))
	# Use's OSX's say command to speak the morse code out
	# says at a rate of 90 words per minute


def close():
	sys.exit()
	# function which closes the program

if __name__ == '__main__':
	main()
