# функция для разделения названий городов запятыми
def city(list_cities):
    str_cities = ''
    for index_city, cit in enumerate(list_cities):
        if index_city == len(list_cities) - 1:
            str_cities = str(str_cities) + str(cit) + '.'
        else:
            str_cities = str(str_cities) + str(cit) + ','
    return str_cities


if __name__ == '__main__':
    list_cities = ['Москва', 'Санкт-Петербург', 'Воронеж']
    print(city(list_cities))
