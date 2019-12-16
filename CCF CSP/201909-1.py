n, m =map(int,input().split())
b = []
c = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(sum(a[1:]))
    c.append(sum(a))
print(sum(c), b.index(min(b)) + 1, abs(min(b)))
