# Ceaser Cipher
# https://www.nostrach,com/crackingcodes/ (BSD Licensed)

import pyperclip

# THe string to be encrypted / decrypted
message = input("Enter You Secret : ")

# The encryption / decryption key
key = int(input("Choose your key between 0 to 25 : "))

# Whether the program encrypt or decrypts:
mode = input("encrypt / decrypt : ")

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted / decrypted form of the message: 
translated = ''

for symbol in message:

	if symbol in SYMBOLS:
		# Note: Only symbols in the SYMBOLS string can be encrypted / decrypted.
		symbolIndex = SYMBOLS.find(symbol)
	
		#Perform encryption / decryption
		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key

		# Handle wraparound, if needed:
		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex - len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex = translatedIndex + len(SYMBOLS)

		translated = translated + SYMBOLS[translatedIndex]

	else:
		# Append the symbol without encrypting / decrypting
		translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)	
