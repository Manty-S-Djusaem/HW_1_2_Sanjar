from random import randint, choice, sample
from datetime import datetime as dt
file = open('new file.txt', 'w')
file.write('start = dt.now()')
file.close()
attempt = 0
start = dt.now()

while True:
    a = randint(1, 5)
    b = randint(6, 9)
    right_answer = a * b
    name = input('Укажите Имя: ')
    user_answer = input(f'Сколько будет {a} * {b} = \n')
    #with open('results.txt', 'a') as file:

    # from time import sleep
    # from random import randint
    #
    # data = []
    #
    # # chance = [5]
    # user = input('Введите имя: ')
    #
    # while True:
    #     try:
    #         chance = 5
    #         a = randint(1, 4)
    #         b = randint(4, 9)
    #         right_answer = a * b
    #         print(f"У вас есть {chance} шансов")
    #         chance -= 1
    #         user_answer = int(input(f'Сколько будет {a} * {b} = \n'))
    #         if user_answer == right_answer:
    #             print('ok')
    #         else:
    #             if user_answer == right_answer:
    #                 chance -= 1
    #     except TypeError:
    #         print('Введите правильный ответ')
    #     except ValueError:
    #         print('Введите только цифры')