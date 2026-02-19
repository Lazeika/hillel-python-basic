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
