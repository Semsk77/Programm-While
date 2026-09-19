N = float(input("Введите число N: "))
if N > 0:
    q = 0
    while N > 1 and N % 3 == 0:
        N //= 3
    if N == 1:
        print("TRUE")
    else:
        print("FALSE")
else:
    print("N < 0")
    #19.09.2026 17:05