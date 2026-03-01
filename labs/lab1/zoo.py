zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

def add_bear():
    zoo.insert(1, 'bear')
    return zoo

def add_birds(birds_list):
    zoo.extend(birds_list)
    return zoo

def remove_elephant():
    zoo.remove('elephant')
    return zoo

def get_cage_number(animal):
    return zoo.index(animal) + 1

def print_cage(animal, name):
    print(f'{name} сидит в клетке номер {get_cage_number(animal)}')