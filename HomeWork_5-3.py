import string

text = input("Введіть текст: ")

# 1. Видаляємо пунктуацію
for symbol in string.punctuation:
    text = text.replace(symbol, "")

# 2. Розбиваємо на слова
words = text.split()

# 3. Робимо кожне слово з великої літери
hashtag = "#"

for word in words:
    hashtag += word.capitalize()

# 4. Обрізаємо до 140 символів
hashtag = hashtag[:140]

print(hashtag)