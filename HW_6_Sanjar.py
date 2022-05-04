# 1
ten = []
for i in range(1, 11):
    ten.append(i)
print('ten: ', ten)

# 2
evens = list(filter(lambda x: x % 2 == 0, ten))
print('evens: ', evens)

# 3
evens_xx = list(map(lambda x: x ** 2, evens))
print('evens_xx: ', evens_xx)

# 3-2
evens_yy = [i ** 2 for i in evens]
print('evens_yy:', evens_yy)


# 4
def get_number(lst=ten):
    while True:
        try:
            my_index = input('Введите индекс: ')
            if my_index == 'exit':
                break
            else:
                print(ten[int(my_index)])
        except Exception:
            print(f'Введите число с 0 до 9{len(lst) - 1}')
            # {len(ten) - 1}')


get_number()
