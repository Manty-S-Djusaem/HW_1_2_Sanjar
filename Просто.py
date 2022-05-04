day = int(input("День:"))
mon = int(input("Месяц:"))

if (day >= 21 and day <= 31 and mon == 3) or (mon == 4 and day >= 1 and day <= 19):
    print('Знак зодиака: Овен')
elif day >= 20 and day <= 30 and mon == 4 or (mon == 5 and day >= 1 and day <= 20):
    print('Знак зодиака: Телец')
