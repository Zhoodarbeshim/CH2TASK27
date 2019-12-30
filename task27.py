# list_ = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, 0]
list_ = input("Enter some num: ").split(" ")
pos = []
neg = []
for i in list_:
    if int(i) > 0:
        pos.append(i)
    elif int(i) < 0:
        neg.append(i)
print(pos)
print(neg)