import logging

logger = logging.getLogger('First logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('cezar.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('Program started')


LittleLetters: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
BigLetters: str = 'AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
while True:  # Вообще если при выборе кодировки или раскодировки или хотим ли мы выйти из программы. при вводе других
    NewCoddedMessage, Message = '', ''  # символов цикл просто начнеться заново - так сказать проверочка.
    check = input('Вы хотите совершить операцию над сообщением?, 1 - да, 2 -нет : ')
    if check == '2':  # Проверка на выход.
        logger.info('Program stopped')
        break
    elif check == '1':
        Message = input('Введите сообщение: ')
        logger.info('Inputted message: %s' % Message)
        Shift = int(input('Введите смещение: '))
        logger.info('Inputted shift: %s' % Shift)
        check2 = input('Вы хотите раскодировать или закодировать сообщение?, 1 - раскодировать, 2 - закодировать : ')
        if check2 == '1':
            logger.info('type of program operation: decryption')
            Shift = (-1) * Shift
        elif check2 == '2':
            logger.info('type of program operation: encryption')
        else:
            logger.info('Incorrect input')
            continue

        logger.info('Program started working on the message')
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
        logger.info('Program successfully finished working on the message')
        print('Полученное сообщение:', NewCoddedMessage)
