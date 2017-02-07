# coding:utf-8

MAIN_MENU = '''
0 - выйти
1 - показать записи
2 - добавить запись
3 - Удалить запись
4 - Изменить запись

Выберите действие: '''

translits = {
    'id': 'id',
    'make': 'Марка',
    'model': 'Модель',
    'year': 'Год выпуска'
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