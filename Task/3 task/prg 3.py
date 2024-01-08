A = int(input("Введите значение A: "))
B = int(input("Введите значение B: "))

for i in range(A, B-1, -1):
    if i % 2 != 0:
        print(i)