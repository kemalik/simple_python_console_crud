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

def main():
    print_to_console(cars)


if __name__ == '__main__':
    main()