
size=int(input())
arr=list(map(int,input().split()))
maxi=0
for i in range(size):
    total=0
    for j in range(i+1,size):
        if j==i+1:
            total+=arr[i]+arr[j]
        else:
            total+=arr[j]
        maxi=max(total,maxi)
print(maxi)
    
