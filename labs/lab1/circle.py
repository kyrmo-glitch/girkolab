def s(radius):
    pi = 3.1415926
    area = round(pi * radius ** 2,4)
    return area

def tochka1(point_1,radius):
    dist1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    return dist1 <= radius

def tochka2(point_2,radius):
    dist2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    return dist2 <= radius

