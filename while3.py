N = float(input("Введите число N: "))
K = float(input("Введите число K: "))
if N > 0 and K > 0:
    q = 0
    while N >= K:
        N -= K
        q += 1
        r = N
    print(f"Частное = {q}")
    print(f"Остаток = {r}")
else:
    print("N > 0 иK > 0")
    #19.09.2026 17:02