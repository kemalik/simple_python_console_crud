# coding:utf-8

from data import *


def get_spaces():
    for record in cars:
        for key, value in record.items():
            value_length = len(value)
            translit_length = len(translits[key])

            if spaces[key] < value_length or spaces[key] < translit_length:
                if value_length > translit_length:
                    spaces[key] = value_length
                else:
                    spaces[key] = translit_length
    return spaces


def print_to_console():
    if cars:
        print "=============================================="
        spaces = get_spaces()
        print u'| id | Марка{make_space}| Модель{model_space}| Год выпкска{year_space}|'.format(
            make_space=' '*(spaces['make']-len(translits['make'])+1),
            model_space=' '*(spaces['model']-len(translits['model'])+1),
            year_space=' '*(spaces['year']-len(translits['year'])+1),
        )
        for car in cars:
            id_space = ' ' * (spaces['id']-len(car['id']))
            make_space = ' ' * (spaces['make']-len(car['make']))
            model_space = ' ' * (spaces['model']-len(car['model']))
            year_space = ' ' * (spaces['year']-len(car['year']))
            print u'| {id} | {make} | {model} | {year} |'.format(
                id=car['id']+id_space,
                make=car['make']+make_space,
                model=car['model']+model_space,
                year=car['year']+year_space
            )
        print "=============================================="
    else:
        print u'Нет записей'


def get_next_id():
    if len(cars):
        max_id = int(max(i['id'] for i in cars))
        return str(max_id + 1)
    return 0