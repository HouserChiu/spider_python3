def product(*n):
    s = 1
    for i in n:
        s = s * i
    return s
print('product(5) =', product(5))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))