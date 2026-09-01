a,b=map(int,input().split())
ct=1
while a%2==0 or b%2==0:
    if a%2==0 and b%2==0:
        ct*=2
    if a%2==0:
        a=a//2
    if b%2==0:
        b=b//2
while a!=b:
    if a>b:
        a=(a-b)//2
    else:
        b=(b-a)//2
print(ct*a)
                                                             
                                                             
                                                             
