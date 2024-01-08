n = int(input("Введите количество чисел из ряда Фибоначчи: "))

fibonacci_sequence = [0, 1]

for i in range(2, n):
    next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(next_number)

sum_of_fibonacci = sum(fibonacci_sequence[:n])

print()
print("Ряд Фибоначчи:", fibonacci_sequence)

print()
print("Сумма чисел из ряда Фибоначчи:", sum_of_fibonacci)

