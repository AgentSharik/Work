A = int(input("Введите значение A: "))
B = int(input("Введите значение B: "))

if A <= B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)