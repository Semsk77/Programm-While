N = float(input("Введите число N: "))

if N > 0:
    K = 0
    while N > 1:
        N //= 2
        K += 1
    print(f"K = {K}")
else:
    print("N < 0 ")
    #19.09.2026 17:12