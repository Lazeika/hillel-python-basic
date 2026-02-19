""" Перший приклад з іменем і віком
name = input("Введи своє ім'я: ")
age = int(input("А ще введи свій вік: "))
print(f"Привіт, {name}! Через рік тобі буде {age + 1} років")"""

""" Математичні приклади
x = int(input("Введи своє число: "))
print("Число в квадраті", x ** 2)
print("Число в кубі", x ** 3)
print("Остача ділення", x % 2)
print("Ділення", x / 3)"""
""" Математичні порівняння
x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
print(f"Чи {x} > {y}", x > y)
print(f"Чи {x} = {y}", x == y)
print(f"Чи {x} <= {y}", x <= y)"""

# Логічні оператори
""" Оператор "and" працює тільки коли всі умови виконались
x = 15
print(f"Якщо x = {x}, тоді {x} > 10 та {x} < 20, тоді це ", x > 10 and x < 20)
print(f"Якщо x = {x}, тоді {x} > 10 та {x} < 5 тоді це ", x > 10 and x < 5)"""
""" Оператор "or" працює коли хоча б одна умова виконалась. Після виконання однієї умови перевірки інших не буде
x = 5
print(f"Якщо x = {x}, тоді {x} < 10 або {x} > 100, то це", x < 10 or x > 100)
print(f"Якщо x = {x}, тоді {x} > 10 або {x} > 100, то це", x > 10 or x > 100)"""
""" Оператор "not" змінює булеве (bool) значення на протилежне
x = 5
print(not(x > 10)) #false -> true
print(not(x < 10)) #true -> false"""
""" Тренінг операторів
x = int(input("Введіть число: "))
print("Ваше число в діапазоні від 0 до 10?", x > 0 and x < 100)
print("Ваше число менше нуля, або більше 100?", x < 0 or x > 100)
print("Ваше число це не 5?", not(x == 5))"""

"""Синтаксис "if", "elif" та "else"
x = int(input("Введи число: "))
if x > 10:
    print("Ваше число більше ніж 10")
elif x < 10:
    print("Ваше число менше 10")
else:
    print("Ваше число це 10")"""
"""Задачка із визначенням парності або непарності числа
x = int(input("Введи своє число: "))
if x % 2 == 0:
    print("Ваше число парне")
else:
    print("Ваше число непарне")"""

# Синтаксис "while"
""" Приклад 1
x = 1
while x <= 5:
    print(x)
    x += 1
else:
    print("Закінчив виконання")"""
""" Приклад 2
x = int(input("Введіть число: "))
while x != 0:
    print(x)
    x = int(input("Введіть інше число: "))
print("Програма завершена")"""
""" Використання "break"
while True:
    x = int(input("Введіть число: "))
    if x == 0:
        break
    print(f"Ви ввели {x}")"""
""" Використання "continue"
x = 0
while x < 5:
    x += 1
    if x == 3: # Переклад з компудахтурної мови: Якщо х = 3, то спрацьовує continue і трійка пропускається (не пишеться)
        continue
    print(x)"""

# Списки (lists)
"""Це списки. В них ми вказуємо вручну кожен "об'єкт". Індекси в списках ЗАВЖДИ починаються з нуля, тобто print(fruits[0]) це буде "something1" і так далі...
list1 = ["Something1", "Something2", "Something3"]
playlist2 = ["Someone1", "Someone2", "Someone3"]
group5 = ["Somewhere1", "Somewhere2", "Somewhere3"]
x = int(input("Введіть від 1 до 3: "))
if x == 1:
    print(list1)
elif x == 2:
    print(playlist2)
elif x == 3:
    print(group5)
else:
    print("Попробуйте іншим разом")"""

"""Списки + вибір варіанту
print("1. Fruits")
print("2. Vegetables")
fruits = ["Ябко", "Банан", "Груша"]
vegetables = ["Помідор", "Картофан", "Цибуля"]
choice = input("Що Ви любите більше?: ")
if choice == "1":
    print(fruits)
elif choice == "2":
    print(vegetables)"""
# Ще є команди: Додати елемент - fruits.append("груша"), Видалити елемент - fruits.remove("Банан"), Визначити к-сть елементів - len(fruits)
# Перевірити наявність елементу - "Яблуко" in fruits (True/False), та Ітерація по списку - for fruit in fruits: |наступний рядок| print(fruit) це виведе всі елементи по черзі

"""Списки тренінг
favgames = ["osu!", "Terraria", "Path Of Exile 2", "Escape The Backrooms", "The Binding Of Isaac: Rebirth"]
favgames.append("Minecraft")
favgames.remove("Terraria")
print(favgames)
print("================================")
for game in favgames:
    print(game)"""
"""Комбінація
for x in range(1, 11): # Від 1 до 10 включно
    if x % 2 == 0:
        print(f"{x} - парне")
    else:
        print(f"{x} - непарне")"""
# Візуалізація Списку зі списками - matrix[row][column]
# print(2 in lst)