def searchediv(n):
    div = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
        if len(div) > 2:

            break
    return div
for i in range(174457, 174506):
    d= sorted(searchediv(i))
    if len(d) == 2:
        print( d[0], d[1])
