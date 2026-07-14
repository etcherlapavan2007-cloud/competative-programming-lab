n=int(input())
arr=list(map(int,input().split()))
res=[0]*(max(arr)+1)
for  i in arr:
    res[i]+=1
if len(res)==99:
    res.append(0)
print(*res)
