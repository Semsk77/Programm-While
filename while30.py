A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

if A > 0 and B > 0 and C > 0:
    c = 0
    l_c = 0
    t = A
    while t >= C:
        t -= C
        l_c += 1
    w_c = 0
    t = B
    while t >= C:
        t -= C
        w_c += 1
    for _ in range(l_c):
        c += w_c
    print(f"Кол-во квадратов = {c}")
else:
    print("A, B, C <0")
    #27.09.2026 15:13