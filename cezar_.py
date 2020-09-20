LittleLetters: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BigLetters: str = 'AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
while True:
	NewCoddedMessage, Message = '', ''
	check = input('Вы хотите закодировать сообщение?, 1 - да, 2 - нет: ')
	if check == '2':
		break
	elif check == '1':
		Message = input('Введите сообщение, которое хотите закодировать: ')
		Shift = int(input('Насколько хотите сдвинуть буквы в строке?: '))
		for letter in range(len(Message)):
			if Message[letter] in LittleLetters:
				NumberInAlphabet = LittleLetters.index(Message[letter])
				if 32 - NumberInAlphabet < Shift:
					delta = - 33 + Shift
				else:
					delta = Shift
				NewCoddedMessage += LittleLetters[NumberInAlphabet + delta]
			elif Message[letter] in BigLetters:
				NumberInAlphabet = BigLetters.index(Message[letter])
				if 32 - NumberInAlphabet < Shift:
					delta = - 33 + Shift
				else:
					delta = Shift
				NewCoddedMessage += BigLetters[NumberInAlphabet + delta]
			else:
				NewCoddedMessage += Message[letter]
		print(NewCoddedMessage)
