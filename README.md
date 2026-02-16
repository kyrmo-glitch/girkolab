## Отчет по лабораторной работе №1
#### 00_distance

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


