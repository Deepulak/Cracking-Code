# Reverse Cipher
# https://www.nostarch.com/crackingcodes/

message = input('Enter Message for Encryption : ')
translated = ''

i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	print('i is', i, ', message[i] is', message[i], ', translated is', translated)
	i = i - 1

print(translated)