import random

length = random.randint(3, 10)

mylist = []
for x in range(length):
    mylist.append(random.randint(0, 10))

print("Початковий список:", mylist)

mynewlist = [mylist[0], mylist[2], mylist[-2]]

print("Другий список:", mynewlist)