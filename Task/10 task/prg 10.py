def fibonacci_sum(N, K):
    fib_sequence = [0, 1]  # начальные значения ряда Фибоначчи

    for i in range(2, N + K):  # генерируем ряд Фибоначчи длиной N + K
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    sum_numbers = sum(fib_sequence[K:K + N])  # суммируем числа, начиная с порядкового номера K и до K + N
    print("Ряд Фибоначчи:", fib_sequence)
    print()
    return sum_numbers


# чтение входных данных
N = int(input("Введите количество чисел из ряда Фибоначчи (N): "))
K = int(input("Введите порядковый номер, с которого нужно начать (K): "))

# вызов функции и вывод результатов
print()
result = fibonacci_sum(N, K)
print("Сумма чисел:", result)

