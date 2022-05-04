# print('угадай числоo')
# print('конверсация числа')
# print('гласные согласные')

# name = 'Sana'
# name = input('Whats ur name?:')
# job = 'mvd'
# surname = "Sa'na"
# print("Hello Sana + name + surname, works in ")
# print(f"Hello, {name.title()} {surname.title()}, works in {job.upper()}")


# or, and, not


# name = "Sana"
# password = 123456
# print(2 != 3)
# print(23 != 23)


# print(2 == 2+1)ш
# print(2 != 2)
# print(2 > 2)
# print(2 >= 2)
# print(2 > 1 and 3 > 1)
# print(2 > 1 < 3)
# print(2 > 3 or 2 == 3)
# print(2 < 2)
# print(2 <= 2)


# age = 18

#    print('awfy')
# elif age < 18:
# print('sy')
# else age:
# print()
# name = 'Sana'
# password = "123456"

# input_name = input('name: ')
# input_password = input('Wright your password: ')
# if input_password == name and input_password == password:
# print('Ok')
# else:
# print('Error')

# need = 'coca'
# need2 = 'fanta'

# check = input('drink ')

# if check in need or check in need2:
# print('ok')
# else:
# print('боло берет!')

#    if check not in need or check in need2:
#       print('боло берет!')
#  else:
#     print('ok')


# word = 'Fourteen'
# for letter in word:
# if letter == 't':
#     print('we are skip t')
#      #continue
#       break
#    print(letter, 'Буква!')


# c = 'Ddos'
# while True:
#    print(c)

# c = 0
# while True:
# print(c)
#  c += 1
#   if c == 1000001:
#        break

# word = 'четырнадцать'
# print(len(word))

# while word[-1] != 'ь':
#   print(word[c], c)
#    c += 1
# prinr(word([4])
# c = 0
# while c != len(word):
#   print(word[c], c)
#  c += 1

# numbers_evens = '2468'
# numbers_odds = '13579'

# while 1:
# evens = 0
# odds = 0
# number = input('Введите число')

# for i in number:
#    if i in numbers_evens:
#         evens += 1
#      elif i in number_odds:
#           odds += 1
#
#   print(f'Чётных чисел {evens} \n'
#          f'Нечётные чисел {odds}')


students = ['adilya', 'vadim', 'sanya', 'alina']

# [start:end:step] формулы отрезков

new = students[1:3]

other = students[::2]

# print(new)
print(other)

# count возващает колво
# append указывает в конец
# sort сортлиирует (противоположный revers


new = students

print(students[2])

deleted = students.pop(-2)

new_list = list()
new_list.append(students.pop(-2))

students = []

rus_letter = "йцукенгшщзхъфывапролджэячсмитьбю"
name = 'саша'

print(name[0] is rus_letter)

while True:
    students = input('Кто был: ')
    for i in students:
        if i in rus_letter:
            print('only English letters')
            break

    if students == 'exit':
        print('exit')
        break

    elif students in rus_letter:
        print('only English letters')
        continue

        #Нужно проверить все буквы если есть какаято русская буква то не доболвлять в список




    elif len(students) > 10 or len(students) < 1:
        print('Very long name or short name')
        continue

    elif not students.isalpha():
        print('Only word in name')
    continue

students.append(students.title())
print(students)

print(students)


name = input('Логин: ')
password = int(input('Введите Пароль: '))

# input_name = input('name: ')
# input_password = input('Wright your password: ')
if password > 6:  # == name and input_password == password:
    print('Ваш пароль слишком ненадёжный')
else:
    if password < 6:
        print('Ok')

        ten = []
        for i in range(1, 11):
            ten.append(i)
        print('ten', ten)

        evens = []
        for i in ten:
            if int(i) % 2 == 0:
                evens.append(i)

        print('evens', evens)

        evensx2 = list(map(lambda x: x ** 2, evens))
        print('evens', evensx2)


     # if index != ren:
#   print('False')
#  if index == ren:
#     print('Okay')

# print('ok')


# print('False')
# if index != [ren]:
#   if index.upper().lower() == 'stop' or index.upper().lower() == 'стоп':
#      break
# ren = input("Слово: ")
# if ren.upper().lower() == 'stop' or ren.upper().lower() == 'стоп':
# break

# if evens.upper().lower() == 'stop' or evens.upper().lower() == 'стоп':

# if index.upper().lower() == 'stop' or index.upper().lower() == 'стоп'

# while True:
#   try:
#      id_student = int(input('введите id: '))
#     name = input('name: ')
#    rate = int(input(f'оценку для {name}'))
#   data.append(dict(id=id_student, name=name, rate=rate))
# except:
#   print("внимательней!")
#  continue
# for i in data:
#   print(i)
# print('Wright index: ', int(input(index)))

# index = input("wright index: ")
# evens = input("number: ")
# if evens.upper().lower() == 'stop' or evens.upper().lower() == 'стоп':
#   if index.upper().lower() == 'stop' or index.upper().lower() == 'стоп':

## ren = input("number: ")
## if ren.upper().lower() == 'stop' or ren.upper().lower() == 'стоп':


# for i in evens:
#   print(i * i)