import Morsecode
import os
import sys
__author__ = 'brandonskerritt'



def main():
	message = input("Enter message to convert here: ")
	message = morseconvert(message)
	SpeakMorse(message)
	close()

def morseconvert(message):
	message = Morsecode.to_morse(message)
	return message

def SpeakMorse(message):
	message = ("say -r 90 \"{}\"".format(message))
	os.system(message)

def close():
	sys.exit()

if __name__ == '__main__':
	main()