## Отчет по лабораторной работе №1

### 00_distance
Задание

      
      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      # Есть словарь координат городов
      
      sites = {
          'Moscow': (550, 370),
          'London': (510, 510),
          'Paris': (480, 480),
      }
      
      # Составим словарь словарей расстояний между ними
      # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      
      distances = {}
      
      # TODO здесь заполнение словаря
      
      mx, my = sites['Moscow']
      lx, ly = sites['London']
      px, py = sites['Paris']
      
      dist_ml = ((mx - lx) ** 2 + (my - ly) ** 2) ** 0.5
      dist_mp = ((mx - px) ** 2 + (my - py) ** 2) ** 0.5
      dist_lp = ((lx - px) ** 2 + (ly - py) ** 2) ** 0.5
      
      distances['Moscow'] = {'London': round(dist_ml, 2), 'Paris': round(dist_mp, 2)}
      distances['London'] = {'Moscow': round(dist_ml, 2), 'Paris': round(dist_lp, 2)}
      distances['Paris'] = {'Moscow': round(dist_mp, 2), 'London': round(dist_lp, 2)}
      
      print(distances)
      
Результат

<img width="1246" height="45" alt="image" src="https://github.com/user-attachments/assets/0a23673c-51d1-4451-b07f-7ddae6d4ae24" />


Описание проделанной работы

Даны координаты городов. Первый действием записал координат каждого города в отдельные переменные. Расчитал расстояний между каждыми городами по формуле. Сформировал словарь расстояния от одного города до двух других, с помощью round() окргуглил до 2 знаков после запятой.

---
### 01_circle
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      
      # Есть значение радиуса круга
      radius = 42
      
      # Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
      # подсказки:
      #       формулу можно подсмотреть в интернете,
      #       пи возьмите равным 3.1415926
      #       точность указывается в функции round()
      # TODO здесь ваш код
      
      pi = 3.1415926
      area = pi * radius ** 2
      print(round(area, 4))
      
      # Далее, пусть есть координаты точки
      
      point_1 = (23, 34)
      
      # где 23 - координата х, 34 - координата у
      # Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
      # то выведите на консоль True, Или False, если точка лежит вовне круга.
      # подсказки:
      #       нужно определить расстояние от этой точки до начала координат (0, 0)
      #       формула так же есть в интернете
      #       квадратный корень - это возведение в степень 0.5
      #       операции сравнения дают булевы константы True и False
      # TODO здесь ваш код
      
      distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
      print(distance_1 <= radius)
      
      # Аналогично для другой точки
      
      point_2 = (30, 30)
      
      # Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
      # Или False, если точка лежит вовне круга.
      # TODO здесь ваш код
      
      distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
      print(distance_2 <= radius)
      
      # Пример вывода на консоль:
      # 77777.7777
      # False
      # False
Результат 

<img width="1086" height="91" alt="image" src="https://github.com/user-attachments/assets/ce98434c-0f2b-43d4-a099-f582d0da2cf2" />

Описание проделанной работы

1. Посчитал 

---
### 02_operations
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      
      # Расставьте знаки операций "плюс", "минус", "умножение" и скобки
      # между числами "1 2 3 4 5" так, что бы получилось число "25".
      #
      # Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
      # Порядок чисел нужно сохранить.
      
      # Пример для чисел "1 2 3" и "9"
      result = (1 + 2) * 3
      print(result)
      
      # TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль
      result = 1 * 2 + 3 + 4 * 5
      print(result)  
Результат

<img width="1133" height="63" alt="image" src="https://github.com/user-attachments/assets/5650f912-c082-47a9-9dd8-e94cc6e8f5b2" />

Описание проделанной работы

---
### 03_favorite_movies
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      # Есть строка с перечислением фильмов
      
      my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
      
      # Выведите на консоль с помощью индексации строки, последовательно:
      #   первый фильм
      #   последний
      #   второй
      #   второй с конца
      # Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
      # Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
      # как указано в задании!
      # TODO здесь ваш код
      #   первый фильм
      print(my_favorite_movies[:10])
      
      #   последний
      print(my_favorite_movies[-15:])
      
      #   второй
      print(my_favorite_movies[12:25])
      
      #   второй с конца
      print(my_favorite_movies[-22:-17])
