A = float(input("Введите число A: "))

if A > 1:
    K = 0
    t = 0
    while t <= A:
        K += 1
        t += 1 / K
    print(f"K = {K}")
    print(f"Сумма = {t}")
else:
    print("N < 1 ")
    #19.09.2026 17:43