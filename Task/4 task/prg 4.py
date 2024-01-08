N = int(input("Введите количество чисел: "))

sum = 0
for _ in range(N):
    num = int(input("Введите число: "))
    sum += num

print("Сумма чисел:", sum)
