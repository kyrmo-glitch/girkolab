from otstup import printnomer

printnomer()

from distance import calculate_city_distances
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
print(calculate_city_distances(sites))

printnomer()

from circle import s, tochka1, tochka2
print(s(42))
print(tochka1((23, 34),42))
print(tochka2((30, 30),42))

printnomer()

from operations import result
print(result())

printnomer()

from favourite_movies import get_films
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
first, last, second, second_last = get_films(my_favorite_movies)
print(first, last, second, second_last, sep='\n')

printnomer()

from my_family import get_father_height, get_total_height
print(get_father_height())
print(f'Рост отца - {get_father_height()} см')
print(f'Общий рост моей семьи - {get_total_height()} см')

printnomer()

from zoo import add_bear, add_birds, remove_elephant, print_cage
birds = ['rooster', 'ostrich', 'lark']
print(add_bear())
print(add_birds(birds))
print(remove_elephant())
print_cage('lion', 'Лев')
print_cage('lark', 'Жаворонок')

printnomer()

from songs_list import task1, task2
print(f'Три песни звучат {task1()} минут')
print(f'Три песни звучат {task2()} минут')

printnomer()

from secret import decode_message
print(decode_message())

printnomer()

from garden import all_flowers, common, garden_only, meadow_only
print("Все:", all_flowers())
print("Общие:", common())
print("Только в саду:", garden_only())
print("Только на лугу:", meadow_only())

printnomer()

from shopping import print_sweets
print(print_sweets())

printnomer()

from store import print_lamp, print_table, print_sofa, print_chair
print(print_lamp())
print(print_table())
print(print_sofa())
print(print_chair())


