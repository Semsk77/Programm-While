A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
if A > 0 and B> 0 and A > B:
    c = 0
    while A >= B:
        A -= B
        c += 1
    print(f"Кол-во отрезков = {c}")
else:
    print("A > B > 0")
    #19.09.2026 16:56