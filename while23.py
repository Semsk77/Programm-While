A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A > 0 and B > 0:
    while B != 0:
        A, B = B, A % B
    print(f"NOD = {A}")
else:
    print("A < 0 or B < 0")
    #27.09.2026 14:14