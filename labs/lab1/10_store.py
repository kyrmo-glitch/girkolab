#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
table_code = goods['Стол']
table1_qty = store[table_code][0]['quantity']
table1_price = store[table_code][0]['price']
table2_qty = store[table_code][1]['quantity']
table2_price = store[table_code][1]['price']
table_total_qty = table1_qty + table2_qty
table_total_cost = table1_qty * table1_price + table2_qty * table2_price
print(f'Стол - {table_total_qty} шт, стоимость {table_total_cost} руб')

divan_code = goods['Диван']
divan1_qty = store[divan_code][0]['quantity']
divan1_price = store[divan_code][0]['price']
divan2_qty = store[divan_code][1]['quantity']
divan2_price = store[divan_code][1]['price']
divan_total_qty = divan1_qty + divan2_qty
divan_total_cost = divan1_qty * divan1_price + divan2_qty * divan2_price
print(f'Диван - {divan_total_qty} шт, стоимость {divan_total_cost} руб')

chair_code = goods['Стул']
chair1_qty = store[chair_code][0]['quantity']
chair1_price = store[chair_code][0]['price']
chair2_qty = store[chair_code][1]['quantity']
chair2_price = store[chair_code][1]['price']
chair3_qty = store[chair_code][2]['quantity']
chair3_price = store[chair_code][2]['price']
chair_total_qty = chair1_qty + chair2_qty + chair3_qty
chair_total_cost = chair1_qty * chair1_price + chair2_qty * chair2_price + chair3_qty * chair3_price
print(f'Стул - {chair_total_qty} шт, стоимость {chair_total_cost} руб')