
n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
res=list()
i,j=0,0
while i<n1 and j<n2:
    if arr1[i]<arr2[j]:
        res.append(arr1[i])
        i+=1
    else:
        res.append(arr2[j])
        j+=1
while i<n1:
    res.append(arr1[i])
    i+=1
while j<n2:
    res.append(arr2[j])
    j+=1
print(*res)
    
