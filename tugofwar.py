n=int(input())
arr=list(map(int,input().split()))
lsum,rsum=0,0
temp=n//2
i=0
j=n-1
arr.sort()
for k in range(1,temp):
    lsum+=arr[i]+arr[j]
    i+=1
    j-=1
if n%2!=0:
    lsum+=arr[i]
    i+=1
while i<=j:
    rsum+=arr[i]+arr[j]
    i+=1
    j-=1
print(abs(lsum-rsum))
        
    
        
        
        
