N = float(input("Введите число N: "))

if N > 1:
    K = 0
    t = 0
    while t + (K + 1)<= N:
        K += 1
        t += K
    print(f"K = {K}")
    print(f"Сумма ={t}")
else:
    print("N < 1 ")
    #19.09.2026 17:38