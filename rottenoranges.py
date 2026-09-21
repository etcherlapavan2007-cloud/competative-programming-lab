from collections import deque
n, m = map(int, input().split())
a = []
q = deque()
fresh = 0
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(m):
        if row[j] == 2:
            q.append((i, j))
        elif row[j] == 1:
            fresh += 1
time = 0
while q and fresh > 0:
    size = len(q)
    for _ in range(size):
        i, j = q.popleft()
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < n and 0 <= y < m and a[x][y] == 1:
                a[x][y] = 2
                fresh -= 1
                q.append((x, y))
    time += 1
if fresh == 0:
    print(time)
else:
    print(-1)
