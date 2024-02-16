lst = [1, 5, 6, 3]

def ohms(massiv):
    result = 0

    for num in massiv:
        result += num
    print(f"{result} ohms")


ohms(massiv=lst)