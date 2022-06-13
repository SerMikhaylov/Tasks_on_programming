def check(array_1, array_2):
    # запишем повторяющиеся значения из первого и второго массивов в отдельные списки
    repeat_1 = [x for x in array_1 if array_1.count(x) > 1]
    repeat_2 = [y for y in array_2 if array_2.count(y) > 1]
    rez = []  # список для записи чисел, которые имеют два и более повторений в массивах 1 и 2 соответственно, и встречаются в обоих массивах данных
    for num_1 in repeat_1:
        for num_2 in repeat_2:
            if num_2 == num_1:
                rez.append(num_2)
    rez = list(set(rez))
    return rez


if __name__ == '__main__':
    array_1 = [7, 17, 1, 9, 1, 17, 56, 56, 23]
    array_2 = [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]
    print(check(array_1, array_2))
