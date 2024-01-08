n = int(input("Введите число n: "))

sum_of_factorials = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum_of_factorials += factorial

print("Сумма факториалов от 1 до", n, ":", sum_of_factorials)

