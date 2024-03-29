# Caesar Cipher
# Sophie Chen

'''
This program implements the Caesar cipher, a well-known substitution cipher that shifts each letter in the plaintext down the alphabet a fixed number of times. This program shifts only letters in the English alphabet.

This program is run by `python3 caesar.py [-e |-d] [shift] [message]`. To handle spaces correctly, you may have to put your message between quotes. [shift] should be an integer.

Example commands: python3 caesar.py -d 7 'Olssv Dvysk!'
				  python3 caesar.py -e 7 'Hello World!'
'''

# Setup
import sys

# Crypto Functions 
def shifter(message, shift):
	'''
	Shifts each letter of the message forward in the alphabet a fixed number.

	Parameter:
	(str) message - the message to be encrypted
	(int) shift - the number to shift by (negative integers shift backwards)
	
	Returns the resulting text. (str)
	'''
	try:
		if shift > 25 or shift < -25:
			raise ValueError
	
	except ValueError:
		print("Error: shift value should be between -25 and 25, inclusive")
		exit(1)

	result = ""

	for c in message:
		c = ord(c)

		if (c >= ord('a') and c <= ord('z')):
			result += chr((c - ord('a') + shift) % 26 + ord('a'))
		elif (c >= ord('A') and c <= ord('Z')):
			result += chr((c - ord('A') + shift) % 26 + ord('A'))
		else:
			result += chr(c)

	return result

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 4 or len(sys.argv) > 5):
		print("Usage: python3 caesar.py [-e |-d] [shift] [message]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 caesar.py [-e |-d] [shift] [message]")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(shifter(sys.argv[3], int(sys.argv[2])))
	else:
		print(shifter(sys.argv[3], int(sys.argv[2]) * -1))

if __name__ == "__main__": 
	main()