#!/usr/bin/python
# coding:utf-8

MAIN_MENU = u'''
0 - выйти
1 - показать записи
2 - добавить запись
3 - Удалить запись
4 - Изменить запись

Выберите действие: '''

translits = {
    'id': u'id',
    'make': u'Марка',
    'model': u'Модель',
    'year': u'Год выпуска'
}

cars = [
    {'id': '1', 'make': 'BMW', 'model': 'X5', 'year': '2010'},
    {'id': '2', 'make': 'Lamborghini', 'model': 'Aventador', 'year': '2011'},
    {'id': '3', 'make': 'Bugatti', 'model': 'Veyrona', 'year': '2007'},
    {'id': '4', 'make': 'Toyota', 'model': 'Camry', 'year': '2015'},
]

spaces = {
    'id': 2,
    'make': 2,
    'model': 2,
    'year': 2
}


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
