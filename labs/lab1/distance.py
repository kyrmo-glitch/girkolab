def city_distances():
    sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
    distances = {}
    
    mx, my = sites['Moscow']
    lx, ly = sites['London']
    px, py = sites['Paris']
    
    dist_ml = ((mx - lx) ** 2 + (my - ly) ** 2) ** 0.5
    dist_mp = ((mx - px) ** 2 + (my - py) ** 2) ** 0.5
    dist_lp = ((lx - px) ** 2 + (ly - py) ** 2) ** 0.5
    
    distances['Moscow'] = {'London': round(dist_ml, 2), 'Paris': round(dist_mp, 2)}
    distances['London'] = {'Moscow': round(dist_ml, 2), 'Paris': round(dist_lp, 2)}
    distances['Paris'] = {'Moscow': round(dist_mp, 2), 'London': round(dist_lp, 2)}
    
    return distances