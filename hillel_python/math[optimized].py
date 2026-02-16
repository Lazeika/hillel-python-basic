# Дію необхідну для виконання можна вибрати в терміналі після запуску програми
print("Виберіть дію:")
print("1 - Квадрат числа")
print("2 - Середнє арифметичне трьох чисел")
print("3 - Перетворити хвилини -> години та хвилини")
print("4 - Розрахунок знижки")
print("5 - Остання цифра числа")
print("6 - Периметр прямокутника")
print("7 - Вивести число в стовпчик")

# Вибір дії
choice = input("Введіть номер дії [1-7]: ")

# 1. Квадрат числа
if choice == "1":
    x = float(input("Введіть число: "))
    print("Квадрат числа:", x * x)

# 2. “Середнє трьох чисел”
elif choice == "2":
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))
    avg = (a + b + c) / 3
    print("Середнє арифметичне:", avg)

# 3. “Перетворення хвилин у години”
elif choice == "3":
    minutes = int(input("Введіть кількість хвилин: "))
    hours = minutes // 60
    mins = minutes % 60
    print(f"{hours} год {mins} хв")

# 4. “Розрахунок знижки”
elif choice == "4":
    price = float(input("Введіть ціну: "))
    discount = float(input("Введіть знижку в %: "))
    final_price = price * (1 - discount / 100)
    print("Ціна зі знижкою:", final_price)

# 5. “Остання цифра числа”
elif choice == "5":
    number = int(input("Введіть число: "))
    last_digit = number % 10
    print("Остання цифра:", last_digit)

# 6. “Периметр прямокутника”
elif choice == "6":
    length = float(input("Введіть довжину: "))
    width = float(input("Введіть ширину: "))
    perimeter = 2 * (length + width)
    print("Периметр:", perimeter)

# 7. Виведення числа в стовпчик
elif choice == "7":
    num = int(input("Введіть 4-значне число: "))
    d1 = num // 1000
    d2 = (num % 1000) // 100
    d3 = (num % 100) // 10
    d4 = num % 10
    print(d1)
    print(d2)
    print(d3)
    print(d4)

# [ПОМИЛКА] Користувач ввів неіснуючу/невірну дію.
else:
    print("Невірний вибір")
