A = float(input("Введите число A: "))

if A > 1:
    K = 0
    t = 0
    while t + 1 / (K + 1) < A:
        K += 1
        t += 1 / K
    print(f"K = {K}")
    print(f"Сумма = {t}")
else:
    print("A < 1 ")
    #19.09.2026 18:07