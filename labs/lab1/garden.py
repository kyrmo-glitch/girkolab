garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

def all_flowers():
    return set(garden) | set(meadow)

def common():
    return set(garden) & set(meadow)

def garden_only():
    return set(garden) - set(meadow)

def meadow_only():
    return set(meadow) - set(garden)