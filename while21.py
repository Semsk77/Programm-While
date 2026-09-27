N = int(input("Введите число N: "))

if N > 0:
    f = False
    while N > 0:
        if (N % 10) % 2 != 0:
            f = True
            break
        N //= 10
    print("TRUE" if f else "FALSE")
else:
    print("N > 0")
    #27.09.2026 14:05