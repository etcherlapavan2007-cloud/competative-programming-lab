n1,n2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
i,j=0,0
res=[]
if n1==0 and n2==0:
    print(0)
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
mid=len(res)//2
if len(res)%2==0:
    print(int(res[mid-1]+res[mid])/2)
else:
    print(res[mid])
