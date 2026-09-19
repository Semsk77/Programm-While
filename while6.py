N = float(input("Введите число N: "))

if N > 0:
    r = 1
    i = N
    while i > 0:
        r *= i
        i -= 2
    print(f"N!! = {r}")
else:
    print("N < 0 ")
    #19.09.2026 17:20