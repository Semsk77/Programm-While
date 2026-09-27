N = float(input("Введите число N: "))

if N > 1:
    r = 0
    while N > 0:
        r = r * 10 + N % 10
        N //= 10
    print(f"Перевёрнутое число = {r}")
else:
    print("N > 0")
    #27.09.2026 13:59