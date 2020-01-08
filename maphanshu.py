def normalize(name):

    return str.capitalize(name)

list(map(normalize,['adma','LISA','barT']))
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)