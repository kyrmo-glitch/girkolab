zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
birds = ['rooster', 'ostrich', 'lark']
def add_bear():
    zoo.insert(1, 'bear')
    return zoo

def add_birds():
    zoo.extend(birds)
    return zoo

def remove_elephant():
    zoo.remove('elephant')
    return zoo

def cage_number(animal, name):
    count = zoo.index(animal) + 1
    print(f'{name} сидит в клетке номер {count}')
