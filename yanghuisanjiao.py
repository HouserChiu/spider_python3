def triangle():
    L1 = [1]
    cnt = 1
    while cnt <= 10:
        yield L1
        cnt = cnt + 1
        L2 = []
        for i in range(cnt):
            if i == 0 or i == cnt - 1:
                L2.append(1)
            else:
                L2.append(L1[i] + L1[i-1])
        L1 = L2
    return 'done'
for L1 in triangle():
    print(L1)