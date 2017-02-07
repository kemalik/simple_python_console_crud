#!/usr/bin/python
# coding:utf-8

from functions import *


# ==================== CREATE ====================
def create_record():
    make = raw_input('Введите марку машины')
    model = raw_input('Введите модель машины')
    year = raw_input('Введите год выпуска машины')
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
        print 'Запись успешно добавлена'
    else:
        print 'Вы ввели пустые значения'


# ==================== UPDATE ====================
def update_record():
    if cars:
        print_to_console()
        record_id = raw_input('Введите id записи')
        for record in cars:
            if record['id'] == record_id:
                for key, value in record.items():
                    if key == 'id':
                        continue
                    new_record = raw_input(
                        'Текущее значение {current_name}: {current_record}, введите новое значение либо оставьте пустым: '.format(
                            current_name=translits.get(key), current_record=value
                        )
                    )
                    if new_record:
                        record[key] = new_record
                        print 'Запись успешно обновлена'
                break
        else:
            print 'Запись с таким id не найдена'
    else:
        print 'Нет записей'

# ==================== DELETE ====================
def delete_record():
    if cars:
        print_to_console()
        record_id = raw_input('Введите id записи')
        for record in cars:
            if record['id'] == record_id:
                cars.remove(record)
                print 'Запись успешно удалена'
                break
        else:
            print 'Запись с таким id не найдена'
    else:
        print 'Нет записей'


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
            print 'Нет действия на {action}'.format(action=action)


if __name__ == '__main__':
    main()
