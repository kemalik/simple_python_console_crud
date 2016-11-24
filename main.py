#!/usr/bin/python
# coding:utf-8

cars = [
    {'id': '1', 'make': 'BMW', 'model': 'X5', 'year': '2010'},
    {'id': '2', 'make': 'Lamborghini', 'model': 'Aventador', 'year': '2011'},
    {'id': '3', 'make': 'Bugatti', 'model': 'Veyrona', 'year': '2007'},
    {'id': '4', 'make': 'Toyota', 'model': 'Camry', 'year': '2015'},
]

def print_to_console(records=None):
    if records:
        print "===================================="
        print u'| id | Марка | Модель | Год выпкска |'
        for car in cars:
            print u'| {id} | {make} | {model} | {year} |'.format(
                id=car['id'], make=car['make'], model=car['model'], year=car['year']
            )
        print "===================================="
    else:
        print u'Нет записей'


def create_record(records=None):
    make = raw_input(u'Введите марку машины')
    model = raw_input(u'Введите модель машины')
    year = raw_input(u'Введите год выпуска машины')
    for record in records:
        if set([make, model, year]).issubset(record.values()):
            print u'Машина {make} {model} {year} года уже есть в базе'
            return
    records.append({
        'id': 1,
        'make': make,
        'model': model,
        'year': year
    })
    print u'Запись успешно добавлена'




def main():
    action = 1
    while action != 0:
        action = raw_input(u'0 - выйти\n1 - показать записи\n2 - добавить запись\n\nВыберите действие: ')
        if action == '1':
            print_to_console(cars)
        elif action == '2':
            create_record(cars)
        else:
            break


if __name__ == '__main__':
    main()