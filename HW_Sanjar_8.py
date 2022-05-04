from datetime import datetime as dt
from random import randint

user = input('Введите имя: ')
chance = int(input('Сколько попыток?: '))
start = dt.now()
total_chance = str(chance)
file = open('results.txt', 'w')
correct = 'правильно'
wrong = 'неправильно'

while True:
    try:
        a = randint(1, 9)
        b = randint(1, 9)
        right_answer = a * b
        print(f"У вас есть {chance} попытки")
        user_answer = int(input(f'Сколько будет {a} * {b} = ? '))

        if user_answer == right_answer:
            chance -= 1
            print(right_answer)
            file.write(f'{a} * {b} = {user_answer} ({right_answer}) {correct} \n')
        if user_answer != right_answer:
            chance -= 1
            print(right_answer)
            file.write(f'{a} * {b} = {user_answer} ({right_answer}) {wrong} \n')
        if chance == 0:
            print(f"Было {total_chance} попыток,", f"потраченное время: {dt.now() - start},", f"имя: {user}")
            break
    except ValueError:
        print('Вводите только цифры!')

file.write(f'Было {total_chance} попыток, потраченное время: {dt.now() - start}, имя: {user}')
file.close()
