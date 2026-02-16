## Отчет по лабораторной работе №1
#### 00_distance
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      sites = {
          'Moscow': (550, 370),
          'London': (510, 510),
          'Paris': (480, 480),
      }
      distances = {}
      x1, y1 = sites['Moscow']
      x2, y2 = sites['London']
      distances['Moscow-London'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      x1, y1 = sites['Moscow']
      x2, y2 = sites['Paris'] 
      distances['Moscow-Paris'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      x1, y1 = sites['London']
      x2, y2 = sites['Paris']
      distances['London-Paris'] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      print(distances)
Результат

<img width="1207" height="53" alt="image" src="https://github.com/user-attachments/assets/e35dc55d-054c-4066-aa04-64ae004d80bf" />

Описание проделанной работы




#### 01_circle
Задание

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-


      radius = 42



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
      #
      # 77777.7777
      # False
      # False



