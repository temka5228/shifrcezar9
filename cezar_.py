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
			if Message[letter] in LittleLetters:
				NewCoddedMessage += LittleLetters[letter + 1]
			if Message[letter] in BigLetters:
				NewCoddedMessage += BigLetters[letter+1]
		print(NewCoddedMessage)
