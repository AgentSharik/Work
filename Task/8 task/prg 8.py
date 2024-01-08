n = int(input("Введите натуральное число n: "))

if n <= 9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
else:
    print()
    print("Значение выпадает из допустимого диапазона. Введите ещё раз.")

