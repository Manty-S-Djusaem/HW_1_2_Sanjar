###import colorama

# word = 'python language programming'
# new = word.split()
# print(new)

# def get_first_word(sentence: str):
# first_word = ''
# for i in sentence:
#    if i != ' ':
#         first_word += i
#      else:
#           return first_word


# if type(sentence) != str:
#   return False
# return sentence.split()[0]

# print(get_first_word(word))
# print(get_first_word(234))
# print(get_first_word(True))


# names = ['aza', 'beka', 'tima']


# def up(word: str):
#    return word.title()


# def get_title(lst, func):
#  for i in lst:
#       print(func(i))

#        get_title(names, up)
##        get_title(names, up2)


# def b(a):
#   return a * a

# a = lambda x: x * x
# a = lambda *x: x * 2
# a = lambda x: x * a
# a = lambda x: x * 2

# print(a(5))
# print(b(5))


# numbers = [1, 2, 3, 4, 5, 6]

# new = list(map(lambda x: x**3, numbers))

# other = list(filter(lambda x: x > 10, new))
# other = list(filter(lambda x: x > 10, numbers))
# sort1 = list(sorted(numbers, key=(len))

# print(other)
# print(new)


# numbers = [0, 1, 2, 3, 4, 5]

# other = [i**3 for i in numbers if i%2 == 0]

# numbers1 = list(range(2, 6))

# print(numbers)
# print(numbers1)


# try:
#    expression
# except
#    expression


# try:
#    print(10/0)
# except:
#   print('You cant devided zero on zero!')


# names = ['aza', 'sam', 'rick', 'jack']
# names1 = ['aza', 'sam', 'rick']

# while True:
# try:
#    index = int(input('Wright index: '))
#     print(names1[index])
#      #print(names[index])
#   except ValueError:
#        print('Wright only ordinal numbers at 0 from 5!')
# except IndexError:
#   print(print)

# print(names[0])


students = [2, 4, 5, 7, 9, 10, 11, 12, 13, 14, 15]

data = []

while True:
    try:
        id_student = int(input('Wright id: '))
        name = input('name: ')
        rate = int(input(f'marks for {name}'))
        data.append(dict(id=id_student, name=name, rate=rate))
    except:
        print('Carrefule')
        continue
    for i in data:
        print(i)
        for r, v in i.items():
            #print(k, v)
