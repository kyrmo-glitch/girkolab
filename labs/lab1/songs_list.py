songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
def task1():
    time = 0
    for song in songs_list:
        if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
            time += song[1]
    return round(time, 2)

def task2():
    time = songs_dict['Sweetest Perfection'] + songs_dict['Policy of Truth'] + songs_dict['Blue Dress']
    return round(time, 2)