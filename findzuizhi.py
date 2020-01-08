def findminandmax(a):
    min = a[0]
    max = a[0]
    if len(a) == 0:
        return (None, None)
    if len(a) == 1:
        return (min, max)
    for n in a:
        if n > max:
            max = n
        if n < min:
            min = n
    return (min, max)
print('findminandmax=', findminandmax([1, 2, 3, 4, 5, 6, 7]))
