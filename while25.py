N = int(input("Введите число N: "))

if N > 1 :
    f1, f2 = 1, 1
    while f2 <= N:
        f1, f2 = f2, f1 + f2
    print(f"Первое число Фибоначи > {N}: {f2}")
else:
    print("N < 1")
    #27.09.2026 14:28