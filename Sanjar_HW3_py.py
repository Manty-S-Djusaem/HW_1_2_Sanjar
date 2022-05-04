data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
letters.reverse()
numbers.reverse()
letters[1] = 'G'
letters[7] = 'c'

numbers[0] = numbers[0] ** 2
numbers[1] = numbers[1] ** 2
numbers[2] = numbers[2] ** 2

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print(letters_tuple)
print(numbers_tuple)
