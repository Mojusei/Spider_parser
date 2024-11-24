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


def update_db_data(db_file='my_database.db'):
    """ Обновление базы данных """
    import csv
    from Database import Database

    database = Database(db_file) 
    
    with open('stocks.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for row in reader:
            database.insert_data(title=row['Заголовок'], refer=row['Ссылка'])

        print ('Запись завершена')

    database.close_db()
    print('База данных обновлена')
