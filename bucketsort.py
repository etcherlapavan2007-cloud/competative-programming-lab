n = int(input())
arr = list(map(float, input().split()))
if n == 0:
    print([])
    exit()
buckets = [[] for _ in range(n)]
for i in arr:
    index = int(i * n)
    if index >= n:
        index = n - 1
    buckets[index].append(i)
res = []
for j in buckets:
    j.sort()
    res.extend(j)
for x in res:
    if x.is_integer():
        print(int(x), end=" ")
    else:
        print(f"{x:.2f}", end=" ")
