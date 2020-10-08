LittleLetters: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BigLetters: str = 'AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
while True:  # Вообще если при выборе кодировки или раскодировки или хотим ли мы выйти из программы. при вводе других
    NewCoddedMessage, Message = '', ''  # символов цикл просто начнеться заново - так сказать проверочка.
    check = input('Вы хотите совершить операцию над сообщением?, 1 - да, 2 -нет : ')
    if check == '2':  # Проверка на выход.
        break
    elif check == '1':
        check2 = input('Вы хотите раскодировать или закодировать сообщение?, 1 - раскодировать, 2 - закодировать : ')
        Message = input('Введите сообщение: ')
        Shift = int(input('Введите смещение: '))
        if check2 == '1': Shift = (-1) * Shift  # Если сообщение надо раскодить,
        for letter in range(len(Message)):  # то смещение делаем в обратную сторону.
            if Message[letter] in LittleLetters:  # Если буква в нижнем регистре.
                NumberInAlphabet = LittleLetters.index(Message[letter])  # Узнаем какая по счету буква в сообщении.
                if 32 - NumberInAlphabet < Shift:  # Проверка: если прибавить смещение к номеру буквы в сообщении
                    delta = - 33 + Shift  # выходит ли за рамки длинны алфавита. Если выходит -
                else:  # то остаток начинаем с начала алфавита.
                    delta = Shift
                NewCoddedMessage += LittleLetters[NumberInAlphabet + delta]  # Добавляем букву в новое сообщение
            elif Message[letter] in BigLetters:  # Если буква в верхнем регистре. По факту то же самое,
                NumberInAlphabet = BigLetters.index(Message[letter])  # что и с нижним регистром.
                if 32 - NumberInAlphabet < Shift:
                    delta = - 33 + Shift
                else:
                    delta = Shift
                NewCoddedMessage += BigLetters[NumberInAlphabet + delta]
            else:
                NewCoddedMessage += Message[letter]
        print('Полученное сообщение:', NewCoddedMessage)
