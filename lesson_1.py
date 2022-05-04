# insert - Добавляет указанный элемент в список на указанную позицию.
# pop - Возвращает элемент [на указанной позиции], удаляя его из списка.
# tuple - Из квадратных в круглые скобки
# remove - Удаляет из списка указанный элемент.
# reverse - меняет местами
# tuple - кортёж

other = dict(surname='Alykulov', job='engineer')
student = {
    'name': 'Aziz',
    # 'age': 20,
    'hobby': ['english', 'boxing'],
}
student.update(other)

student['hobby'].append('books')
student['hobby'] = tuple(student['hobby'])

for k, v in student.items():
    print(f'{k}: {v}')

print(student)

new = ([2, 'asd'], [3, 'rtyrty'], [4, 'dfhbvcn'])
new = dict(new)
print(new)
print(student.keys())
print(student.values())
print(student.items())





student['address'] = 'Ibraimova 255'

student['age'] = 21

del student[2]
deleted = student.pop((1, 2, 3))

student['deleted'] = deleted
print(deleted)
print(student)

