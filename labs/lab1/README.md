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
      point_1 = (23, 34)
      distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
      print(distance_1 <= radius)
      point_2 = (30, 30)
      distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
      print(distance_2 <= radius)
Результат 

<img width="1086" height="91" alt="image" src="https://github.com/user-attachments/assets/ce98434c-0f2b-43d4-a099-f582d0da2cf2" />

Описание проделанной работы

#### 02_operations
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



     



