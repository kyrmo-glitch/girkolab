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











     



