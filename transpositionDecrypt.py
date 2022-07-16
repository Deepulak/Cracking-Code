# Tranposition Cipher Decryption
# https://www.nostrach.com/crackingcodes/  (BSD Licensed)
# The plain text is
# Common sense is not so common.
# The cipher text
# Cenoonommstmme oo snnio. s s c



import math, pyperclip

def main():
	myMessage = input("Enter your secret message: ")
	myKey = 8

	plainText = decryptMessage(myKey, myMessage)

	# Print with a | (called "pipe" character) after it in case
	# there are spaces at the end of the decrypted message:
	print(plainText + '|')

	pyperclip.copy(plainText)

def decryptMessage(key, message):
	# The transpos decrypt function will simulate the "columns" and
	# "rows" of the grid that the plaintext is written on by using a list
	# of strings. First, we need to calculate a few values.

	# The number of "columns" in our transposition grid:
	numOfColumns = int(math.ceil(len(message) / float(key)))
	# The number of "rows" in our grid:
	numOfRows = key
	# The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	# Each string in plaintext represents a column in the grid:
	plaintext = [''] * numOfColumns

	# The column and row variabls point to where in the grid next 
	# character in the encrypted message will go:
	column = 0
	row = 0

	for symbol in message:
		plaintext[column] += symbol
		column += 1 	# Point to the next column

		# If there are no more columns OR we're at a shaded boc, go back
		# to the first column and the next row:
		if(column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1

	return ''.join(plaintext)

# If the transposition_decrypt.py is run (instead of imported as module),
# call the main() function:
if __name__ == "__main__":
	main()


