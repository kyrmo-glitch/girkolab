#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Список продуктов
products = ['печенье', 'конфеты', 'карамель', 'пирожное']

for product in products:
    print(f"{product}:")
    
    # Собираем цены
    prices = []
    for shop_name in shops:
        for item in shops[shop_name]:
            if item['name'] == product:
                prices.append([shop_name, item['price']])
    
    # Сортировка пузырьком (или просто встроенная сортировка по первому элементу)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i][1] > prices[j][1]:
                prices[i], prices[j] = prices[j], prices[i]
    
    # Выводим два первых
    for i in range(2):
        print(f"  {prices[i][0]}: {prices[i][1]} руб.")
    print()
