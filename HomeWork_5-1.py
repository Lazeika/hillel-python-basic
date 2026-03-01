import keyword

name = input("Введіть ім'я змінної: ")

is_valid = True

# 1. Не порожній рядок
if name == "":
    is_valid = False

# 2. Не починається з цифри
elif name[0].isdigit():
    is_valid = False

# 3. Немає великих літер
elif not name.islower():
    is_valid = False

# 4. Лише літери, цифри і _
elif not name.replace("_", "").isalnum():
    is_valid = False

# 5. Не більше одного _
elif name.count("_") > 1:
    is_valid = False

# 6. Не є зарезервованим словом
elif keyword.iskeyword(name):
    is_valid = False

print(is_valid)