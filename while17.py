N = float(input("Введите процент N: "))

if N > 0:
    while N > 0:
        print(N % 10)
        N //= 10
else:
    print("N < 0")
    #19.09.2026 18:18