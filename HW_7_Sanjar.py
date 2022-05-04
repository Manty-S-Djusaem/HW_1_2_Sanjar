import random
from datetime import datetime as dt

attempt = 0
secret = random.randint(1, 100)
start = dt.now()

while True:
    try:
        number = int(input('Enter Number: '))
        if number > 100:                            #TODO: хотел сделать так, но не сработало: if 1 > number > 100:
            print("Only in range 1-100")
        elif number < 1:
            print("Only in range 1-100")
        elif number < secret:
            print("number < secret")
            attempt += 1
        elif number > secret:
            print("number > secret")
            attempt += 1
        elif type(number) == str:
            print("Entered not a number")
        else:
            print(f"Вы угадали число - {secret}!")
            attempt += 1
            print('Кол-во попыток: ', attempt)
            print(dt.now() - start)
            break
    except ValueError:
        print(f'Entered not a number')
