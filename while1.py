A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
if A > 0 and B> 0 and A > B:
    while A >= B:
        A -= B
    print(f"Длина незанятой части = {A}")
else:
    print("A > b > 0")