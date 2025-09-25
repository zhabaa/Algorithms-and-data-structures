def foo(x: int):
    result = []
    i = 1

    while i <= x:
        result.append(i)
        i *= 3

    result = set()
    a = 1

    while a <= x:
        b = a

        while b <= x:
            c = b

            while c <= x:
                result.add(c)
                c *= 7

            b *= 5
        a *= 3

    return sorted(result)


if __name__ == "__main__":
    x = int(input("Введите x: "))
    numbers = foo(x)

    print("Числа от 1 до x вида 3^K * 5^L * 7^M:")

    for num in numbers:
        print(num, end=' ')
