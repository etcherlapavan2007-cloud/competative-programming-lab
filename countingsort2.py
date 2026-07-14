
n=int(input())
arr=list(map(int,input().split()))
res=[0]*(max(arr)+1)
result=[0]*len(arr)
for  i in arr:
    res[i]+=1
for i in range(1,len(res)):
    res[i]+=res[i-1]
for i in range(len(arr)):
    t=arr[i]
    result[res[t]-1]=t
    res[t]-=1
print(*result)
