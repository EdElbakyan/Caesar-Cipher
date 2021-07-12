alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
	direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))



	def ceaser(text,shift,direction):
		end_text = ""
		if direction == "decode":
			shift *= -1
		for letter in text:
			if letter in alphabet:
				index = alphabet.index(letter)	
				new_index = index +shift
				if new_index < 0:
					new_index = 26 +new_index
				elif new_index >25:
					new_index = new_index%25 -1
				new_letter = alphabet[new_index]
				end_text += new_letter
			else:
				end_text += letter
		print(f"\nThe {direction}d text is: {end_text}")
	ceaser(text,shift,direction)