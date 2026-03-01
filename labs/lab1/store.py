goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
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

def print_lamp():
    code = goods['Лампа']
    qty = store[code][0]['quantity']
    cost = qty * store[code][0]['price']
    return f'Лампа - {qty} шт, стоимость {cost} руб'

def print_table():
    code = goods['Стол']
    items = store[code]
    qty = items[0]['quantity'] + items[1]['quantity']
    cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price']
    return f'Стол - {qty} шт, стоимость {cost} руб'

def print_sofa():
    code = goods['Диван']
    items = store[code]
    qty = items[0]['quantity'] + items[1]['quantity']
    cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price']
    return f'Диван - {qty} шт, стоимость {cost} руб'

def print_chair():
    code = goods['Стул']
    items = store[code]
    qty = items[0]['quantity'] + items[1]['quantity'] + items[2]['quantity']
    cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price'] + items[2]['quantity'] * items[2]['price']
    return f'Стул - {qty} шт, стоимость {cost} руб'