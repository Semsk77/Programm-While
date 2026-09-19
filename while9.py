N = float(input("Введите число N: "))

if N > 1:
    K = 0
    p = 1
    while p <= N:
        p *= 3
        K += 1
    print(f"K = {K}")
else:
    print("N < 1 ")
    #19.09.2026 17:29