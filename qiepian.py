def trim(s):
    if len(s)!=0:
        while s[0]==' ':
            s=s[1:]
        while s[-1]==' ':
            s=s[:-1]
        return s
    else:
        return s

s = input("请输入一串字符: ")

print(trim(s))
