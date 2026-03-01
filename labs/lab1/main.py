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







