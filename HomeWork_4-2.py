mylist = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
# mylist = [1, 3, 5] #=> 30
# mylist = [6] #=> 36
# mylist = [] #=> 0

x = 0

for y in range(len(mylist)):
    if y % 2 == 0:
        x = x + mylist[y]

if len(mylist) == 0:    # Для порожнього масиву
    result = 0          # результат завжди 0.
else:
    result = x * mylist[-1]

print(result)