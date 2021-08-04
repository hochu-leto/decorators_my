import json
from datetime import datetime


def decorator_maker_with_arguments(fin_file):
    def my_decorator(func):
        def wrapped(*args, **kwargs):
            today = datetime.today()

            with open(fin_file, 'w', encoding='utf-8') as fw:
                fw.write('Вызов функции был ' + today.strftime("%Y-%m-%d %H:%M:%S") + '\n')
                fw.write('Имя функции ' + func.__name__ + '\n')
                fw.write('Аргументы функции ' + json.dumps(args) + '\n')
                fw.write('и ' + json.dumps(kwargs) + '\n')
                fw.write('Функция вернула ' + json.dumps(func(*args, **kwargs)) + '\n')
            return func(*args, **kwargs)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments('log.txt')
def read_cook_book(file):
    data = {}
    key = ['ingredient_name', 'quantity', 'measure']
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            ingredients = []
            name = f.readline().rstrip()
            if not name:
                break
            ingredient_count = f.readline().rstrip()
            for i in range(int(ingredient_count)):
                ing = f.readline().rstrip()
                ing_list = ing.strip().split("|")
                ingredient = dict(zip(key, ing_list))
                ingredient['quantity'] = int(ingredient['quantity'])
                ingredients.append(ingredient)
            data[name] = ingredients
            f.readline().rstrip()
    return data


file = 'c_book.txt'
data = read_cook_book(file)
print(data)