Результат

<img width="1236" height="101" alt="image" src="https://github.com/user-attachments/assets/4a473feb-248a-4deb-af3b-3975d8ec6474" />

Описание проделанной работы

---
### 04_my_family
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      # Создайте списки:
      # моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
      
      my_family = ['папа', 'мама', 'я', 'брат']
      
      # список списков приблизительного роста членов вашей семьи
      
      my_family_height = [
          ['папа', 180],
          ['мама', 165],
          ['я', 175],
          ['брат', 170]
      ]
      
      # Выведите на консоль рост отца в формате
      #   Рост отца - ХХ см
      
      print(f'Рост отца - {my_family_height[0][1]} см')
      
      # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
      #   Общий рост моей семьи - ХХ см
      
      total_height = 0
      for member in my_family_height:
          total_height += member[1]
      
      print(f'Общий рост моей семьи - {total_height} см')
Результат

<img width="1300" height="68" alt="image" src="https://github.com/user-attachments/assets/083395a0-b487-475f-ae2c-fc3aea0ca33e" />

Описание проделанной работы 

---
### 05_zoo
Задание

      # добавьте птиц из списка birds в последние клетки зоопарка
      
      birds = ['rooster', 'ostrich', 'lark', ]
      
      #  и выведите список на консоль
      
      zoo.extend(birds)
      print(zoo)
      
      # уберите слона
      #  и выведите список на консоль
      
      zoo.remove('elephant')
      print(zoo)
      
      # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
      # Номера при выводе должны быть понятны простому человеку, не программисту.
      
      lion_index = zoo.index('lion') + 1
      lark_index = zoo.index('lark') + 1
      print(f'Лев сидит в клетке номер {lion_index}')
      print(f'Жаворонок сидит в клетке номер {lark_index}')
Результат

<img width="1270" height="123" alt="image" src="https://github.com/user-attachments/assets/d8e1ae9f-9eb8-4512-8648-1fdf7e97181e" />

Описание проделанной работы

---
### 06_songs_list
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      # Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
      # Точность указывается в функции round(a, b)
      # где a, это число которое надо округлить, а b количество знаков после запятой
      # более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round
      violator_songs_list = [
          ['World in My Eyes', 4.86],
          ['Sweetest Perfection', 4.43],
          ['Personal Jesus', 4.56],
          ['Halo', 4.9],
          ['Waiting for the Night', 6.07],
          ['Enjoy the Silence', 4.20],
          ['Policy of Truth', 4.76],
          ['Blue Dress', 4.29],
          ['Clean', 5.83],
      ]
      # распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
      #   Три песни звучат ХХХ.XX минут
      # Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
      # Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
      # TODO здесь ваш код
      # распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean'
      # Находим время для каждой песни
      halo_time = 0
      enjoy_time = 0
      clean_time = 0
      for song in violator_songs_list:
          if song[0] == 'Halo':
              halo_time = song[1]
          elif song[0] == 'Enjoy the Silence':
              enjoy_time = song[1]
          elif song[0] == 'Clean':
              clean_time = song[1]
      # Суммируем и округляем до 2 знаков
      total_time = round(halo_time + enjoy_time + clean_time, 2)
      print(f'Три песни звучат {total_time} минут')
      # Есть словарь песен группы Depeche Mode
      violator_songs_dict = {
          'World in My Eyes': 4.76,
          'Sweetest Perfection': 4.43,
          'Personal Jesus': 4.56,
          'Halo': 4.30,
          'Waiting for the Night': 6.07,
          'Enjoy the Silence': 4.6,
          'Policy of Truth': 4.88,
          'Blue Dress': 4.18,
          'Clean': 5.68,
      }
      # распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
      #   А другие три песни звучат ХХХ минут
      # TODO здесь ваш код
      sweet_time = violator_songs_dict['Sweetest Perfection']
      policy_time = violator_songs_dict['Policy of Truth']
      blue_time = violator_songs_dict['Blue Dress']
      # Суммируем и округляем до 2 знаков
      other_total = round(sweet_time + policy_time + blue_time, 2)
      print(f'А другие три песни звучат {other_total} минут')
