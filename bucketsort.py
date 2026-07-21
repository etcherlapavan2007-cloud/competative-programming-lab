n = int(input())
arr = list(map(float, input().split()))
buckets = [[] for i in range(n)]
if n == 0:
        print([])
for i in arr:
    index = int(i * n)
    buckets[index].append(i)
res = []
for j in buckets:
    j.sort()
    res.extend(j)
print(*["{:.2f}".format(x) for x in res])
