n=int(input())
arr1=list(map(int,input().split()))
maxi=n//2
if n==0:
    print(-1)
for i in arr1:
    if arr1.count(i)>maxi:
        print(i)
        break
else:
    print(-1)
        