Результат

<img width="1314" height="60" alt="image" src="https://github.com/user-attachments/assets/92ab7aa2-946e-4189-9c89-f2b82e0bde02" />

Описание проделанной работы

----
### 07_secret
Задание 

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      
      # Есть зашифрованное сообщение
      
      secret_message = [
          'квевтфпп6щ3стмзалтнмаршгб5длгуча',
          'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
          'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
          'ьд5фму3ежородт9г686буиимыкучшсал',
          'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
      ]
      
      # Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
      # Должна получиться фраза на русском языке, например: как два байта переслать.
      
      # Ключ к расшифровке:
      #   первое слово - 4-я буква
      #   второе слово - буквы с 10 по 13, включительно
      #   третье слово - буквы с 6 по 15, включительно, через одну
      #   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
      #   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
      #
      # Обратите вниманме:
      #   даны номера букв, а не индексы
      #   срез не включает последний индекс
      #   подробную информацию об обратных срезах см https://clck.ru/MfEMS
      #
      # Подсказки:
      #   В каждом элементе списка защифровано одно слово.
      #   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
      #   4е и 5е слова нужно получить за 1 срез
      #   Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат
      
      # TODO вывести расшифрованное сообщение
      word1 = secret_message[0][3]                     
      word2 = secret_message[1][9:13]                 
      word3 = secret_message[2][5:15:2]                
      word4 = secret_message[3][12:6:-1]          
      word5 = secret_message[4][20:15:-1]        
      result = f'{word1} {word2} {word3} {word4} {word5}'
      print(result)
Результат

<img width="1263" height="39" alt="image" src="https://github.com/user-attachments/assets/d0c6c2ec-7785-43a6-8ea0-a15a6b2cf439" />

Описание проделанной работы

---
### 08_garden
Задание 

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      
      # в саду сорвали цветы
      garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
      
      # на лугу сорвали цветы
      meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
      
      # создайте множество цветов, произрастающих в саду и на лугу
      garden_set = set(garden)
      meadow_set = set(meadow)
      
      # выведите на консоль все виды цветов
      all_flowers = garden_set | meadow_set  # или garden_set.union(meadow_set)
      print("Все виды цветов:", all_flowers)
      
      # выведите на консоль те, которые растут и там и там
      common_flowers = garden_set & meadow_set  # или garden_set.intersection(meadow_set)
      print("Цветы, которые растут и там и там:", common_flowers)
      
      # выведите на консоль те, которые растут в саду, но не растут на лугу
      garden_only = garden_set - meadow_set  # или garden_set.difference(meadow_set)
      print("Цветы, которые растут только в саду:", garden_only)
      
      # выведите на консоль те, которые растут на лугу, но не растут в саду
      meadow_only = meadow_set - garden_set  # или meadow_set.difference(garden_set)
      print("Цветы, которые растут только на лугу:", meadow_only)
Результат

<img width="1270" height="101" alt="image" src="https://github.com/user-attachments/assets/b075a020-ec22-4117-be00-7f4cc1467e43" />

Описание проделанной работы

---
### 09_shopping
Задание

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
Результат

<img width="1321" height="346" alt="image" src="https://github.com/user-attachments/assets/827edcf8-16eb-48c5-b0ac-2f0d628464c8" />

Описание проделанной работы

---
### 10_store
Задание

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
Результат

<img width="1280" height="107" alt="image" src="https://github.com/user-attachments/assets/5e750f7d-8092-4bc2-b1f4-ad421d362cda" />

Описание проделанной работы

---
### Подсказка для git

















     



