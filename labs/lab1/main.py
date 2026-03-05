print('№1')

from distance import city_distances
print(city_distances())

print('№2')

from circle import s, tochka1, tochka2
print(s(42))
print(tochka1((23, 34),42))
print(tochka2((30, 30),42))

print('№3')

from operations import result
print(result())

print('№4')

from favourite_movies import films
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
first, last, second, second_last = films(my_favorite_movies)
print(first, last, second, second_last, sep='\n')

print('№5')

from my_family import father_height, total_height
print(father_height())
print(f'Рост отца - {father_height()} см')
print(f'Общий рост моей семьи - {total_height()} см')

print('№6')

from zoo import add_bear, add_birds, remove_elephant, cage_number
print(add_bear())
print(add_birds())
print(remove_elephant())
cage_number('lion', 'Лев')
cage_number('lark', 'Жаворонок')

print('№7')

from songs_list import task1, task2
print(f'Три песни звучат {task1()} минут')
print(f'Три песни звучат {task2()} минут')

print('№8')

from secret import decode_message
print(decode_message())

print('№9')

from garden import all_flowers, common, garden_only, meadow_only
print("Все:", all_flowers())
print("Общие:", common())
print("Только в саду:", garden_only())
print("Только на лугу:", meadow_only())

print('№10')

from shopping import print_sweets
print_sweets()

print('№11')

from store import print_lamp, print_table, print_sofa, print_chair
print(print_lamp())
print(print_table())
print(print_sofa())
print(print_chair())


