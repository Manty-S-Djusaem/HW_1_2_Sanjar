#Создал переменные, в которые пользователь будет вводить данные
chui = int(input('Введите тепмпературу в Чуйской области: '))
narin = int(input('Введите тепмпературу в Нарынской области: '))
osh = int(input('Введите тепмпературу в Ошской области: '))
issikkl = int(input('Введите тепмпературу в Иссык-Кульской области: '))
batken = int(input('Введите тепмпературу в Баткенской области: '))
talas = int(input('Введите тепмпературу в Таласской области: '))
jalalabad = int(input('Введите тепмпературу в Джалал-Абадской области: '))

#Создал массив и поместил в него переменные
region = [chui, narin, osh, issikkl,  batken, talas, jalalabad]

#Создал ещё одну переменную для вычесления среднего значения
average = sum(region) / 7

#Вывел среднюю температуру в градусах по Цельсию
print('Средняя температура воздуха по КР на сегодня:\t' + str(round(average)) + '°C')







for i in evens:
    print(i * i)

while True:
    if evens.upper().lower() == 'stop' or evens.upper().lower() == 'стоп':
        try:
            id_ren = int(input('введите id: '))
            name = input('name: ')
            rate = int(input(f'оценку для {name}: '))
            evens.append(dict(id=id_ren, name=name, rate=rate))

        except:
            print('Carrefule')
            continue
        for i in evens:
            print(i)



