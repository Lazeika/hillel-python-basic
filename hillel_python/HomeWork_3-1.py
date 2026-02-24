version = 2
# [v1 СТАРИЙ] Старий варіант калькулятора
if version == 1:
    x = int(input("Введіть перше число: "))

    print("Оберіть дію:")
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")

    choice = input("Ваш вибір: ")

    if choice not in ["1", "2", "3", "4"]:
        print("Помилка вибору дії!")
        exit()

    y = int(input("Введіть друге число: "))

    if choice == "1":
        print("Результат:", x + y)

    elif choice == "2":
        print("Результат:", x - y)

    elif choice == "3":
        print("Результат:", x * y)

    elif choice == "4":
        if y != 0:
            print("Результат:", x / y)
        else:
            print("Ділення на нуль неможливе!")

    else:
        print("Невірний вибір")

# [v1.1 НОВИЙ] Варіант з ручним вводом математичного знаку (+, -, *, /)                                     {ПОТЕНЦІЙНО ПРАВИЛЬНЕ ВИКОНАННЯ ТЗ}
elif version == 2:
    x = int(input("Введіть перше число: "))

    operation = input("Введіть операцію (+, -, *, /): ")

    y = int(input("Введіть друге число: "))

    if operation == "+":
        print("Відповідь: ", x + y)
    elif operation == "-":
        print("Відповідь: ", x - y)
    elif operation == "*":
        print("Відповідь: ", x * y)
    elif operation == "/":
        if y != 0:
            print("Відповідь: ", x / y)
        else:
            print("Ділення на нуль неможливе!")

    else:
        print("Невірний вибір")

# [v1.2 НОВИЙ] Варіант калькулятора із перевіркою на помилки вводу користувача
elif version == 3:
    first = input("Введіть перше число: ")

    if not first.isdigit():
        print("Помилка! Можна вводити тільки цифри.")
        exit()

    sign = input("Введіть знак (+ - * /): ")

    if sign not in "+-*/":
        print("Помилка! Дозволені тільки + - * /")
        exit()

    second = input("Введіть друге число: ")

    if not second.isdigit():
        print("Помилка! Можна вводити тільки цифри.")
        exit()

    first = int(first)  # Окремо вказую який тип у змінних first та second, тому що неможливо одразу одночасно вказувати тип змінної і перевіряти чи її тип введений користувачем підходить, оскільки програма просто впаде від помилки
    second = int(second) # ^^^^^

    if sign == "/" and second == 0:
        print("Не можна ділити на 0!")
        exit()

    if sign == "+":
        result = first + second
    elif sign == "-":
        result = first - second
    elif sign == "*":
        result = first * second
    elif sign == "/":
        result = first / second

    print("Результат:", result)

else:
    print("Неправильно вибрана версія")