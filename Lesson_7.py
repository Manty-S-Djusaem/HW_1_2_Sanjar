from random import randint, choice, sample
import datetime
from datetime import datetime as dt
# students = list(range(1, 15))
# ask_students = students.copy()
# del students[6], students[10]
#
# while len(students) != 0:
#     id_s = choice(students)
#     name = input(f'name for {id_s}: ')
#     print(sample(ask_students, 2))
#     rate = int(input(f'marks for {name}: '))
#     students.remove(id_s)
#     print(students)
#     print(ask_students)
#
# print(sample(students, 2))
# import random
# from random import randint, choice, sample
#
#
# print(random.randint(1, 20))
#
#
# students = ['kairat', 'bakdoolot', 'emir', 1, 3]

# print(choice(students))
# print(sample(students, 2))

# print(randint(1, 20))




from random import randint, choice, sample
import datetime
from datetime import datetime as dt
from time import sleep

start = dt.now()
print(start)
command = input('enter command: ')
c = 0
while c != 0:
    if command == 'stop':
        print(dt.now() - start)
        break
    print(c)
    c += 1
    sleep(1)



print(dt.now() - start)


#Kortezh tipo
# player = randint(1, 6), randint(1, 6)
# comp = randint(1, 6), randint(1,6)
#
# cash = 100
# c = 0
# while cash != 0:
#     player = randint(4, 6), randint(4, 6)
#     comp = randint(1, 3), randint(1, 3)
#
#     c += 1
#     if c == 3:
#         player = randint(1, 3), randint(1, 3)
#         comp = randint(4, 6), randint(5, 6)
#     bet = int(input(f'Сделайте ставку: (доступно - {cash})'))
#     if bet > cash:
#         print("Недостаточно средств")
#         continue
#     print(f'{player} vs {comp}')
#
#     if sum(player) > sum(comp):
#         cash += bet
#         print(f'You Won, available {cash}')
#
#     elif sum(player) < sum(comp):
#         cash -= bet
#         print(f'You Lose available {cash}')
#
#     else:
#         print('Draw')
#
#     print(player)
#     print(comp)

# numbers = 100
# bet = int(input('bet: '))
# print(f'')
