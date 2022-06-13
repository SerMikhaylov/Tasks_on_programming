def rounding():
    num = float(input('Введите число:'))
    # определим число, которое делится без остатка на 5 и является ближайшим к введенному
    num_five = num // 5
    delta_num = abs(num - num_five*5)
    if delta_num < 2.5:
        num = num_five*5
    else:
        num = (num_five + 1)*5
    return num

if __name__ == '__main__':
    print(rounding())