N = float(input("Введите процент N: "))

if N:
    c = 0
    t = 0
    while N > 0:
        t += N % 10
        c += 1
        N //= 10
    print(f"Кол-во цифр = {c}")
    print(f"Сумма цифр = {t}")
else:
    print("N < 0")
    #19.09.2026 18:16