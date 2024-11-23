def write_csv(data):
    """ Запись данных в фаил csv формата"""
    import csv

    with open('stocks.csv', 'w', newline="", encoding='utf-8') as file:    
        writer = csv.DictWriter(file, fieldnames=(data[0].keys()), delimiter=';')    
        writer.writeheader()    
        
        for row in data:        
            writer.writerow(row)

    print('Запись завершена')


def check_commas(string):
    """ Проверка на наличие запятых в строке"""
    import re

    res = re.search(',', string)

    if res != None:
        string = string.replace(',', '')
    
    return string