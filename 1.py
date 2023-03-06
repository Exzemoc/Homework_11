def progre(x, c):
    a = 1
    b = a
    for i in range(0, x):
        n = b * c
        print(n)
        b = n
        yield b


tuc = progre(7,8)
next(tuc)
next(tuc)
next(tuc)
next(tuc)
next(tuc)
