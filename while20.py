N = int(input("Введите число N: "))

if N > 1:
    f = False
    while N > 0:
        if N % 10 == 2:
            f = True
            break
        N //= 10
    print("TRUE" if f else "FALSE")
else:
    print("N > 0")
    #27.09.2026 14:01