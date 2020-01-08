import math

def quadratic(a,b,c):

    d = b*b - 4*a*c

    e = 2*a

    if d > 0:

        x1 = (-b + math.sqrt(d))/e

        x2 = (-b - math.sqrt(d))/e

        print("方程有两个不同实根: x1 = %f   x2 = %f"%(x1,x2))

    elif d == 0:

        x1 = float(-b/e)

        print("方程有两个相同实根: x1 = x2 = %f"%x1)

    else:

        print("该方程无实根!")

a = float(input("请输入非零实数a的值: "))

while a == 0:

    print("a的值不能为零")

    a = float(input("请再次输入非零实数a的值: "))

b = float(input("请输入b的值: "))

c = float(input("请输入c的值: "))

quadratic(a,b,c)