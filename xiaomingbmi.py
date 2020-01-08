m=float(input('身高m:'))
n=float(input('体重kg:'))
BMI=n/(m*m)
if BMI>32:

    print("严重肥胖")

elif BMI>28:

    print("肥胖")

elif BMI>25:

    print("过重")

elif BMI>18.5:

    print("正常")

else:

    print("过轻")