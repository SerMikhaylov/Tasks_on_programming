def numbers():
    num = int(input('Введите целое число:'))
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        rez = 'Введенное число не является простым'
    elif num % 1 == 0 and num % num == 0:
        rez = 'Введенное число является простым'
    return rez

if __name__ == '__main__':
    print(numbers())