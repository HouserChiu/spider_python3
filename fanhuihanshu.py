def createCounter():

    def plus():

        n = 0

        while True:

            n = n + 1

            yield n

    x = plus()

    def counter():

        return next(x)

    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())