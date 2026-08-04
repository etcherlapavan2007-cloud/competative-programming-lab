m,n=map(int,input().split())
maxi=0
if m>n:
    m,n=n,m
for i in range(m,n+1):
    ct=1
    temp=i
    while temp!=1:
        if temp%2==0:
            temp=temp//2
        else:
            temp=3*temp+1
        ct+=1   
    maxi=max(maxi,ct)
print(m,n,maxi)
