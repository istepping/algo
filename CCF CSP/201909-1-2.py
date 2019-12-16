N, M = map(int, input().split())
total = []
dictionary = {}
for i in range(N):
    temp = list(map(int, input().split()))
    total.append(sum(temp))
    dictionary[i + 1] = abs(sum(temp[1:]))
maxval = 0
index = 0
for key in dictionary.keys():
    if (dictionary[key] > maxval):
        maxval = dictionary[key]
        index = key
print(sum(total), index, maxval)
