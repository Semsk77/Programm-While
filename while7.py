N = float(input("Введите число N: "))

if N > 0:
    K = 1
    while K * K <= N:
        K += 1
    print(f"K = {K}")
else:
    print("N < 0 ")
    #19.09.2026 17:25