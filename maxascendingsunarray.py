n=int(input())
arr1=list(map(int,input().split()))
maxi=total=arr1[0]
if n==1:
    print(arr1[0])
for i in range(n-1):
    if arr1[i]<arr1[i+1]:
        total+=arr1[i+1]
    else:
        total=arr1[i+1]
    maxi=max(maxi,total)
print(maxi)
