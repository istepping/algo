a = [(x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if ((x != y) and (y != z) and (x != z))]
print("个数=", a.__len__())
print(a)
