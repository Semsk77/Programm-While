P = float(input("Введите процент P (0 < P < 25): "))

if 0 < P < 25:
    K = 0
    S = 1000
    while S <= 1100:
        K += 1
        S *= (1 + P / 100)
    print(f"K = {K}")
    print(f"S = {S:.2f}")
else:
    print("Ошибка")
    #19.09.2026 18:11