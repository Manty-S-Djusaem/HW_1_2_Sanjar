# 1 - Написать функцию, которая возвращает первое слово из полученного предложения.

def first_word(word='Hello world'):
    if type(word) == str:
        word = word.split()
        print(word[0])
    else:
        print(False)


first_word('Geek Tech')


# 2 - Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.

def average(*num):
    print(sum(num) // len(num))
#    print(int(sum(num) // len(num)))


average(1, 2, 43, 999, 543)


# 3(1), вариант решения #1 - Написать функцию, проверяющую надежность пароля.


def strong_pass(password):
    if len(password) >= 6:
        if password.isdigit():
            print(False, 'только цифры')
        elif password.isalpha():
            print(False, 'только буквы')
        else:
            print('Надёжно')
    else:
        print(False, 'меньше 6')


strong_pass('65432r1')

# 3 (2) вариант решения #2 - Написать функцию, проверяющую надежность пароля.

import re


def strong_password(password):
    if len(password) < 6 or re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None or re.search(
            '[a-z]', password) is None:
        print("Weak password!")
    else:
        print("Strong password!")
    return True


strong_password("12345")
strong_password("123456")
strong_password("A123456")
strong_password("A123456z")

