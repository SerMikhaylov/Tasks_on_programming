def correct_word():
    num = int(input('Введите целое число:'))
    # определим количество цифр в введенном числе
    num_str = len(str(num))
    # определим какое число записано в разряде единиц
    num_1 = int(str(num)[-1])
    comp = 'компьютер'
    if num_str >= 2:
    # определим какое число записано в разряде десятков
        num_10 = int(str(num)[-2])
        if num_10 != 1 and (num_1 == 0 or num_1 == 5 or num_1 == 6 or num_1 == 7 or num_1 == 8 or num_1 == 9):
            rez = str(num) + ' ' + comp + 'ов'
        elif num_10 != 1 and (num_1 == 2 or num_1 == 3 or num_1 == 4):
            rez = str(num) + ' ' + comp + 'а'
        elif num_10 != 1 and (num_1 == 1):
            rez = str(num) + ' ' + comp
        elif num_10 == 1:
            rez = str(num) + ' ' + comp + 'ов'
    else:
        pass
    if num_str == 1 and (num_1 == 0 or num_1 == 5 or num_1 == 6 or num_1 == 7 or num_1 == 8 or num_1 == 9):
        rez = str(num) + ' ' + comp + 'ов'
    elif num_str == 1 and (num_1 == 2 or num_1 == 3 or num_1 == 4):
        rez = str(num) + ' ' + comp + 'а'
    elif num_str == 1 and (num_1 == 1):
        rez = str(num) + ' ' + comp
    return rez


if __name__ == '__main__':
    print(correct_word())
