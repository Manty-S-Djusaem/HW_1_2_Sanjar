while True:
    word = input("Слово: ")
    if word.upper().lower() == 'stop' or word.upper().lower() == 'стоп':
        break

    glasnyi = 0
    soglastniy = 0

    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'aeiouауоыиэяюёе':
                glasnyi += 1
            else:
                soglastniy += 1
    print('Колличество букв: ' + str(len(word)))
    print("Соласных букв: %i\nГласных букв: %i" % (soglastniy, glasnyi))
    print('Гласные/Согласные: ' + str(round(glasnyi / len(word) * 100, 2)) + '%' + ' / ' + str(
        round(soglastniy / len(word) * 100, 2)) + '%')
