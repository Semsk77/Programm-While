N = int(input("Введите число N: "))

if N > 0:
    p = True
    d = 2
    while d * d <= N:
        if N % d == 0:
            p = False
            break
        d += 1
    print("TRUE" if p else "FALSE")
else:
    print("N > 1")
    #27.09.2026 14:09