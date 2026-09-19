P = float(input("Введите процент P (0 < P < 50): "))

if 0 < P < 50:
    d = 10
    S = 0
    K = 0
    while S <= 200:
        K += 1
        S += d
        d *= (1 + P / 100)
    print(f"K = {K}")
    print(f"S = {S:.2f}")
else:
    print("Ошибка")
    #19.09.2026 18:16