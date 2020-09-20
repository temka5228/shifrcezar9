LittleLetters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BigLetters = 'AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
while True:
	NewCoddedMessage, Message = '', ''
	check = input('Вы хотите закодировать сообщение?, 1 - да, 2 - нет: ')
	if check == '2':
		break
	elif check == '1':
		Message = input('Введите сообщение, которое хотите закодировать: ')
		for letter in range(len(Message)):
			if Message[letter].islower():
				NumberInAlphabet = LittleLetters.index(Message[letter])
				if NumberInAlphabet == 32: delta = -32
				NewCoddedMessage += LittleLetters[NumberInAlphabet + delta]
			if Message[letter].isupper():
				NumberInAlphabet = BigLetters.index(Message[letter])
				if NumberInAlphabet == 32: delta = -32
				NewCoddedMessage += BigLetters[NumberInAlphabet + delta]
		print(NewCoddedMessage)
