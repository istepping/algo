# a = [(x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if ((x != y) and (y != z) and (x != z))]
# print("个数=", a.__len__())
# print(a)
count = 0
for i in range(2, 100):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
    if prime:
        count += 1
        print(i, end="\t")
        if count % 10 == 0:
            print("")
