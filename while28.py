eps = float(input("Введите число e (> 0): "))

if eps > 0:
    A_p = 2
    K = 1
    while True:
        K += 1
        A_c = 2 + 1 / A_p
        if abs(A_c - A_p) < eps:
            break
        A_p = A_c
    print(f"K = {K}")
    print(f"A_(k-1) = {A_p}")
    print(f"A_K = {A_c}")
else:
    print("e < 0")
    #27.09.2026 14:43