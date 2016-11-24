#!/usr/bin/python
# coding:utf-8

from data import *
from functions import *


# ==================== CREATE ====================
def create_record():
    make = raw_input(u'Введите марку машины')
    model = raw_input(u'Введите модель машины')
    year = raw_input(u'Введите год выпуска машины')
    for record in cars:
        if set([make, model, year]).issubset(record.values()):
            print u'Машина {make} {model} {year} года уже есть в базе'
            return
    if make and model and year:
        cars.append({
            'id': get_next_id(),
            'make': make,
            'model': model,
            'year': year
        })
        print u'Запись успешно добавлена'
    else:
        print u'Вы ввели пустые значения'


# ==================== UPDATE ====================
def update_record():
    if cars:
        print_to_console()
        record_id = raw_input(u'Введите id записи')
        for record in cars:
            if record['id'] == record_id:
                for key, value in record.items():
                    if key == 'id':
                        continue
                    new_record = raw_input(
                        u'Текущее значение {current_name}: {current_record}, введите новое значение либо оставьте пустым: '.format(
                            current_name=translits.get(key), current_record=value
                        )
                    )
                    if new_record:
                        record[key] = new_record
                        print u'Запись успешно обновлена'
                break
        else:
            print u'Запись с таким id не найдена'
    else:
        print u'Нет записей'

# ==================== DELETE ====================
def delete_record():
    if cars:
        print_to_console()
        record_id = raw_input(u'Введите id записи')
        for record in cars:
            if record['id'] == record_id:
                cars.remove(record)
                print u'Запись успешно удалена'
                break
        else:
            print u'Запись с таким id не найдена'
    else:
        print u'Нет записей'


# ==================== MAIN ====================
def main():
    while True:
        action = raw_input(MAIN_MENU)
        if action == '1':
            print_to_console()
        elif action == '2':
            create_record()
        elif action == '3':
            delete_record()
        elif action == '4':
            update_record()
        elif action == '0':
            break
        else:
            print u'Нет действия на {action}'.format(action=action)


if __name__ == '__main__':
    main()
