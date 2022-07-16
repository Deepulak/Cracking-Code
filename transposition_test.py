# Tranposition Cipher Test
# https://www.nostrach.com/crackingcodes/ 	(BSD Licensed)

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
	random.seed(42)		# Set the random "seed" to a static value.

	for i in range(20):  # Run 20 tests.
		# Generate random message to test.
		# The message will have a random length.
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 20)

		# Convert the message strin to a list to shuffle it:
		message = list(message)

		random.shuffle(message)
		message = ''.join(message)		# Converts the list back to a string

		print("Test #%s: '%s...'" % (i + 1, message[:50]))

		# Check all possible keys for each message:
		for key in range(1, int(len(message) / 2)):
			encrypted = transpositionEncrypt.encryptMessage(key, message)
			decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

			# If the decryption doesn't march the original message, display
			# an error message and quit:
			if message != decrypted:
				print("Mismatch with key %s and message %s." % (key, message))
				print("decrypted as : " + decrypted)
				sys.exit()

	print("Transposition cipher test is passed.")

# If transpositionTest.py is run (instead of imported as module)
# call the main() function:
if __name__ == "__main__":
	main()