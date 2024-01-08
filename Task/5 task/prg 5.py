n = int(input("Введите число n: "))
sum = 0

for i in range(1, n + 1):
    sum += i ** 3

print("Сумма кубов от 1 до", n, ":", sum)
