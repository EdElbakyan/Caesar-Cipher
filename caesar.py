alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))


	def encrypt(text,shift):
		cipher_text = ""
		for letter in text:
			index = alphabet.index(letter) # getting the indexes of the letters
			new_index = index + shift	   # assigning the new indexes
			if new_index >25:			   # a case when the index is bigger than the alphabets highest index 
				new_index = new_index%25 - 1
			new_letter = alphabet[new_index]
			cipher_text += new_letter	
		print(f"The encoded text is: {cipher_text}")


	def decrypt(text,shift):
		plain_text = ""
		for letter in text:
			index = alphabet.index(letter)
			new_index = index - shift
			if new_index < 0:
				new_index = 26 + new_index
			new_letter = alphabet[new_index]
			plain_text+= new_letter
		print(f"The decoded text is: {plain_text}")


	if direction == "encode":
		encrypt(text,shift)
	elif direction == "decode":
		decrypt(text,shift)
	else:
		print("Please input the correct direction")