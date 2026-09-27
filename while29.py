eps = float(input("Введите число e (> 0): "))

if eps > 0:
    A1 = 1
    A2 = 2
    K = 2
    while True:
        K += 1
        A3 = (A1 + 2 * A2) / 3
        if abs(A3 - A2) < eps:
            break
        A1, A2 = A2, A3
    print(f"K = {K}")
    print(f"A_(K-1) = {A2}")
    print(f"A_K = {A3}")
else:
    print("e < 0")
    #27.09.2026 14:48