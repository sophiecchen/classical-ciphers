# Vigenère Cipher
# Sophie Chen

'''
This program implements the Vigenère cipher, a cipher that encodes each plaintext letter with a different Caesar cipher. This program shifts only letters in the English alphabet.

This program is run by `python3 vigenere.py [-e |-d] [key] [message]`. To handle spaces correctly, you may have to put your message between quotes. [key] should composed of only letters in the English alphabet.

Example commands: python3 vigenere.py -d abc "Hfnlp Yosnd!"
				  python3 vigenere.py -e ABC "Hello World!"
'''

# Setup
import sys
from caesar import shifter

# Helper Functions
def key_translate(key, length, is_encrypt):
	'''
	Translates the key into an array of shifts.

	Parameter:
	(str) key - the message to be encrypted
	(int) length - length of the shift
	(bool) is_encrpyt - True if we are encrypting, and False otherwise
	
	Returns an array of shifts.
	'''
	shifts = []
		
	for i in range(length):
		c = ord(key[i % len(key)])

		if (c >= ord('a') and c <= ord('z')):
			shifts.append(c - ord('a'))
		elif (c >= ord('A') and c <= ord('Z')):
			shifts.append(c - ord('A'))
		else:
			print("Error: key should only include characters in the English alphabet")
			exit(1)

	if not is_encrypt:
		for i in range(length):
			shifts[i] = shifts[i] * -1

	return shifts

# Crypto Functions
def chain_shift(message, shifts):
	'''
	Translates the key into an array of shifts.

	Parameter:
	(str) message - the message to be encrypted
	(int array) shifts - the number to shift each character by

	Returns the resulting text. (str)
	'''
	result = ""

	i = 0
	for c in message:
		last_char = shifter(c, shifts[i])
		result += last_char

		if (ord(last_char) >= ord('a') and ord(last_char) <= ord('z')) or (ord(last_char) >= ord('A') and ord(last_char) <= ord('Z')):
			i += 1

	return result
		

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 4 or len(sys.argv) > 5):
		print("Usage: python3 vigenere.py [-e|-d] [key] [message]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 vigenere.py [-e|-d] [key] [message]")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(chain_shift(sys.argv[3], key_translate(sys.argv[2], len(sys.argv[3]), True)))
	else:
		print(chain_shift(sys.argv[3], key_translate(sys.argv[2], len(sys.argv[3]), False)))

if __name__ == "__main__": 
	main()