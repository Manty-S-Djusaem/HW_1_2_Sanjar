while True:
    try:
        number_1 = float(input("number_1 = "))
        s = input("(+, -, *, /): ")
        number_2 = float(input("number_2 = "))
        if s in ('+', '-', '*', '/'):
            if s == '+':
                print("%.2f" % (number_1 + number_2))
            elif s == '-':
                print("%.2f" % (number_1 - number_2))
            elif s == '*':
                print("%.2f" % (number_1 * number_2))
            elif s == '/':
                print("%.2f" % (number_1 / number_2))
        else:
            print("Нельзя ставить буквы!")
    except ZeroDivisionError:
        print("Нельзя делить на 0!")
