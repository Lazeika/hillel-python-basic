mylist = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
# mylist = [0] #-> [0]
# mylist = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
# mylist = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

zeros = [x for x in mylist if x == 0]
others = [x for x in mylist if x != 0]
result = others + zeros

print(result)
