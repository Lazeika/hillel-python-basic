while True:

    first = input("Введіть перше число: ")

    if not first.isdigit():
        print("Помилка! Можна вводити тільки цифри.")
        continue

    sign = input("Введіть знак (+ - * /): ")

    if sign not in "+-*/":
        print("Помилка! Дозволені тільки + - * /")
        continue

    second = input("Введіть друге число: ")

    if not second.isdigit():
        print("Помилка! Можна вводити тільки цифри.")
        continue

    first = int(first)
    second = int(second)

    if sign == "/" and second == 0:
        print("Не можна ділити на 0!")
        continue

    if sign == "+":
        result = first + second
    elif sign == "-":
        result = first - second
    elif sign == "*":
        result = first * second
    elif sign == "/":
        result = first / second

    print("Результат:", result)

    again = input("Продовжити? (y/n): ")

    if again.lower() != "y":
        print("Калькулятор завершено.")
        break